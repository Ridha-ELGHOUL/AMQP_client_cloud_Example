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
mqtthost = "localhost"  
mqttuser = "guest"  
mqttpass = "guest"  
mqtttopic = "data"  

def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code %d." % (rc))
def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
 
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
    (rc, mid) = client.publish(mqtttopic, str(randN), qos=1)
    time.sleep(0.5)
