from flask import Flask, render_template,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('home2.html')




if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0") #host="0.0.0.0" will make the page accessable
                            #by going to http://[ip]:5000/ on any computer in 
                            #the network.