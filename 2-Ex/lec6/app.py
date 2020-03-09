from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def HiRTC():
    return "HiRTC"

@app.route("/h1/<name>")
def HiRTC1(name):
    return "<h1>Hi "+name+"</h1>"

@app.route("/templates/<name>")
def viewPage(name):
    return render_template("index.html",name=name)

@app.route("/ShowEmpData")
def ShowEmpData():
    return  request.args

if __name__=="__main__":
    app.run()



