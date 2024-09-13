from flask import Flask,render_template,request,redirect,url_for,session
app=Flask(__name__) 
app.secret_key='123@flask'
Student_list = [{"Name":"Yogalakshmi","Age":22 ,"Roll_NO": 101, "Marks":[90,75,80,98,75]},
                {"Name":"Abdul","Age":23 ,"Roll_NO": 102, "Marks":[90,75,80,98,65]},
                {"Name":"Kalaiselvan","Age":24 ,"Roll_NO": 103, "Marks":[90,75,80,78,99]},
                {"Name":"Sneha","Age":26 ,"Roll_NO": 104, "Marks":[94,75,80,88,85]}]
@app.route("/")
def details():
    return render_template("index.html", students=Student_list)

@app.route("/add",methods={"GET","POST"})
def add():
    if request.method=="POST":
        stu_dic={}
        name=request.form.get("name")
        age=request.form.get("age")
        roll_no=request.form.get("roll_no")
        marks=[]
        marks1=request.form.get("marks1")
        marks2=request.form.get("marks2")
        marks3=request.form.get("marks3")
        marks4=request.form.get("marks4")
        marks5=request.form.get("marks5")
        marks.append(marks1)
        marks.append(marks2)
        marks.append(marks3)
        marks.append(marks4)
        marks.append(marks5)
        stu_dic.update({"Name":name})
        stu_dic.update({"Age":age})
        stu_dic.update({"Roll_NO":roll_no})
        stu_dic.update({"Marks":marks})

        Student_list.append(stu_dic)
        return redirect(url_for("details"))
    return render_template("add.html",students=Student_list)

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    if request.method=="POST":
        stu_dic={}
        name=request.form.get("name")
        age=request.form.get("age")
        roll_no=request.form.get("roll_no")
        marks=[]
        marks1=request.form.get("marks1")
        marks2=request.form.get("marks2")
        marks3=request.form.get("marks3")
        marks4=request.form.get("marks4")
        marks5=request.form.get("marks5") 
        marks.append(marks1)
        marks.append(marks2)
        marks.append(marks3)
        marks.append(marks4)
        marks.append(marks5)

        std_list=Student_list[index-1]

        std_list["Name"]=name
        std_list["Age"]=age
        std_list["Roll_NO"]=roll_no
        std_list["Marks"]=marks
        

        return redirect(url_for("details"))
    student=Student_list[index-1]
    return render_template("edit.html",students=student)

@app.route("/delete/<int:index>", methods=["GET", "POST"])
def delete(index):
    if request.method=="POST":
        Student_list.pop(index-1)
        return redirect(url_for("details"))
    
@app.route("/login",methods=["GET","POST"])
def login():
     user_name="yogalakshmi"
     Password="password123"
     if request.method=="POST":
          username=request.form['username']
          password=request.form['password']
          if username == user_name and password == Password:
            session['user_name']=user_name
            return redirect(url_for("details"))
          else:
              return 'login unsuccessfull'
     return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user_name",None)
    return redirect(url_for('login'))    

if __name__=="__main__":
    app.run(debug=True)