from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def mass():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <h1>Миссия Колонизация Марса</h1>
</head>
<body>

</body>
</html>'''


@app.route('/index')
def dev():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <h1>И на Марсе будут яблони цвести!</h1>
</head>
<body>

</body>
</html>'''


@app.route('/promotion')
def promotion():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <h1>Человечество вырастает из детства.</h1>

<h1>Человечеству мала одна планета.</h1>

<h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1>

<h1>И начнем с Марса!</h1>

<h1>Присоединяйся!</h1>
</head>
<body>

</body>
</html>'''


@app.route('/promotion_image')
def rek():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <h1>Человечество вырастает из детства.</h1>

<h1>Человечеству мала одна планета.</h1>

<h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1>

<h1>И начнем с Марса!</h1>

<h1>Присоединяйся!</h1>
</head>
<body>

</body>
</html>'''


@app.route('/image_mars')
def mars():
    return f'''<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Привет, Яндекс!</title>
</head>
<body>
<h1 style="color: red;">Жди нас, Марс!</h1>
<img src="{url_for('static', filename='img/mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">
<div class="rec1" role="alert" style="background: #d6d8d9;margin-top: 8px;width:450px;height:30px; font-size:20px">
    Человечество вырастает из детства.
</div>
<div class="rect2" role="alert" style="background: #d4edda;margin-top: 8px;width:450px;height:30px;color: #155724;font-size:20px">
    Человечеству мала одна планета.
</div>
<div class="rect3" role="alert" style="background: #e2e3e5;margin-top: 8px;width:450px;height:45px;color: #383d41;font-size:20px">
Мы сделаем обитаемыми безжизненные пока планеты.
</div>
<div class="rect4" role="alert" style="background: #fff3cd;margin-top: 8px;width:450px;height:30px;color: #856404;font-size:20px">
И начнем с Марса!
</div>
<div class="rect5" role="alert" style="background: #f8d7da;margin-top: 8px;width:450px;height:30px;color: #721c24;font-size:20px">
Присоединяйся!
</div>
</body>
</html>'''


if __name__ == "__main__":
    app.run(port=8000, host="127.0.0.1")
