# 🔐 Encrypt Decrypt Web App

A simple encryption and decryption tool using AES (Advanced Encryption Standard), built with Flask and JavaScript.

## ✨ Features
- Encrypt large messages
- Decrypt using the same key
- Clean frontend UI
- Secure AES encryption (CBC mode with SHA-256 key)

## 📁 Structure

- `app.py` – Flask routes
- `templates/` – HTML UI
- `static/` – CSS
- `crypto/aes_util.py` – AES logic
- `requirements.txt` – dependencies

## 🚀 Run Locally

```bash
pip install -r requirements.txt
python app.py
