from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append({'name': task, 'done': False, 'due_date': ''})
    return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    if request.method == 'POST':
        del tasks[index]
        return redirect(url_for('index'))
    return render_template('index.html', tasks=tasks)

@app.route('/toggle/<int:index>', methods=['POST'])
def toggle(index):
    if request.method == 'POST':
        tasks[index]['done'] = not tasks[index]['done']
    return redirect(url_for('index'))

@app.route('/due_date/<int:index>', methods=['POST'])
def due_date(index):
    if request.method == 'POST':
        tasks[index]['due_date'] = request.form['due_date']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
