import time

from kafka import KafkaConsumer, KafkaProducer
from kafka_topics import create_topic, list_topics
from kafka_services import KafkaServices
from kafka_producer_consumer import KafkaProducerConsumer
from threading import Thread


def num_of_lines(file_path: str):
    return sum(1 for _ in open(file_path))


"""
def producer_part():
    reader = open(file='r.txt', mode='rb')
    producer = KafkaProducer(bootstrap_servers='localhost:9092')

    for line in reader:
        print('sending:%s' % line)
        producer.send('kahve', line)
    producer.flush()
    reader.close()
    for i in range(200):
        print('*=*', i)
        producer.send('kahve', b'end')
    return


def consumer_part():
    consumer = KafkaConsumer('kahve')

    writer = open(file='w.txt', mode='wb')
    msg = next(consumer)
    while msg.value != b'end':
        print(' > "%s"' % msg.value.decode()[:-1], '[Offset:%d, Partition:%d]' % (msg.offset, msg.partition))
        writer.write(msg.value)
        msg = next(consumer)
        if msg.value == b'end':
            print('!!!!! > "%s"' % msg.value.decode(), '[Offset:%d, Partition:%d]' % (msg.offset, msg.partition))

    print('consumer exiting...')
    writer.close()
"""


def producer_part(topic: str):
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    print('Producer is initiated..')

    for i in range(1000):
        print('sending:%d' % i)
        producer.send(topic, str(i).encode())
        time.sleep(2)
    producer.flush()
    return


def consumer_part(topic: str):
    consumer = KafkaConsumer(topic)
    print('Consumer is initiated..')

    for msg in consumer:
        print(' > "%s"' % msg.value.decode()[:-1], '[Offset:%d, Partition:%d]' % (msg.offset, msg.partition))
    print('consumer exiting...')


if __name__ == '__main__':
    kafka_services = KafkaServices()
    kafka_services.start_all()
    exit(22)
    create_topic(topic='foo',lh_port=9092)
    list_topics()

    KafkaProducerConsumer.start_consumer(topic='dummy3')
    Thread(target=producer_part(topic='dummy3')).start()

    # Thread(target=consumer_part(topic='Events')).start()
    # time.sleep(3)
