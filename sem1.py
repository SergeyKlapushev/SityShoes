import logging
from flask import Flask, render_template, make_response, redirect, flash, request, url_for

app = Flask(__name__)
logger = logging.getLogger(__name__)

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

#Логинимся
#GET запрос
@app.get('/loging/')
def loging_get():
       return render_template('loging.html')

#POST запрос
@app.post('/loging/')
def submit_post():
    name = request.form.get('name')
    setCookie(name)
    cName = request.cookies.get("username")
    print(cName)
    context ={
        "zagolovok" : "Главная",
        "hi" : f"Добро пожаловать в наш магазин {cName}"
    }
    return render_template('entrance.html', **context)

#Присваиваем cookie
def setCookie(name):
    response = make_response("cookie установлены")
    response.set_cookie(f"username", f"{name}")
    return response

#Обработка ошибок
@app.errorhandler(404)
def page_not_found(e):
    logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url,
    }
    return render_template('404.html', **context), 404

if __name__ == "__main__": 
    app.run(debug=True)