from django.conf import settings 
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string
from ..forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            if not email:
                messages.error(request, 'The email field is required')
                return render(request, 'contact.html', {'form': form})

            if len(name) < 3:
                messages.error(request, 'The name field must have at least 3 characters')
                return render(request, 'contact.html', {'form': form})

            if len(subject) < 5:
                messages.error(request, 'The subject field must have at least 5 characters')
                return render(request, 'contact.html', {'form': form})

            if len(message) < 10:
                messages.error(request, 'The message field must have at least 10 characters')
                return render(request, 'contact.html', {'form': form})

            email_content = render_to_string('email.html', {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message,
            })

            try :
                send_mail(
                    subject + ' - DjanBlog',
                    message,
                    email,
                    [settings.EMAIL_TO],
                    html_message=email_content,
                    fail_silently=False,
                )

                messages.success(request, "Your message has been sent with success!")
                
                return render(request, 'success.html')
            
            except Exception as e:
                messages.error(request, "Your message was not sent due to an error!")
                
                return render(request, 'fail.html', {'error': str(e)})            
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})