from datetime import datetime
from flask import Flask, session, g, render_template
app = Flask(__name__)

from flask_website.views import base
app.register_blueprint(base.mod)