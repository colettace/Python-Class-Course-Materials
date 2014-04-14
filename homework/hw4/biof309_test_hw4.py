"""
Autograding code for BIOF 309 Homework 4: Nucleotide to Amino Acid translator
Run this code from the command line: python biof309_test_hw4.py your_file.py

You can run this program on the provided byte-compiled solution to see that it works.
"""
import unittest
import importlib
import sys

zscan4_dna_seq = "CCTTGTAATTCATAAATCTCTGAAAACTTAAAAGTTTGAGCAAAAGTTTGTCATGTTTCTATGAGTAATTTATAATAAAACTTGATCAGAATTTGTGAGACTAACGTTTGTCTTTATATTTTCCTTTTTTTTTTTTTTTTTTTTGAGACACAGTCTCGCTCTGTCGTCCAGGCTGGAGTGCCGTGGCGTAATCTCGGCTCACTGCAACCTCTGCCTCCTGGATTCAAACAATTCTTCTGCCTCAGCCTCCTGAGTAGCTGGGATTACAGGACCAGTGATGGTATAGAACACTGTATTAGAGACATGGAGCTGGGGCTGGATGAAGATTCCATCAGTAATTCAATCAACAGACAAGTGTTATCCAATCACGTCTTTAAATCAATCACTGACATGGAGCTGGGGCTGGATGAAGATTCCATCAGTAATTCAATCAACAGACAAGTGTTATCCAATCACGTCTTTAAATCAATCACTGATCCCAGCCCCTATAAAAGGGAGCAGCCTTAGGAGGCACATCAGATAAACCCAGTGTGGAAAGCTAGTCACACATCAGCTCAGTGTTCGGCCCGGGATTACCCAGTCAACCAAGGAGCTTGCAGTTTTAAAGAATCCACCAACTGTTGAAACAAATCCCTAGAGACACAAGGCAAGAGACTGAATCATCAAAGTAAAGTCTCTCTGAGAATTATTGCTAAGAATGGCTTTAGATCTAAGAACCATATTTCAGTGTGAACCATCCGAGAATAATCTTGGATCAGAAAATTCAGCGTTTCAACAAAGCCAAGGACCTGCTGTTCAGAGAGAAGAAGGGATTTCTGAGTTCTCAAGAATGGTGCTCAATTCATTTCAAGACAGCAATAATTCATATGCAAGGCAGGAATTGCAAAGACTTTATAGGATCTTTCACTCATGGCTGCAACCAGAAAAGCACAGCAAGGATGAAATTATTTCTCTATTAGTCCTGGAGCAGTTTATGATTGGTGGCCACTGCAATGACAAAGCCAGTGTGAAAGAGAAATGGAAATCAAGTGGCAAAAACTTGGAGAGATTCATAGAAGACCTGACTGATGACAGCATAAATCCACCTGCCTTAGTCCACGTCCACATGCAGGGACAGGAAGCTCTCTTTTCTGAGGATATGCCCTTAAGAGATGTCATTGTTCATCTCACAAAACAAGTGAATGCCCAAACCACAAGAGAAGCAAACATGGGGACACCCTCCCAGACTTCCCAAGATACTTCCTTAGAAACAGGACAAGGATATGAAGATGAACAAGATGGCTGGAACAGTTCTTCGAAAACTACTCGAGTAAATGAAAATATTACTAATCAAGGCAATCAAATAGTTTCCCTAATCATCATCCAGGAAGAGAACGGTCCTAGGCCTGAAGAGGGAGGTGTTTCTTCTGACAACCCATACAACTCAAAAAGAGCAGAGCTAGTCACTGCTAGATCTCAGGAAGGGTCCATAAATGGAATCACTTTCCAAGGTGTCCCTATGGTGATGGGAGCAGGGTGTATCTCTCAACCAGAGCAGTCCTCCCCTGAGTCTGCCCTTACCCACCAGAGCAATGAGGGAAATTCCACATGTGAGGTACATCAGAAAGGATCCCATGGAGTCCAAAAATCATACAAATGTGAAGAATGCCCCAAGGTCTTTAAGTATCTCTGTCACTTATTAGCTCACCAGAGAAGACACAGGAATGAGAGGCCATTTGTTTGTCCCGAGTGTCAAAAAGGCTTCTTCCAGATATCAGACCTACGGGTGCATCAGATAATTCACACAGGAAAGAAGCCTTTCACATGCAGCATGTGTAAAAAGTCCTTCAGCCACAAAACCAACCTGCGGTCTCATGAGAGAATCCACACAGGAGAAAAGCCTTATACATGTCCCTTTTGTAAGACAAGCTACCGCCAGTCATCCACATACCACCGCCATATGAGGACTCATGAGAAAATTACCCTGCCAAGTGTTCCCTCCACACCAGAAGCTTCCTAAGCTGCTGGTCTGATAATGTGTATAAATATGTATGCAAGTATGTATATTCCTATAGTATTTATCTACTTAGGATATAAGATATAATCTCCTGATTATGCTTTCAATTTATTGTCTTGCTTCATTAAAATGTAAGGCTAAGGAGAGCATGGAATTTGTCAGTTTTGTTCACTAAAGTATTCCAAGTGGTTGGGAAAGTGGAACATTTCCAAGAACCAATAAATTTCTGTTGAATAAATGAATGAATCCAAAAAAAAAAAAAAA"
zscan4_dna_test_substring = zscan4_dna_seq[900:-900]
list_of_files = \
"""zscan4_rna.fasta
zscan4_dna.txt
zscan4_dna_invalid_nt.fasta
zscan4_dna_invalid_nt.txt
zscan4_dna_too_long.fasta
zscan4_dna_too_long.txt"""

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
class TestHW4DNA( unittest.TestCase ):
    """All these test have to pass to get an A"""

    def setUp( self ):
        """Create a properly instantiated RNASequence for C-level tests"""

        self.stumod = TestModule.getMod()
        self.zscan4 = self.stumod.DNASequence.NewFromFastaFile( 'zscan4_dna.fasta' )
        self.errmsg_no_implement = "Tried to use {} on an instance of your class but I got a " +\
                     "TypeError. Either you forgot to implement the special function {}" +\
                     " or something is wrong with your implementation."
        self.errmsg_wrong_output = "Wrong output!! Called:\n{}\nExpected:\n{}\nGot:\n{}"


    # The C grade tests

    #============================================
    def test_len( self ):
        """Check to see len() was implemented and returns correct output"""
        try:
            thelen = len(self.zscan4)
        except TypeError:
            self.fail( self.errmsg_no_implement.format( 'len()', '__len__' ) )
        except NotImplementedError:
            self.fail( "You forgot to implement {}!".format( '__len__' ) )

        try:
            self.assertEqual( len( zscan4_dna_seq ), thelen )
        except AssertionError:
            self.fail( self.errmsg_wrong_output.format( "len( zscan4 )", len(zscan4_dna_seq), thelen ) )

    #============================================
    def test_str( self ):
        """Check to see str() was implemented and returns correct output"""
        try:
            thestr = str(self.zscan4)
        except TypeError:
            self.fail( self.errmsg_no_implement.format( 'str()', '__str__' ) )
        except NotImplementedError:
            self.fail( "You forgot to implement {}!".format( '__str__' ) )

        try:
            self.assertEqual( zscan4_dna_seq, thestr )
        except AssertionError:
            self.fail( self.errmsg_wrong_output.format( "str( zscan4 )", zscan4_dna_seq, thestr ) )

    #============================================
    def test_repr( self ):
        """Check to see __repr__() was implemented"""
        try:
            self.zscan4.__repr__()
        except NotImplementedError:
            self.fail( "You forgot to implement {}!".format( '__repr__' ) )

    #============================================
    def test_in( self ):
        """Check to see __contains__ was implemented and returns correct output"""
        try:
            inval = zscan4_dna_test_substring in self.zscan4
        except TypeError:
            self.fail( self.errmsg_no_implement.format( 'in', '__contains__' ) )
        except NotImplementedError:
            self.fail( "You forgot to implement {}!".format( '__contains__' ) )

        try:
            self.assertTrue( inval )
        except AssertionError:
            print "\nError: Check to make sure the following string is contained in your zscan4 dna instance:\n"
            print zscan4_dna_test_substring
            self.fail( self.errmsg_wrong_output.format( "zscan4_dna_test_substring in zscan4", True, inval )  )

    #============================================
    def test_count( self ):
        print self.zscan4.count('GGAA')

    #============================================
    def test_IsValidSequence( self ):
        pass

    #============================================
    def test_GCContent( self ):
        pass

    # The B grade tests


    #============================================
    def test_NewFromFastaFila( self ):
        pass

    #============================================
    def test_TranslateToAA( self ):
        pass

    # The B grade tests

    #============================================
    def test_OpenReadingFrames( self ):
        pass



if __name__ == '__main__':


    _ = TestModule()

    print "******************BIOF 309 HW4 TEST PROGRAM, version 1.0 *******************"

    del sys.argv[1:]
    unittest.main(verbosity=3)
