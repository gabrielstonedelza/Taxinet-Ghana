from django.apps import AppConfig


class TaxinetUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'taxinet_users'

    def ready(self):
        import taxinet_users.signals
