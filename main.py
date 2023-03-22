import flask
from flask import render_template, request

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        lst = ['first', 'second', 'third', 'fourth', 'pw', 'gp']
        rp = 0
        for subject in lst:
            point = float(request.form[subject])
            rp += point
        return render_template('rp.html', rp=rp)
    return 'None'

if __name__ == '__main__':
    app.run(debug=True)
