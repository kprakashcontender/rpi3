from flask import Flask, render_template
import goddess_info

app = Flask(__name__, static_url_path="/static")


@app.route("/DurgaInterface")
def durga_interface():
    template_data = {'goddess_names': goddess_info.durga_names,
                     'goddess_images': goddess_info.durga_names_to_images}

    return render_template("durga_interface.html", **template_data)


@app.route("/DurgaInterface/<goddess_name>/")
def perform(goddess_name):
    # Get Name of the Music File
    for key, value in goddess_info.durga_names.iteritems():
        if value.upper() == goddess_name.upper():
            music_file = goddess_info.durga_names_to_music[key]

    template_data = {'goddess_name': goddess_name.upper(), "music_file": music_file}
    return render_template("playing_song.html", **template_data)


if __name__ == "__main__":
    app.run(host="192.168.56.1", port=5000, debug=True)
