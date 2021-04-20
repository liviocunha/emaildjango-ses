"""
Python SECRET_KEY generator.
"""
import random

chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
size = 50
secret_key = "".join(random.sample(chars, size))

CONFIG_STRING = """
DEBUG=True
SECRET_KEY=%s
ALLOWED_HOSTS=127.0.0.1, .localhost

EMAIL_BACKEND=django_ses.SESBackend
AWS_ACCESS_KEY_ID=YOUR-ACCESS-KEY-ID
AWS_SECRET_ACCESS_KEY=YOUR-SECRET-ACCESS-KEY

# Additionally, if you are not using the default AWS region of us-east-1,
# you need to specify a region, like so:
AWS_SES_REGION_NAME=us-east-2
AWS_SES_REGION_ENDPOINT=email.us-east-2.amazonaws.com
""".strip() % (secret_key)

# Writing our configuration file to '.env'
with open('.env', 'w') as configfile:
    configfile.write(CONFIG_STRING)

print('Success!')
print('Type: cat .env')