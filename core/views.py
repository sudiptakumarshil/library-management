from django.shortcuts import render
from django.views.generic import TemplateView, View
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'
    
class BookDetailView(View):
    template_name = 'details.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)