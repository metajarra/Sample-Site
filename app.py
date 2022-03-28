from flask import Flask, render_template

app = Flask(__name__)

# The goal of this app is to show messages sent across space, not across time
# Messages are organized according to the lat/long of where they were sent from (rounded to int)

@app.route("/")
def post():
    # Adding a new marker
    f = open("marker_count.txt", "r")
    count = int(f.read())
    count += 1
    f.write(str(count))
    f.close()

    return render_template("index.html", count=count)

if __name__ == "__main__":
    app.run()