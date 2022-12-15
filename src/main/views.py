from django.views.generic import TemplateView, DetailView

from src.main.models import About, Services, WhyUs, Team, Testimonials


class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['about'] = About.objects.get()
        context['whyus'] = WhyUs.objects.get()
        context['services'] = Services.objects.order_by('id')
        context['testimonials'] = Testimonials.objects.order_by('id')

        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['about'] = About.objects.get()
        context['whyus'] = WhyUs.objects.get()
        context['team'] = Team.objects.order_by('id')
        return context


class ServiceDetailView(DetailView):
    model = Services
    template_name = 'service_detail.html'
    context_object_name = 'service'


class ContactView(TemplateView):
    template_name = 'contact.html'
