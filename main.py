import flask from Flask, render_template

app = Flask(__name__)

Users = [
       {
            
                "Name" : "Pulete",
                "Age" : "12",
                "Clasa" : "69",
            
            
            },{
            
                "Name" : "Pulete2",
                "Age" : "13",
                "Clasa" : "62",
            
            
            }, 
            {
            
                "Name" : "Pulet3",
                "Age" : "22",
                "Clasa" : "19",
            
            
            },
        
        
        ]



@app.route("/")
def home():
    return render_template("index.html", users = Users)


if __name__ == "__main__":
    app.run(debug=True)
