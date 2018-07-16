import requests
import sys

print("Welcome to QuickShare Python")
print("Checking connectivity to QuickShare...")
try:
  lic = requests.get("https://qshare.ga/f/_LICENSE")
except:
  print("Connection error.")
  sys.exit()
print("Connection OK. Read license?")
if input("y/n: ") == "y":
  print(lic.text)
print("Enter 'exit' in message ID to quit")
def ask():
  id = input("Enter message ID: ")
  if id == "exit":
    print("Closing!")
    sys.exit()
  msg = requests.get('https://qshare.ga/f/' + id)
  if msg.status_code != 200:
    print("Error!")
  else:
    print(msg.text)
while True:
  ask()