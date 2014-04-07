#!/usr/bin/env python
"""
FAES BIOF309 Introduction To Python
Template File for Homework 4:
OBJECT-ORIENTED NUCLEOTIDE-TO-AMINO-ACID TRANSLATOR

Anywhere you see a "raise NotImplementedError" in this file, you have to fill in that method's 
implementation.

You are not allowed to change the method declaration lines, which are the lines with the
"def" in them. In computer science terms "the interface is fixed."
However, the implementation details are totally up to you. Feel free to add any
private helper methods (i.e., methods for internal use only, ones that start with '_')
to any of the classes.

The base class NucleotideSequence is inherited by the subclasses DNASequence
and RNASequence. You are implementing functions in the base class which means the logic
must work for both DNA and RNA. The instance attributes "self._translation_table", 
"self._valid_nts" are all set to their proper DNA/RNA values in each subclass'
__init__() function, so you can make your methods work independent of 
whether they're DNA or RNA by referencing those two instance attributes 
rather than hardcoding 'G', 'A', 'C', 'T', or 'U' in anywhere. Also, it is not allowed
to mention the subclasses in base class code. In other words, you can't use the
words "DNASequence" or "RNASequence" anywhere in your base class code.

A new genomics concept that is introduced in this assignment that was left
out of the last assignment is the concept of choosing a desired reading frame before
translating the sequence to AA. The template methods given below have arguments
in which the directionality of the transcription can be specified 
( True = 5'to3', False = 3'to5' ) as well as the position of the reading frame (1, 2, or 3).

I will use as input to test your implementation a mRNA sequence which contains more
than just one coding region. If you want to get an A, your code must find and return all the 
open reading frames (coding regions) in my input sequence (see the function 
OpenReadingFrames() below).
"""
import sys
import re

#==================================================================
class NucleotideSequence( object ):
	"""Abstract base class to be inherited by subclasses DNASequence and RNASequence.

	Your assignment is to replace each "raise NotImplementedError" line with your
	implementation of that method.
	
	This class is not meant to be used in the wild, meaning you wouldn't ever 
	instantiate an object of class NucleotideSequence, but rather you would only ever
	instantiate an object of DNASequence or RNASequence, and that the functionality
	you're about to implement here in the base class would be "inherited" by the subclasses.
	"""

	def __init__( self, sequence=None ):
		self._data = sequence
		self._translation_table = None
		self._valid_nts = None

	# YOU MUST IMPLEMENT THE FOLLOWING METHODS FOR A MAXIMUM GRADE OF C:

	def __len__( self ):
		"""This is the method Python will run when the user calls len() on this instance.
		Return the total number of ucleotides in the sequence contained in self._data."""
		raise NotImplementedError

	def __str__( self ):
		"""This is the method Python will run when the user calls str() on this instance"""
		raise NotImplementedError

	def __repr__( self ):
		"""This is the method Python will run when the user types the name of the
		instance in a Python interpreter."""
		raise NotImplementedError

	def __contains__( self, substr ):
		"""This is the method Python will run when the user wants to use the keyword "in",
		e.g., "TAG" in my_sequence."""
		raise NotImplementedError

	def count( self, substring, start=0, end=sys.maxint ):
		"""Return the number of times the substring appears in the sequence.
		This function should work just like str.count."""
		raise NotImplementedError

	def IsValidSequence( self ):
		"""This function should raise a ValueError if it detects a character
		which is not a valid nucleotide character for its molecule type."""
		raise NotImplementedError

	def GCContent( self ):
		"""Return the fraction of nucleotides in this sequence that are Cytosine and Guanine"""
		raise NotImplementedError


	#==================================================================
	# YOU MUST IMPLEMENT THE FOLLOWING METHODS FOR A MAXIMUM GRADE OF B

	@classmethod
	def NewFromFastaFile( cls, path_to_fasta_file ):
		"""This function should read a nucleotide sequence from a fasta file,
		parse it, check if the nucleotide sequence is valid by calling IsValidSequence(),
		instantiate a new object, populate its instance attribute "_data" with the sequence,
		and finally return the new instance."""
		raise NotImplementedError

	#==================================================================
	def TranslateToAA( self, directionality5to3=True, reading_frame=1 ):
		"""Return the sequence translated into amino acids. The user is able to specify
		the direction of translation (5'->3' or vice versa) and the reading frame offset,
		either 1, 2, or 3"""
		raise NotImplementedError

	#==================================================================
	# YOU MUST IMPLEMENT THE FOLLOWING METHOD FOR A MAXIMUM GRADE OF A

	def OpenReadingFrames( self, directionality5to3=True, reading_frame=1 ):
		"""This function should return a list of tuples which contain, for the given 
		directionality and reading frame, 1. the aa start position, 2. aa end position, and 
		3. amino acid sequence of every open reading frame in the sequence. Remember,
		ORFs start with a Methionine (generally) and end with a stop codon. Hint:
		use a regular expression."""
		raise NotImplementedError

	# end class NucleotideSequence definition
	#==================================================================

