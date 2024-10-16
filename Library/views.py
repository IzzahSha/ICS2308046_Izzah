from django.shortcuts import render
from .models import Student,Book,Borrowing,Course,Mentor
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    context = {
        'firstname' : 'Nur Izzah',
        'greeting' : 1,
    }
    return render (request, "index.html", context)

def view(request):
    return render (request, 'view.html')

def dbstudent(request):
    mystudent =Student.objects.all().values()
    context = {
        'mystudent': mystudent,
    }
    return render (request, 'dbstudent.html', context)

def dbbook(request):
    mybook = Book.objects.all().values()
    context = {
        'mybook' : mybook,
    }
    return render (request, 'dbbook.html', context)

def dbborrow(request):
    myborrow = Borrowing.objects.all().values()
    context = {
        'myborrow' : myborrow,
    }
    return render (request, 'dbborrow.html', context)

def course(request):
    if request.method == 'POST':
        c_code = request.POST['code']
        c_desc = request.POST['description']
        data = Course(code=c_code, description =c_desc)
        data.save()
        mycourse = Course.objects.all().values()
        dict = {
            'message' : '',
            'mycourse' : mycourse,
        }

    else :
        dict = {
            'message' : ''
        }
       
    return render (request, 'course.html', dict)

def update_course(request,code):
    data = Course.objects.get(code=code)
    context = {
        'data': data
    }
    return render (request, "update_course.html", context)

def save_update_course(request, code):
    c_decs = request.POST['description']
    data = Course.objects.get(code=code)
    data.description = c_decs
    data.save()
    return HttpResponseRedirect(reverse('course'))

def delete_course(request,code):
    data = Course.objects.get(code=code)
    data.delete()
    return HttpResponseRedirect(reverse('course'))

def search_course(request):
    if request.method == 'GET':
        c_code = request.GET.get('c_code')

        if c_code:
            data = Course.objects.filter(code=c_code.upper())
        else:
            data = None
        
        context = {
            'data' : data
        }

        return render (request, "search_course.html", context)
    
    return render (request, "search_course.html")

def newmentor(request):
    if request.method == 'POST':
        m_id = request.POST['id']
        m_name = request.POST['name']
        m_room = request.POST['room']
        data = Mentor(menid = m_id, menname = m_name, meroomno = m_room)
        data.save()
        mymentor = Mentor.objects.all().values()
        dict = {
            'message' : '',
            'mymentor' : mymentor,
        }

    else :
        dict = {
            'message' : ''
        }
       
    return render (request, 'newmentor.html', dict)