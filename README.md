<!-- PROJECT LOGO -->
<p align="center">
  <img src="https://img.icons8.com/external-others-iconmarket/96/000000/external-AI-artificial-intelligence-others-iconmarket.png" width="100" alt="HOMI Logo">
</p>

<h1 align="center">🤖 HOMI — Your Personal PC Manager Bot</h1>

<p align="center">
  <em>Inspired by Dr. Homi J. Bhabha — India's visionary scientist</em><br>
  Built with 💻 Python automation and powered by 🧠 innovation.
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python"></a>
  <a href="https://github.com/<your-username>/HOMI/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"></a>
  <a href="https://github.com/<your-username>/HOMI/stargazers"><img src="https://img.shields.io/github/stars/<your-username>/HOMI?style=social" alt="Stars"></a>
  <a href="https://github.com/<your-username>/HOMI/forks"><img src="https://img.shields.io/github/forks/<your-username>/HOMI?style=social" alt="Forks"></a>
  <a href="#"><img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey.svg" alt="Platform"></a>
</p>

---

## 🧠 Overview

**HOMI** is an intelligent automation bot designed to act as your **personal PC manager**, controllable entirely through **WhatsApp commands**.  
It can automate daily PC tasks, monitor activity, send or reply to messages, and even capture screenshots — all remotely and securely.

Built using powerful Python libraries like `pyautogui`, `opencv`, and `pywhatkit`, HOMI merges **automation** with **communication** — creating a seamless bridge between your smartphone and computer.

---

## ⚙️ Features

### 💬 WhatsApp Command Control
Control your entire system with WhatsApp messages — no need for physical access to your PC!

### 🧠 Admin Authentication
Differentiates between **admin** and **guest users** to ensure data privacy and secure access.

### 🖱️ Screen & Pixel Automation
Detect pixels and visual cues on the screen using `pyautogui` and `opencv`, then act accordingly (click, scroll, type, open files, etc.).

### 🪟 Remote Monitoring
Request screenshots or view active windows right from your phone.

### 🎥 Camera & Microphone Access
Activate your webcam or microphone remotely (admin-only access).

### 💻 System Process Tracking
Check which programs are running on your computer in real time.

### ⏰ Task & Message Scheduling
Schedule WhatsApp messages or automated PC tasks to run later — even when you’re away.

### 🤖 Auto Chat Mode
HOMI can reply to WhatsApp messages or chat automatically on your behalf.

---

## 🧩 Tech Stack

| Category | Technologies Used |
|-----------|------------------|
| **Language** | Python 🐍 |
| **Automation** | `pyautogui`, `schedule`, `os`, `subprocess` |
| **Communication** | `pywhatkit`, WhatsApp Web |
| **Vision** | `opencv-python` |
| **Utilities** | `datetime`, `time`, `json` |

---

## 🔐 Security

HOMI ensures secure operations by:
- Limiting sensitive features (camera/mic) to admin users  
- Verifying commands before execution  
- Restricting potentially harmful actions  

---

## 🧭 Future Enhancements

| Feature | Description |
|----------|--------------|
| 🗣️ Voice Command Integration | Control HOMI using speech recognition |
| 🤖 NLP Command Understanding | Interpret natural language commands |
| 🌐 Web Dashboard | Monitor PC activity in real time |
| 📱 Multi-Device Support | Control multiple PCs via a single interface |

---

## 🪶 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/HOMI.git
   cd HOMI

