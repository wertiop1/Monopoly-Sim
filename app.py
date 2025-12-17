from flask import Flask, render_template, url_for
from PIL import Image, ImageEnhance
import matrix as m
import numpy as np
import os
app = Flask(__name__)

@app.route("/")
def monopolysim():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
