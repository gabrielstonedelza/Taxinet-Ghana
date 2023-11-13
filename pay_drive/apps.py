from django.apps import AppConfig


class PayDriveConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pay_drive'

    def ready(self):
        import pay_drive.signals
