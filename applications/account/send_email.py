from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'Space_Cinema', # title
        f'http://localhost:8000/account/activate/{code}', # body
        'sspacecinema@gmail.com', # from
        [email] # to
    )