# 🎬 VideoSphere – YouTube Video Management System

A full-stack Flask web application to manage your personal YouTube video library.  
Users can **add, update, view, and delete videos** with details like title, duration, and URL.  
VidVault provides a clean interface and RESTful backend — perfect for organizing your YouTube watchlist.

---

## 🚀 Features

- 📜 List all videos  
- 🔍 View single video details  
- ➕ Add new videos  
- ✏️ Update existing videos  
- ❌ Delete videos  
- 🧱 RESTful API endpoints for Postman testing  
- 💾 SQLite (local) / PostgreSQL (cloud) database support  
- 🌐 Responsive UI using HTML, CSS, and JavaScript  
- ☁️ Deployable on Render  

---

## 🛠️ Tech Stack

**Backend:** Flask, SQLAlchemy, Flask-Migrate  
**Frontend:** HTML, CSS, JavaScript, Jinja2 Templates  
**Database:** SQLite (Development), PostgreSQL (Production)  
**Deployment:** Render  

---

## 📁 Project Structure

YouTube_Manager/
│
├── src/
│ ├── app/
│ │ ├── init.py # Flask app factory
│ │ ├── extensions.py # DB and migration setup
│ │ ├── models.py # Video model
│ │ ├── routes.py # Application routes (CRUD)
│ │ ├── forms.py # Flask-WTF forms
│ │ └── templates/ # HTML templates
│ │ ├── base.html
│ │ ├── index.html
│ │ ├── add_video.html
│ │ ├── edit_video.html
│ │ ├── view_video.html
│ │ └── components/
│ │ └── _video_list.html
│ ├── manage.py # Entry point for local runs
│ └── static/ # CSS, JS, images
│
├── requirements.txt
├── README.md
└── Procfile # For Render deployment


---

## ⚙️ Setup Instructions (Local)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/VideoSphere.git
cd VideoSphere

### 2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate      # For Windows
# or
source venv/bin/activate   # For Mac/Linux

### 4️⃣ Initialize the database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

### 5️⃣ Run the application
python src/manage.py


The app will run locally at:
➡️ http://127.0.0.1:5000/

### Future Enhancements

🔐 User authentication & login system

🎞️ YouTube API integration for automatic video metadata

📊 Video analytics dashboard

🌍 Multi-user video collections

### Author

B.K. Yadav
🚀 Full Stack Developer | Flask | React | PostgreSQL
kumarbisho02@gmail.com
https://www.linkedin.com/in/bisho-kumar-9485a126a/