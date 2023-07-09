from flask import Flask, render_template
menu = ['First', 'Second', 'Third']
app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', title= 'About Flask', menu = menu)
@app.route('/about')
def about():
    return render_template('biography.html', title = 'About')
@app.route('/help')
def help():
    return render_template('help.html', title = 'HELP')
if __name__ == '__main__':
    app.run(debug=True)