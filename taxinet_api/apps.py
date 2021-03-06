from django.apps import AppConfig


class TaxinetApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'taxinet_api'

    def ready(self):
        import taxinet_api.signals
