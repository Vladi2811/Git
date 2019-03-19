import numpy as np 
import sys
sys.path.append('D:\Programacion\git\LiveMerge\src')
from merge import merge

import time
tiempo = time.time()
merge.mergeImages("InFiles/logo.png", "img1.jpg", "right-top")
print(time.time()-tiempo)
