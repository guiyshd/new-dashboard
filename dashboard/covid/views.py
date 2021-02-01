from django.views.generic import TemplateView
from .methods import insert


class Dashboard(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        insert()
