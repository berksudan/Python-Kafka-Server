from os.path import isabs, dirname, realpath
from pathlib import Path

# Common configs for all modules in project, you can change this.
KAFKA_SERVER_DIR = 'kafka_lib/default-kafka'
KAFKA_BROKER_PROPERTIES = '{path_to_kafka_dir}/config/server.properties'
ZOO_KEEPER_PROPERTIES = '{path_to_kafka_dir}/config/zookeeper.properties'

# Derived configs, do not touch this.
if not isabs(KAFKA_SERVER_DIR):  # If KAFKA_SERVER_DIR path is not absolute, prepend the current directory's path
    KAFKA_SERVER_DIR = str(Path(dirname(realpath(__file__)), KAFKA_SERVER_DIR))
    
KAFKA_BROKER_PROPERTIES = KAFKA_BROKER_PROPERTIES.format(path_to_kafka_dir=KAFKA_SERVER_DIR)
ZOO_KEEPER_PROPERTIES = ZOO_KEEPER_PROPERTIES.format(path_to_kafka_dir=KAFKA_SERVER_DIR)
