from flask import Flask, render_template,request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list')
def list():
    return render_template('list_organisations.html')

if __name__ == "__main__":
    app.run(debug=True)
