from flask import Flask, url_for, request

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
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Привет, Марс!</title>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">
    <br>
    Вот она какая, красная планета
</head>
<body>
</body>
</html>'''


@app.route("/promotion_image")
def promotion_image():
    file = open("promotion_image.html", encoding='utf-8', mode='r')
    data = file.read()
    file.close()
    return data


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        with open('astronaut_selection.html', encoding='utf-8') as file:
            return file.read()
    if request.method == "POST":
        return """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Пример формы</title>
</head>
<body>Вы успешно записаны</body>"""


if __name__ == "__main__":
    app.run(port=8000, host="127.0.0.1")
