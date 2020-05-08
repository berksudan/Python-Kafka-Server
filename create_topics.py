from sys import argv
from typing import List

from src.kafka_topics import create_topic, list_topics

DEFAULT_HOST_IP = 'localhost'
DEFAULT_PORT = 9092


def create_topics(topic_list: List[str], host_ip: str = DEFAULT_HOST_IP, port: int = DEFAULT_PORT):
    list_topics(host_ip=host_ip, port=port)  # Before topic creation.
    for topic in topic_list:
        create_topic(topic, host_ip=host_ip, port=port, rep_factor=1, partitions=1)
    list_topics(host_ip=host_ip, port=port)  # After topic creation.


if __name__ == '__main__':
    host_ip_param = argv[1]
    port_param = int(argv[2])
    topic_list_param = argv[3:]
    if not topic_list_param:
        raise Exception("Topics must be entered as arguments.")
    create_topics(topic_list=topic_list_param, host_ip=host_ip_param, port=port_param)
