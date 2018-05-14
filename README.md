# AMQP_client_cloud_Example
An example of an AMQP implementation client using rabbitMQ as server. A producer publish data with a random function. The consumer get the data from ther server. (Two option is performed: Cloud server and local rabbitMQ server.)

# Steps:
1. For Local use : Dowload Install a rabbitMQ server from https://www.rabbitmq.com/download.html by choosing the appropriate OS version.
2. For Cloud use : create a cloud accound for free (limited features) testing https://www.cloudamqp.com/ then create an instance. You must have a token for using your account by externel cloud client. 
Change the url adress in both consumer and producer files with yours (url token).
3. Make sure that the python version (last version) is completely installed in your environnement.
4. Run consumer by running the follow commandin terminal:
 python consumer.py (Linux/Mac) ;  python .\consumer.py (Win 10)
4. Run producer by running the follow command in terminal:
 python producer.py (Linux/Mac) ;  python .\producer.py (Win 10)
