from flask import Flask, render_template, request, redirect, url_for
import wave
import contextlib
import find_celeb
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    fname = ""
    duration = ""
    celeb = ""
    imgfname= ""
    audioname= ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:

            fname = file.filename
            fullfname="./static/audio/"+fname
            with contextlib.closing(wave.open(fullfname, 'r')) as f:
                frames = f.getnframes()
                rate = f.getframerate()
                duration = frames / float(rate)
                duration = round(duration)

            audioname = "audio/" + fname
            celeb = find_celeb.find_celeb('./static/audio')
            imgfname = "images/"+celeb+".jpg"


            #return redirect('/')
            # return redirect(url_for('resultPage'))
            

    #return render_template('index.html', fname=fname, duration=duration, celeb=celeb,image_file=imgfname)
    return render_template('temp.html', fname=fname, duration=duration, celeb=celeb, image_file=imgfname, audio_file=audioname)
@app.route("/result")
def resultPage():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
