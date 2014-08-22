import os
import json
from flask import Flask, render_template

app = Flask(__name__)

def load_config(app, relative_path, environment):
  config = None
  with open(os.path.join(app.root_path, relative_path), "r") as rf:
    config = json.load(rf)
  app.config.update(config[environment])

from . import controllers
