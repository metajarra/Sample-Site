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
    return render_template("seeposts.html", map = "./images/Equirectangular_projection_SW.png")

if __name__ == "__main__":
    app.run()

# The goal of this app is to show messages sent across space, not across time
# Messages are organized according to the lat/long of where they were sent from (rounded to int)