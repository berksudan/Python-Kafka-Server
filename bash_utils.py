from subprocess import check_output, call


def run_bash(shell_command: str, new_terminal: bool = False, return_output: bool = False, debug_msg=False):
    if new_terminal:
        shell_command = 'gnome-terminal -e "%s"' % shell_command

    if debug_msg:
        print('Running shell command:', '<<%s>>' % shell_command)

    if return_output:
        return check_output([shell_command], shell=True).decode()
    else:
        return call(shell_command, shell=True)
