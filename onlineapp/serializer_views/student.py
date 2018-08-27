# from onlineapp.models import *
# from onlineapp.serializers import *
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
#
#
#
# from django.core.exceptions import ObjectDoesNotExist
# from django.db import IntegrityError
# from django.db.models import F
# from rest_framework.utils import json
# from rest_framework.views import APIView
# from rest_framework.status import *
#
# from onlineapp.serializers import StudentViewSerializer, MarksSerializer, StudentSerializer, StudentDetailsSerializer
# from onlineapp.models import MockTest1, Student, College
# from django.http import JsonResponse
#
#
# def get_students(request,acronym):
#     students = MockTest1.objects.values('student__name','student__db_folder','total').annotate(name=F('student__name'),db_name=F('student__db_folder')).filter(student__college__acronym=acronym)
#     print(students)
#     students = students.values('name', 'db_folder', "total")
#     students=StudentViewSerializer(students,many=True)
#     return JsonResponse(students.data,safe=False,status=200)
#
#
# class StudentListandAdd(APIView):
#     def get(self,request,*args,**kwargs):
#         try:
#             student = Student.objects.get(db_folder=kwargs['db_folder'])
#         except Exception:
#             return JsonResponse({'error':'Student not found!'},status=HTTP_404_NOT_FOUND)
#         data = StudentDetailsSerializer(student)
#         return JsonResponse(data.data,status=HTTP_200_OK)
#
#     def post(self,request,*args,**kwargs):
#         college=College.objects.get(acronym=kwargs['acronym'])
#         try:
#             marks={}
#             request_data=dict(request.POST)
#             for key in request_data.keys():
#                 if type(request_data[key]) == list:
#                     request_data[key]="".join(request_data[key])
#             marks['problem1']=int(request_data.pop('problem1'))
#             marks['problem2']=int(request_data.pop('problem2'))
#             marks['problem3']=int(request_data.pop('problem3'))
#             marks['problem4']=int(request_data.pop('problem4'))
#             marks['total']=marks['problem1']+marks['problem2']+marks['problem3']+marks['problem4']
#             request_data['marks']=marks
#             request_data['college']=college
#             student=StudentDetailsSerializer()
#             student=student.create(request_data)
#             student=StudentDetailsSerializer(student)
#             return JsonResponse(student.data, status=HTTP_201_CREATED)
#         except IntegrityError as e:
#             return JsonResponse({'error':'Student already exists!'},status=HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return JsonResponse({'error':'Invalid Data!'},status=HTTP_400_BAD_REQUEST)
#
#     def put(self,request,*args,**kwargs):
#         try:
#             marks={}
#             request_data=dict(request.POST)
#             for key in request_data.keys():
#                 if type(request_data[key]) == list:
#                     request_data[key]="".join(request_data[key])
#             marks['problem1']=int(request_data.pop('problem1'))
#             marks['problem2']=int(request_data.pop('problem2'))
#             marks['problem3']=int(request_data.pop('problem3'))
#             marks['problem4']=int(request_data.pop('problem4'))
#             marks['total']=marks['problem1']+marks['problem2']+marks['problem3']+marks['problem4']
#             request_data['marks']=marks
#             student=Student.objects.get(db_name=kwargs['db_folder'])
#             student_serializer=StudentDetailsSerializer(student)
#             student=student_serializer.update(student,request_data)
#             student = StudentDetailsSerializer(student)
#             return JsonResponse(student.data, status=HTTP_200_OK)
#         except ObjectDoesNotExist as e:
#             return JsonResponse({'error':'Student not found!'},status=HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return JsonResponse({'error':'Invalid Data!'},status=HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,*args,**kwargs):
#         try:
#             student=Student.objects.get(db_name=kwargs['db_folder'])
#             student_serializer = StudentDetailsSerializer(student)
#             student_serializer.__delete__(student)
#             return JsonResponse({'success':'Deleted successfully!'},status=HTTP_200_OK)
#         except ObjectDoesNotExist as e:
#             return JsonResponse({'error':'Student not found!'},status=HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return JsonResponse({'error':'Invalid Data!'},status=HTTP_400_BAD_REQUEST)
#
# # class studentDetailsApi(ListAPIView):
# #     serializer_class = studentDetailSerialize
# #
# #     def get_queryset(self):
# #         queryset = Student.objects.all().filter(college__id=self.kwargs.get('college__id')).filter(
# #             id=self.kwargs.get('student__id'))
# #         return queryset
# #
# # class studentDetailsUpdateApi(UpdateAPIView):
# #     serializer_class = studentDetailSerialize
# #     lookup_field = 'pk'
# #
# #     def get_queryset(self):
# #         queryset = Student.objects.all()
# #         return queryset
# #
# # class studentDeleteApi(DestroyAPIView):
# #     queryset = Student.objects.all()
# #     serializer_class = studentDetailSerialize
# #     lookup_field = 'pk'
#
#
#
# # @api_view(['GET', 'POST'])
# # def students_list(request, pk):
# #     if(request.method == 'GET'):
# #         students =Student.objects.filter(college_id = pk)
# #         # import ipdb
# #         # ipdb.set_trace()
# #         #serializer = StudentSerializer(students, many = True)
# #         serializer = StudentDetailSerializer(students, many=True)
# #         return Response(serializer.data)
# #
# #     elif(request.method == 'POST'):
# #         #serializer = StudentSerializer(data = request.data)
# #         serializer = StudentDetailSerializer(data=request.data)
# #         if(serializer.is_valid()):
# #             student = serializer.save()
# #             student.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
# from  onlineapp.serializers import *
# from onlineapp.models import *
# from django.http import HttpResponse
#
#
# class StudentDetailViewSerializer(ListAPIView):
#     serializer_class = StudentDetailSerializer
#
#     def get_queryset(self):
#         queryset = Student.objects.filter(pk=self.kwargs['pk'])
#         return queryset
#
#
# class CreateStudenteViewSerializer(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentDetailSerializer
#
#     def create(self, request, *args, **kwargs):
#         student = Student.objects.create(name=request.data['name'], dob=request.data['dob'],
#                                          email=request.data['email'], college_id=kwargs['pk'],db_folder=request.data['db_folder'])
#         total = int(request.data['mocktest1.problem1']) + int(request.data['mocktest1.problem2'])
#         total = int(total)+  int(request.data['mocktest1.problem3']) + int(request.data['mocktest1.problem4'])
#         MockTest1.objects.create(problem1=request.data['mocktest1.problem1'],
#                                  problem2=request.data['mocktest1.problem2'],
#                                  problem3=request.data['mocktest1.problem3'],
#                                  problem4=request.data['mocktest1.problem4'],
#                                  total=str(total),
#                                  student_id=student.id)
#         html = "success"
#         return HttpResponse(html)
#
#
# class EditStudentViewSerializer(ListAPIView, UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentDetailSerializer
#     lookup_field = 'pk'
#
#     def get_queryset(self):
#         queryset = Student.objects.filter(pk=self.kwargs['pk'])
#         return queryset
#
#
# class DeleteStudentViewSerializer(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentDetailSerializer
#     lookup_field = 'pk'













from onlineapp.models import Student
from onlineapp.serializers import StudentSerializer,StudentDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class APIStudentList(APIView):

   def get_queryset(self):
      students = Student.objects.filter(college__id=self.kwargs['college_id'])
      return students

   def get(self,request,*args,**kwargs):
      students = self.get_queryset()
      serializer = StudentSerializer(students, many=True)
      return Response(serializer.data)

   def post(self, request, **kwargs):
      serializer = StudentDetailSerializer(data={**request.data, **kwargs})
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      else:
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIStudentDetail(APIView):

   def get(self,request,*args,**kwargs):
      student = get_object_or_404(Student,**kwargs)
      serializer = StudentDetailSerializer(student,many=False)
      if not serializer:
         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
      return Response(serializer.data)

   def put(self, request, **kwargs):
      student_details = get_object_or_404(Student, **kwargs)
      serializer = StudentDetailSerializer(student_details, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      else:
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   def delete(self, request, **kwargs):
      student_details = get_object_or_404(Student, **kwargs)
      student_details.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)