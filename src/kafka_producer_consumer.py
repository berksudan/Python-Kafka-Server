import configs
from .bash_facade import run_bash

"""
* This is MANUAL version of creating producer and consumer.
* You can test your topic by sending data with producer and reading it with consumer.
* It runs on Linux Terminal.
"""

start_produce_prefix = 'sh %s/bin/kafka-console-producer.sh ' % configs.KAFKA_SERVER_DIR
start_consumer_prefix = 'sh %s/bin/kafka-console-consumer.sh' % configs.KAFKA_SERVER_DIR


def start_consumer(topic: str, host_ip: str, port: int):
    run_bash(start_consumer_prefix + ' --bootstrap-server %s:%d --topic %s --from-beginning' % (host_ip, port, topic))


def start_producer(topic: str, host_ip: str, port: int):
    run_bash(start_produce_prefix + ' --broker-list %s:%d --topic %s' % (host_ip, port, topic))


def unit_test():
    start_consumer('dummy_topic', host_ip='localhost', port=9092)
    start_producer('dummy_topic', host_ip='localhost', port=9092)


if __name__ == '__main__':
    unit_test()
