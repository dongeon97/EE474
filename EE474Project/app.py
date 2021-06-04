from flask import Flask, render_template, request, redirect
#import main python code

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

            # file is the input of the main source code
            # Use function for the result
            # result = Func(file)

    #return render_template('index.html', fname=fname, result= result)
    return render_template('index.html', fname=fname)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
