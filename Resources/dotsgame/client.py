import subprocess
import json

# https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output
     
result = subprocess.run(['python3', 'app-client.py','127.0.0.1','5555','search','ring'], stdout=subprocess.PIPE)
r = json.loads(result.stdout)

#r = str(r, encoding='ascii')

print(r)