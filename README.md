# 🚘 ParkirAI: Smart Parking Management System Based on YOLOv8

ParkirAI is a modern parking management solution that leverages **Computer Vision** and **Deep Learning** to automatically detect and monitor vehicles. Built with **Flask** and integrated with **YOLOv8**, this system supports real-time surveillance, vehicle tracking, and user data management via a responsive web interface.

---

## 🌟 Key Features

- **🧠 Automatic Vehicle Detection**  
  Real-time vehicle detection using YOLOv8 — supports various types of vehicles including cars, motorcycles, and trucks.

- **🎥 Smart Tracking**  
  Track vehicles entering and exiting the parking area using *Object Tracking* modules with virtual lines.

- **🧾 User (Student) Management**  
  Registration and management system for users based on license plate and campus ID.

- **🅿️ Real-Time Parking Slot Monitoring**  
  Automatically updated parking slot status (available/occupied) based on visual detection.

- **📚 Automatic Log History**  
  Records vehicle entry and exit times automatically and stores them in the system log.

- **🛠️ Integrated Admin Panel**  
  Full access for managing user data, statistics, and system settings.

- **🔔 Real-Time Notifications**  
  Instant system updates via WebSocket so the admin always receives the latest information.

- **📱 Modern & Responsive UI**  
  HTML5 and CSS-based interface that works well on both desktop and mobile devices.

---

## ⚙️ Technologies Used

### Backend
- **Flask (v2.3.3)** – Main web framework
- **SQLAlchemy & Flask-Migrate** – ORM and database migration
- **Flask-SocketIO** – Real-time communication
- **Flask-Session** – Session management

### Computer Vision & AI
- **YOLOv8 (Ultralytics)** – Vehicle object detection
- **OpenCV** – Image/video preprocessing and streaming
- **NumPy & Pillow** – Image and numerical data manipulation

### Database
- **SQLite** – For development
- **Migration support** for production deployment (e.g., PostgreSQL)

### Development Tools
- **pytest** – Unit testing
- **Black, Flake8, MyPy** – Code formatting, linting, and type checking
- **Optional: Docker, Gunicorn** – Deployment

---

## 📦 System Requirements

- Python 3.10+
- Webcam or IP camera
- Minimum 4GB RAM (8GB recommended)
- GPU (optional, for better inference performance)

---

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ParkirAI.git
cd ParkirAI
```

### 2. Activate Virtual Environment
```bash
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python run.py
```

Access the app at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧠 Detection Configuration

Configuration file: `app/config.py`

```python
MODEL_PATH = "app/ml/best.pt"
CONFIDENCE_THRESHOLD = 0.6
IOU_THRESHOLD = 0.5

ENTRY_LINE = [(258, 312), (388, 248)]   # Entry detection line
EXIT_LINE = [(287, 341), (420, 267)]    # Exit detection line
```

---

## 🗂️ Project Structure

```
Parking-system-/
├── app/
│   ├── api/                 # API routes
│   ├── ml/                  # Machine Learning modules
│   │   ├── detector.py      # YOLOv8 detector
│   │   ├── tracker.py       # Vehicle tracking
│   │   └── best.pt          # Trained model
│   ├── models/              # Database models
│   ├── services/            # Business logic
│   ├── routes/              # Web routes
│   ├── templates/           # HTML templates
│   ├── static/              # CSS, JS, images
│   ├── utils/               # Utility functions
│   └── websocket/           # WebSocket events
├── instance/                # Database files
├── flask_session/           # Session files
├── logs/                    # Application logs
├── tests/                   # Unit tests
└── requirements.txt         # Dependencies
```

---

## 📊 User Modes

### 🛠️ Admin Panel
- Default login: `admin` / `admin123`
- Change password after first login
- Manage user data, monitor parking slots, and view vehicle logs

### 👤 Student Mode
- Register with student ID and license plate number
- The system will automatically recognize the vehicle upon entry/exit

---

## 🧪 Testing

```bash
# Run all unit tests
pytest

# Run with coverage
pytest --cov=app
```

---

## 🔐 Security

- **Session Security:** HttpOnly cookies, SameSite, 30-minute timeout
- **Database:** Regular backups, do not share `.db` files
- **Production:** Ensure `DEBUG = False`, use HTTPS
- **Dependencies:** Regular updates for security patches

---

## 📦 Deployment

### Docker (Optional)
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:create_app()"]
```

### Production Checklist
- [ ] Set `DEBUG = False`
- [ ] Use production database (e.g., PostgreSQL)
- [ ] Setup reverse proxy (e.g., Nginx)
- [ ] Enable SSL/TLS
- [ ] Regular database backups

---

## 📝 Important Notes

This project is an original work created as a practical solution to parking management issues in campus or public environments. **Any form of plagiarism or unauthorized use is strictly prohibited** and unethical.

---

## 💬 Support & Contributions

If you encounter any issues:
1. Check the troubleshooting section
2. Search for existing issues
3. Create a new issue with detailed information

### How to Contribute
1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Create a Pull Request


