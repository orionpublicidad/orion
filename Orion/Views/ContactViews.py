from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render

from Forms.ContactForm import ContactForm

from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.shortcuts import redirect

class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm()

        return context

    def post(self, request, *args, **kwargs):
        nomape = request.POST.get('nomape')
        numtel = request.POST.get('numtel')
        email = request.POST.get('email')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        body = render_to_string(
            'email_content.html', {
                'nomape': nomape,
                'numtel': numtel,
                'email': email,
                'mensaje': mensaje,
            },
        )

        email_message = EmailMessage(
            subject=asunto,
            body=body,
            from_email=email,
            to=[''],
        )
        email_message.content_subtype = 'html'
        email_message.send()

        return redirect('contacto')

    

    