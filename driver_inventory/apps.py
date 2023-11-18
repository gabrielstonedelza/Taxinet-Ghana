from django.apps import AppConfig


class DriverInventoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'driver_inventory'

    def ready(self):
        import driver_inventory.signals