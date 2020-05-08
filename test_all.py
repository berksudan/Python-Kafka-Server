from configs import ZOO_KEEPER_PROPERTIES, KAFKA_BROKER_PROPERTIES
from create_topics import create_topics, DEFAULT_HOST_IP, DEFAULT_PORT
from delete_topics import delete_topics
from src import kafka_producer_consumer
from start_kafka_server import start_kafka_services
from stop_kafka_server import stop_kafka_services

TEST_TOPICS = ['Events', 'Actions', 'MaterialEvents', 'PredictionResults', 'AssociationRulesRawEvents',
               'GetRequestResults', 'Rules']


def test(create_producer_consumers: bool = False):
    stop_kafka_services(broker_prop=KAFKA_BROKER_PROPERTIES, zk_prop=ZOO_KEEPER_PROPERTIES)
    start_kafka_services(broker_prop=KAFKA_BROKER_PROPERTIES, zk_prop=ZOO_KEEPER_PROPERTIES)
    create_topics(topic_list=TEST_TOPICS, host_ip=DEFAULT_HOST_IP, port=DEFAULT_PORT)

    if create_producer_consumers:
        for topic in TEST_TOPICS[0]:  # Create producers and consumers for first topic only
            kafka_producer_consumer.start_producer(topic=topic, host_ip=DEFAULT_HOST_IP, port=DEFAULT_PORT)
            kafka_producer_consumer.start_consumer(topic=topic, host_ip=DEFAULT_HOST_IP, port=DEFAULT_PORT)

    delete_topics(topic_list=TEST_TOPICS, host_ip=DEFAULT_HOST_IP, port=DEFAULT_PORT)
    stop_kafka_services(broker_prop=KAFKA_BROKER_PROPERTIES, zk_prop=ZOO_KEEPER_PROPERTIES)

    print("Successfully terminated.")


if __name__ == '__main__':
    test(create_producer_consumers=False)

    # If program is working on server-side, don't activate it, due to lack of GUI.
    # test(create_producer_consumers = True)
