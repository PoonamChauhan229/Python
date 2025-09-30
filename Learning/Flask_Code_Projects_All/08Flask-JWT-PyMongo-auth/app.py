from app import createapp

app=createapp()

@app.route('/')
def homepage():
    return "Welcome to the CRUD with JWT,Mongo,Flask,Blueprint"

if(__name__=="__main__"):
    app.run(debug=True)