from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')    

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skate')
def skate():
    return render_template('skate.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
