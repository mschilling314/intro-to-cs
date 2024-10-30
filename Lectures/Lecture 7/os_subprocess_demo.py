import os
import subprocess

print("Using OS module's environment variable retrieval:")
print(os.environ["api_key"])

print("\nUsing Subprocess to execute an equivalent shell command")
cmd = "echo ${api_key}"
subprocess.run(cmd, shell=True)