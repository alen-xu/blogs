import os
import sys

root = os.path.dirname(__file__)
path1 = sys.path.insert(0, os.path.join(root, '..', 'py2env/Lib/site_packages'))
print(type(path1))
print(path1)