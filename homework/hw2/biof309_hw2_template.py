"""
BIOF 309 - Homework 2 - Number Guessing Game
by Christopher Coletta - christopher.coletta@gmail.com

This file is a template. Your job is to replace the two "pass" placeholders in the functions
SolicitInteger and RunTurn with your code.

The object of the game is to guess an integer chosen randomly by the computer, the integer
being within a certain range of values that the user provides. The game can have up to ten
players who will take turns guessing. The program keeps track of the time it takes for each
player to guess their number and how many turns s/he needed.  At the end of the game it prints
out a report on how the contestants did, the winner being the one who took the least amount of
time to guess their number. The program then asks the user(s) if they want to play again.
"""

#==========================================================================
def SolicitInteger(lobound=None, hibound=None, default_return=None):
	"""Interactively asks the user to input an integer and returns that integer.
	
	Arguments:
	lobound -- an integer indicating the lowest acceptable user input. By default lbound is
	           assigned the value None, i.e., no lower bound on what's an acceptable integer.
	hibound -- an integer indicating the highest acceptable user input. By default hibound is
	           assigned the value None, i.e., no upper bound on what's an acceptable integer.
	default_return -- an integer indicating the value this function should return if the user
	           indicates s/he prefers the default by just pressing Enter.

	Behavior:
	* Print "invalid input" and return None if user input is not interpretable as an integer
	  or the user presses Enter and default_return is None.
	* Print "too low" and return None if lbound is specified in the function call and
	  user input is less than lbound.
	* Print "too high and return None if hibound is specified in the function call and
	  input is greater than hibound.
	* Return default_return if it is specified in the function call and the user just
	  presses enter.
	* Return the input converted to an integer if it passes all the criteria for valid input.
	
	Tips:
	* The integer 0 IS a legal value for a lower or upper bound.
	* No loops in here. This function asks for input once and returns something based on that.
	* I did it in 14 lines. Can you do it in less?? :-)
	"""
	pass


#==========================================================================
def AskHowManyPlayers():
	"""Prompts the user for an integer and checks for valid input."""

	# Loop forever until the user enters an integer between 1 and 10, inclusive.
	while True:
		print "How many players? Enter a number between 1 and 10, or press enter for default 2:"
		num_players = SolicitInteger( lobound=1, hibound=10, default_return=2 )
		if num_players != None:
			print "Ok, {} players.".format( num_players )
			return num_players

#==========================================================================
def AskForNumberRange():
	"""Prompts the user to enter a range of numbers and checks for valid input."""

	while True:
		# This OUTER loop will loop forever until the user enters correct integers for
		# lower and upper bound, such that lobound < hibound.

		while True:
			# This INNER loop will loop forever until the user enters a valid value for lobound
			print "Enter the LOWER bound for the range of numbers, or press enter for default 1:"
			lobound = SolicitInteger( default_return=1 )
			if lobound != None:
				print "Ok, lower bound of {}.".format( lobound )
				break

		while True:
			# This INNER loop will loop forever until the user enters a valid value for hibound
			print "Enter the UPPER bound for the range of numbers that's greater than the lowerbound, or press enter for default 20:"
			hibound = SolicitInteger( default_return=20 )
			if hibound != None:
				print "Ok, upper bound of {}.".format( hibound )
				break

		if lobound < hibound:
			# We've got what we need! return out of this function!
			return lobound, hibound

		# Uh oh. If we're still here, the user didn't enter in a correct range
		print "***Invalid input: upper bound must be greater than lower bound***"
		# Back to the beginning of the outer loop

#==========================================================================
def RunTurn( lobound=1, hibound=20 ):
	"""Generates a random number on interval [lobound, hibound) and interactively prompts
	user to guess it. Returns a tuple containing the number of guesses and the time it took
	for user to correctly guess.
	
	Arguments:
	lobound -- an integer indicating the lower endpoint of the interval from which the computer
	           should choose a random integer. Default is 1.
	hibound -- an integer indicating the upper endpoint of the interval from which the computer
	           should choose a random integer. Default is 20.

	Return:
	A tuple containing two values, the number of guesses and the time it took
	for user to correctly guess, in that order.

	Pseudocode:
	1. Choose a random number
	2. Record what time it is now
	3. Loop forever asking the user to guess the number. Break out when they guess.
	4. Keep track of how many times you've looped.
	5. Total elapsed time is the current time now minus the time you recorded in step 2.
	6. Print out a message as to how they did
	7. Return the values

	Tips:
	* Use your completed SolicitInteger function in here.
	* I did it in 15 lines, but it is definitely possible to do it in less :-)
	"""
	pass

#==========================================================================
def RunGame():

	try:
		while True:
			print "Welcome to the BIOF309 Homework 2 Number Guessing Game!"

			num_players = AskHowManyPlayers()
			lobound, hibound = AskForNumberRange()

			player_timings = []
			num_guesses_for_each_player = []

			for player_number in range( 1, num_players + 1 ):
				raw_input( "Player {}, your turn! Hit any key to begin...".format( player_number ) )
				num_guesses, total_elapsed_time = RunTurn( lobound, hibound )
				player_timings.append( total_elapsed_time )
				num_guesses_for_each_player.append( num_guesses )

			# Now that all the players have taken their turns, let's decide who won.

			# Bind up the game results into a sortable list of tuples
			# where you have a row for each player and the columns correspond with 
			# the player number, his/her time, and his/her number of guesses, respectively.
			standings = zip( range( 1, num_players + 1 ), player_timings, num_guesses_for_each_player )
			
			# Sort the game results in order of the players' elapsed time, i.e., column 1.
			# Pass to the sorter a little one-line lambda function that tells it to look at the
			# 1th column when comparing players pairwise for sorting purposes.
			standings.sort( key = lambda row: row[1] )

			print "FINAL SCORE:"
			print "Place\tPlayer\tTime\tNum Guesses"
			for place_number, player_info in enumerate( standings, start = 1 ):
				print "{}\t{}\t{:0.2f}\t{}".format( place_number, *player_info )

 			response = raw_input( "Would you like to play again (y/n)?" )
			if response.upper() != 'Y':
				break

	except KeyboardInterrupt:
		# If the user decides s/he doesn't want to play anymore and hits Ctrl-C
		# don't bark at them! Just catch the exception and exit gracefully...
		pass

	print "\n\nThanks for playing!"


#==========================================================================

if __name__ == '__main__': # What the hell is this line for?!?! I'll tell you:

	# If you run this program, Python will execute the code in this block and start the game.
	# However, if you import this code as a module into some other program (as is done by the
	# autograder), it WILL NOT run the code in this block, and therefore will not automatically
	# start a new game.

	# Python keeps track of the context of where code is run using the global variable
	# __name__. If this main program, __name__ will be set to '__main__', but if 
	# some other program imported this code, __name__ will be set to something else.

	# This way, this file can serve double duty as being a runnable program in itself, as well
	# as a module containing a library of functions that other programs can import and reuse.

	RunGame()	

