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
    return render_template("seeposts.html", map = "https://upload.wikimedia.org/wikipedia/commons/8/83/Equirectangular_projection_SW.jpg")

@app.route("/writetomarkers")
def writeToMarkers(text, lat, long):
    message = text + "|" + lat + "|" + long

    m = open("marker_count.txt", "r")
    n = open("markers.txt", "r")

    current_m = int(m.read())
    current_n = n.read()

    m.close()
    n.close()

    new_m = current_m + 1
    new_n = current_n + "\n" + message

    m = open("marker_count.txt", "w")
    n = open("markers.txt", "w")

    m.write(new_m)
    n.write(new_n)

    m.close()
    n.close()

    print("deez")

if __name__ == "__main__":
    app.run()

# The goal of this app is to show messages sent across space, not across time
# Messages are organized according to the lat/long of where they were sent from (rounded to int)