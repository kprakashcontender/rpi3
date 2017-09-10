from flask import Flask, render_template

app = Flask(__name__, static_url_path="/static")
@app.route("/")
def hello():
    return "Hello World"

@app.route("/DurgaInterface")
def durga_interface():
    return render_template("durga_interface.html")

@app.route("/DurgaInterface/<goddess_name>/")
def play_song(goddess_name):
    return render_template("playing_song.html")

if __name__ == "__main__":
    app.run(host="192.168.56.1", port=5000, debug=True)
