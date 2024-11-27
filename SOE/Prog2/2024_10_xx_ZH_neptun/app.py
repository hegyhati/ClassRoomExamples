from flask import Flask, render_template, redirect, request, url_for
from db import Student, get_course_list, register_grade

app = Flask(__name__)


@app.get("/")  
def student_select():
    return render_template("student_selector.html", students=Student.get_all())


@app.get("/student")
def student_redirect():
    return redirect(url_for("student_page", neptun=request.args.get("student")))
    
@app.get("/student/<neptun>")
def student_page(neptun: str):
    student = Student.get_by_neptun(neptun)
    return render_template("student_detail.html", student=student, nameday=student.has_nameday(), courses = student.get_courses())


@app.get("/admin")
def admin():
    return render_template("admin.html", students = Student.get_all(), courses = get_course_list())

@app.post("/grade")
def new_grade():
    student_id = request.form.get("student")
    course_id = request.form.get("course")
    grade = request.form.get("grade")
    register_grade(student_id, course_id, grade)
    return redirect(url_for("admin"))
