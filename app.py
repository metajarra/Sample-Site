from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():

    # Load current count
#    f = open("marker_count.txt", "r")
#    count = int(f.read())
#    f.close()

    # Increment the count
#    count += 1

    # Overwrite the count
#    f = open("marker_count.txt", "w")
#    f.write(str(count))
#    f.close()

#    g = open("markers.txt", "r")
#    gcontent = str(g.read())
#    g.close()

#    g = open("markers.txt", "w")
#    newMarker = gcontent + "MX|latitude|longitude|content"
#    g.write(str(newMarker))
#    g.close()

    # Render HTML with count variable
    return render_template("geo.html")

if __name__ == "__main__":
    app.run()

# The goal of this app is to show messages sent across space, not across time
# Messages are organized according to the lat/long of where they were sent from (rounded to int)