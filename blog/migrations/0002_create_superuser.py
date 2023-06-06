from django.db import migrations
from django.contrib.auth.models import User
from django.conf import settings


def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            "admin", "test@test.cxx", settings.DJANGO_SUPERUSER_PASSWORD)


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
