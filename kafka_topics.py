import settings
import time
from bash_utils import run_bash

# Bash Script prefixes for topics.
create_topic_prefix = 'sh %s/bin/kafka-topics.sh --create ' % settings.kafka_server_dir
delete_topic_prefix = 'sh %s/bin/kafka-topics.sh --delete ' % settings.kafka_server_dir
list_topics_prefix = 'sh %s/bin/kafka-topics.sh --list ' % settings.kafka_server_dir


def create_topic(topic: str, lh_port: int, rep_factor: int = 1, partitions: int = 1):
    run_bash(
        create_topic_prefix + '--bootstrap-server localhost:%d --replication-factor %d --partitions %d --topic %s' % (
            lh_port, rep_factor, partitions, topic))


def delete_topic(topic: str, lh_port: int):  # delete.topic.enable must be true to delete.
    run_bash(delete_topic_prefix + '--bootstrap-server localhost:%d  --topic %s' % (lh_port, topic))


def list_topics(lh_port: int, sleep_secs_before: float = 3):
    time.sleep(sleep_secs_before)  # Wait for a while to ensure that topic creation (if there is any) is ended.
    listed_topics_str = run_bash(list_topics_prefix + '--bootstrap-server localhost:%d' % lh_port, return_output=True)
    print('EXISTING TOPICS:')
    if not listed_topics_str:
        return print(' No topics!')
    listed_topics = listed_topics_str[:-1].split('\n')
    for cnt, topic in enumerate(listed_topics):
        print(' [%d] <<%s>>' % (cnt + 1, topic))


def unit_test(topic: str, localhost_port: int):
    list_topics(lh_port=localhost_port)
    create_topic(topic=topic, lh_port=localhost_port)
    list_topics(lh_port=localhost_port)


if __name__ == '__main__':
    unit_test(topic='dummy_topic_1234', localhost_port=9092)
