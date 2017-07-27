"""
A simple LabPal setup using Jython
"""
import sys
sys.path.append('labpal.jar')
from ca.uqac.lif.labpal import Laboratory, Experiment

"""
A experiment written in Python
"""
class MyExperiment(Experiment):
	def __init__(self, a):
		self.setDescription('An experiment that multiplies a number by 2')
		self.setInput('a', a)
		self.describe('a', 'An arbitrary integer number')
		self.describe('b', 'The double of that integer')
	def execute(self):
		a = self.readInt('a')
		self.write('b', 2 * a)

"""
A simple lab written in Python
"""
from ca.uqac.lif.labpal import Laboratory
class MyLab(Laboratory):
	def setup(self):
		self.setTitle('A simply LabPal setup using Jython')
		self.add(MyExperiment(0))
		self.add(MyExperiment(1))

# -------------------------------
# Start the lab
# -------------------------------
lab = MyLab()
lab.initialize(sys.argv, lab.getClass())