# from rest_framework import serializers
# from onlineapp.models import *
#
# class CollegeSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length = 128)
#     location = serializers.CharField(max_length = 64)
#     acronym = serializers.CharField(max_length = 8)
#     contact = serializers.EmailField()
#
#     def create(self, validated_data):
#         del validated_data['id']
#         #return CollegeSerializer(**validated_data)
#         return College.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         #instance.id = validated_data.get('id', instance.id)
#         instance.name = validated_data.get('name', instance.name)
#         instance.location = validated_data.get('location', instance.location)
#         instance.acronym = validated_data.get('acronym', instance.acronym)
#         instance.contact = validated_data.get('contact', instance.contact)
#         instance.save()
#         return instance
#
#
# from rest_framework.serializers import ModelSerializer,CharField,IntegerField
#
# class StudentSerializer(ModelSerializer):
#     class Meta:
#         model = Student
#         exclude = ['college']
#
#     def __str__(self):
#         return self.data
#
# class MarksSerializer(ModelSerializer):
#     class Meta:
#         model = MockTest1
#         fields = ('problem1', 'problem2', 'problem3', 'problem4', 'total')
#
#     def __str__(self):
#         return str(self.data)
#
# class StudentDetailsSerializer(ModelSerializer):
#     marks = MarksSerializer()
#
#     class Meta:
#         model = Student
#         fields = ('name', 'email', 'db_folder', 'dropped_out', 'marks')
#
#     def create(self, validated_data):
#         marks_data = validated_data.pop('marks')
#         student = Student.objects.create(**validated_data)
#         student.marks = MockTest1.objects.create(student=student, **marks_data)
#         return student
#
#     def update(self, instance, validated_data):
#         marks_data = validated_data.pop('marks')
#         marks = instance.marks
#         instance.name = validated_data.get('name', instance.name)
#         instance.dropped_out = validated_data.get('dropped_out', instance.dropped_out)
#         instance.email = validated_data.get('email', instance.email)
#         instance.save()
#         marks.problem1 = marks_data.get('problem1', marks.problem1)
#         marks.problem2 = marks_data.get('problem2', marks.problem2)
#         marks.problem3 = marks_data.get('problem3', marks.problem3)
#         marks.problem4 = marks_data.get('problem4', marks.problem4)
#         marks.total = marks_data.get('total', marks.total)
#         marks.save()
#         instance.marks = marks
#         return instance
#
#     def __delete__(self, instance):
#         instance.delete()
#
#     def __str__(self):
#         return str(self.data)
#
# class StudentViewSerializer(serializers.Serializer):
#     name = CharField(max_length=128)
#     db_folder = CharField(max_length=50)
#     total = IntegerField()
#
#     def create(self, validated_data):
#         return StudentViewSerializer.objects.create(**validated_data)
#
# class CollegeDetailsSerializer(ModelSerializer):
#     student_set = StudentSerializer(many=True)
#
#     class Meta:
#         model = College
#         fields = ('name', 'acronym', 'location', 'contact', 'student_set')
#
#     def __str__(self):
#         return self.data
#
# # class MockTest1Serializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = MockTest1
# #         fields = ('id', 'problem1', 'problem2', 'problem3', 'problem4', 'total')
# #
# # class StudentSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Student
# #         fields = ('id', 'name', 'dob', 'email', 'db_folder', 'dropped_out', 'college')
# #
# #
# # class StudentDetailSerializer(serializers.ModelSerializer):
# #     stud = StudentSerializer()
# #     mocktest1 = MockTest1Serializer()
# #
# #     class Meta:
# #         model = Student
# #         fields = ('id', 'name', 'email', 'db_folder', 'dropped_out', 'college', 'mocktest1')
# #
# #
# #     def create(self, validated_data):
# #
# #         user_data = validated_data.pop('id')
# #         stud = StudentSerializer.create(StudentSerializer(), validated_data=user_data)
# #         stud, created = MockTest1.objects.update_or_create(student=stud)
# #         return stud
# #
# #     def update(self, instance, validated_data):
# #         instance.id = validated_data.get('id', instance.id)
# #         instance.name = validated_data.get('name', instance.name)
# #         instance.dob = validated_data.get('dob', instance.dob)
# #         instance.email =  validated_data.get('email', instance.email)
# #         instance.db_folder = validated_data.get('db_folder', instance.db_folder)
# #         instance.droppped_out = validated_data('dropped_out', instance.droppped_out)
# #
# #         instance.college_id = validated_data('college', instance.college_id)
# #
# #         mockdata = validated_data.pop('mocktest1')
# #         if not hasattr(instance, 'mocktestdat1'):
# #             mocktestdata = {'problem1': 0, 'problem2': 0, 'problem3': 0, 'problem4': 0, 'total':0}
# #             mock = MockTest1.objects.create(instance, **mocktestdata)
# #             setattr(instance, 'mocktest1', mock)
# #
# #         instance.mocktest1.problem1 = mockdata.get('problem1', instance.mocktest1.problem1)
# #         instance.mocktest1.problem2 = mockdata.get('problem2', instance.mocktest1.problem2)
# #         instance.mocktest1.problem3 = mockdata.get('problem3', instance.mocktest1.problem3)
# #         instance.mocktest1.problem4 = mockdata.get('problem4', instance.mocktest1.problem4)
# #         instance.save()
# #         return instance
#
#
#
# # class StudentSerializer(serializers.Serializer):
# #     name = serializers.CharField(max_length = 128)
# #     dob = serializers.DateField(allow_null = True)
# #     email = serializers.EmailField()
# #     db_folder = serializers.CharField(max_length = 50)
# #     dropped_out = serializers.BooleanField(default = True)
# #     #college = serializers.For
# #
# # class MockTest1Serializer(serializers.Serializer):
# #     problem1 = serializers.IntegerField()
# #     problem2 = serializers.IntegerField()
# #     problem3 = serializers.IntegerField()
# #     problem4 = serializers.IntegerField()
# #     total = serializers.IntegerField()



