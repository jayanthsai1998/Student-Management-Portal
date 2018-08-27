from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import *
from onlineapp.models import *
from onlineapp.forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


from django.shortcuts import redirect, get_object_or_404, HttpResponse





















#  CLASS BASED VIEW

class CollegeView(View):

    def get(self, request, *args, **kwargs):

        clg_obj = College.objects.all()

        # import ipdb
        # ipdb.set_trace()

        return render(
            request,
            template_name = "index.html",
            context={
                'clg_obj': clg_obj
            }
        )

class CollegeListView( ListView):
    login_url = '/login/'
    model = College
    context_object_name = 'clg_obj'
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super(CollegeListView, self).get_context_data(**kwargs)

        # import ipdb
        # ipdb.set_trace()

        # we can write the query whatever we wnt here..

        context.update({'user_permissions' : self.request.user.get_all_permissions})
        return context

# class CreateCollegeView(LoginRequiredMixin, PermissionError)


class CollegeDetailsView(DetailView):
    login_url = '/login/'
    model = College
    context_object_name = 'particular_clg_obj'
    template_name = "particular_college.html"

    def get_object(self, queryset = None):
        return get_object_or_404(College, **self.kwargs)

    def get_context_data(self, **kwargs):
        context = super(CollegeDetailsView, self).get_context_data(**kwargs)
        # import ipdb
        # ipdb.set_trace()
        college = context.get('particular_clg_obj')
        students = list(college.student_set.order_by("-mocktest1__total"))

        context.update(
            {
                'college' : college,
                self.context_object_name : students,
                'user_permission' : self.request.user.get_all_permissions()
            }
        )

        return context



class CreateCollegeView(CreateView, LoginRequiredMixin, PermissionRequiredMixin):

    login = '/login/'
    permission_required = "index"
    permission_denied_message = "User does not have permission to change college"
    raise_exception = True

    model = College
    form_class = AddCollege
    template_name = "add_colleges.html"
    success_url = reverse_lazy('index')




class UpdateCollegeView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):

    login = '/login/'
    permission_required = "index"
    permission_denied_message = "User does not have permission to edit college"
    raise_exception = True

    model = College
    form_class = AddCollege
    template_name = "update_college.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super(UpdateCollegeView, self).get_context_data(**kwargs)
        return context

class DeleteCollegeView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):

    login = '/login/'
    permission_required = "index"
    permission_denied_message = "User does not have permission to delete college"
    raise_exception = True

    model = College
    template_name = "delete_college.html"
    success_url = reverse_lazy("index")