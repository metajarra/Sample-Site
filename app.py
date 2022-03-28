from flask import Flask, render_template

app = Flask(__name__)

#@app.route("/")
#def index():

    # Load current count
#    f = open("count.txt", "r")
#    count = int(f.read())
#    f.close()

    # Increment the count
#    count += 1

    # Overwrite the count
#    f = open("count.txt", "w")
#    f.write(str(count))
#    f.close()

    # Render HTML with count variable
#    return render_template("index.html", count=count)

#if __name__ == "__main__":
#    app.run()

# The goal of this app is to show messages sent across space, not across time
# Latitude is displayed on the vertical axis, longitude is displayed on the horizontal axis
# Messages are organized according to the lat/long of where they were sent from (rounded to 1 decimal place)
# Clicking on a lat/long coordinate opens a more conventional timeline, where every message sent at those coordinates is shown chronologically (maybe)

@app.route("/")
def geo():

    # Get input from user on location (city name + country), convert to coordinates
    
    
    # Find appropriate coordinates on the page


    # Place message there


    # Render