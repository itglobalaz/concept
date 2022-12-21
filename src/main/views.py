from django.contrib import messages
from django.views.generic import TemplateView, DetailView, FormView
from django.utils.translation import gettext_lazy as _

from config.etc.mail_settings import send_email_feedback
from src.main.forms import ContactForm
from src.main.models import About, Services, WhyUs, Team, Testimonials, Project


class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['about'] = About.objects.get()
        context['whyus'] = WhyUs.objects.get()
        context['services'] = Services.objects.order_by('id')
        context['testimonials'] = Testimonials.objects.order_by('id')
        context['projects'] = Project.objects.order_by('id')[:4]

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


class ProjectsView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(ProjectsView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.order_by('id')
        return context

    template_name = 'projects.html'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'


class SendContactMessage(FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def form_valid(self, form):
        send_email_feedback(form.cleaned_data)
        messages.success(self.request, _('Təşəkkür edirik!'))
        return super().form_valid(form)

    def get_success_url(self):
        redirect_url = self.request.GET.get('redirect_url')
        return redirect_url or super().get_success_url()
