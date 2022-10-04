from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin# This is needed for object oriented programming. A class should only inherit one class. A Mixin is another class that can be inherited from allwoing for a class to inherit more classes essentially.
from django.urls import reverse_lazy
from .models import Issue

class IssueListView(ListView):
    template_name = "issues/list.html"
    model = Issue

class IssueDetailView(DetailView):
    template_name = "issues/detail.html"
    model = Issue

class IssueCreateView(LoginRequiredMixin, CreateView):
    template_name = "issues/new.html" 
    model = Issue
    fields = ["title", "subtitle", "body"]

    def form_valid(self, form): # This overrides the default form_valid() method of Django 
        form.instance.author = self.request.user # Allows the Author to request the user model.
        return super().form_valid(form) # Super() calls the form method

class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # REMEMBER, Mixin order matters for validations.
    template_name = "issues/edit.html"
    model = Issue
    fields = ["title", "subtitle", "author", "body"] # Fields will be showed on the page
    # Test for UserPassesTestMixin that the user needs to pass
    def test_func(self):
        issue_obj = self.get_object()
        return issue_obj.author == self.request.user

# delete view for details
class IssueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # REMEMBER, Mixin order matters for validations.
    model = Issue
    # success_url ="/issues" # You can specify success urlurl to redirect after successfully
    template_name = "issues/confirm_delete.html" # deleting object
    success_url = reverse_lazy("list") # From Django's urls module. Redirects after successfully deleting object
    # Test for UserPassesTestMixin that the user needs to pass
    def test_func(self):
        issue_obj = self.get_object()
        return issue_obj.author == self.request.user