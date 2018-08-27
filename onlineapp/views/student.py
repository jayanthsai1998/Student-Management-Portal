from django.views import View
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import *
from onlineapp.models import *
from onlineapp.forms import *
from django.urls import reverse_lazy
from onlineapp.forms.mocktest import *

class CreateStudentView(CreateView):
    model = Student
    form_class = AddStudent
    template_name = "add_student.html"
    success_url = reverse_lazy('index.html')

    def get_context_data(self, **kwargs):
        context = super(CreateStudentView, self).get_context_data(**kwargs)
        context.update(
            {
                'mark_form': AddMarks()
            }
        )
        return context

    def post(self, request, *args, **kwargs):
        college = get_object_or_404(College, pk=kwargs.get('college_id'))
        student_form = AddStudent(request.POST)
        test_form = AddMarks(request.POST)

        if student_form.is_valid():
            student = student_form.save(False)
            student.college = college
            student.save()

            if test_form.is_valid():
                test = test_form.save(False)
                test.student = student
                test.total = sum(test_form.cleaned_data.values())
                test.save()

        college_id = college.id
        return redirect("particular_college", **{'pk': college_id})

class UpdateStudentView(UpdateView):
    model = Student
    form_class = AddStudent
    template_name = 'edit_student.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateStudentView, self).get_context_data(**kwargs)
        student = context.get('student')
        test_form = AddMarks(instance=student.mocktest1)
        context.update({
            'edit': True,
            'mark_form': test_form
        })
        return context

    def get_success_url(self):
        return redirect('particular_college', **{'pk':self.kwargs.get('college_id')}).url

    def post(self, request, *args, **kwargs):

        student = Student.objects.get(pk=kwargs.get('pk'))
        _mock_test = student.mocktest1
        form = AddStudent(request.POST, instance=student)
        test_form = AddMarks(request.POST, instance=_mock_test)
        test = test_form.save(False)
        test.total = sum(test_form.cleaned_data.values())
        form.save()
        test_form.save()

        return redirect('particular_college', **{'pk':self.kwargs.get('college_id')}).url



class DeleteStudentView(DeleteView):

    model = Student
    template_name = "delete_student.html"
    success_url = reverse_lazy('particular_college')
    pass


