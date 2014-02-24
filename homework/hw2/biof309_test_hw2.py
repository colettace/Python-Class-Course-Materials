"""
Autograding code for BIOF 309 Homework 2: Number Guessing Game
Run this code from the command line: python biof309_test_hw2.py your_file.py

You can run this program on the provided byte-compiled solution to see that it works.
"""
import unittest
import importlib



class TestHW2( unittest.TestCase ):
	"""All these test have to pass to get an A"""

	def setUp( self ):
		import sys
		modulename = sys.argv[1]
		# FIXME: strip .py out basename
		self.student_module = importlib.import_module( modulename )

	def test_SolicitInteger( self ):
		"""signature: SolicitInteger(lobound=None, hibound=None, default_return=None)"""

		assert( hasattr(sys.stdout, "getvalue") , "need to run in buffered mode" )


		invalid_garbage = (
				( ( None, None, None ), "l jdf", None ),
				( ( None, None, None ), "",      None ),
				( ( None, None, None ), "19fgd", None ))

		invalid_toolow = (
				( ( -10, None, None ), "-11",    None ), # standard case
				( (   0, None, None ), "-1",     None ), # zero lbound case
				( ( -10, None, None ), "0",      None ), # zero input case
				( ( -10, None,  -11 ), "",       None )) # default less than lbound case

		invalid_toohigh = (
				( ( None,  10, None ), "11",     None ), # standard case
				( ( None,   0, None ), "1",      None ), # zero ubound case
				( ( None, -10, None ), "0",      None ), # zero input case
				( ( None,  10,   11 ), "",       None )) # default greater than ubound case

		valid_default = (
				( ( None, None, -10 ), "",      -10   ), # standard negative case
				( ( None, None,  10 ), "",       10   ), # standard positive case
				( ( None, None,   0 ), "",        0   ), # zero case
				( ( -10, None,  -10 ), "",      -10   ), # default same as lbound case
				( ( None, 10,    10 ), "",       10   )) # default same as ubound case

		valid = (
				( ( None, None, None ), "-10",   -10  ),  # standard negative case
				( ( None, None, None ), "10",     10  ),  # standard positive case
				( ( None, None, None ), "0",       0  ),  # standard zero case
				( (  -11, None, None ), "-10",   -10  ),  # input greater than lbound
				( ( None,   11, None ), "10",     10  ),  # input less than ubound
				( (  -11, None, None ), "0",       0  ),  # zero input greater than lbound
				( ( None,   11, None ), "0",       0  ),  # zero input less than ubound
				( (  -11,   10, None ), "-10",   -10  ),  # input greater than lbound & less than ubound
				( (  -11,   10, None ), "0",       0  ))  # zero input greater than lbound & less than ubound


		use_cases = (
				( invalid_garbage, None ),
				( invalid_toolow,  "too hi" ),
				( invalid_toohigh, "too lo" ),
				( valid_default, None ),
				( valid, None ))

		for inputs, expected_message in use_cases:
			for _args, _input, _output in inputs:
				self.student_module.raw_input = lambda _: _input
				retval = None
				try:
					retval = self.student_module.SolicitInteger( *args )
					self.assertEqual( retval, _output )
					output = sys.stdout.getvalue().strip()
					if expected_message:
						self.assertIn( output.lower(), expected_message )

				except Exception as e:
					self.testFail( "Uncaught exception in SolicitInteger when calling with " + \
							"lbound={}, hibound={}, default_return={}, input={}".format( *_args, _input ))

		self.student_module.raw_input = raw_input


	def test_RunTurn( self ):
		self.assertTrue( True )
		# enter trash and see if it's dealt with
		# Check to see that 0 is a valid lower and upper bound
		# check that the number chosen by the computer is really random by running RunTurn 5 times
		RunTurn(-1000,1000)

if __name__ == '__main__':

	#http://docs.python.org/2/library/unittest.html#unittest.TestResult.buffer

	assert not hasattr(sys.stdout, "getvalue")

	unittest.main(module=__name__, buffer=True)
