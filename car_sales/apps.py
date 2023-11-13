from django.apps import AppConfig


class CarSalesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'car_sales'

    def ready(self):
        import car_sales.signals
