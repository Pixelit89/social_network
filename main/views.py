from django.shortcuts import render
from django.views import generic
from .models import ExtendedUser

class IndexView(generic.DetailView):
    template_name = 'user.html'
    model = ExtendedUser

    # def get_context_data(self, **kwargs):
    #     context = super(IndexView, self).get_context_data(**kwargs)
    #     return context

