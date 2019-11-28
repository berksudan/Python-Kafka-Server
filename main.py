from kafka_topics import list_topics, create_topic
from kafka_services import KafkaServices
import kafka_producer_consumer
import settings

if __name__ == '__main__':
    kafkaServices = KafkaServices(broker_prop='%s/config/server-tmp.properties' % settings.kafka_server_dir)
    kafkaServices.restart_all()

    create_topic(topic='Events', host_ip='192.168.10.46', port=9092)
    create_topic(topic='Actions', host_ip='192.168.10.46', port=9092)

    list_topics(host_ip='192.168.10.46', port=9092)

    kafka_producer_consumer.start_consumer(topic='Actions', host_ip="192.168.10.46", port=9092)
    kafka_producer_consumer.start_consumer(topic='Events', host_ip="192.168.10.46", port=9092)
