from celery import shared_task
import time

@shared_task
def notify_delivery_creation(delivery_id):
    print(f"Iniciando proceso pesado para entrega #{delivery_id}...")
    time.sleep(5)
    print(f"¡Notificación enviada con éxito para la entrega #{delivery_id}!")
    return True