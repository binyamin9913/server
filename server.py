from flask import Flask
from flask import request
from flask import render_template
import urllib.parse
text=""
app = Flask(__name__)
@app.route('https://binyamin9913.github.io/server')
@app.route('https://binyamin9913.github.io/server', methods=['POST'])
def response():
    text = request.date
     return flask.render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)



text.encode(encoding='UTF-8',errors='strict')   
urllib.parse.quote(url_text)