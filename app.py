from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'POST':
        return render_template("base.html")
    else:
       return render_template("home.html") 

@app.route("/operators")
def operators():
    return render_template("operators.html")

if __name__=="__main__":
    app.run()