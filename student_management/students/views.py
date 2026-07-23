from django.shortcuts import render, redirect
from .models import Student
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def register(request):
    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            return redirect("login")

    return render(request, "register.html")

@login_required
def home(request):

    students = Student.objects.all()

    context = {
        "students": students,
        "college": "Makerere University"
    }

    return render(request, "home.html", context)

def add_student(request):

    if request.method == "POST":

        Student.objects.create(
            name=request.POST["name"],
            age=request.POST["age"],
            course=request.POST["course"]
        )

        return redirect("/")

    return render(request, "add_student.html")

def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    student.delete()

    return redirect("home")
def edit_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":

        student.name = request.POST["name"]

        student.age = request.POST["age"]

        student.course = request.POST["course"]

        student.save()

        return redirect("home")

    return render(
        request,
        "edit_student.html",
        {"student": student}
    )

def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")

    return render(request, "login.html")    

def logout_view(request):

    logout(request)

    return redirect("login")
    