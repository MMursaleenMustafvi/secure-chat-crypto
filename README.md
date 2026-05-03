# 🔐 SecureChat - Professional Encrypted Messaging System

A premium end-to-end encrypted chat application with real-time algorithm switching and modern UI.

## ✨ Features

### 🎨 Premium UI/UX
- Modern gradient design with glassmorphism effects
- Smooth animations and transitions
- Fully responsive mobile-first design
- Professional color scheme
- Clean and intuitive interface

### 🔒 Encryption Algorithms
- **AES** (Advanced Encryption Standard)
- **Caesar Cipher**
- **Affine Cipher**
- **Rail Fence Cipher**
- **Row Transposition**
- **Playfair Cipher**

### 🚀 Advanced Features
- **Real-time Algorithm Switching**: Change encryption during chat
- **Live Key Updates**: Modify encryption keys on the fly
- **Room-based Chat**: Multiple isolated chat rooms
- **Message Status**: Visual indicators for encrypted/decrypted messages
- **Auto-scroll**: Smooth message feed updates
- **Enter to Send**: Quick message sending

## 📦 Installation

### Prerequisites
```bash
Python 3.7+
pip
```

### Install Dependencies
```bash
pip install flask flask-socketio pycryptodome
```

## 🚀 Running the Application

```bash
python app.py
```

Visit: `http://localhost:5000`

## 📖 How to Use

### 1. Join a Room
- Enter your name
- Choose a room ID (same for all participants)
- Select encryption algorithm
- Enter encryption key
- Click "Join Secure Room"

### 2. Chat Features
- **Send Messages**: Type and press Enter or click Send
- **Change Algorithm**: Use dropdown to switch encryption method during chat
- **Update Key**: Modify the encryption key anytime
- **View Status**: Lock icons show if messages are encrypted/decrypted

### 3. Algorithm Key Formats

| Algorithm | Key Format | Example |
|-----------|-----------|---------|
| AES | Any text (16 chars recommended) | `mySecretKey123` |
| Caesar | Number (shift value) | `3` |
| Affine | Two numbers: a,b | `5,8` |
| Rail Fence | Number of rails | `3` |
| Row Transposition | Keyword | `SECRET` |
| Playfair | Keyword | `MONARCHY` |

## 🏗️ Project Structure

```
SecureChat/
├── app.py                 # Main Flask application
├── crypto/                # Encryption algorithms
│   ├── __init__.py
│   ├── aes.py
│   ├── caesar.py
│   ├── affine.py
│   ├── railfence.py
│   ├── row_transposition.py
│   └── playfair.py
├── templates/             # HTML templates
│   ├── index.html        # Join page
│   └── chat.html         # Chat interface
└── README.md
```

## 🔐 Security Notes

⚠️ **Important**: This is a demonstration application. For production use:
- Implement proper key exchange mechanisms
- Use HTTPS/WSS for transport layer security
- Add user authentication
- Implement proper key management
- Use stronger encryption modes (not ECB for AES)
- Add message integrity verification

## 🎓 Educational Purpose

This application demonstrates:
- Classical and modern cryptography
- Real-time web socket communication
- Full-stack web development
- Encryption algorithm implementation
- Modern UI/UX design principles

## 👨‍💻 Developers

**Muhammad Mursaleen Mustafvi**  
**Muhammad Bin Talib**

## 📄 License

Educational and demonstration purposes only.

## 🙏 Acknowledgments

Built with:
- Flask & Flask-SocketIO
- Socket.IO
- PyCryptodome
- Font Awesome
- Google Fonts (Inter)

---

**Made with ❤️ for secure communication**