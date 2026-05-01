# DocBridge — Smart Doctor Appointment System

> Symptom-based doctor appointment system with voice input and Telegram notifications.

**Deployed:** https://docbridge-770d.onrender.com

---

## About

DocBridge helps patients find the right doctor by analyzing symptoms. Describe your symptom via **text or voice**, get a specialist recommendation, and book an appointment instantly.

## Features

- 🎤 Voice input (Web Speech API, Russian)
- 🧠 Symptom analysis (82 keywords, 8 specializations)
- ⚠️ Emergency detection (heart attack, stroke, fever)
- 👨‍⚕️ Doctor matching with profiles
- 📅 Slot booking (7-day availability)
- 📱 Telegram notifications
- 🔍 Appointment lookup by ID

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python + Flask |
| Database | SQLite |
| Frontend | HTML + CSS + JavaScript |
| Voice | Web Speech API |
| Alerts | python-telegram-bot |
| Deployment | Render |

## Run Locally

```bash
git clone https://github.com/aoutvina/docbridge.git
cd docbridge
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
Open http://127.0.0.1:5050

Project Structure
text
docbridge/
├── app.py
├── models.py
├── symptom_analyzer.py
├── telegram_bot.py
├── static/css/style.css
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── doctors.html
│   ├── doctor.html
│   └── check.html
└── screenshots/
Team
Name	Student ID	Role
Khudaiberganova Elvina	240103122	Project Lead & Backend
Aidarbekkyzy Aigerim	240103117	Frontend & UI/UX
Kemalova Ayaulym	240103119	Database & Testing
Akylbekkyzy Nazerke	240103204	Documentation
SDU University | INF395 | Spring 2026

text

---

## Шаг 2: Запушь

```bash
git add README.md
git commit -m "Add README"
git push
Напиши "README готов".

вообще read me должен быть идеальным не так? не просто тексты а реально репрезент твоего продукта с фотками итд
Ты права. README — это лицо проекта. Сделаем красивый, с эмодзи, бейджами, скриншотами — как у настоящих стартапов на GitHub.

Замени README.md полностью:
markdown
<div align="center">

<img src="screenshots/image-2.png" alt="DocBridge" width="600"/>

# 🏥 DocBridge

### Intelligent Symptom-Based Doctor Appointment System

[![Deployed](https://img.shields.io/badge/Live-Render-2563eb?style=for-the-badge)](https://docbridge-770d.onrender.com)
[![GitHub](https://img.shields.io/badge/Repo-GitHub-black?style=for-the-badge)](https://github.com/aoutvina/docbridge)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1-000000?style=flat-square&logo=flask)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-Academic-blue?style=flat-square)]()

</div>

---

## 📖 Overview

DocBridge bridges the gap between **patients and the right doctors**. Instead of guessing which specialist to visit, users describe their symptoms via **text or voice**, and the system instantly recommends the appropriate medical specialist — then books the appointment.

> 🔗 **Try it now:** [docbridge-770d.onrender.com](https://docbridge-770d.onrender.com)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎤 **Voice Input** | Speak your symptoms in Russian — Web Speech API handles the rest |
| 🧠 **Smart Analysis** | Rule-based expert system with **82 keywords** across **8 specializations** |
| ⚠️ **Emergency Detection** | Identifies heart attack, stroke, and critical fever symptoms |
| 👨‍⚕️ **Doctor Matching** | Finds available doctors matching the recommended specialization |
| 📅 **Slot Booking** | 7-day availability with real-time double-booking prevention |
| 📱 **Telegram Alerts** | Instant booking confirmation via Telegram Bot |
| 🔍 **Appointment Lookup** | Check your booking by ID number |
| 📱 **Responsive** | Works on desktop and mobile (375px+) |

---

## 🖼️ Screenshots

<div align="center">

| | | |
|---|---|---|
| **Homepage** | **Analysis Results** | **Doctor Slots** |
| ![Home](screenshots/image-2.png) | ![Analysis](screenshots/image-3.png) | ![Slots](screenshots/image-4.png) |
| **Booking Confirmation** | **Telegram Notification** | |
| ![Confirmation](screenshots/image-5.png) | ![Telegram](screenshots/image-6.png) | |

</div>

---

## 🛠 Tech Stack

| Layer | Technology | Version |
|---|---|---|
| Backend | Python + Flask | 3.11 / 3.1 |
| Database | SQLite | 3 |
| Frontend | HTML5 + CSS3 + Vanilla JS | — |
| Voice | Web Speech API (Chrome) | W3C |
| Alerts | python-telegram-bot | 22.7 |
| Server | Gunicorn | 25.3 |
| Hosting | Render | Free Tier |

---

## 📁 Project Structure
docbridge/
├── app.py # Flask routes & logic
├── models.py # Database schema & seed data
├── symptom_analyzer.py # 82-keyword expert system
├── telegram_bot.py # Telegram notification module
├── requirements.txt # Python dependencies
├── static/
│ └── css/
│ └── style.css # Custom design system
├── templates/
│ ├── base.html # Layout shell
│ ├── index.html # Homepage (symptom input)
│ ├── doctors.html # Doctor gallery
│ ├── doctor.html # Doctor profile + booking
│ └── check.html # Appointment lookup
└── screenshots/ # Project screenshots

text

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Chrome browser (for voice input)

### Local Setup

```bash
# Clone the repo
git clone https://github.com/aoutvina/docbridge.git
cd docbridge

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run
python app.py
Open http://127.0.0.1:5050

Telegram Bot Setup (Optional)
Create a bot via @BotFather

Get your token

Add token to telegram_bot.py or set BOT_TOKEN environment variable

🧪 Usage Flow
text
1. Open homepage
2. Describe symptom: "болит горло, температура 38"
      ↓
3. System analyzes → recommends ENT + Therapist
      ↓
4. Select doctor → choose time slot
      ↓
5. Fill name & phone → confirm booking
      ↓
6. Receive Telegram notification ✅
📊 Testing
23 test cases — 100% pass rate.

Category	Tests	Passed
Symptom Analysis	10	✅ 10
Booking System	6	✅ 6
UI/UX	6	✅ 6
Integration	4	✅ 4
👥 Team
Name	ID	Role
Khudaiberganova Elvina	240103122	Project Lead & Backend Developer
Aidarbekkyzy Aigerim	240103117	Frontend Developer & UI/UX Designer
Kemalova Ayaulym	240103119	Database Engineer & Tester
Akylbekkyzy Nazerke	240103204	Technical Writer & QA
📄 Documentation
Full report: REPORT.md

Deployed URL: docbridge-770d.onrender.com

🔮 Future Roadmap
User authentication (login/register)

PostgreSQL migration

Admin dashboard for clinics

Cancel & reschedule appointments

SMS notifications (Twilio)

Kazakh language voice support

<div align="center">
SDU University • INF395 • Spring 2026

</div> ```