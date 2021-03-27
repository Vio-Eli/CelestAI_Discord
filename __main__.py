""" CelestAI start """

import sys
from os import path

# Add "celestai" to python's path
sys.path.insert(0, path.dirname(path.dirname(path.abspath(__file__))))
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from celestai import brain
# import brain

brain.init()
brain.inst.run()
