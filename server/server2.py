import pika
import time

def on_message(channel, method_frame, header_frame, body):
	print("Message body", body)
	channel.queue_declare(queue=body, auto_delete=True)
	channel.basic_ack(delivery_tag=method_frame.delivery_tag)

credentials = pika.PlainCredentials('guest', 'guest')
parameters =  pika.ConnectionParameters('localhost', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.exchange_declare(exchange="celery", exchange_type="direct", passive=False, durable=True, auto_delete=False)
channel.queue_declare(queue="standard", auto_delete=True)
channel.queue_bind(queue="standard", exchange="celery", routing_key="standard_key")
channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_message, 'standard')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

#def run():
#print("listening for message...")
#	

#while True:
#	run()
#	time.sleep(5)
