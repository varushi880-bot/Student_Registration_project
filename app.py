from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def home():
     return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
     name=request.form.get("name")
     email=request.form.get("email")
     age=request.form.get("age")
     course=request.form.get("course")
     mobile =request.form.get("mobile")
     gender=request.form.get("gender")
     
     return render_template("success.html",name=name,email=email,age=age,course=course,mobile=mobile,gender=gender)
if __name__=="__main__":
    app.run(debug=True)