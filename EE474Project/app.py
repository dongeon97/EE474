from flask import Flask, render_template, request, redirect, url_for
import wave
import contextlib
import find_celeb
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    celeblist = ["박명수", "임시완", "한예슬", "서현", "stevejobs", "meganfox", "dr.dre", "taylorswift" ]
    oplist=[0, 0, 0, 0, 0, 0, 0, 0]
    conlist=[0, 0, 0, 0, 0, 0, 0, 0]
    exlist=[0, 0, 0, 0, 0, 0, 0, 0]
    aglist=[0, 0, 0, 0, 0, 0, 0, 0]
    nelist=[0, 0, 0, 0, 0, 0, 0, 0]
    fname = ""
    duration = ""
    celeb = ""
    imgfname= ""
    audioname= ""
    opnum = 0
    connum = 0
    exnum = 0
    agnum = 0
    nenum = 0
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
            celeb = find_celeb.find_celeb('./static/audio')
            imgfname = "images/"+celeb+".jpg"
            opnum=50
            connum=70
            exnum=80
            agnum=30
            nenum=40
           # for nn in celeblist:
           #     if nn == celeb:
           #         break
           #     else:
           #         i = i+1
           # opnum = oplist[i]
           # connum = conlist[i]
           # exnum = exlist[[i]
           # agnum = aglist[i]
           # nenum = nelist[i]

            #return redirect('/')
            # return redirect(url_for('resultPage'))
            

    #return render_template('index.html', fname=fname, duration=duration, celeb=celeb,image_file=imgfname)
    return render_template('temp.html', fname=fname, duration=duration, celeb=celeb, image_file=imgfname, audio_file=audioname, opnum=opnum, connum=connum, agnum=agnum, exnum=exnum, nenum=nenum)
@app.route("/result")
def resultPage():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
