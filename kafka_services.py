import settings
import time
from bash_facade import run_bash

# Bash Scripts for services.
scripts = {
    'start_broker': 'sh %s/bin/kafka-server-start.sh' % settings.kafka_server_dir,  # Broker starter bash file.
    'stop_broker': 'sh %s/bin/kafka-server-stop.sh' % settings.kafka_server_dir,  # Broker stopper bash file.
    'start_zk': 'sh %s/bin/zookeeper-server-start.sh' % settings.kafka_server_dir,  # Zookeeper starter bash file.
    'stop_zk': 'sh %s/bin/zookeeper-server-stop.sh' % settings.kafka_server_dir  # Zookeeper stopper bash file.
}
# Default properties for services, you can change this in KafkaServices constructor.
default_properties = {
    'broker': '%s/config/server-tmp.properties' % settings.kafka_server_dir,
    'zookeeper': '%s/config/zookeeper.properties' % settings.kafka_server_dir
}


class Service:
    def __init__(self, name: str, process_name: str, starter: str, stopper: str, prop: str, debug_mode: bool = False):
        self.name = name
        self.process = process_name
        self.starter = starter
        self.properties = prop
        self.stop_cmd = stopper
        self.debug_mode = debug_mode

    @property
    def start_script(self):
        return self.starter + " " + self.properties

    def start(self):
        while not self.is_running():
            print(' > Starting....%s' % self.name)
            run_bash(shell_command=self.start_script, new_terminal=True, debug_msg=self.debug_mode)
            time.sleep(5)  # Value of sleeping time is determined by rule of thumb, it can change.

    def stop(self):
        print(' > Stopping....%s' % self.name)
        run_bash(shell_command=self.stop_cmd, debug_msg=self.debug_mode)

    def is_running(self) -> bool:
        jps_output = run_bash(shell_command='jps', return_output=True, debug_msg=self.debug_mode)
        return self.process in jps_output


class KafkaServices:
    excluded_java_processes = ('Jps', 'Main')

    def __init__(self, broker_prop: str = default_properties['broker'], zk_prop: str = default_properties['zookeeper']):
        self.zoo_keeper = Service('ZooKeeper', 'QuorumPeerMain', scripts['start_zk'], scripts['stop_zk'], prop=zk_prop)
        self.broker = Service('KafkaBroker', 'Kafka', scripts['start_broker'], scripts['stop_broker'], prop=broker_prop)

    @property
    def running_processes(self):
        jps_output = run_bash(shell_command='jps', return_output=True)

        processes = []
        for process in jps_output.split('\n')[:-1]:
            process_id, process_name = process.split(' ')
            processes.append({'id': process_id, 'process': process_name})
        return [p for p in processes if p['process'] not in self.excluded_java_processes]

    def start_all(self):
        print('Starting Apache Kafka services..')
        self.zoo_keeper.start()
        self.broker.start()
        print('------------------------------------ started all.')

    def stop_all(self):
        print('Stopping Apache Kafka services..')
        self.zoo_keeper.stop()
        self.broker.stop()
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
