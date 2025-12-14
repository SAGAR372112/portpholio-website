import os
from django.apps import AppConfig

class CoreConfig(AppConfig):
    name = "core"

    def ready(self):
        if os.environ.get("CREATE_ADMIN") != "true":
            return

        from django.contrib.auth import get_user_model
        User = get_user_model()

        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="Admin@123"
            )
