"""
Autograding code for BIOF 309 Homework 2: Number Guessing Game
Run this code from the command line: python biof309_test_hw2.py your_file.py

You can run this program on the provided byte-compiled solution to see that it works.
"""
import unittest
import importlib

class TestHW2( unittest.TestCase ):
	"""All these test have to pass to get an A"""

	def test_SolicitInteger( self ):

		list_of_responses_and_expected_outcomes = [\
				(1, 1), (2, 2), (10,10), (5.0, 5), ('10',10), (-10, ValueError), ]

		# Capture too low or too high

		# enter trash and see if it's dealt with
		# Check to see that 0 is a valid lower and upper bound
		biof309_hw2.SolicitIntegeer()
		if not hasattr(sys.stdout, "getvalue"):
		self.fail("need to run in buffered mode")
		output = sys.stdout.getvalue().strip() # because stdout is an StringIO instance
		self.assertEquals(output,'hello world!')

	def test_RunTurn( self ):
		self.assertTrue( True )
		# enter trash and see if it's dealt with
		# Check to see that 0 is a valid lower and upper bound
		# check that the number chosen by the computer is really random by running RunTurn 5 times
		RunTurn(-1000,1000)

if __name__ == '__main__':
	import sys
	modulename = sys.argv[1]
	importlib.import_module( modulename )

	#http://docs.python.org/2/library/unittest.html#unittest.TestResult.buffer
	assert not hasattr(sys.stdout, "getvalue")
	unittest.main(module=__name__, buffer=True, exit=False)	
