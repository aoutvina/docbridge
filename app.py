from flask import Flask, render_template, request, jsonify
from models import get_db, init_db, seed_data
from symptom_analyzer import analyze_symptoms
from datetime import datetime, timedelta
from telegram_bot import send_appointment_notification, BOT_TOKEN
import os

app = Flask(__name__)
app.secret_key = 'docbridge-secret-key-2026'

if not os.path.exists('docbridge.db'):
    init_db()
    seed_data()

def get_doctors_by_specialization(specialization):
    conn = get_db()
    cursor = conn.cursor()
    clean_spec = specialization.split('(')[0].strip().split('/')[0].strip()
    cursor.execute(
        'SELECT * FROM doctors WHERE specialization LIKE ?',
        (f'%{clean_spec}%',)
    )
    doctors = cursor.fetchall()
    conn.close()
    return doctors

def get_available_slots(doctor_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        '''SELECT * FROM slots 
           WHERE doctor_id = ? AND is_booked = 0 AND date >= date('now')
           ORDER BY date, time''',
        (doctor_id,)
    )
    slots = cursor.fetchall()
    conn.close()
    return slots


@app.route('/')
def index():
    return render_template('index.html', bot_token=BOT_TOKEN)


@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    user_text = data.get('text', '')
    result = analyze_symptoms(user_text)
    
    all_doctors = []
    seen_ids = set()
    
    for spec in result['specialists']:
        doctors = get_doctors_by_specialization(spec)
        for doc in doctors:
            doc_dict = dict(doc)
            if doc_dict['id'] not in seen_ids:
                seen_ids.add(doc_dict['id'])
                doc_dict['matched_specialization'] = spec
                all_doctors.append(doc_dict)
    
    return jsonify({
        'success': True,
        'analysis': result,
        'doctors': all_doctors[:5]
    })


@app.route('/doctor/<int:doctor_id>')
def doctor_detail(doctor_id):
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM doctors WHERE id = ?', (doctor_id,))
    doctor = cursor.fetchone()
    
    if not doctor:
        conn.close()
        return "Врач не найден", 404
    
    slots = get_available_slots(doctor_id)
    
    today = datetime.now().strftime('%Y-%m-%d')
    tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    
    conn.close()
    return render_template('doctor.html', 
                         doctor=doctor, 
                         slots=slots, 
                         today=today, 
                         tomorrow=tomorrow)


@app.route('/book', methods=['POST'])
def book_appointment():
    data = request.get_json()
    
    patient_name = data.get('patient_name', '').strip()
    patient_phone = data.get('patient_phone', '').strip()
    slot_id = data.get('slot_id')
    symptom_text = data.get('symptom_text', '').strip()
    recommended_specialist = data.get('recommended_specialist', '')
    telegram_chat_id = data.get('telegram_chat_id', '').strip()
    
    if not patient_name or not patient_phone or not slot_id:
        return jsonify({'success': False, 'message': 'Заполните все обязательные поля'})
    
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM slots WHERE id = ? AND is_booked = 0', (slot_id,))
    slot = cursor.fetchone()
    
    if not slot:
        conn.close()
        return jsonify({'success': False, 'message': 'Этот слот уже занят'})
    
    # Получаем информацию о враче
    cursor.execute('''
        SELECT doctors.name FROM slots 
        JOIN doctors ON slots.doctor_id = doctors.id 
        WHERE slots.id = ?
    ''', (slot_id,))
    doctor_info = cursor.fetchone()
    doctor_name = doctor_info['name'] if doctor_info else 'Врач'
    
    cursor.execute(
        '''INSERT INTO appointments (patient_name, patient_phone, slot_id, symptom_text, recommended_specialist, telegram_chat_id)
           VALUES (?, ?, ?, ?, ?, ?)''',
        (patient_name, patient_phone, slot_id, symptom_text, recommended_specialist, telegram_chat_id)
    )
    
    cursor.execute('UPDATE slots SET is_booked = 1 WHERE id = ?', (slot_id,))
    
    conn.commit()
    appointment_id = cursor.lastrowid
    conn.close()
    
    # Отправляем уведомление в Telegram если указан chat_id
    telegram_sent = False
    if telegram_chat_id:
        telegram_sent = send_appointment_notification(
            telegram_chat_id,
            patient_name,
            doctor_name,
            slot['date'],
            slot['time'],
            appointment_id
        )
    
    return jsonify({
        'success': True,
        'message': f'Вы успешно записаны! Номер записи: #{appointment_id}',
        'appointment_id': appointment_id,
        'doctor_name': doctor_name,
        'slot_date': slot['date'],
        'slot_time': slot['time'],
        'telegram_sent': telegram_sent
    })


@app.route('/doctors')
def doctors_list():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM doctors ORDER BY specialization')
    doctors = cursor.fetchall()
    conn.close()
    return render_template('doctors.html', doctors=doctors)


@app.route('/check/<int:appointment_id>')
def check_appointment(appointment_id):
    """Проверка записи по номеру"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT appointments.*, slots.date, slots.time, doctors.name as doctor_name 
        FROM appointments 
        JOIN slots ON appointments.slot_id = slots.id 
        JOIN doctors ON slots.doctor_id = doctors.id 
        WHERE appointments.id = ?
    ''', (appointment_id,))
    appointment = cursor.fetchone()
    conn.close()
    
    if not appointment:
        return render_template('check.html', found=False, appointment_id=appointment_id)
    
    return render_template('check.html', found=True, appointment=appointment)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5050))
    app.run(debug=False, host='0.0.0.0', port=port)