from flask_app import app, load_config
load_config(app, "../config/app.json", "production")
