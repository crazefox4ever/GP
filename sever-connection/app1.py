from flask import Flask,render_template,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('h.html')

@app.route("/in")
def first():
    return render_template('home.html')

@app.route("/index2")
def second():
    return redirect("http://127.0.0.1:5001/")#web application 


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0") #host="0.0.0.0" will make the page accessable
                            #by going to http://[ip]:5000/ on any computer in 
                            #the network.