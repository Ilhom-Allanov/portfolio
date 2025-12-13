from django.views.generic import TemplateView
from app.models import Portfolio, Portfolio2, Contact, Portfolio3


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolios'] = Portfolio.objects.all()
        context['portfolios2'] = Portfolio2.objects.all()
        context['portfolios3'] = Portfolio3.objects.all()
        return context
