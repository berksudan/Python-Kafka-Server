import time

import configs
from .bash_facade import run_bash, run_bash_with_output

# Bash Script prefixes for topic_list.
CREATE_TOPIC_PREFIX = 'sh %s/bin/kafka-topics.sh --create ' % configs.KAFKA_SERVER_DIR
DELETE_TOPIC_PREFIX = 'sh %s/bin/kafka-topics.sh --delete ' % configs.KAFKA_SERVER_DIR
LIST_TOPICS_PREFIX = 'sh %s/bin/kafka-topics.sh --list ' % configs.KAFKA_SERVER_DIR

# Boolean flag to control if topic creation will contain STDOUT and STDERR I/O or not.
QUIET_WHILE_CREATING_TOPICS = True


def create_topic(topic: str, host_ip: str, port: int, rep_factor: int = 1, partitions: int = 1, created_before_ok=True):
    res = run_bash(CREATE_TOPIC_PREFIX + '--bootstrap-server %s:%d --replication-factor %d --partitions %d --topic %s'
                   % (host_ip, port, rep_factor, partitions, topic), quiet=QUIET_WHILE_CREATING_TOPICS)
    if res != 0:
        if not created_before_ok:  # If result is fail and not OK to situation that the topic was created before.
            raise Exception('[ERROR] Topic: "{topic_name}" was created before, exiting..'.format(topic_name=topic))
        print('[WARN] Topic: "{topic_name}" was created before.'.format(topic_name=topic))


def delete_topic(topic: str, host_ip: str, port: int):  # In Kafka Library, "delete.topic.enable" must be true.
    run_bash(DELETE_TOPIC_PREFIX + '--bootstrap-server %s:%d  --topic %s' % (host_ip, port, topic))


def list_topics(host_ip: str, port: int, sleep_secs_before: float = 3.0):
    time.sleep(sleep_secs_before)  # Wait for a while to ensure that topic creation (if there is any) is ended.
    listed_topics_str = run_bash_with_output(LIST_TOPICS_PREFIX + ' --bootstrap-server %s:%d' % (host_ip, port))
    print('[INFO] EXISTING TOPICS:')
    if not listed_topics_str:
        return print(' No topic_list!')
    listed_topics = listed_topics_str[:-1].split('\n')
    for cnt, topic in enumerate(listed_topics):
        print(' [%d] <<%s>>' % (cnt + 1, topic))


def unit_test(topic: str, host_ip: str, port: int):
    list_topics(host_ip, port)

    create_topic(topic, host_ip, port)
    list_topics(host_ip, port)

    delete_topic(topic, host_ip, port)
    list_topics(host_ip, port)


if __name__ == '__main__':
    unit_test(topic='dummy_topic_1234', host_ip="localhost", port=9092)
