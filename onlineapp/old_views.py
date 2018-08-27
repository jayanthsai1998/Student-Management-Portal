from django.shortcuts import render

# Create your views here.
import os
from django.http import HttpResponse
#from onlineapp import templates
import onlineapp.templates
from onlineapp.models import *
import django

os.environ['DJANGO_SETTINGS_MODULE'] = "onlineproject.settings"
django.setup()

def college_details(request):
    # text = "<h1>Hye World!</h1>"
    # fp = open("C:\\work\\appscourse\\djangoproject\\onlineproject\\onlineapp\\templates\\index.html","r")
    # text=""
    # for line in fp:
    #     text += line

    clg_obj = College.objects.values('name','acronym')

    #clg_obj = College.objects.all()
    #stud_obj = Student.objects.all()
    #mark_obj = MockTest1.objects.all()

    # text="""
    # <!DOCTYPE html>
    # <html lang="en">
    #     <head>
    #         <meta charset="UTF-8">
    #         <title>JAY</title>
    #     </head>
    #     <body><table>
    #     """
    #
    # for obj in clg_obj:
    #     text+= "<tr> <td>%s<td/>  <td>%s</td> </tr>" % (obj.name, obj.acronym)
    #
    # text +="""
    # </table>
    # </body>
    # </html>
    # """

    #return HttpResponse(text)
    return render(request, "index.html", {'clg_obj':clg_obj})

# def stud_details(request):
#     std_obj = Student.objects.values('name', 'email', 'college__acronym')
#     return render(request, "std_details.html",{'std_obj':std_obj})

def stud_details(request):
    std_obj = Student.objects.values('name', 'email', 'college__acronym', 'pk', "mocktest1__total")
    print(std_obj)
    return render( request, "std_details.html", {'std_obj':std_obj} )

def get_marks(request, std_id):
    print("asssssssssssssssssssssss")
    mark_obj = MockTest1.objects.filter(student__pk=std_id).values('problem1','problem2','problem3','problem4','total')
    print(mark_obj)
    return render( request, "std_marks.html", {'mark_obj':mark_obj} )

def get_marks_01(request, std_id):
    std = MockTest1.objects.filter(student__pk=std_id).values('problem1','problem2','problem3','problem4',"total", "student__name", "student__email")
    return render(request, "std_marks.html", { 'std':std})
    #return HttpResponse(std)


def particular_student(request, std_id):
    st_ob = Student.objects.filter(pk = std_id).values('name', 'email', 'college__acronym')
    if(st_ob):
        return render( request, "id_std.html",{'st_ob':st_ob} )
    else:
        return render(request,"invalid_page.html",{})

def test_session(request):
    counter = request.session.setdefault('counter' , 0)
    request.session['counter'] = counter + 1
    return HttpResponse("reached %d time" % (request.session['counter']))

def error_testing(request):
    raise ValueError
    return HttpResponse("Error raised")


def get_student_marks(request):
    studs = Student.objects.values("name", "email", "college__acronym", "mocktest1__total", "pk")
    return render(request, "std_details.html", {"studs" : studs})