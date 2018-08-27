# from django.contrib import admin
# from django.urls import path
# from onlineapp.serializers import *
# from onlineapp.views import *
# from onlineapp.serializer_views import *
#
# urlpatterns = [
#
#     # path(r"api/colleges/" , college_list , name = "api_college_list" ),
#     # path(r"api/colleges/<int:pk>/" , college_details , name = "api_add_college_list" ),
#     # path(r"api/colleges/<int:pk>/students/" , StudentListandAdd , name = "api_student_list" ),
#     # #path(r"api/colleges/<int:pk>/students/<str:acronym>" , get_students , name = "students_by_acronym" ),
#     # path(r"api/colleges/<str:acronym>/" , get_students , name = "students_by_acronym" ),
#
# path('colleges_/',collegeListViewSerializer.as_view(),name="colleges_"),
# path('colleges_/add/',CreateCollegeViewSerializer.as_view(),name="addCollege_"),
# path('colleges_/<int:pk>/edit/',EditCollegeViewSerializer.as_view(),name="editCollege_"),
# path('colleges_/<int:pk>/delete/',DeleteCollegeViewSerializer.as_view(),name='deleteCollege_'),
#
#
#
# path('colleges_/<int:college_id>/students/',APIStudentList.as_view(),name='studentDetails_'),
# path('colleges_/<int:college_id>/students/<int:pk>',APIStudentDetail.as_view(),name='studentDetail_'),
#
#
#
# # path('colleges_/<int:cpk>/students/<int:pk>/',StudentDetailViewSerializer.as_view(),name='studentDetails_'),
# # path('colleges_/<int:pk>/students/addstudent/', CreateStudenteViewSerializer.as_view(), name="addStudent_"),
# # path('colleges_/<int:cpk>/students/<int:pk>/editstudent/',EditStudentViewSerializer.as_view(),name="editStudent_"),
# # path('colleges_/<int:cpk>/students/<int:pk>/deletestudent/',DeleteStudentViewSerializer.as_view(),name="deleteStudent_"),
#
#
# ]


from django.urls import path
from onlineapp.views import *
from onlineapp.serializer_views import *
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
# from onlineapp.views import CollegeListView,CollegeDetailsView,CreateCollegeView,CreateStudentView,
# EditCollege,DeleteCollege,EditStudent,DeleteStudent,CreateUser,LoginForm

app_name = 'onlineapp'

urlpatterns = [
   # path('', hello_world),
   # path('collegelist/', list_colleges),
   # path('sample/', sample_index),
   # path('student_list/', student_details),
   # path('student_list/<int:id>/', student_details2),
   # path('college_summary/<str:acronym>/', college_student_list),
   # path('test_session/', test_sessions),

   # path('colleges/', CollegeListView.as_view(), name='colleges_html'),
   # path('colleges/<int:id>/', CollegeDetailsView.as_view(), name='college_details_id'),
   # path('colleges/<str:acronym>/', CollegeDetailsView.as_view(), name='college_details_ac'),
   # path('college/add/', CreateCollegeView.as_view(), name='add_college'),
   # path('colleges/<int:college_id>/add/',CreateStudentView.as_view(),name='add_student'),
   # path('colleges/<int:pk>/edit',EditCollege.as_view(),name='edit_college'),
   # path('colleges/<int:pk>/delete',DeleteCollege.as_view(),name='delete_college'),
   # path('colleges/<int:college_id>/<int:pk>/edit',EditStudent.as_view(),name='edit_student'),
   # path('colleges/<int:college_id>/<int:pk>/delete', DeleteStudent.as_view(),name='delete_student'),
   # path('signup/',CreateUser.as_view(),name='signup'),
   # path('login/',LoginUser.as_view(),name='login'),
   # path('logout/',logout_user,name='logout'),

   path('api/colleges/',api_college_list,name='api_colleges'),
   path('api/colleges/<int:pk>/',api_college_detail,name='api_college_detail'),
   path('api/colleges/<int:college_id>/students/',APIStudentList.as_view(),name='api_students'),
   path('api/colleges/<int:college_id>/students/<int:pk>/',APIStudentDetail.as_view(),name='api_student_detail'),
   path('api/api-token-auth/', obtain_jwt_token,name='create_token'),
   # path('api/colleges/',APICollegeList.as_view(),name='api_colleges'),
   # path('api/colleges/<int:pk>/',APICollegeDetail.as_view(),name='api_college_detail')
]