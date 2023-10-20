from django.views.generic import TemplateView


class FormsViews(TemplateView):
    template_name = "forms.html"


class EntityFormView(TemplateView):
    template_name = "components/forms/entity_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instrument = self.request.GET.get("instrument", None)
        context["instrument_param"] = instrument or ""
        return context
