from django.views.generic import TemplateView

class ProductIndexView(TemplateView):
    template_name = 'product/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'World'
        return context