dna_codon_dict = { "TTT" : "F", "TCT" : "S", "TAT" : "Y", "TGT" : "C", \
"TTC" : "F", "TCC" : "S", "TAC" : "Y", "TGC" : "C", \
"TTA" : "L", "TCA" : "S", "TAA" : ".", "TGA" : ".", \
"TTG" : "L", "TCG" : "S", "TAG" : ".", "TGG" : "W", \
"CTT" : "L", "CCT" : "P", "CAT" : "H", "CGT" : "R", \
"CTC" : "L", "CCC" : "P", "CAC" : "H", "CGC" : "R", \
"CTA" : "L", "CCA" : "P", "CAA" : "Q", "CGA" : "R", \
"CTG" : "L", "CCG" : "P", "CAG" : "Q", "CGG" : "R", \
"ATT" : "I", "ACT" : "T", "AAT" : "N", "AGT" : "S", \
"ATC" : "I", "ACC" : "T", "AAC" : "N", "AGC" : "S", \
"ATA" : "I", "ACA" : "T", "AAA" : "K", "AGA" : "R", \
"ATG" : "M", "ACG" : "T", "AAG" : "K", "AGG" : "R", \
"GTT" : "V", "GCT" : "A", "GAT" : "D", "GGT" : "G", \
"GTC" : "V", "GCC" : "A", "GAC" : "D", "GGC" : "G", \
"GTA" : "V", "GCA" : "A", "GAA" : "E", "GGA" : "G", \
"GTG" : "V", "GCG" : "A", "GAG" : "E", "GGG" : "G" }

rna_codon_dict = { "UUU" : "F", "UCU" : "S", "UAU" : "Y", "UGU" : "C", \
"UUC" : "F", "UCC" : "S", "UAC" : "Y", "UGC" : "C", \
"UUA" : "L", "UCA" : "S", "UAA" : ".", "UGA" : ".", \
"UUG" : "L", "UCG" : "S", "UAG" : ".", "UGG" : "W", \
"CUU" : "L", "CCU" : "P", "CAU" : "H", "CGU" : "R", \
"CUC" : "L", "CCC" : "P", "CAC" : "H", "CGC" : "R", \
"CUA" : "L", "CCA" : "P", "CAA" : "Q", "CGA" : "R", \
"CUG" : "L", "CCG" : "P", "CAG" : "Q", "CGG" : "R", \
"AUU" : "I", "ACU" : "T", "AAU" : "N", "AGU" : "S", \
"AUC" : "I", "ACC" : "T", "AAC" : "N", "AGC" : "S", \
"AUA" : "I", "ACA" : "T", "AAA" : "K", "AGA" : "R", \
"AUG" : "M", "ACG" : "T", "AAG" : "K", "AGG" : "R", \
"GUU" : "V", "GCU" : "A", "GAU" : "D", "GGU" : "G", \
"GUC" : "V", "GCC" : "A", "GAC" : "D", "GGC" : "G", \
"GUA" : "V", "GCA" : "A", "GAA" : "E", "GGA" : "G", \
"GUG" : "V", "GCG" : "A", "GAG" : "E", "GGG" : "G" }

class DNASequence( NucleotideSequence ):

	_translation_table = dna_codon_dict

	def __init__( self, sequence=None ):
		self._data = sequence
		self._valid_nts = "AGCT"

class RNASequence( NucleotideSequence ):

	_translation_table = rna_codon_dict

	def __init__( self, sequence=None ):
		self._data = sequence
				self._valid_nts = "AGCU"


if __name__ == '__main__':
	DNAseq = DNASequence.NewFromFastaFile( 'zscan4.fasta' )

	reading_frames = ( (True, 1), (True, 2), (True, 3), (False, 1), (False, 2), (False, 3) )

	for direction, reading_frame in reading_frames:
		print "{} direction, reading frame {}:".format( "5'to3'" if direction else "3'to5'", reading_frame )
		print DNAseq.OpenReadingFrames( direction, reading_frame )
