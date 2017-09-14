from flask import Flask, render_template
import goddess_info
import gpio_utils

app = Flask(__name__, static_url_path="/static")


@app.route("/DurgaInterface")
def durga_interface():
    template_data = {'goddess_names': goddess_info.durga_names,
                     'goddess_images': goddess_info.durga_names_to_images}
    
    gpio_utils.refresh_board()

    return render_template("durga_interface.html", **template_data)


@app.route("/DurgaInterface/<goddess_name>/")
def perform(goddess_name):
    gpio_pins = get_gpio_pins_for_goddess(goddess_name)
    gpio_utils.refresh_board()
    gpio_utils.pin_setup_for_output(gpio_pins)
    gpio_utils.turn_on(gpio_pins)
    music_file = get_music_file(goddess_name)
    template_data = {'goddess_name': goddess_name.upper(), "music_file": music_file}
    return render_template("playing_song.html", **template_data)


def get_music_file(goddess_name):
    # Get Name of the Music File
    for key, value in goddess_info.durga_names.iteritems():
        if value.upper() == goddess_name.upper():
            music_file = goddess_info.durga_names_to_music[key]
    return music_file


def get_gpio_pins_for_goddess(goddess_name):
   for key, value in goddess_info.durga_names.iteritems():
       if value.upper() == goddess_name.upper():
           return goddess_info.durga_names_to_color[key]['pin']


if __name__ == "__main__":
    app.run(host="192.168.1.105", port=5000, debug=True)
