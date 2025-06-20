# rabbit_consumer.py
import os
import pika
import logging
from flask import current_app

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def start_consumer(app):
    def callback(ch, method, properties, body):
        with app.app_context(): 
            try:
                event_id = int(body.decode('utf-8'))
                result = current_app.report_service.delete_report_by_id_event(event_id)
                logger.info(f"Deleted {result.deleted_count} reports for event_id {event_id}")
            except ValueError:
                logger.info(f"Mensaje recibido desde la cola: {body}")
                logger.warning("Invalid message format: Expected an integer")
            except Exception as e:
                logger.error(f"Error processing message: {e}")

    connection_parameters = pika.ConnectionParameters('rabbitmq')
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()

    queue_name = os.getenv('NAME_QUEUE')
    channel.queue_declare(queue=queue_name, durable=True)

    channel.basic_consume(queue=queue_name, auto_ack=True, on_message_callback=callback)

    logger.info("RabbitMQ consumer started and waiting for messages.")
    channel.start_consuming()
