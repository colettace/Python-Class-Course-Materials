"""FAES BIOF 309 Introduction to Python
Homework 5: Guess Chris's Girlfriend's Name

When my girlfriend first introduced herself to me, she gave me a riddle to guess her name.
She said her name was the name of a bird that was mentioned in passing in the text of
Henry David Thoreau's Walden.

So I successfully used NCBI taxonomy data to obtain the name of every known species of bird
(class Aves), and I cross-referenced that against the text of Walden. She was impressed!

In this file, I have included three functions that parse NCBI taxonomy files and provide
the list of species of a given taxon node id.

It is your task to complete the last step by writing a function that parses a file 
containing the text of Walden and returns a set of all the words used. Then you find
the intersection of the two sets, and my girlfriend's name will be one of the words in 
the intersection.

"""

import re
#==============================================================================
def BuildTaxonNamesDict( names_file ):
	"""Parses a names.dmp file and returns a dict of taxon node ids/taxon names.

	INPUT:  A path to an NCBI names.dmp file.
	RETURN: common_names_dict =: { keys = taxon node ids;
	                               values = names associated with taxon }
	NOTES:  It will concatenate multiple common names with a '/' character. It will
	        use the scientific name if no common name(s) is given.
	"""
	p = re.compile( r'\t\|\t' )

	common_names_dict = {}
	scientific_names_dict = {}
	with open( names_file ) as names:
		for line in names:
			#print line
			node_id, name_txt, crap, name_class  = p.split( line, 3 )
			if 'common name' in name_class:
				if node_id not in common_names_dict:
					common_names_dict[ node_id ] = name_txt
				else:
					common_names_dict[ node_id ] += '/' + name_txt
			if 'scientific name' in name_class:
				if node_id not in scientific_names_dict:
					scientific_names_dict[ node_id ] = name_txt

	# Default to the scientific name if there's no common name available.
	set_of_scientific_nodes_wo_common_names = \
	   set( scientific_names_dict.keys() ) - set( common_names_dict.keys() )
	for node_id in set_of_scientific_nodes_wo_common_names:
		common_names_dict[ node_id ] = scientific_names_dict[ node_id ]
	return common_names_dict

#==============================================================================
def BuildTaxonomyTree( tax_file ):
	"""Parses a nodes.dmp file are returns two dicts used to traverse the taxonomy tree.

	INPUT:   A path to an NCBI nodes.dmp file.
	RETURN1: taxonomy_node_dict := { keys = taxon node ids;
	                                 values = list of node ids that are children to taxon }
	RETURN2: taxonomy_rank_dict := { keys = taxon node ids;
	                                 values = rank of taxon (genus, order, family, etc) }
	"""
	p = re.compile( r'\t\|\t' )

	taxonomy_node_dict = {}
	taxonomy_rank_dict = {}
	with open( tax_file ) as nodes:
		for line in nodes:
			child_node_id, parent_node_id, rank, crap = p.split( line, 3 )
			if parent_node_id not in taxonomy_node_dict:
				taxonomy_node_dict[ parent_node_id ] = []
			taxonomy_node_dict[ parent_node_id ].append( child_node_id )
			taxonomy_rank_dict[ child_node_id ] = rank
	return taxonomy_node_dict, taxonomy_rank_dict

#==============================================================================
def TaxonomyWalker( parent_node_id, node_dict, rank_dict, names_dict, indent_level=0 ):
	"""Returns the set of names of all species or subspecies that are children to a given parent taxon.
	
	INPUT1: parent_node_id := string containing the parent taxon id.
	INPUT2: node_dict      := dict that has parent/child taxonomy relationships.
	INPUT3: rank_dict      := dict that associates rank (genus, order, family, etc) to taxon.
	INPUT4: names_dict     := dict that associates taxon name to taxon id.
	INPUT5: indent_level   := Keeps track of what generation this taxon is relative to
	                          parent_node_id (used for pretty-printing traversal output).
	RETURN: set_of_species_names := set of names of all species/subspecies that are children
	                          to parent node.
	"""

	format_str = '{}Found {} {} "{}" in parent {} {} "{}"'
	set_of_species_names = set()

	parent_rank = rank_dict[ parent_node_id ]
	# Here, we use "names_dict.get(parent_node_id, '')" instead of "names_dict[ parent_node_id ]"
	# because .get() won't raise a KeyError exception if parent_node_id is not in the names_dict
	parent_name = names_dict.get( parent_node_id, '' )

	# Iterate over this node's children taxa:
	for child_node_id in node_dict[ parent_node_id ]:
		child_rank = rank_dict[ child_node_id ]
		child_name = names_dict.get( child_node_id, '' )
		print format_str.format( indent_level*"  ", child_rank, child_node_id, child_name, parent_rank, parent_node_id, parent_name )
		# If this child taxon is a species, add its name to my own list.
		if 'species' in child_rank:
			set_of_species_names.add( child_name )
		# If this child taxon has children of its own, check to see if any of them are species or 
		# subspecies by recursively calling TaxonomyWalker on the child, and add their species 
		# names to my list.
		if child_node_id in node_dict:
			set_of_species_names.update( TaxonomyWalker( child_node_id, node_dict, rank_dict, names_dict, indent_level+1 ) )
	return set_of_species_names

#==============================================================================
def ReturnSetOfWordsInFile( input_file ):
	"""Parses the test file "input_file" and returns a set of all the words contained therein.
	INPUT1: input_file := string path to a file which is to be parsed
	RETURN: set_of_words_in_file := set of words contained in input_file
	"""
	#YOU MUST IMPLEMENT THIS METHOD!
	pass

#==============================================================================
if __name__ == '__main__':

	names_dict = BuildTaxonNamesDict( 'names.dmp' )
	taxonomy_node_dict, taxonomy_rank_dict = BuildTaxonomyTree( 'nodes.dmp' )
 	set_of_species_names = TaxonomyWalker( '8782', taxonomy_node_dict, taxonomy_rank_dict, names_dict )
	
	set_of_walden_words = ReturnSetOfWordsInFile( 'walden.txt' )
	
	# Now find the intersection of the two sets of words.
	# Email me the intersection set as well as your guess as to
	# what my girlfriend's name is.
	# Good luck!
	# -Chris

