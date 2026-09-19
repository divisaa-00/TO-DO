from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)
valid_user=dict()

@app.route("/",methods=["GET","POST"])
def signin():
    if request.method == 'POST':
        print("signin successfull")#
        Username = request.form.get('username')
        Email = request.form.get('email')
        Password = request.form.get('password')
        if Username not in valid_user:
            print("inside if")#
            valid_user[Username]=[Password,Email]
            return redirect(url_for('Home'))
        else:
            print("inside else")#
            return redirect(url_for('login'))
    return render_template("signin.html")

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='POST':
        print("LOGIN successfull")#
        Username=request.form.get('username')
        Password=request.form.get('password')
        return redirect(url_for("Home"))
    return render_template("login.html")

@app.route("/Home",methods=['GET','POST'])
def Home():
    return "Home page"

if __name__=="__main__":
    app.run(debug=True)
