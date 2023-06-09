from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from .models import Project, Yarn

class ProjectListView(LoginRequiredMixin,ListView):
    model = Project
    context_object_name = 'projects'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['name', 'project_type', 'instructions']
    success_url = "/yarn/new"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
class ProjectUpdateView(UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['name', 'project_type', 'instructions', 'end_time']
    success_url = "/"

    def test_func(self):
        project = self.get_object()
        return self.request.user == project.user

class ProjectDeleteView(UserPassesTestMixin, DeleteView):
    model = Project
    success_url = "/"

    def test_func(self):
        project = self.get_object()
        return self.request.user == project.user


class YarnCreateView(LoginRequiredMixin, CreateView):
    model = Yarn
    fields = ['name', 'brand', 'length']
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['existing_yarns'] = Yarn.objects.filter(user=self.request.user).exclude(name='')
        context['existing_projects'] = Project.objects.filter(user=self.request.user)
        return context

    def form_valid(self, form):
        existing_yarn_pk = self.request.POST.get('existing_yarn')

        if existing_yarn_pk:
            existing_yarn = get_object_or_404(Yarn, pk=existing_yarn_pk)
            project_pk = self.request.POST.get('project')

            if project_pk:
                existing_yarn.project_id = project_pk
            else:
                existing_yarn.project = None

            form.instance = existing_yarn
            return super().form_valid(form)
        form.instance.user = self.request.user
        return super().form_valid(form)
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class YarnUpdateView(UserPassesTestMixin, UpdateView):
    model = Yarn
    fields = ['name', 'brand', 'length']
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['existing_yarns'] = Yarn.objects.filter(user=self.request.user).exclude(name='')
        context['existing_projects'] = Project.objects.filter(user=self.request.user)
        return context

    def form_valid(self, form):
        existing_yarn_pk = self.request.POST.get('existing_yarn')

        if existing_yarn_pk:
            existing_yarn = get_object_or_404(Yarn, pk=existing_yarn_pk)
            project_pk = self.request.POST.get('project')

            if project_pk:
                existing_yarn.project_id = project_pk
            else:
                existing_yarn.project = None

            form.instance = existing_yarn
            return super().form_valid(form)
        form.instance.user = self.request.user
        return super().form_valid(form)
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
    def test_func(self):
        yarn = self.get_object()
        return self.request.user == yarn.user
        
class YarnListView(LoginRequiredMixin, ListView):
    model = Yarn
    context_object_name = 'yarns'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class YarnDeleteView(UserPassesTestMixin, DeleteView):
    model = Yarn
    success_url = "/"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class RegisterView( CreateView):
	form_class = UserCreationForm
	template_name = "registration/registration.html"
	success_url = "/login"
	success_message = "Registration accepted. You can now log in. "


