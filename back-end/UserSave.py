from flask import Flask, render_template,request
import json 
    
app = Flask(__name__)

@app.route("/saveUser",methods=["GET","POST"])
def saveUser():

    print(request.method)       

    name = "Empy"
    amount = 0

    if request.method == "POST":
        print(request.form)
        if "name" in request.form:
            name = request.form["name"]
        if "amount" in request.form:
            amount = request.form["amount"]


    print(name," : ",amount )

    dict1 ={ 
    'Users' : [
                    {
                        'name' : name,
                        'Amount' : amount,
                    },
                ] 
            } 

    out_file = open("myfile.json", "w")
    json.dump(dict1, out_file, indent = 2)
    out_file.close() 

    return render_template("index.html")




if __name__ =="__main__":
    app.run(debug=True)