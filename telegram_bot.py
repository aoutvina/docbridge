import asyncio
from telegram import Bot
from telegram.error import TelegramError

import os
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

async def send_telegram_message(chat_id, message):
    """Отправка сообщения в Telegram"""
    try:
        bot = Bot(token=BOT_TOKEN)
        await bot.send_message(chat_id=chat_id, text=message, parse_mode='HTML')
        return True
    except TelegramError as e:
        print(f"Ошибка отправки в Telegram: {e}")
        return False

def send_appointment_notification(chat_id, patient_name, doctor_name, date, time, appointment_id):
    """Отправить уведомление о записи"""
    message = f"""
🏥 <b>DocBridge — Запись подтверждена!</b>

👤 <b>Пациент:</b> {patient_name}
👨‍⚕️ <b>Врач:</b> {doctor_name}
📅 <b>Дата:</b> {date}
🕐 <b>Время:</b> {time}
🔢 <b>Номер записи:</b> #{appointment_id}

Спасибо, что выбрали DocBridge! Мы напомним вам о приёме.
"""
    return asyncio.run(send_telegram_message(chat_id, message))

def send_reminder(chat_id, patient_name, doctor_name, time):
    """Отправить напоминание о приёме"""
    message = f"""
⏰ <b>Напоминание о приёме!</b>

👤 {patient_name}, ваш приём у врача <b>{doctor_name}</b> начнётся в <b>{time}</b>.

Пожалуйста, не опаздывайте!
"""
    return asyncio.run(send_telegram_message(chat_id, message))