from flask import Flask, render_template

app = Flask(__name__)

@app.route('/main/')
def main():
    context ={
        "zagolovok" : "Главная",
        "hi" : "Добро пожаловать в наш магазин"
    }
    return render_template("main.html", **context)

@app.route('/hats/')
def hats():
    context ={
        "zagolovok" : "Шляпы",
    }
    return render_template("hats.html", **context)

@app.route('/clothes/')
def clothes():
    context ={
        "zagolovok" : "Одежда",
    }
    return render_template("clothes.html", **context)

@app.route('/shoes/')
def shoes():
    context ={
        "zagolovok" : "Обувь",
    }
    return render_template("shoes.html", **context)

if __name__ == "__main__": 
    app.run(debug=True)