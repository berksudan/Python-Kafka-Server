from os import devnull
from subprocess import check_output, call, CalledProcessError

BASH_ERROR = CalledProcessError  # Abstraction for error handling in modules which uses this module.


def run_bash(shell_command: str, new_terminal: bool = False, print_command: bool = True, quiet: bool = False) -> int:
    if new_terminal:  # Executes the command in new terminal, not applicable for operating systems with no GUI.
        shell_command = 'gnome-terminal -e "%s"' % shell_command
    if print_command:
        print('[INFO] Running shell command:', '<<%s>>' % shell_command)

    if quiet:
        return call(shell_command, shell=True, stdout=open(devnull, 'w'), stderr=open(devnull, 'w'))
    return call(shell_command, shell=True)  # returns status-code process, i.e., 0 if success, else fail.


def run_bash_with_output(shell_command: str, new_terminal: bool = False, print_command: bool = True) -> str:
    if new_terminal:  # Executes the command in new terminal, not applicable for operating systems with no GUI.
        shell_command = 'gnome-terminal -e "%s"' % shell_command
    if print_command:
        print('[INFO] Running shell command:', '<<%s>>' % shell_command)

    return check_output([shell_command], shell=True).decode()
