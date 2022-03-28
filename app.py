from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():

    # Load current count
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    # Increment the count
    count += 1

    # Overwrite the count
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()

    # Render HTML with count variable
    return render_template("index.html", count=count)

if __name__ == "__main__":
    app.run()

# The goal of this app is to show messages sent across space, not across time
# Messages are organized according to the lat/long of where they were sent from (rounded to int)

#@app.route("/")
#def post():
#    # Adding a new marker
#    f = open("marker_count.txt", "r")
#    count = int(f.read())
#    count += 1
#    f.write(str(count))
#    f.close()

#    return render_template("index.html", count=count)

#if __name__ == "__main__":
#    app.run()