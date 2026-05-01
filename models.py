import sqlite3
from datetime import datetime, timedelta
import random

DATABASE = 'docbridge.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            specialization TEXT NOT NULL,
            experience_years INTEGER,
            photo_url TEXT,
            description TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS slots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doctor_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            is_booked INTEGER DEFAULT 0,
            FOREIGN KEY (doctor_id) REFERENCES doctors (id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT NOT NULL,
            patient_phone TEXT NOT NULL,
            slot_id INTEGER NOT NULL,
            symptom_text TEXT,
            recommended_specialist TEXT,
            telegram_chat_id TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (slot_id) REFERENCES slots (id)
        )
    ''')
    
    conn.commit()
    conn.close()

def seed_data():
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM doctors')
    if cursor.fetchone()[0] > 0:
        conn.close()
        return
    
    doctors = [
        ('Айжанова Айгуль', 'Терапевт', 12, '👩‍⚕️', 'Врач общей практики. Диагностика и лечение широкого спектра заболеваний.'),
        ('Муратов Бауыржан', 'ЛОР (оториноларинголог)', 8, '👨‍⚕️', 'Лечение заболеваний уха, горла, носа.'),
        ('Касенова Динара', 'Невролог', 15, '👩‍⚕️', 'Диагностика и лечение заболеваний нервной системы.'),
        ('Сериков Ерлан', 'Кардиолог', 10, '👨‍⚕️', 'Лечение сердечно-сосудистых заболеваний.'),
        ('Нурланова Асель', 'Дерматолог', 7, '👩‍⚕️', 'Лечение кожных заболеваний.'),
        ('Тулегенов Асхат', 'Гастроэнтеролог', 9, '👨‍⚕️', 'Лечение заболеваний ЖКТ.'),
        ('Искакова Мадина', 'Окулист (офтальмолог)', 11, '👩‍⚕️', 'Диагностика и коррекция зрения.'),
        ('Садыков Нурлан', 'Стоматолог', 6, '👨‍⚕️', 'Лечение и протезирование зубов.'),
    ]
    
    for doc in doctors:
        cursor.execute(
            'INSERT INTO doctors (name, specialization, experience_years, photo_url, description) VALUES (?, ?, ?, ?, ?)',
            doc
        )
    
    doctor_ids = [1, 2, 3, 4, 5, 6, 7, 8]
    time_slots = ['09:00', '10:00', '11:00', '14:00', '15:00', '16:00']
    
    for day_offset in range(7):
        date = (datetime.now() + timedelta(days=day_offset + 1)).strftime('%Y-%m-%d')
        for doc_id in doctor_ids:
            random.shuffle(time_slots)
            for time in time_slots[:4]:
                cursor.execute(
                    'INSERT INTO slots (doctor_id, date, time, is_booked) VALUES (?, ?, ?, 0)',
                    (doc_id, date, time)
                )
    
    conn.commit()
    conn.close()
    print("База данных создана и заполнена!")