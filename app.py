from flask import Flask, render_template, url_for
from PIL import Image, ImageEnhance
import numpy as np
import os
app = Flask(__name__)

def reset():
    pass

def opacityById(ID, opacity):
    pass

@app.route("/")
def monopolysim():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
