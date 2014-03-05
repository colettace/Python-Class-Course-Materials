"""
Autograding code for BIOF 309 Homework 2: Number Guessing Game
Run this code from the command line: python biof309_test_hw2.py your_file.py

You can run this program on the provided byte-compiled solution to see that it works.
"""
import unittest
import importlib
import sys

#=========================================================================
class TestModule( object ):
	student_module = None

	def __init__( self ):
		import os.path
		modulename, _ = os.path.splitext( sys.argv[1] )
		TestModule.student_module = importlib.import_module( modulename )

	@staticmethod
	def getMod():
		return TestModule.student_module

#=========================================================================
class TestHW2( unittest.TestCase ):
	"""All these test have to pass to get an A"""

	#============================================
	def callSolicitInteger( self, inputs, expected_message ):
		"""helper function"""
		stu_mod = TestModule.getMod()

		for (lobound, hibound, default), _input, _output in inputs:
			stu_mod.raw_input = lambda: _input
			retval = None
			retval = stu_mod.SolicitInteger( lobound, hibound, default )
			try:
				self.assertEqual( retval, _output )
			except AssertionError:
				errmsg = 'Your SolicitInteger returned a "{}" instead of a "{}" '.format(
						retval, _output)
				errmsg += "when calling with lobound={}, hibound={}, default_return={} ".format(
						lobound, hibound, default )
				errmsg += "and user input={}".format( _input )
				self.fail( errmsg )
			if expected_message:
				try:
					output = sys.stdout.getvalue().splitlines()[-1]
					self.assertIn( expected_message, output.lower() )
				except AssertionError:
					errmsg = 'Your SolicitInteger should have printed something along the lines of ' +\
							'"{}" instead of a "{}" '.format( expected_message, output)
					errmsg += "when calling with lobound={}, hibound={}, default_return={} ".format(
							lobound, hibound, default )
					errmsg += "and user input={}".format( _input )
					self.fail( errmsg )
				except IndexError:
					errmsg = 'Your SolicitInteger should have printed something along the lines of ' +\
							'"{}" instead printed nothing '.format( expected_message )
					errmsg += "when calling with lobound={}, hibound={}, default_return={} ".format(
							lobound, hibound, default )
					errmsg += "and user input={}".format( _input )
					self.fail( errmsg )

		stu_mod.raw_input = raw_input



	#============================================
	def test_SolicitInteger_TooLow( self ):
		"""Does your SolicitInteger function correctly handle user input that's too low?"""

		invalid_toolow = (
				( ( -10, None, None ), "-11",    None ), # standard case
				( (   0, None, None ), "-1",     None ), # zero lbound case
				( (  10, None, None ), "0",      None ), # zero input case
				( ( -10, None,  -11 ), "",       None )) # default less than lbound case

		self.callSolicitInteger( invalid_toolow, 'too lo' )

	#============================================
	def test_SolicitInteger_TooHi( self ):
		"""Does your SolicitInteger function correctly handle user input that's too high?"""

		invalid_toohigh = (
				( ( None,  10, None ), "11",     None ), # standard case
				( ( None,   0, None ), "1",      None ), # zero ubound case
				( ( None, -10, None ), "0",      None ), # zero input case
				( ( None,  10,   11 ), "",       None )) # default greater than ubound case

		self.callSolicitInteger( invalid_toohigh, 'too hi' )

	#============================================
	def test_SolicitInteger_Default( self ):
		"""Does your SolicitInteger function correctly handle defaults?"""

		valid_default = (
				( ( None, None, -10 ), "",      -10   ), # standard negative case
				( ( None, None,  10 ), "",       10   ), # standard positive case
				( ( None, None,   0 ), "",        0   ), # zero case
				( ( -10, None,  -10 ), "",      -10   ), # default same as lbound case
				( ( None, 10,    10 ), "",       10   )) # default same as ubound case

		self.callSolicitInteger( valid_default, None )

	#============================================
	def test_SolicitInteger_Valid( self ):
		"""Does your SolicitInteger function correctly handle user input that's too low?"""

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

		self.callSolicitInteger( valid, None )

	#============================================
	def test_SolicitInteger_Garbage( self ):
		"""Does your SolicitInteger function correctly handle garbage input?"""

		invalid_garbage = (
				( ( None, None, None ), "l jdf", None ),
				( ( None, None, None ), "",      None ),
				( ( None, None, None ), "19fgd", None ),
				( ( -10, None, None ), "crap", None ),
				( ( -10, 10, None ), "crappetycrap", None ),
				( ( None, 10, None ), "dasisnichtsogut", None ),
				( ( None, 10, 5 ), "sadkjfhslakfhkl lk", None ),
				( ( -10, None , 10 ), "sadkjfhslakfhkl lk", None ))

		self.callSolicitInteger( invalid_garbage, 'invalid input' )

	#============================================
	@unittest.skip( "Not testing RunTurn with unittest" )
	def test_RunTurn( self ):
		# enter trash and see if it's dealt with
		# Check to see that 0 is a valid lower and upper bound
		# check that the number chosen by the computer is really random by running RunTurn 5 times

		pass
		#stu_mod.RunTurn(-1000,1000)

if __name__ == '__main__':


	_ = TestModule()

	print "******************BIOF 309 HW2 TEST PROGRAM, version 2.1 *******************"

	del sys.argv[1:]
	unittest.main(buffer=True,verbosity=3)
