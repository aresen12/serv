from flask import Flask

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
    with open("sait.html", encoding='utf-8') as file:
        return file.read()


if __name__ == "__main__":
    app.run(port=8000, host="127.0.0.1")
