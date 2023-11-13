from django.apps import AppConfig


class DrivePayConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'drive_pay'

    def ready(self):
        import drive_pay.signals
