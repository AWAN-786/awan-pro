try:
  import urllib3
except:
  import os
  os.system('pip uninstall idna urllib3 requests chardet certifi -y ;pip install urllib3 requests chardet certifi idna ')

print("[1] New Ids Menu")
print("[2] Mix Ids Menu")
if input("[?] Choose : ")=="2":
  import MIX3
else:
  import LXD

