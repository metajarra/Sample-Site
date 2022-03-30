import os
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
@app.route("/geo")
def geo():
    return render_template("geo.html")

@app.route("/makepost")
def makepost():
    return render_template("makepost.html")

@app.route("/seeposts")
def seeposts():
    return render_template("seeposts.html", map = "https://upload.wikimedia.org/wikipedia/commons/8/83/Equirectangular_projection_SW.jpg")

@app.route("/writetomarkers", methods=["POST", "GET"])
def writeToMarkers():    
    output = request.form.to_dict()
    text = output["text"]
    lat = output["latitude"]
    long = output["longitude"]
    
    message = text + "|" + lat + "|" + long

    m = open("marker_count.txt", "r")
    n = open("markers.txt", "r")

    current_m = int(m.read())
    current_m += 1

    current_n = n.read()

    m.close()
    n.close()

    m = open("marker_count.txt", "w")
    n = open("markers.txt", "w")

    m.write(str(current_m))
    n.write(current_n + "\n" + message)

    m.close()
    n.close()

    return render_template("makepost.html")

if __name__ == "__main__":
    app.run()

# The goal of this app is to show messages sent across space, not across time
# Messages are organized according to the lat/long of where they were sent from (rounded to int)