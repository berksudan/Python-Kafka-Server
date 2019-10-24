import settings
from bash_utils import run_bash

"""
*******[CRUCIAL WARNING] *******
* This is MANUAL version of creating producer and consumer.
* Do NOT use this, unless you debug topic or your program.
"""

start_produce_prefix = 'sh %s/bin/kafka-console-producer.sh ' % settings.kafka_server_dir
start_consumer_prefix = 'sh %s/bin/kafka-console-consumer.sh --from-beginning ' % settings.kafka_server_dir


def start_consumer(topic: str, lh_port: int):
    run_bash('' + start_consumer_prefix + '--bootstrap-server localhost:%d --topic %s' % (lh_port, topic),
             new_terminal=True, debug_msg=True)


def start_producer(topic_name: str, lh_port: int):
    run_bash(start_produce_prefix + '--broker-list localhost:%d --topic %s' % (lh_port, topic_name), new_terminal=True,
             debug_msg=True)


def unit_test():
    start_consumer('Events', lh_port=9092)
    #start_producer('hello-kafka', lh_port=9092)


if __name__ == '__main__':
    unit_test()
