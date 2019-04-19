from flask import Flask, request, render_template, redirect

app = Flask(__name__)


tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
    return render_template('todo.html', title='Get It Done App', tasks=tasks)


if __name__ == '__main__':
    app.run(debug=True)