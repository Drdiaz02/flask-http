from flask import Flask
from flask import send_file, request
app = Flask(__name__)

template = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Flask Lab!</title>
  </head>

  <body>
    {content}
  </body>
</html>
""".strip()

@app.route('/')
def hello_world():
    return template.replace("{content}", '<h1>Beginning</h1><p>This is where I can add content!</p>')

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    sum = a + b
    return (f"{a} + {b} = {sum}")

if __name__ == '__main__':
    app.run(debug=True)
