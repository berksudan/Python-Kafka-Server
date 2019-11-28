import settings
from bash_facade import run_bash

"""
*******[CRUCIAL WARNING] *******
* This is MANUAL version of creating producer and consumer.
* Do NOT use this, unless you debug topic or your program.
"""

start_produce_prefix = 'sh %s/bin/kafka-console-producer.sh ' % settings.kafka_server_dir
start_consumer_prefix = 'sh %s/bin/kafka-console-consumer.sh --from-beginning ' % settings.kafka_server_dir


def start_consumer(topic: str, host_ip: str, port: int):
    run_bash(start_consumer_prefix + '--bootstrap-server %s:%d --topic %s' % (host_ip, port, topic), new_terminal=True)


def start_producer(topic_name: str, host_ip: str, port: int):
    run_bash(start_produce_prefix + '--broker-list %s:%d --topic %s' % (host_ip, port, topic_name), new_terminal=True)


def unit_test():
    start_consumer('dummy_topic', port=9092)
    start_producer('dummy_topic', port=9092)


if __name__ == '__main__':
    unit_test()
