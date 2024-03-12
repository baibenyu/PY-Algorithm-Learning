In [14]: s = 'abd#@%32309ABCpasswordXYZjk69EDFpasswwwordOPQ3-63'

In [15]: s
Out[15]: 'abd#@%32309ABCpasswordXYZjk69EDFpasswwwordOPQ3-63'

In [16]: import re

In [17]: re.findall(r'[A-Z]{3}([a-z]+)[A-Z]{3}', s)
Out[17]: ['password', 'passwwword']
