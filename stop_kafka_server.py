from sys import argv

from configs import ZOO_KEEPER_PROPERTIES, KAFKA_BROKER_PROPERTIES
from src.kafka_services import KafkaServices


def stop_kafka_services(broker_prop: str = KAFKA_BROKER_PROPERTIES, zk_prop: str = ZOO_KEEPER_PROPERTIES):
    kafka_services = KafkaServices(broker_prop=broker_prop, zk_prop=zk_prop)
    kafka_services.stop_all()  # Try to stop all processes of all services are killed.
    kafka_services.kill_all()  # Make sure that all processes of all services are killed.


if __name__ == '__main__':
    if len(argv) > 1:  # If first argument passed, use it as kafka-broker properties file.
        kafka_broker_properties = argv[1]
        stop_kafka_services(broker_prop=kafka_broker_properties)
    elif len(argv) > 2:  # If second argument passed, use it as zookeeper properties file.
        kafka_broker_properties = argv[1]
        zoo_keeper_properties = argv[2]
        stop_kafka_services(broker_prop=kafka_broker_properties, zk_prop=zoo_keeper_properties)
    else:  # Otherwise, use Default Kafka Properties file.
        stop_kafka_services()
