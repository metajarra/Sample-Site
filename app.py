import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def geo():
    return render_template("geo.html")

@app.route("/makepost")
def makepost():
    return render_template("makepost.html")

@app.route("/seeposts")
def seeposts():
    full_filename = os.path.join("images", "Equirectangular_projection_SW.png")
    return render_template("seeposts.html", map = "https://lumiere-a.akamaihd.net/v1/images/databank_watto_01_169_ecd563f1.jpeg?region=0%2C0%2C1560%2C780")

if __name__ == "__main__":
    app.run()

# The goal of this app is to show messages sent across space, not across time
# Messages are organized according to the lat/long of where they were sent from (rounded to int)