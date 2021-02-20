from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from . import forms
from . import models


class SignupView(CreateView):
    """
    The view isn't part of urls.py but you can add it to your own project's
    url configuration if you want to use it.

    To mount it, add a source_id kwarg, for instance::

        path("signup/<int:source_id>/", SignupView.as_view()),
    """

    model = models.UserConsent
    form_class = forms.EmailConsentForm
    template_name = "consent/signup/create.html"

    def dispatch(self, request, *args, **kwargs):
        self.consent_source = get_object_or_404(
            models.ConsentSource, id=kwargs["source_id"]
        )
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["consent_source"] = self.consent_source
        return kwargs

    def get_success_url(self):
        return reverse(
            "signup_confirmation", kwargs={"source_id": self.consent_source.id}
        )


class SignupConfirmationView(TemplateView):
    """
    Tells the user to check their inbox after a successful signup.

    To mount it, add a source_id kwarg, for instance::

        path("signup/<int:source_id>/confirmation/", SignupConfirmationView.as_view()),
    """

    template_name = "consent/signup/confirm.html"
