from flask import Flask
from flask import send_file, request
app = Flask(__name__)

template = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Flask Lab!</title>
    <link rel="icon" href="/mars" type="image/png">
  </head>

  <body>
    {content}
  </body>
</html>
""".strip()

@app.route('/')
def hello_world():
    return template.replace("{content}", """
                          <h1>Beginning</h1> 
                          <p>This is where I can add content!</p> 
                          <img src= '/sunset.jpg' alt = 'Sunset' > """)

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    sum = a + b
    return template.replace("{content}",f"{a} + {b} = {sum}")

@app.route('/reverse')
def reverse():
    q = request.args.get("q", "")
    rev_string = q[::-1]
    return template.replace("{content}", f"<p>{q} reversed is {rev_string}</p>")

@app.route('/sunset.jpg')
def sunset():
  return send_file("sunset.jpg")

@app.route('/mars.png')
def mars():
    return send_file("mars.png")

if __name__ == '__main__':
    app.run(debug=True)
