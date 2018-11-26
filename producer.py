import pika
import mysql.connector


connection = mysql.connector.connect(host='localhost',
                            database='mail_db',
                            user='root',
                            password='1234')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='selam')

# yukarıda aldığımız kanala bir iş gönderiyoruz
channel.basic_publish(exchange='',
                      routing_key='selam',
                      body='Merhaba!')

print("Selam mesajı sıraya gönderildi.")

connection.close()