import sys
import os
import subprocess
import argparse

#Launcher for Meowthv2

def parse_cli_args():
    parser = argparse.ArgumentParser(description="Meowth Launcher - Pokemon Go Bot for Discord")
    parser.add_argument("--start","-s",help="Starts Meowth",action="store_true")
    parser.add_argument("--announce","-a",help="Announces Update/Reboot Message to all server owners.",action="store_true")
    parser.add_argument("--auto-restart","-r",help="Auto-Restarts Meowth in case of a crash.",action="store_true")
    return parser.parse_args()

def run_meowth(autorestart):
    interpreter = sys.executable
    if interpreter is None:
        raise RuntimeError("Python could not be found")

    if args.announce:
        cmd = (interpreter, "meowth.py", "reboot", "launcher")
    else:
        cmd = (interpreter, "meowth.py", "launcher")

    while True:
        try:
            code = subprocess.call(cmd)
        except KeyboardInterrupt:
            code = 0
            break
        else:
            if code == 0:
                break
            elif code == 26:
                #standard restart
                print("")
                print("Restarting Meowth")
                print("")
                cmd = (interpreter, "meowth.py", "launcher")
                continue
            elif code == 27:
                #announce on restart
                print("")
                print("Restarting Meowth")
                print("")
                cmd = (interpreter, "meowth.py", "reboot", "launcher")
                continue
            else:
                if not autorestart:
                    break
                print("")
                print("Restarting Meowth from crash")
                print("")
                cmd = (interpreter, "meowth.py", "launcher")

    print("Meowth has closed. Exit code: {exit_code}".format(exit_code=code))

args = parse_cli_args()

if __name__ == '__main__':
    abspath = os.path.abspath(__file__)
    dirname = os.path.dirname(abspath)
    os.chdir(dirname)

    if args.start:
        print("Launching Meowth...")
        run_meowth(autorestart=args.auto_restart)
