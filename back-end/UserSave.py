from flask import Flask, render_template,request
import json 
    
app = Flask(__name__)

@app.route("/saveUser",methods=["GET","POST"])
def saveUser():

    name = "Empy"
    amount = 0
    
    print(request.data)

    if request.method == "POST":
        print(request)
        if "userName" in request.form:
            name = request.data
        if "amount" in request.form:
            amount = request.form["amount"]

    return request.get_json()["userName"]


if __name__ =="__main__":
    app.run(debug=True)
