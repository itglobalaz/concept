from django.core.mail import EmailMessage

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'smtp.yandex.ru'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'info@alfagroup.az'
# EMAIL_HOST_PASSWORD = 'Alfa-2022'
# DEFAULT_FROM_EMAIL = 'info@alfagroup.az'
EMAIL_USE_TLS = True


def send_email_feedback(data):
    name = data['name']
    email = data['email']
    subject = data['subject']
    description = data['description']
    email_body = (f'<strong>Mövzu</strong>: {subject}<br/>'
                  f'<strong>Ad</strong>: {name}<br/>'
                  f'<strong>Poçt:</strong> {email}<br/>'
                  f'<strong>Məlumat</strong>: {description}<br/>'
                  f'Письмо отправлена из сайта concepthouse.az'
                  )
    email = EmailMessage('Название темы', email_body, 'info@concepthouse.az', to=['info@concepthouse.az'])
    email.content_subtype = "html"
    email.send()