import pika
from random import gauss
import paho.mqtt.client as paho
import time
k =0 
#url ='amqp://dvbbxdot:Z_TsnQ5lDj8wtwR3r4de2Y2Ot_YSnG@hound.rmq.cloudamqp.com/'
#params=pika.URLParameters(url)
#connection = pika.BlockingConnection(params)
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel= connection.channel()

client = paho.Client()
client.on_connect = on_connect
client.on_publish = on_publish
client.username_pw_set(mqttuser,mqttpass)
client.connect(mqtthost, 1883,60)


client.loop_start()
print("Sending Data ...")
while (1):
    k=k+1
    randN = gauss(1,500)
    #print ((randN))
    channel.basic_publish(exchange='',routing_key='Data',body=str(randN)+'  Ref: '+str(k))
    time.sleep(0.5)
