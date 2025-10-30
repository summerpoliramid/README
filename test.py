import os
import sys
import json
import subprocess
from subprocess import Popen

COMMAND_NAME = "terminal"
def execute(args=None):
    if isinstance(args, str):
        try:
            args = json.loads(args)
        except json.JSONDecodeError as e:
            return f"Error: Failed to parse args as JSON: {str(e)} {args}"
    if isinstance(args, dict) and "action" in args:
        action = args["action"]
        if action == "execute":
            flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
            p = Popen(args.get("command"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=flags)
            stdout, stderr = p.communicate()

            encoding = "cp866" if os.name == "nt" else locale.getpreferredencoding(False)

            try:
                return (stdout + stderr).decode(encoding, errors="replace")
            except:
                return (stdout + stderr).decode("utf-8", errors="replace")
    return "Invalid or no arguments"
