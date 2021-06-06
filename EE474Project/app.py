from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    fname = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            fname = file.filename

            return redirect('/result')
            # return redirect(url_for('resultPage'))
            

    return render_template('index.html', fname=fname)

@app.route("/result")
def resultPage():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
