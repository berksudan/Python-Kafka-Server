import settings
import time
from bash_facade import run_bash

# Bash Script prefixes for topics.
create_topic_prefix = 'sh %s/bin/kafka-topics.sh --create ' % settings.kafka_server_dir
delete_topic_prefix = 'sh %s/bin/kafka-topics.sh --delete ' % settings.kafka_server_dir
list_topics_prefix = 'sh %s/bin/kafka-topics.sh --list ' % settings.kafka_server_dir


def create_topic(topic: str, host_ip: str, port: int, rep_factor: int = 1, partitions: int = 1):
    run_bash(create_topic_prefix + '--bootstrap-server %s:%d --replication-factor %d --partitions %d --topic %s' % (
            host_ip, port, rep_factor, partitions, topic))


def delete_topic(topic: str, host_ip: str, port: int):  # delete.topic.enable must be true to delete.
    run_bash(delete_topic_prefix + '--bootstrap-server %s:%d  --topic %s' % (host_ip, port, topic))


def list_topics(host_ip: str, port: int, sleep_secs_before: float = 3):
    time.sleep(sleep_secs_before)  # Wait for a while to ensure that topic creation (if there is any) is ended.
    listed_topics_str = run_bash(list_topics_prefix + '--bootstrap-server %s:%d' % (host_ip, port), return_output=True)
    print('EXISTING TOPICS:')
    if not listed_topics_str:
        return print(' No topics!')
    listed_topics = listed_topics_str[:-1].split('\n')
    for cnt, topic in enumerate(listed_topics):
        print(' [%d] <<%s>>' % (cnt + 1, topic))


def unit_test(topic: str, host_ip: str, port: int):
    list_topics(host_ip, port)
    create_topic(topic, host_ip, port)
    list_topics(host_ip, port)


if __name__ == '__main__':
    unit_test(topic='dummy_topic_1234', host_ip="localhost", port=9092)
