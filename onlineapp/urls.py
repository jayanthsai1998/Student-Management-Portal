
from django.contrib import admin
from django.urls import path
from onlineapp.old_views import *

from onlineapp.views import *



urlpatterns =[
    # path('colleges', college_details),
    # path('std',stud_details),
    # path('id/<int:std_id>',particular_student),
    # path('mark_id/<int:std_id>',get_marks_01),
    # path('testsession',test_session),
    # path('err',error_testing),
    # path("get_marks/", get_student_marks),

    #path("Colleges/", CollegeView.as_view(), name = "index.html"),

    path("Colleges/", CollegeListView.as_view(), name = "index"),
    path(r"Colleges/Addcollege", CreateCollegeView.as_view(), name="add_colleges"),
    path(r"Colleges/<int:pk>/",CollegeDetailsView.as_view(), name = "particular_college"),
    path(r"Colleges/<int:pk>/edit/", UpdateCollegeView.as_view(), name="edit_college"),
    path(r"Colleges/<int:pk>/delete/", DeleteCollegeView.as_view(), name="delete_college"),


    path(r"Colleges/<int:college_id>/student/add/",CreateStudentView.as_view(), name = "add_student"),
    path(r"Colleges/<int:college_id>/student/edit/",UpdateStudentView.as_view(), name = "edit_student"),
    path(r"Colleges/<int:college_id>/student/delete/",DeleteStudentView.as_view(), name = "delete_student"),

    path(r"signup/",SignUpView.as_view(), name = "sign_up"),
    path(r"login/",LoginView.as_view(), name = "login"),
    path(r"logout", logout_user ,name = "logout")

    #path(r"Colleges/<int:pk>/",CollegeDetailsView.as_view(), name = "id_std"),

    #path(r"Colleges/Addstudent", CreateStudentView.as_view(), name="add_colleges.html"),

]

