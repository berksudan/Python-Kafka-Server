from os.path import isabs, dirname, realpath
from pathlib import Path

# Common configs for all modules in project, you can change this.
KAFKA_SERVER_DIR = 'kafka_lib/default-kafka'
KAFKA_BROKER_PROPERTIES = '%s/config/server.properties' % KAFKA_SERVER_DIR
ZOO_KEEPER_PROPERTIES = '%s/config/zookeeper.properties' % KAFKA_SERVER_DIR

# Derived configs, do not touch this.
if not isabs(KAFKA_SERVER_DIR):  # If KAFKA_SERVER_DIR path is not absolute, prepend the current directory's path
    KAFKA_SERVER_DIR = str(Path(dirname(realpath(__file__)), KAFKA_SERVER_DIR))
