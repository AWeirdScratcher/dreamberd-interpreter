import os

cmd = input("What's your command for pip? (e.g., pip)\n>> ")
print("... installing DreamBerd for Python")
os.system(cmd + " install rich rure termcolor --quiet")
print("Installation completed!")
