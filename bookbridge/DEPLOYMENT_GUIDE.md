# Deployment Guide: BookBridge (Vivekananda Institute of Professional Studies)

This guide provides instructions to deploy the **BookBridge** campus book and learning-material exchange website to a live public URL for free.

---

## Pre-Configured Deployment Files Included

Your project directory already contains all the cloud configuration files needed:
- `requirements.txt`: Pinned Python dependencies (`Flask`, `gunicorn`, `Werkzeug`, `Jinja2`).
- `Procfile`: Production process file (`web: gunicorn wsgi:app`).
- `wsgi.py`: WSGI entry point with automatic SQLite database auto-seeding.
- `render.yaml`: 1-click Blueprint configuration for [Render.com](https://render.com).
- `runtime.txt`: Standard Python runtime specification (`python-3.11.9`).

---

## Option 1: Deploy on Render.com (Recommended – Free & Automated)

**Render** gives you a free live `https://...onrender.com` public URL with automated deployments whenever you update your code.

### Step 1: Push Code to GitHub
1. Open PowerShell or Terminal in `C:\Users\SANYA\.gemini\antigravity\scratch\bookbridge`.
2. Initialize git and commit your files:
   ```bash
   git init
   git add .
   git commit -m "Initial commit of BookBridge VIPS Portal"
   ```
3. Create a new repository on [GitHub](https://github.com/new) (e.g., `vips-bookbridge`).
4. Link and push your repository:
   ```bash
   git remote add origin https://github.com/<your-github-username>/vips-bookbridge.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy on Render
1. Visit [Render.com](https://render.com) and sign up / log in with your GitHub account.
2. Click **New +** in the top navigation and select **Web Service**.
3. Choose **Build and deploy from a Git repository** and connect your `vips-bookbridge` repo.
4. Render will auto-detect the configuration, or you can verify:
   - **Name:** `vips-bookbridge`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn wsgi:app`
   - **Instance Type:** `Free`
5. Click **Create Web Service**.
6. In 2–3 minutes, your website will be live at:
   `https://vips-bookbridge.onrender.com`

---

## Option 2: Deploy on PythonAnywhere (Free Forever – No Git Needed)

**PythonAnywhere** is an educational cloud host that lets you host Flask apps for free without credit cards.

1. Sign up for a free account at [PythonAnywhere.com](https://www.pythonanywhere.com/).
2. In your dashboard, open the **Web** tab and click **Add a new web app**.
3. Select **Flask** and choose **Python 3.10+**.
4. Set path to your project folder or use the Bash console to clone your repo:
   ```bash
   git clone https://github.com/<your-username>/vips-bookbridge.git
   ```
5. In the **Virtualenv** section, install requirements:
   ```bash
   pip install -r requirements.txt
   ```
6. In the **WSGI configuration file** link, set:
   ```python
   import sys
   path = '/home/<your-username>/vips-bookbridge'
   if path not in sys.path:
       sys.path.append(path)
   from app import app as application
   ```
7. Click the green **Reload** button. Your site is live at:
   `https://<your-username>.pythonanywhere.com`

---

## Option 3: Deploy on Railway.app

1. Sign up at [Railway.app](https://railway.app/) using GitHub.
2. Click **New Project** &rarr; **Deploy from GitHub repo**.
3. Select your `vips-bookbridge` repository.
4. Railway automatically detects `Procfile` and `requirements.txt` and starts `gunicorn wsgi:app`.
5. Under **Settings** &rarr; **Networking**, click **Generate Domain** to get a free live `.up.railway.app` URL.

---

## Option 4: Local Network / Campus Wi-Fi Live Demonstration

You can also run the website directly on your computer so anyone connected to the same Wi-Fi (such as faculty, friends, or evaluators) can access the live website from their mobile phones or laptops without internet hosting:

1. Double click `run.bat` or run:
   ```powershell
   python app.py
   ```
2. Find your local IP address in PowerShell:
   ```powershell
   ipconfig
   # Look for IPv4 Address, e.g., 192.168.1.45
   ```
3. Any device on the same Wi-Fi network can visit:
   `http://192.168.1.45:5000`
