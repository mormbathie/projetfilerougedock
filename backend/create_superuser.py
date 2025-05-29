import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'odc.settings')
django.setup()

from django.contrib.auth.models import User

username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'mormbathie98')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'mormbathie98@gmail.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', '1234')

if not User.objects.filter(username=username).exists():
    user = User.objects.create_superuser(username=username, email=email, password=password)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print(f"Superuser {username} created with is_staff=True.")
else:
    print(f"Superuser {username} already exists.")
