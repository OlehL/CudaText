import os;      os.putenv("PYTHONIOENCODING",'utf-8')
import sys;     sys.getfilesystemencoding = lambda: 'utf-8'
import locale;  locale.getpreferredencoding = lambda: 'utf-8'

# this is context of app, "sys" already imported
_v = sys.version_info
print("Python %d.%d.%d" % (_v[0], _v[1], _v[2]) )

# can comment this line to speedup, it's to test API in console
from cudatext import *
