from flask import Flask, render_template

app = Flask(__name__)

# sass --watch static/scss/style.scss:static/css/style.css

# sass --watch static/scss/style.scss:static/css/style.css

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
