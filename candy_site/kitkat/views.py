from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "kitkathome.html"

class AboutView(TemplateView):
    template_name = "kitkatabout.html"
