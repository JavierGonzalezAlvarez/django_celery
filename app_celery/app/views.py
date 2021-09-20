from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import EmailForm
from .tasks import sendEmailTask


def sendEmail(request):
    if request.method == 'POST':
        # cremaos una isntancia del formulario
        form = EmailForm(request.POST)
        # form valido
        if form.is_valid():
            # get campos del formulario con cleaned_data
            subject = form.cleaned_data['asunto']
            message = form.cleaned_data['texto']
            sender = form.cleaned_data['email']
            # ejecutar task (asincronía)
            sendEmailTask.delay(subject, message, sender)

            #subject = form.cleaned_data['asunto']
            #message = form.cleaned_data['texto']
            #sender = form.cleaned_data['email']
            # email_message = EmailMessage(
            #    subject=subject,
            #    body=message,
            #    to=[sender],
            # )
            # email_message.send()

            # limpiar post formulario
            form = EmailForm()
            return HttpResponseRedirect('')
    # si es GET el formulario en blanco
    else:
        form = EmailForm()

    return render(request, 'emailTemplate.html', {'form': form})
