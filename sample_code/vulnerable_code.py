import pickle
import subprocess

def insecure_deserialization(data):
    return pickle.loads(data)

def command_injection(user_input):
    subprocess.call("echo " + user_input, shell=True)

password = "hardcoded_password"