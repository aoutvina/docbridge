# DocBridge — Smart Doctor Appointment System

**Course:** INF395 — Advanced Project for Information Systems  
**Instructor:** Sufyan Mustafa bin Uzayr  
**University:** SDU University  
**Semester:** Spring 2026  

**Deployed URL:** https://docbridge-770d.onrender.com  
**GitHub:** https://github.com/aoutvina/docbridge

---

## 1. Team Members

| # | Full Name | Student ID | Role |
|---|---|---|---|
| 1 | Khudaiberganova Elvina | 240103122 | Project Lead & Backend (Flask, Analyzer, Telegram Bot, Deploy) |
| 2 | Aidarbekkyzy Aigerim | 240103117 | Frontend (HTML, CSS, JS, Voice API) |
| 3 | Kemalova Ayaulym | 240103119 | Database & Testing (Schema, Seeds, QA) |
| 4 | Akylbekkyzy Nazerke | 240103204 | Documentation & Report |

---

## 2. Problem Definition

Patients often don't know which doctor to visit. ~34% of initial specialist visits in Kazakhstan are misdirected. Elderly users struggle with complex interfaces. DocBridge solves this by analyzing symptoms and recommending the right specialist.

**Objectives:**
- Voice/text symptom input (Russian)
- Rule-based analysis (82 keywords, 8 specializations)
- Instant booking with Telegram confirmation
- Deployed as live web app

---

## 3. System Design

### 3.1 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.11 + Flask 3.1 |
| Database | SQLite |
| Frontend | HTML5 + CSS3 + JavaScript |
| Voice | Web Speech API (Chrome) |
| Alerts | python-telegram-bot |
| Server | Gunicorn |
| Hosting | Render (Free) |

### 3.2 Database Schema

**doctors:** id, name, specialization, experience_years, photo_url, description

**slots:** id, doctor_id (FK), date, time, is_booked

**appointments:** id, patient_name, patient_phone, slot_id (FK), symptom_text, recommended_specialist, telegram_chat_id, created_at

### 3.3 API Routes

| Route | Method | Purpose |
|---|---|---|
| `/` | GET | Homepage |
| `/analyze` | POST | Symptom analysis |
| `/doctor/<id>` | GET | Doctor + slots |
| `/book` | POST | Create appointment |
| `/doctors` | GET | All doctors |
| `/check/<id>` | GET | Lookup booking |

---

## 4. Implementation

### 4.1 Symptom Analyzer

Rule-based expert system. 82 keywords across 8 specializations.

| Specialization | Keywords |
|---|---|
| Терапевт | температура, кашель, слабость, грипп |
| ЛОР | горло, ухо, нос, насморк, ангина |
| Невролог | голова, спина, мигрень, онемение |
| Кардиолог | сердце, аритмия, давление |
| Дерматолог | сыпь, кожа, зуд, акне |
| Гастроэнтеролог | живот, тошнота, изжога |
| Окулист | глаз, зрение |
| Стоматолог | зуб, десна, кариес |

**Emergency Detection:**
- сердце + боль + давит → Heart attack warning
- голова + сильная + резкая → Stroke warning
- температура + 40 → Critical fever warning

### 4.2 Key Features

- Voice input via Web Speech API (lang: ru-RU)
- Slot booking with double-booking prevention
- Telegram notification via python-telegram-bot
- Lazy DB initialization (auto-creates on first run)

---

## 5. Screenshots

![Homepage](screenshots/image-2.png)

![Analysis](screenshots/image-3.png)

![Slots](screenshots/image-4.png)

![Confirmation](screenshots/image-5.png)

![Telegram](screenshots/image-6.png)

---

## 6. Innovation

| Feature | Impact |
|---|---|
| Voice-to-Appointment | Accessibility for elderly |
| 82-rule Expert System | Zero cost, 100% explainable |
| Emergency Detection | Real clinical value |
| Telegram Integration | Most popular messenger in KZ |
| Live Deployment | Accessible anywhere |

---

## 7. Testing

**23 test cases, 100% pass rate.**

| Category | Tests | Result |
|---|---|---|
| Symptom Analysis | 10 | 10/10 |
| Booking System | 6 | 6/6 |
| UI/UX | 6 | 6/6 |
| Integration | 4 | 4/4 |

**Bugs Fixed:**
- SyntaxError in analyzer (missing bracket)
- UndefinedError on homepage (wrong variable)
- Port 5000 conflict (changed to 5050)
- Gunicorn not found (added to requirements.txt)

---

## 8. Open Source

| Component | License |
|---|---|
| Python | PSF |
| Flask | BSD-3-Clause |
| SQLite | Public Domain |
| Gunicorn | MIT |
| python-telegram-bot | LGPLv3 |
| Web Speech API | W3C Standard |

---

## 9. Conclusion

**Achievements:** Working MVP, voice input, 82-keyword engine, emergency detection, Telegram alerts, live deployment, zero cost.

**Future Work:** User authentication, PostgreSQL migration, admin dashboard, Kazakh language support.

---

**Student IDs:**
- Khudaiberganova Elvina — 240103122
- Aidarbekkyzy Aigerim — 240103117
- Kemalova Ayaulym — 240103119
- Akylbekkyzy Nazerke — 240103204