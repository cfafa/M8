from flask import Flask, render_template,request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lists')
def lists():
    return render_template('list_organisations.html')

@app.route('/guides')
def guides():
    return render_template('eco_guides.html')

@app.route('/centers')
def centers():
    return render_template('recycling centers.html')

if __name__ == "__main__":
    app.run(debug=True)
