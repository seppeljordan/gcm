""" command detection utility for gcm
"""

import subprocess


def checkCommand(command, param="-v"):
    """Check if a command is installed and in the systems path

    This command assumes that the host machine uses spaces to seperate
    commands from parameters.  It is also assumed that the command
    that you want to check returns 0 on succesful execution.  This
    procedure is not portable.

    Arguments:
    command -- the command that we want to check
    param -- a parameter that is passed to the command, defaults
             to '-v'

    Returns True when the command was found and otherwise False.

    """
    # check if the command works by checking its error code
    cmd = [command,param]
    try:
        proc = subprocess.check_call(cmd)
    except subprocess.CalledProcessError:
        return False
    except OSError:
        return False
    return True
