from flask import Flask, render_template
from os import environ

app = Flask('landing',template_folder='templates', static_folder='static')


@app.route('/')
def webprint():
    return render_template('index.html') 

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=environ.get('PORT'))
    app.debug = True