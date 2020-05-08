import time
from typing import List, Dict, Any

import configs
from .bash_facade import run_bash, run_bash_with_output

# Bash Scripts for services.
scripts = {
    'start_broker': 'sh %s/bin/kafka-server-start.sh' % configs.KAFKA_SERVER_DIR,  # Broker starter bash file.
    'stop_broker': 'sh %s/bin/kafka-server-stop.sh' % configs.KAFKA_SERVER_DIR,  # Broker stopper bash file.
    'start_zk': 'sh %s/bin/zookeeper-server-start.sh' % configs.KAFKA_SERVER_DIR,  # Zookeeper starter bash file.
    'stop_zk': 'sh %s/bin/zookeeper-server-stop.sh' % configs.KAFKA_SERVER_DIR  # Zookeeper stopper bash file.
}


class Service:
    def __init__(self, name: str, ps_name: str, starter: str, stopper: str, prop: str,
                 no_out: bool = True, print_commands: bool = True):
        self.name = name
        self.process = ps_name
        self.starter = starter
        self.properties = prop
        self.stop_cmd = stopper
        self.debug_mode = print_commands
        self.no_output = no_out

    @property
    def start_script(self):
        if self.no_output:
            return self.starter + " " + self.properties + " > /dev/null &"
        else:
            return self.starter + " " + self.properties + " &"

    def start(self):
        while not self.is_running():
            print('[INFO] Starting....%s' % self.name)
            run_bash(shell_command=self.start_script, new_terminal=False, print_command=self.debug_mode)
            time.sleep(5)  # Value of sleeping time is determined by rule of thumb, it can change.

    def stop(self):
        print('[INFO] Stopping....%s' % self.name)
        run_bash(shell_command=self.stop_cmd, print_command=self.debug_mode)

    def is_running(self) -> bool:
        jps_output = run_bash_with_output(shell_command='jps', print_command=self.debug_mode)
        return self.process in jps_output


class KafkaServices:
    EXCLUDED_JAVA_PROCESSES = ('Jps', 'Main')

    def __init__(self, broker_prop: str, zk_prop: str):
        self.zoo_keeper = Service('ZooKeeper', 'QuorumPeerMain', scripts['start_zk'], scripts['stop_zk'], prop=zk_prop)
        self.broker = Service('KafkaBroker', 'Kafka', scripts['start_broker'], scripts['stop_broker'], prop=broker_prop)

    @property
    def running_processes(self) -> List[Dict[str, Any]]:  # Return running processes of ZooKeeper and KafkaBroker.
        jps_output = run_bash_with_output(shell_command='jps')

        processes = []
        for process in jps_output.split('\n')[:-1]:
            process_id, process_name = process.split(' ')
            processes.append({'id': process_id, 'process': process_name})
        return [p for p in processes if p['process'] not in self.EXCLUDED_JAVA_PROCESSES]

    def start_all(self):  # Start all processes of ZooKeeper and KafkaBroker.
        print('[INFO] Starting Apache Kafka services..')
        self.zoo_keeper.start()
        self.broker.start()
        print('===================== started all.\n')

    def stop_all(self):  # Stop all processes of ZooKeeper and KafkaBroker.
        print('[INFO] Stopping Apache Kafka services..')
        self.zoo_keeper.stop()
        self.broker.stop()
        print('===================== stopped all.\n')

    def kill_all(self):  # Kill all processes of ZooKeeper and KafkaBroker.
        print('[INFO] Killing Apache Kafka processes..')
        running_processes = self.running_processes
        if not running_processes:
            return print(' > No Process!')
        for p in running_processes:
            run_bash(shell_command='kill -9 %s' % p['id'])
            print('[INFO] Killed process: id=%s, process=%s' % (p['id'], p['process']))
        print('[INFO] Processes after kill_all:', run_bash_with_output('jps', print_command=False).splitlines())
        print('===================== killed all.\n')

    def __str__(self):
        as_str = 'Processes:\n'
        for i, p in enumerate(self.running_processes):
            as_str += ' > [%d].process: %r\n' % (i + 1, p)
        return as_str

    @staticmethod
    def unit_test():
        default_props = {  # Default properties for services
            'broker': '%s/config/server.properties' % configs.KAFKA_SERVER_DIR,
            'zookeeper': '%s/config/zookeeper.properties' % configs.KAFKA_SERVER_DIR
        }
        ks = KafkaServices(broker_prop=default_props['broker'], zk_prop=default_props['zookeeper'])
        ks.stop_all()
        ks.kill_all()
        ks.start_all()
        print(ks)


if __name__ == '__main__':
    KafkaServices.unit_test()
