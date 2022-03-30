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
    #return render_template("seeposts.html", map = "https://upload.wikimedia.org/wikipedia/commons/8/83/Equirectangular_projection_SW.jpg")

    m = open("marker_count.txt", "r")
    n = open("markers.txt", "r")

    current_m = int(m.read())
    current_n = n.read()

    m.close()
    n.close()

    return render_template("seeposts.html", content = current_n, size = current_m)

@app.route("/writetomarkers", methods=["POST", "GET"])
def writeToMarkers():
    m = open("marker_count.txt", "r")

    current_m = int(m.read())
    current_m += 1

    m.close()

    m = open("marker_count.txt", "w")

    m.write(str(current_m))

    m.close()
    
    output = request.form.to_dict()
#    text = output["text"]
#    lat = output["latitude"]
#    long = output["longitude"]
    
#    message = text + "|" + lat + "|" + long

    return render_template("makepost.html")

if __name__ == "__main__":
    app.run()

# The goal of this app is to show messages sent across space, not across time
# Messages are organized according to the lat/long of where they were sent from (rounded to int)