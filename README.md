# Django Mailer

A simple Django application to send emails using SMTP.

## Features

- Send emails via SMTP
- Easy integration with Django projects
- Supports plain text and HTML emails
- Configurable email settings

## Installation

1. Ensure you have Django installed in your project. If not, you can install it using pip:

    ```bash
    pip install django
    ```

2. Clone this repository and add it to your Django project.

## Configuration

1. Add your email configurations in your Django project's `settings.py` file:

    ```python
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.your-email-provider.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'your-email@example.com'
    EMAIL_HOST_PASSWORD = 'your-email-password'
    ```

2. (Optional) To avoid hardcoding sensitive information in your `settings.py`, consider using environment variables or Django's `django-environ` package.

## Usage
3. Add this to your `views.py` file of app

### Sending a Simple Email

To send a simple email, you can use Django's built-in `send_mail` function:

  ```python
    from django.core.mail import send_mail
    from django.conf import settings
    
    send_mail(
        subject='Hello from Django SMTP Mailer',
        message='This is a test email.',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['recipient@example.com'],
        fail_silently=False,
    )
   ```
