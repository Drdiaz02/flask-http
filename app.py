from flask import Flask
from flask import send_file, request
app = Flask(__name__)

template = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  </head>

  <body>
    {content}
  </body>
</html>
""".strip()

@app.route('/')
def hello_world():
    return template.replace("{content}", 'Hello, World!')

if __name__ == '__main__':
    app.run(debug=True)
