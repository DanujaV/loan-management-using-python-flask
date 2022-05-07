from flask import Flask, render_template,request
import json
import os 
    
app = Flask(__name__)

file_path='myfile.json'

def is_file_empty(file_path):
    return os.path.exists(file_path) and os.stat(file_path).st_size == 0




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

    is_empty = is_file_empty(file_path)
    if is_empty:
        print('File is empty')
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
    else:
        print('File is not empty')
        def write_json(new_data, filename='myfile.json'):
    
            with open(filename,'r+') as file:
                # First we load existing data into a dict.
                file_data = json.load(file)
                # Join new_data with file_data inside emp_details
                file_data["Users"].append(new_data)
                # Sets file's current position at offset.
                file.seek(0)
                # convert back to json.
                json.dump(file_data, file, indent = 4)

	# python object to be appended
        y = {"name":name,
            "amonut": amount
            }
            
        write_json(y)

    



    return render_template("index.html")




if __name__ =="__main__":
    app.run(debug=True)