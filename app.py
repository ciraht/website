from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/caos')
def caos():
    return render_template('caos.html')

@app.route('/acabada')
def acabada():
    return render_template('acabada.html')

@app.route('/imagination')
def imagination():
    return render_template('imagination.html')

if __name__ == '__main__':
    app.run(debug=True)