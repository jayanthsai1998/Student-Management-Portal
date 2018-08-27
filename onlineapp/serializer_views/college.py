# """API BASED VIEWS"""
#
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
# @csrf_exempt
# def college_list(request):
#     if request.method == 'GET':
#         snippets = College.objects.all()
#         serializer = CollegeSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         # print(request.data)
#         serializer = CollegeSerializer(data=request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
#
#
# @csrf_exempt
# def college_details(request, pk):
#     try:
#         snippet = College.objects.get(pk=pk)
#     except College.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = CollegeSerializer(snippet)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = CollegeSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#     # elif request.method == 'POST':
#     #     serializer = CollegeSerializer(snippet, request.PUT)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return JsonResponse(serializer.post)
#     #     return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)
#
#
#
#
# # @api_view(['GET', 'PUT', 'DELETE'])
# # def student_details(request, pk, ):
# #     if(request)
#
# # @api_view(['GET', 'POST'])
# # def colleges_list(request):
# #     if request.method == 'GET':
# #         colleges = College.objects.all()
# #         serializer = CollegeSerializer(colleges, many=True)
# #         return Response(serializer.data)
# #     if request.method == 'POST':
# #         serializer = CollegeSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         else:
# #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #
# #
# # @api_view(['GET', 'PUT', 'DELETE'])
# # def colleges_details(request, pk):
# #     college = get_object_or_404(College, pk=pk)
# #     serializer = CollegeSerializer(college)
# #     if not college:
# #         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
# #
# #     if request.method == 'GET':
# #         return Response(serializer.data)
# #     elif request.method == 'PUT':
# #         serializer = CollegeSerializer(college, data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         else:
# #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #     elif request.method == 'DELETE':
# #         college.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)



# from rest_framework.generics import ListAPIView,UpdateAPIView,CreateAPIView,DestroyAPIView
# from  onlineapp.serializers import *
# from onlineapp.models import *
#
# class collegeListViewSerializer(ListAPIView):
#     queryset = College.objects.all()
#     serializer_class = CollegeSerializer
#
#
# class CreateCollegeViewSerializer(CreateAPIView):
#     queryset = College.objects.all()
#     serializer_class = CollegeSerializer
#
#
# class EditCollegeViewSerializer(UpdateAPIView):
#     queryset = College.objects.all()
#     lookup_field = 'pk'
#     serializer_class = CollegeSerializer
#
#
# class DeleteCollegeViewSerializer(DestroyAPIView):
#     queryset = College.objects.all()
#     serializer_class = CollegeSerializer
#     lookup_field = 'pk'


from onlineapp.models import College
from onlineapp.serializers import CollegeSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# class APICollegeList(View):
#  def get(self, request):
#     colleges = College.objects.all()
#     serializer = CollegeSerializer(colleges,many=True)
#     return JsonResponse(serializer.data,safe=False)
#
#  def post(self, request):
#     data = JSONParser().parse(request)
#     serializer = CollegeSerializer(data=data)
#     if serializer.is_valid():
#        serializer.save()
#        return JsonResponse(serializer.data, status=201)
#     return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def api_college_list(request):

   if request.method == 'GET':
      colleges = College.objects.all()
      serializer = CollegeSerializer(colleges,many=True)
      return JsonResponse(serializer.data,safe=False)

   elif request.method == 'POST':
      data = JSONParser().parse(request)
      serializer = CollegeSerializer(data=data)
      if serializer.is_valid():
         serializer.save()
         return JsonResponse(serializer.data, status=201)
      return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def api_college_detail(request, pk):
   try:
      college = College.objects.get(pk=pk)
   except College.DoesNotExist:
      return HttpResponse(status=404)

   if request.method == 'GET':
      serializer = CollegeSerializer(college)
      return JsonResponse(serializer.data, safe=False)

   elif request.method == 'PUT':
      data = JSONParser().parse(request)
      serializer = CollegeSerializer(college, data=data)
      if serializer.is_valid():
         serializer.save()
         return JsonResponse(serializer.data)
      return JsonResponse(serializer.errors, status=400)

   elif request.method == 'DELETE':
      college.delete()
      return HttpResponse(status=204)