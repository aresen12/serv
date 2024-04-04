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


@app.route('/choice/<planet_name>')
def planet_change(planet_name):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <meta charset="UTF-8">
    <title>Выбор</title>
</head>
<body>
<h1>моё предложение:{planet_name}</h1>
<h2>Эта планета близка к земле; </h2>
<div class="alert alert-success" role="alert">
    На ней много необходимых ресурсов
</div>
<div class="alert alert-secondary" role="alert">
    На ней есть вода и атмосфера
</div>
<div class="alert alert-warning" role="alert">
    На ней есть небольшое магнитное поле
</div>
<div class="alert alert-danger" role="alert">
  Наконец она просто красива!
</div>
</body>
</html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def get_res(nickname, level, rating):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <meta charset="UTF-8">
    <title>Выбор</title>
</head>
<body>
<h1>Результаты отбора</h1>
<h2>Претендента на участие в мисси {nickname}:</h2>
<div class="alert alert-success" role="alert">
    Поздравляем! Ваш рейтинг после {level} этапа отбора
</div>
составляет {rating}!

<div class="alert alert-warning" role="alert">
    Желаем удачи!
</div>
</body>
</html>'''


if __name__ == "__main__":
    app.run(port=8000, host="127.0.0.1")
