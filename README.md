# Send emails with Amazon SES 
Django project example using the [Django-SES](https://github.com/django-ses/django-ses). 

Protect confidential information in development environment use .env and environment variables in production.

## First of all configure SES on Amazon Web Services.

- Access http://console.aws.amazon.com/sesv2/home#/account
- Create identity in Configuration > Verified identities
- When your SES account is in "sandbox" mode, you can:
    - Only send from verified domains and email addressed, and
    - Only send to verified domains and email addresses

In order to send to anyone else, you must move your account out of sandbox mode by contacting AWS support and requesting it:
https://docs.aws.amazon.com/console/ses/sandbox

## This project was done with:
* Python 3.9.1
* Django 3.1.6
* Django-SES 2.0.0
* Boto3 1.17.2
* python-decouple 3.4

## How to run project?
* Clone this repository.
* Create virtualenv with Python 3.
* Active the virtualenv.
* Install dependences.
* Create .env
* Run the migrations.
* Create user admin.

```bash
git clone https://github.com/liviocunha/emaildjango-ses.git
cd emaildjango-ses
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py makemigrations core
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```