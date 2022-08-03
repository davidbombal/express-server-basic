import subprocess

# We load the newline seperated commands from the commands file.
with open("commands.txt", "r") as fh:
# We drop the empty entries using the filter() function.
    cmds = fh.readlines()
    for item in cmds:
# We run each command using the subprocess.run() function in Python.
        subprocess.run(item.split(" "))
