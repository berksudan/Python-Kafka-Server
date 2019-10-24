import settings
import time
from bash_utils import run_bash

"""
** KAFKA BROKER SCRIPTS:
    * starter: 'bin/kafka-server-start.sh'
    * stopper: 'bin/kafka-server-stop.sh'
    * properties: 'config/server.properties'

** ZOOKEEPER SCRIPTS:
    * starter: 'bin/zookeeper-server-start.sh'
    * stopper: 'bin/zookeeper-server-stop.sh'
    * properties: 'config/zookeeper.properties'
"""

# Bash Scripts for services.
kafka_dir = settings.kafka_server_dir
start_kafka_broker = 'sh %s/bin/kafka-server-start.sh %s/config/server.properties' % (kafka_dir, kafka_dir)
stop_kafka_broker = 'sh %s/bin/kafka-server-stop.sh' % kafka_dir
start_zoo_keeper = 'sh %s/bin/zookeeper-server-start.sh %s/config/zookeeper.properties' % (kafka_dir, kafka_dir)
stop_zoo_keeper = 'sh %s/bin/zookeeper-server-stop.sh' % kafka_dir


class Service:
    def __init__(self, name: str, start_cmd: str, stop_cmd: str, process: str):
        self.name = name
        self.process = process
        self.start_cmd = start_cmd
        self.stop_cmd = stop_cmd

    def start(self, debug: bool = False):
        while not self.is_running():
            print(' > Starting....%s' % self.name)
            run_bash(shell_command=self.start_cmd, new_terminal=True, debug_msg=debug)
            time.sleep(5)  # Value of sleeping time is determined by rule of thumb, it can change.

    def stop(self, debug: bool = False):
        print(' > Stopping....%s' % self.name)
        run_bash(shell_command=self.stop_cmd, debug_msg=debug)

    def is_running(self, debug: bool = False) -> bool:
        jps_output = run_bash(shell_command='jps', return_output=True, debug_msg=debug)
        return self.process in jps_output


class KafkaServices:
    excluded_process_names = ('Jps', 'Main')

    def __init__(self):
        self.zoo_keeper = Service('ZooKeeper', start_zoo_keeper, stop_zoo_keeper, process='QuorumPeerMain')
        self.kafka_broker = Service('KafkaBroker', start_kafka_broker, stop_kafka_broker, process='Kafka')

    @property
    def running_processes(self):
        jps_output = run_bash(shell_command='jps', return_output=True)

        processes = []
        for process in jps_output.split('\n')[:-1]:
            process_id, process_name = process.split(' ')
            processes.append({'id': process_id, 'process': process_name})
        return [p for p in processes if p['process'] not in self.excluded_process_names]

    def start_all(self):
        print('Starting Apache Kafka services..')
        self.zoo_keeper.start()
        self.kafka_broker.start()
        print('------------------------------------ started all.')

    def stop_all(self):
        print('Stopping Apache Kafka services..')
        self.zoo_keeper.stop()
        self.kafka_broker.stop()
        print('------------------------------------ stopped all.')

    def restart_all(self):
        self.stop_all()
        self.kill_all()  # Make sure that all processes of all services are stopped.
        self.start_all()

    def kill_all(self):
        print('Killing Apache Kafka processes..')
        if not self.running_processes:
            return print(' > No Process!')
        for p in self.running_processes:
            run_bash(shell_command='kill -9 %s' % p['id'])
            print(' > Killed process: id=%s, process=%s' % (p['id'], p['process']))
        print('Processes after kill_all:')
        print(run_bash(shell_command='jps', return_output=True)[:-1])
        print('------------------------------------ killed all.')

    def __str__(self):
        as_str = 'Processes:\n'
        for i, p in enumerate(self.running_processes):
            as_str += ' > [%d].process: %r\n' % (i + 1, p)
        return as_str

    @staticmethod
    def unit_test():
        ks = KafkaServices()
        ks.stop_all()
        ks.restart_all()
        print(ks)


if __name__ == '__main__':
    KafkaServices.unit_test()
