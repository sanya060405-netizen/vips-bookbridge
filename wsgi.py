"""
WSGI Entry Point for Production Cloud Deployment (Render, Railway, Heroku, PythonAnywhere)
BookBridge: Vivekananda Institute of Professional Studies
"""
import os
from app import app, ensure_db

# Ensure production database schema and default records exist on cold start
ensure_db()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
