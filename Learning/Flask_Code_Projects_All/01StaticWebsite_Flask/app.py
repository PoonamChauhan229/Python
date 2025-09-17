from flask import Flask , render_template
app=Flask(__name__)

@app.route('/test')
def hello_world():
    return "Hello_World"

@app.route('/')
def test_homepage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)