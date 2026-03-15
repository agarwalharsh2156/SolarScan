# SolarProject-Django

A Django-based solar panel detection and history tracking web app with object detection, user accounts, and a simple UI. This repo contains a full Django project with the backend app code, models, views, and templates.

## ✅ Project Structure

- `backend/` — Django project root
  - `accounts/` — user registration/login and authentication
  - `detections/` — object detection features (YOLO model, image uploads)
  - `history/` — detection history and result tracking
  - `config/` — Django settings, URLs, ASGI/WGI
  - `templates/`— base templates and shared layout
  - `static/` — CSS and static assets
  - `media/` — uploaded images and generated outputs

## 🚀 Quick Start

### 1) Activate virtual environment

Windows PowerShell:
```powershell
cd d:\MyProjects\SolarProject-Django
.\django-env\Scripts\Activate.ps1
```

### 2) Install dependencies

```powershell
cd backend
pip install -r requirements.txt
```

### 3) Apply migrations

```powershell
python manage.py migrate
```

### 4) Create a superuser

```powershell
python manage.py createsuperuser
```

### 5) Run development server

```powershell
python manage.py runserver
```

Open `http://127.0.0.1:8000` in your browser.

## 🧠 Notes

- The app stores uploaded satellite images in `backend/media/satellite_images/`.
- Detection uses YOLO model weights in `backend/detections/best.pt`.
- Keep the model file size tracked outside git (ignored in `.gitignore`).

## 📁 Common Commands

```bash
# Run tests
python manage.py test

# Collect static files (for deployment)
python manage.py collectstatic

# Open Django shell
python manage.py shell
```

## 🧰 Recommended Workflow

1. Create a feature branch
2. Make your changes and run `python manage.py test`
3. Commit with clear messages
4. Push and open a PR

## 📌 Deploying (Production)

For production, configure:
- `DEBUG=False`
- secure `SECRET_KEY`
- allowed hosts in `config/settings.py`
- a production DB (PostgreSQL recommended)
- static/media hosting (e.g., AWS S3)

## 🙏 Contributing

1. Fork the repo
2. Create a branch: `feature/<name>`
3. Push your changes
4. Open a PR

## 📄 License

This project is provided without a license file by default. Add a `LICENSE` if needed.
