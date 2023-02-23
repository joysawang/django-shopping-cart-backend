from django.views.generic import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from category.forms import CategoryForm
from django.urls import reverse_lazy
from django.views.generic import ListView
from category import models

class CategoryIndexView(ListView):
    model = models.Category
    template_name = 'category/index.html'
    paginate_by =25

class CategoryCreateView(CreateView):
    template_name = 'category/create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('manage:categories/index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context