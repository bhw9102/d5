from django.apps import AppConfig


class TicketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ticket'

    def ready(self):
        from .container import TicketContainer
        container = TicketContainer()
        container.wire(modules=[".controller.ticket_controller"])
