from app import creatapp
app=creatapp()

@app.route('/')
def hello_world():
    return "Home Page testing BluePrint"

if __name__=="__main__":
    app.run(debug=True)