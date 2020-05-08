# Apache-Kafka-Server

## Abstract
Handy tool to manage Apache Kafka scripts. You can start Apache-Kafka services, create topics, list topics, create producers and consumers easily. It basically automates shell scripts with the power of simplicity and great scalability of Python 3. 

## Build
Since there is no dependencies, you don't need to build or install any package.

## Run
### Start Kafka Server
If you want to start Kafka services (ZooKeeper and Broker), run:
```bash
$ python3 start_kafka_server.py <KAFKA_BROKER_PROP_FILE> <ZOOKEEPER_PROP_FILE>
# Example #1: $ python3 start_kafka_server.py 
# Example #2: $ python3 start_kafka_server.py /path/to/kafka/config/server.properties /path/to/kafka/config/zookeeper.properties
```
### Create Topics
If you want to create topics, run:
```bash
$ python3 create_topics.py <HOST_IP> <PORT> <TOPIC> [<TOPIC>]
# Example: $ python3 create_topics.py localhost 9092 topic1 topic2 topic3
```

### Create Topics
If you want to delete topics, run:
```bash
$ python3 delete_topics.py <HOST_IP> <PORT> <TOPIC> [<TOPIC>]
# Example: $ python3 delete_topics.py localhost 9092 topic1 topic2 topic3
```

### Stop Kafka Server
If you want to stop Kafka services (ZooKeeper and Broker), run:
```bash
$ python3 stop_kafka_server.py <KAFKA_BROKER_PROP_FILE> <ZOOKEEPER_PROP_FILE>
# Example #1: $ python3 stop_kafka_server.py 
# Example #2: $ python3 stop_kafka_server.py /path/to/kafka/config/server.properties /path/to/kafka/config/zookeeper.properties
```

### Other options
In addition to scripts, you can do the following:
- List Active Topics
- Create Producer (opens in a new Terminal)
- Create Consumer (opens in a new Terminal)

For these functionalities, you need to import the python modules in ```src/``` folder, and then execute the functions within these modules.

## Test
If you want to test all functionalities altogether with default parameters, run:
```bash
$ python3 test_all.py
```

**Sample Output:**
```bash
[INFO] Stopping Apache Kafka services..
[INFO] Stopping....ZooKeeper
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/zookeeper-server-stop.sh>>
No zookeeper server to stop
[INFO] Stopping....KafkaBroker
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/kafka-server-stop.sh>>
No kafka server to stop
===================== stopped all.

[INFO] Killing Apache Kafka processes..
[INFO] Running shell command: <<jps>>
 > No Process!
[INFO] Stopping Apache Kafka services..
[INFO] Stopping....ZooKeeper
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/zookeeper-server-stop.sh>>
No zookeeper server to stop
[INFO] Stopping....KafkaBroker
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/kafka-server-stop.sh>>
No kafka server to stop
===================== stopped all.

[INFO] Killing Apache Kafka processes..
[INFO] Running shell command: <<jps>>
 > No Process!
[INFO] Starting Apache Kafka services..
[INFO] Running shell command: <<jps>>
[INFO] Starting....ZooKeeper
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/zookeeper-server-start.sh kafka_lib/default-kafka/config/zookeeper.properties > /dev/null &>>
[INFO] Running shell command: <<jps>>
[INFO] Running shell command: <<jps>>
[INFO] Starting....KafkaBroker
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/kafka-server-start.sh kafka_lib/default-kafka/config/server.properties > /dev/null &>>
[INFO] Running shell command: <<jps>>
===================== started all.

[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/kafka-topics.sh --list  --bootstrap-server localhost:9092>>
[INFO] EXISTING TOPICS:
 [1] <<>>
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic Events>>
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic Actions>>
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic MaterialEvents>>
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic PredictionResults>>
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic AssociationRulesRawEvents>>
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic GetRequestResults>>
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic Rules>>
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/kafka-topics.sh --list  --bootstrap-server localhost:9092>>
[INFO] EXISTING TOPICS:
 [1] <<Actions>>
 [2] <<AssociationRulesRawEvents>>
 [3] <<Events>>
 [4] <<GetRequestResults>>
 [5] <<MaterialEvents>>
 [6] <<PredictionResults>>
 [7] <<Rules>>
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/kafka-topics.sh --delete --bootstrap-server localhost:9092  --topic Events>>
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/kafka-topics.sh --delete --bootstrap-server localhost:9092  --topic Actions>>
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/kafka-topics.sh --delete --bootstrap-server localhost:9092  --topic MaterialEvents>>
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/kafka-topics.sh --delete --bootstrap-server localhost:9092  --topic PredictionResults>>
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/kafka-topics.sh --delete --bootstrap-server localhost:9092  --topic AssociationRulesRawEvents>>
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/kafka-topics.sh --delete --bootstrap-server localhost:9092  --topic GetRequestResults>>
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/kafka-topics.sh --delete --bootstrap-server localhost:9092  --topic Rules>>
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/kafka-topics.sh --list  --bootstrap-server localhost:9092>>
[INFO] EXISTING TOPICS:
 [1] <<>>
[INFO] Stopping Apache Kafka services..
[INFO] Stopping....ZooKeeper
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/zookeeper-server-stop.sh>>
[INFO] Stopping....KafkaBroker
[INFO] Running shell command: <<sh /[KAFKA_SERVER_PATH]/kafka_lib/default-kafka/bin/kafka-server-stop.sh>>
===================== stopped all.

[INFO] Killing Apache Kafka processes..
[INFO] Running shell command: <<jps>>
[INFO] Running shell command: <<kill -9 25176>>
[INFO] Killed process: id=25176, process=QuorumPeerMain
[INFO] Running shell command: <<kill -9 25530>>
[INFO] Killed process: id=25530, process=Kafka
[INFO] Processes after kill_all: ['31430 Jps', '7309 Main']
===================== killed all.

Successfully terminated.
```

## Contributor
- *Berk Sudan*, [GitHub](https://github.com/berksudan), [LinkedIn](https://linkedin.com/in/berksudan/)