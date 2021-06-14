from flask import Flask, render_template, request, redirect, url_for
import wave
import contextlib
import find_celeb
import numpy as np
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    celeblist = ["박명수", "임시완", "한예슬", "서현", "Steve Jobs", "Megan Fox", "Dr.dre", "Taylor Swift" ]
    oplist = [20, 60, 90, 80, 100, 30, 80, 60]
    conlist = [50, 50, 35, 80, 80, 50, 40, 80]
    exlist = [30, 70, 80, 60, 60, 20, 60, 70]
    aglist = [40, 80, 40, 50, 50, 40, 50, 90]
    nelist = [30, 20, 80, 70, 70, 20, 70, 20]
    wordlist1 =["ISTP", "ENFJ", "ENTP", "ENTJ", "ENTJ", "ISTP", "ENTP", "ENFJ"]
    wordlist2 = ["", "", "", "", "", "", "", ""]
    wordlist3 = ["", "", "", "", "", "", "", ""]
    fname = ""
    duration = ""
    celeb = ""
    imgfname= ""
    audioname= ""
    acc = 0
    accstr = ""
    opnum = 0
    connum = 0
    exnum = 0
    agnum = 0
    nenum = 0
    word1 = ""
    word2 = ""
    word3 = ""
    i = 0
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
            result = find_celeb.find_celeb('./static/audio')
            celeb = result[0]
            acc = result[1]
            acc = np.round(acc, 2)
            accstr = str(acc)[1:-1]
            imgfname = "images/"+celeb+".jpg"

            for nn in celeblist:
                if nn == celeb:
                    break
                else:
                    i = i+1
            opnum = oplist[i]
            connum = conlist[i]
            exnum = exlist[i]
            agnum = aglist[i]
            nenum = nelist[i]
            word1 = wordlist1[i]
            word2 = wordlist2[i]
            word3 = wordlist3[i]


    return render_template('index.html', fname=fname, duration=duration, celeb=celeb, accstr=accstr, image_file=imgfname, audio_file=audioname, word1=word1, word2=word2, word3=word3, opnum=opnum, connum=connum, agnum=agnum, exnum=exnum, nenum=nenum)
@app.route("/result")
def resultPage():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
