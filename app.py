from flask import Flask, redirect, request, render_template

from datetime import datetime

import data

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        conn = data.create_connection()
        readers = data.select_all_readers(conn)
        return render_template('hello.html', readers=readers)
    elif request.method == 'POST':
        reader_id = request.form.get("reader")
        activity = request.form.get('activity')
        endpoint = request.form.get('endpoint')
        conn = data.create_connection()
        endpoint = data.EndpointTuple(reader_id, datetime.now().isoformat(), activity, endpoint)
        data.insert_endpoint(conn, endpoint)
        return redirect('/')


@app.route('/form-example', methods = ['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        return render_template('form.html', info={'firstname': first_name, 'lastname': last_name})


if __name__ == '__main__':
    app.run(debug=True)
