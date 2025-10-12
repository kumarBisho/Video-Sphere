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

## 📁 Project structure

Root layout (actual):

```
DockerFile
requirements.txt
README.md
src/
	├─ manager.py            # application entry (run with `python -m src.manager`)
	└─ app/
		 ├─ __init__.py        # Flask app factory
		 ├─ api.py             # API endpoints
		 ├─ config.py          # configuration
		 ├─ extensions.py      # DB, migrations, other extensions
		 ├─ forms.py           # Flask-WTF forms
		 ├─ models.py          # SQLAlchemy models
		 ├─ routes.py          # web routes (views)
		 └─ templates/         # Jinja2 templates

static/
	├─ css/
	│  └─ styles.css
	└─ js/
		 └─ main.js
```

Notes:
- Static assets live at the repository root under `static/`.
- Application code is under `src/` and the app package is `src.app`.

---

## ⚙️ Local setup & development (PowerShell)

Minimum prerequisites
- Python 3.8+ (3.10+ recommended)
- pip
- (optional) Docker if you want to build the container locally

1) Clone the repository

```powershell
git clone https://github.com/<your-username>/Video-Sphere.git
cd "C:\Users\BK Yadav\OneDrive\Desktop\All_software_activity\YouTube_Manager"
```

2) Create & activate a virtual environment (PowerShell)

```powershell
python -m venv .venv
# PowerShell (recommended)
. .\.venv\Scripts\Activate.ps1
# If you get an execution policy error, run (temporary for the session):
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
. .\.venv\Scripts\Activate.ps1
```

3) Install Python dependencies

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

4) Environment variables (example)

Set these in your shell or create a `.env` if you use python-dotenv.

```powershell
$env:FLASK_APP = 'src.manager'
$env:FLASK_ENV = 'development'
# Example DB URL (SQLite file in project root)
$env:DATABASE_URL = "sqlite:///./dev.db"
```

5) Initialize database (if using Flask-Migrate)

```powershell
# only if Flask-Migrate is used in the project
flask db init           # only first time
flask db migrate -m "Initial"
flask db upgrade
```

6) Run the application

```powershell
# recommended: run via module so package imports work reliably
python -m src.manager

# OR (if manager.py is executable)
python src\manager.py
```

The app should be available at http://127.0.0.1:5000/ unless configured otherwise.

---

## 📦 Docker (build & run)

Build the image using the repository `DockerFile` and run locally:

```powershell
docker build -f DockerFile -t yourname/video-sphere:latest .
docker run -p 5000:5000 yourname/video-sphere:latest
```

To push to GitHub Container Registry (GHCR):

```powershell
# tag and push (after logging in with a PAT if needed)
docker tag yourname/video-sphere:latest ghcr.io/<owner>/video-sphere:latest
docker push ghcr.io/<owner>/video-sphere:latest
```

Note: A GitHub Actions workflow was added to build and push images automatically (see `.github/workflows/docker-build-push.yml`).

---

## 🩺 Troubleshooting

- Virtual env activation fails in PowerShell: run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` then activate.
- If imports fail, prefer running the app with `python -m src.manager` from the repository root.
- If database migrations are missing, re-run `flask db migrate` and `flask db upgrade`.

---

If you want I can also:
- Add an example `.env.example` file with common environment variables
- Add a Makefile or PowerShell script to automate setup
- Update the GitHub Actions workflow to publish to Docker Hub instead of GHCR

### Author

B.K. Yadav
🚀 Full Stack Developer | Flask | React | PostgreSQL
kumarbisho02@gmail.com
https://www.linkedin.com/in/bisho-kumar-9485a126a/