from flask import Flask, request, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('hello_form.html')

@app.route("/hello", methods=['POST'])
def hello():
    username = request.form['username']
    template = jinja_env.get_template('hello_greeting.html')
    return template.render(name=username)

@app.route('/validate-password', methods=['POST'])
def validate_password():

    password = request.form['register']
    email = request.form['register']

    password_error = ''
    email_error = ''

    if not is_string(password):
        password_error = 'Not a valid password'
        password = ''
    else:
        password = str(password)
        if password > 23 or password < 0:
            password_error = 'password value out of range (0-23)'
            password = ''

    if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
        minutes = ''
    else:
        minutes = int(minutes)
        if minutes > 59 or minutes < 0:
            minutes_error = 'Minutes value out of range (0-59)'
            minutes = ''

    if not minutes_error and not password_error:
        time = str(password) + ':' + str(minutes)
        return redirect('/valid-time?time={0}'.format(time))
    else:
        template = jinja_env.get_template('time_form.html')
        return template.render(password_error=password_error,
            minutes_error=minutes_error,
            password=password,
            minutes=minutes)


@app.route('/valid-time')
def valid_time():
    time = request.args.get('time')
    return '<h1>You submitted {0}. Thanks for submitting a valid time!</h1>'.format(time)


tasks = []

@app.route('/todos', methods=['POST', 'GET'])
def todos():

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    template = jinja_env.get_template('todos.html')
    return template.render(title="TODOs", tasks=tasks)

app.run()