from flask import Flask, render_templagit

app = Flask(__name__)

@app.route('/main/')
def main():
    return render_template("main.html")

@app.route('/clothes/')
def clothes():
    return render_template("clothes.html")

@app.route('/hats/')
def hats():
    return render_template("hats.html")

@app.route('/shoes/')
def shoes():
    return render_template("shoes.html")

if __name__ == "__main__": 
    app.run(debug=True)