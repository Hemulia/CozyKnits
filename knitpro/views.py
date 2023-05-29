from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Project, Yarn

class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'

class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'project_type', 'instructions']
    success_url = "/yarn/new"

class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['name', 'project_type', 'instructions']
    success_url = "/"

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = "/"

from django.urls import reverse_lazy

class YarnCreateView(CreateView):
    model = Yarn
    fields = ['name', 'brand', 'length', 'project']
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['existing_yarns'] = Yarn.objects.all()  # Queryset of existing yarns
        return context

    def form_valid(self, form):
        existing_yarn_pk = self.request.POST.get('existing_yarn')  # Get the selected existing yarn

        if existing_yarn_pk:
            existing_yarn = Yarn.objects.get(pk=existing_yarn_pk)

        self.object = form.save(commit=False)  # Create the object but don't save it yet

        project_pk = self.request.POST.get('project')  # Get the selected project
        if project_pk:
            self.object.project_id = project_pk
        else:
            self.object.project = None

        self.object.save()

        return super().form_valid(form)


class YarnUpdateView(UpdateView):
    model = Yarn
    fields = ['name','brand','length', 'project']
    success_url= "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['existing_yarns'] = Yarn.objects.all()  # Queryset of existing yarns
        return context

    def form_valid(self, form):
        existing_yarn_pk = self.request.POST.get('existing_yarn')  # Get the selected existing yarn

        if existing_yarn_pk:
            existing_yarn = Yarn.objects.get(pk=existing_yarn_pk)
            
        self.object = form.save(commit=False)  # Create the object but don't save it yet

        if not self.object.project:
            self.object.project = None

        self.object.save() 

        return super().form_valid(form)
    
class YarnListView(ListView):
    model = Yarn
    context_object_name = 'yarns'

class YarnDeleteView(DeleteView):
    model = Yarn
    success_url = "/"


