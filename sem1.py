from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/main/')
def main():
    return render_template("main.html")

@app.route('/main/clothes/')
def clothes():
    return render_template("clothes.html")

@app.route('/main/hats/')
def hats():
    return render_template("hats.html")

@app.route('/main/shoes/')
def shoes():
    return render_template("shoes.html")

if __name__ == "__main__": 
    app.run(debug=True)