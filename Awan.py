try:
  import idna
except:
  import os
  os.system('pip uninstall idna urllib3 requests chardet certifi -y ;pip install urllib3 requests chardet certifi idna ')
import LXD

