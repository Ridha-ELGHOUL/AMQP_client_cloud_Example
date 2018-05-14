import pika
#url ='amqp://dvbbxdot:Z_TsnQ5lDj8wtwR3r4de2Y2Ot_YSnG@hound.rmq.cloudamqp.com'
#params=pika.URLParameters(url)
#connection = pika.BlockingConnection(params)
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel= connection.channel()
channel.queue_declare(queue='v1')

def callback(ch,method,properties,body):
    print('Data Received %r' %(body))
channel.basic_consume(callback, queue='Data', no_ack=True)
channel.start_consuming()
