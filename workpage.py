
import pika
import smtplib
from smtplib import SMTP

# RabbitMQ üzerine bir bağlantı açıyoruz
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# iletişim için kanalımızı alıyoruz
channel = connection.channel()

# isim vererek bir sıra tanımlaması yapıyoruz
# burada sıranın tanımlı olması önemli değil yine de
# bu yöntem kullanılabilir, daha kesin çalışması sağlanır
channel.queue_declare(queue='selam')


# sıra üzerinde bir mesaj işlendiğinde kullanılacak
# geri çağırma fonksiyonu
def callback(ch, method, properties, body):
    print("Bir mesaj geldi => %r" % body)


print('Sıraya bir mesaj gelmesi bekleniyor...')

# parametreler vererek kanal üzerindeki işleri işlemeye başlıyoruz
channel.basic_consume(callback,
                      queue='selam',
                      no_ack=True)


mail = smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()
mail.login("u.s.cakmak02@gmail.com","Ugur1679")
mail.sendmail.("u.s.cakmak02@gmail.com","ymekeci@gmail.com",body)

channel.start_consuming()