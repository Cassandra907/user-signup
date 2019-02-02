
from flask import Flask, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

app.run()