# from rest_framework import serializers
# from onlineapp.models import *
#
# class CollegeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=College
#         fields=('id','name','location','acronym','contact')
#
#
# class StudentSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model=Student
#         fields=('name','db_folder','email','dob','dropped_out')
#
#
# class MockTest1Serializer(serializers.ModelSerializer):
#     class Meta:
#         model=MockTest1
#         fields=('problem1','problem2','problem3','problem4')
#
#
# class StudentDetailSerializer(serializers.ModelSerializer):
#     mocktest1 = MockTest1Serializer()
#     class Meta:
#         model = Student
#         fields = ('name','db_folder','email','dob','dropped_out','mocktest1')
#
#
#
#     # def create(self,validated_data):
#     #     mock_data = validated_data.pop('mocktest1')
#     #     student = Student.objects.create(**validated_data)
#     #     import ipdb
#     #     ipdb.set_trace()
#     #     #MockTest1.objects.create(student__id = student_id,mock_data)
#     #
#     #     return student
#
#
#
#     def update(self, instance, validated_data):
#         mock_data=validated_data.pop('mocktest1')
#         mocktest=instance.mocktest1
#         instance.__dict__.update(**validated_data)
#         instance.save()
#         mocktest.__dict__.update(mock_data)
#         mocktest.save()
#         return instance


from rest_framework import serializers
from onlineapp.models import College,Student, MockTest1


class CollegeSerializer(serializers.Serializer):
   id = serializers.IntegerField(read_only=True)
   name = serializers.CharField(max_length=128)
   location = serializers.CharField(max_length=64)
   acronym = serializers.CharField(max_length=8)
   contact = serializers.EmailField()

   def create(self, validated_data):
      return College.objects.create(**validated_data)

   def update(self, instance, validated_data):
      instance.name = validated_data.get('name', instance.name)
      instance.location = validated_data.get('location', instance.location)
      instance.acronym = validated_data.get('acronym', instance.acronym)
      instance.contact = validated_data.get('contact', instance.contact)
      instance.save()
      return instance



class StudentSerializer(serializers.ModelSerializer):
   class Meta:
      model = Student
      exclude = []


class MockTest1Serializer(serializers.ModelSerializer):
   class Meta:
      model = MockTest1
      fields = ('problem1','problem2','problem3','problem4','total')

   def create(self, validated_data):
      data_copy = self._kwargs.get('data')
      data_copy.pop('total')
      validated_data['student'] = data_copy.pop('student')
      mocktest1 = MockTest1.objects.create(**validated_data)
      mocktest1.total = sum(data_copy.values())
      mocktest1.save()
      return mocktest1

   def update(self, instance, validated_data):
      instance.problem1 = validated_data.get('problem1', instance.problem1)
      instance.problem2 = validated_data.get('problem2', instance.problem2)
      instance.problem3 = validated_data.get('problem3', instance.problem3)
      instance.problem4 = validated_data.get('problem4', instance.problem4)
      validated_data.pop('total')
      instance.total = validated_data.get('total', sum(validated_data.values()))
      instance.save()
      return instance


class StudentDetailSerializer(serializers.ModelSerializer):
   mocktest1 = MockTest1Serializer(many=False)
   class Meta:
      model = Student
      fields = ('id','name','dob','email','db_folder','dropped_out','college','mocktest1')

   def create(self, validated_data):
      mocktest1_data = dict(validated_data.pop('mocktest1'))
      pk = self._kwargs.get('data').get('college')
      college = College.objects.get(pk=pk)
      validated_data['college'] = college
      student = Student.objects.create(**validated_data)
      mocktest1_data['student'] = student
      mocktest1 = MockTest1Serializer(data=mocktest1_data)
      if mocktest1.is_valid():
         mocktest1.save()
         student.save()
      return student

   def update(self, instance, validated_data):
      instance.name = validated_data.get('name', instance.name)
      instance.email = validated_data.get('email', instance.email)
      instance.dob = validated_data.get('data', instance.dob)
      instance.db_folder = validated_data.get('db_folder', instance.db_folder)
      mocktest1 = MockTest1Serializer(instance.mocktest1, data=dict(
         self._validated_data.get('mocktest1')
      ))
      if mocktest1.is_valid():
         mocktest1.save()
         instance.save()
      return instance