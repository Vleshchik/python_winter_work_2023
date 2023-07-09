from flask import Flask, render_template
menu = ['First', 'Second', 'Third']
app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', title= 'Vadim Leshchik', menu = menu)
@app.route('/biography')
def biography():
    return render_template('biography.html', title = 'About me')
@app.route('/prof_skills')
def prof_skills():
    return render_template('prof_skills.html', title='Professional experience')
@app.route('/hobby')
def hobby():
    return render_template('hobby.html', title = 'My hobbies')

if __name__ == '__main__':
    app.run(debug=True)