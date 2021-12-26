from django.views.generic import TemplateView


class Landing(TemplateView):

    template_name = "home/landing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "success" in self.request.GET:
            context.update({"success": True})
        elif "error" in self.request.GET:
            context.update({"error": True})
        return context
