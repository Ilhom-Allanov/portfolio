from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from app.form import ContactForm
from app.models import Portfolio, Portfolio2, Contact, Portfolio3


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolios'] = Portfolio.objects.all()
        context['portfolios3'] = Portfolio3.objects.all()
        return context

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class BlogView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolios2'] = Portfolio2.objects.all()
        return context
class PortfolioView(TemplateView):
    template_name = 'portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolios'] = Portfolio.objects.all()
        return context
class ServiceView(TemplateView):
    template_name = 'service.html'
