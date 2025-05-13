# TeleRAT - Telegram-Based Remote Access Framework (Educational Purposes Only)

⚠️ **Disclaimer**  
*This project is intended solely for academic research and educational purposes related to cybersecurity. Unauthorized use for malicious activities is strictly prohibited. The developers assume no liability for misuse.*

---

## Key Features
- **Telegram Bot C2** - Fully controlled via Telegram's Bot API
- **System Intelligence Gathering**  
  - Hardware/software inventory collection
  - Network configuration analysis
  - Process monitoring and management
- **File System Operations**  
  - Secure file upload/download via Telegram
  - Directory traversal capabilities
  - File search functionality
- **Persistence Mechanisms**  
  - Startup registration (Windows/Linux/Mac)
  - Process hiding techniques
- **Cross-Platform Support**  
  - Compatible with Windows 10/11, Linux, and macOS
  - Lightweight client (<2MB memory footprint)

---

## Academic Context
Developed as part of ongoing cybersecurity research into modern C2 (Command & Control) channels and their detection methodologies. This implementation demonstrates:

- Messaging platform vulnerabilities
- Cloud-based C2 infrastructure patterns
- Anti-forensic techniques in modern malware

---

## Installation

git clone https://github.com/y9y9/TeleRAT
cd TeleRAT
pip install -r requirements.txt


## Configuration
1. Create Telegram bot via [@BotFather](https://t.me/BotFather)
2. Add bot token to `setup.py`
