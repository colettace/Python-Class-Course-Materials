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

zscan4_translated_aa =\
"""PCNS.ISENLKV.AKVCHVSMSNL..NLIRICETNVCLYIFLFFFFFFETQSRSVVQAGVPWRNLGSLQPLPPGFKQFFCLSLLSSWDYRTSDGIEHCIRDMELGLDEDSISNSINRQVLSNHVFKSITDMELGLDEDSISNSINRQVLSNHVFKSITDPSPYKREQP.EAHQINPVWKASHTSAQCSARDYPVNQGACSFKESTNC.NKSLETQGKRLNHQSKVSLRIIAKNGFRSKNHISV.TIRE.SWIRKFSVSTKPRTCCSERRRDF.VLKNGAQFISRQQ.FICKAGIAKTL.DLSLMAATRKAQQG.NYFSISPGAVYDWWPLQ.QSQCEREMEIKWQKLGEIHRRPD..QHKSTCLSPRPHAGTGSSLF.GYALKRCHCSSHKTSECPNHKRSKHGDTLPDFPRYFLRNRTRI.R.TRWLEQFFENYSSK.KYY.SRQSNSFPNHHPGRERS.A.RGRCFF.QPIQLKKSRASHC.ISGRVHKWNHFPRCPYGDGSRVYLSTRAVLP.VCPYPPEQ.GKFHM.GTSERIPWSPKIIQM.RMPQGL.VSLSLISSPEKTQE.EAICLSRVSKRLLPDIRPTGASDNSHRKEAFHMQHV.KVLQPQNQPAVS.ENPHRRKALYMSLL.DKLPPVIHIPPPYEDS.ENYPAKCSLHTRSFLSCWSDNVYKYVCKYVYSYSIYLLRI.DIIS.LCFQFIVLLH.NVRLRRAWNLSVLFTKVFQVVGKVEHFQEPINFC.INE.IQKKKK
LVIHKSLKT.KFEQKFVMFL.VIYNKT.SEFVRLTFVFIFSFFFFFFLRHSLALSSRLECRGVISAHCNLCLLDSNNSSASAS.VAGITGPVMV.NTVLETWSWGWMKIPSVIQSTDKCYPITSLNQSLTWSWGWMKIPSVIQSTDKCYPITSLNQSLIPAPIKGSSLRRHIR.TQCGKLVTHQLSVRPGITQSTKELAVLKNPPTVETNP.RHKARD.IIKVKSL.ELLLRMALDLRTIFQCEPSENNLGSENSAFQQSQGPAVQREEGISEFSRMVLNSFQDSNNSYARQELQRLYRIFHSWLQPEKHSKDEIISLLVLEQFMIGGHCNDKASVKEKWKSSGKNLERFIEDLTDDSINPPALVHVHMQGQEALFSEDMPLRDVIVHLTKQVNAQTTREANMGTPSQTSQDTSLETGQGYEDEQDGWNSSSKTTRVNENITNQGNQIVSLIIIQEENGPRPEEGGVSSDNPYNSKRAELVTARSQEGSINGITFQGVPMVMGAGCISQPEQSSPESALTHQSNEGNSTCEVHQKGSHGVQKSYKCEECPKVFKYLCHLLAHQRRHRNERPFVCPECQKGFFQISDLRVHQIIHTGKKPFTCSMCKKSFSHKTNLRSHERIHTGEKPYTCPFCKTSYRQSSTYHRHMRTHEKITLPSVPSTPEAS.AAGLIMCINMYASMYIPIVFIYLGYKI.SPDYAFNLLSCFIKM.G.GEHGICQFCSLKYSKWLGKWNISKNQ.ISVE.MNESKKKKK
L.FINL.KLKSLSKSLSCFYE.FIIKLDQNL.D.RLSLYFPFFFFFF.DTVSLCRPGWSAVA.SRLTATSASWIQTILLPQPPE.LGLQDQ.WYRTLY.RHGAGAG.RFHQ.FNQQTSVIQSRL.INH.HGAGAG.RFHQ.FNQQTSVIQSRL.INH.SQPL.KGAALGGTSDKPSVES.SHISSVFGPGLPSQPRSLQF.RIHQLLKQIPRDTRQETESSK.SLSENYC.EWL.I.EPYFSVNHPRIILDQKIQRFNKAKDLLFREKKGFLSSQEWCSIHFKTAIIHMQGRNCKDFIGSFTHGCNQKSTARMKLFLY.SWSSL.LVATAMTKPV.KRNGNQVAKTWRDS.KT.LMTA.IHLP.STSTCRDRKLSFLRICP.EMSLFISQNK.MPKPQEKQTWGHPPRLPKILP.KQDKDMKMNKMAGTVLRKLLE.MKILLIKAIK.FP.SSSRKRTVLGLKREVFLLTTHTTQKEQS.SLLDLRKGP.MESLSKVSLW.WEQGVSLNQSSPPLSLPLPTRAMREIPHVRYIRKDPMESKNHTNVKNAPRSLSISVTY.LTREDTGMRGHLFVPSVKKASSRYQTYGCIR.FTQERSLSHAACVKSPSATKPTCGLMRESTQEKSLIHVPFVRQATASHPHTTAI.GLMRKLPCQVFPPHQKLPKLLV..CV.ICMQVCIFL.YLST.DIRYNLLIMLSIYCLASLKCKAKESMEFVSFVH.SIPSGWESGTFPRTNKFLLNK.MNPKKKK
KKKKKPK.VNKLSLNNQEPLQGERVGEPYEITCFDCLRYERNRNVKLLRSVI.LSY.SSNIEYRIHLFMISLYV.TYV.ICVIVWSSNPSKTTPPL.TVPLKEYSGVYRHHTPTDRHRTECFPCTYSEKRTHLREYSGVQPKHRLPEKCVRRTLSEERTHLIDYVGIQTIDLLRKNCEPCLFTGE.GHRRDHSIIHCLYEFLEPRKKCKHTKNLRYPRKDYMECTP.RE.RDHPFPSESPPDETNSLCGTRVVVSLWNLSLR.IPGKDSRSSLIETRKTQHTQQSSLWREKSGSWQEKDLLLIPLIN.RN.SL.K.MSSSKAS.QGR.NK.KYRNRTKIPS.NPSDPPTGVQTKRTPNP.VNKTLYLLL.RIPV.ESFLSKDRDVHLHLIPST.IRQ.SVQKILREVQKR.TKGKEKV.PKQ.RHRWLVFDEVLIISLLK.ERHEKTNVGTHFLGYFRNVKDGTYT..RQNFT.LVVRTLESLGKKRDLSSRNRNNFAT.KTRF..EPTKCDFIPRI.ISVRIVIKSLSEMKLLSQRTEHRDP.TKLSTT.EILTFEEPTDPLGPGL.LDYTLIERCDPNRLHGGFRRGKISPTLVTN.ISALTYCEQTTNLMTTLEVGRGRGTVTN.ISALTYCEQTTNLMTTLEVGRGRGTEIMSQDMVVTRTLGSMSPPTPSS.QT.VLRLQRHSALMRCREVGPAVSL.HRVFFFFFFPFIFLFAIRVFKTSSK.YLMSIFVLFENEFENSKVSKYLMF
KKKKNLSK.ISCL.ITKNLYKVKGLVNLMKSLVLTV.GTRGIGM.NYFVLLFNFRISPLI.NIGFIYL.YPYMYERMYKYV..SGRRILRRPHLPCEPSH.KSTQEYTATIHLLTAIEQNVFPVHIPKRGHT.ESTLASNQNTDFLKNVYDVHFPKKGHT..TTWASRL.TFFGKTVSPVCLPESKDTEETTRLFTVSMNFWNPVRSVNILKT.GTLGKTTWSVHLKGSNETTHSRLSPLLTRPTLYVGRG.WYPCGTFH.GKYLGRTLDRH.SRREKLNIPNSLLCGGRSPDPGKRRTYY.SL..TNGTNHYKSK.AHQKLLDKVGRTSRSIGTGQRFLHRTLQTLPQGYKRREHQTRK.TKHSTCYCREFPYRSLFSRRTGTYTCT.FRPPKYDSSQSRRYLERFKNGELKVKRKCDRNSNVTGG.YLTRS.LSLY.SRNDTKRPTSVLTF.DISETLRTERILNNDRTLLNSW.ELLSL.GRRETCRPGTETTLRLKRLGSNKSLPSVTLYQESRFR.ESLLRVSLK.NY.VRERNTEIPKQSCQPPKKF.RSRNQLTH.GPACDSTTH.SKGVTQIDYTEDSDEGKYPRP.SLTKFLH.PIVNRQLT..LP.K.VGVEVQSLTKFLH.PIVNRQLT..LP.K.VGVEVQRLCHKIW..PGH.GR.VLRLRLLNKLRSSVSNVTRL.CGAVRSDLLSRSDTEFFFFFFFLLYFCLQSECLRLVQNNI..VSLYCLKTSLKIQKSLNT.CS
KKKKT.VSK.VVFK.PRTFTR.KGW.TL.NHLF.LFKVREESECKITSFCYLTFVLVL.YRI.DSSIYDILICMNVCINMCNSLVVESFEDHTSLVNRPIKRVLRSIPPPYTY.PPSNRMFSLYIFRKEDTPKRVLWRPTKTPTS.KMCTTYTFRRKDTLNRLRGHPDYRPSSEKL.ALFVYRRVRTQKRPLDYSLSL.ISGTP.EV.TY.KPEVP.ERLHGVYTLKGVTRPPIPV.VPS.RDQLSMWDEGSGIPVEPFTKVNTWEGL.IVTDRDEKNSTYPTVFFVEGEVRILAREGPTTNPFDKLTELIIIKVNELIKSFLTRSVEQVEV.EQDKDSFIEPFRPSHRGTNEENTKPVSEQNTLLVTVENSRIGVFSLEGQGRTPAPDSVHLNTTVVSPEDT.RGSKTVN.R.RESVTETVTSPVVSI.RGPDYLFIKVGTTRKDQRRYSLSRIFQKR.GRNVYLITTELYLTRGKNS.VFREEERLVVQEPKQLCDLKD.VLIRAYQV.LYTKNLDFGKNRY.ESL.NETTKSENGTQRSLNKVVNHLRNFDVRGTN.PIRARLVTRLHTDRKV.PK.TTRRIPTRENIPDPSH.LNFCTNLL.TDN.LNDYLRSRSGSRYSH.LNFCTNLL.TDN.LNDYLRSRSGSRYRDYVTRYGSDQDIRVDESSDSVFLTNLGPPSPTSLGSNAVP.GRTCCLALTQSFFFFFFSFYISVCNQSV.D.FKIIFNEYLCTV.KRV.KFKSL.ILNV"""

zscan4_orfs = {}

zscan4_orfs[(True, 1)]=\
((20, 25, 'MSNL.'), (101, 169, 'MELGLDEDSISNSINRQVLSNHVFKSITDMELGLDEDSISNSINRQVLSNHVFKSITDPSPYKREQP.'), (303, 314, 'MAATRKAQQG.'), (339, 356, 'MEIKWQKLGEIHRRPD.'), (529, 531, 'M.'), (545, 547, 'M.'), (548, 554, 'MPQGL.'), (601, 606, 'MQHV.'), (629, 634, 'MSLL.'))
zscan4_orfs[(True, 2)]=\
((17, 21, 'MFL.'), (92, 95, 'MV.'), (106, 174, 'MKIPSVIQSTDKCYPITSLNQSLTWSWGWMKIPSVIQSTDKCYPITSLNQSLIPAPIKGSSLRRHIR.'), (232, 666, 'MALDLRTIFQCEPSENNLGSENSAFQQSQGPAVQREEGISEFSRMVLNSFQDSNNSYARQELQRLYRIFHSWLQPEKHSKDEIISLLVLEQFMIGGHCNDKASVKEKWKSSGKNLERFIEDLTDDSINPPALVHVHMQGQEALFSEDMPLRDVIVHLTKQVNAQTTREANMGTPSQTSQDTSLETGQGYEDEQDGWNSSSKTTRVNENITNQGNQIVSLIIIQEENGPRPEEGGVSSDNPYNSKRAELVTARSQEGSINGITFQGVPMVMGAGCISQPEQSSPESALTHQSNEGNSTCEVHQKGSHGVQKSYKCEECPKVFKYLCHLLAHQRRHRNERPFVCPECQKGFFQISDLRVHQIIHTGKKPFTCSMCKKSFSHKTNLRSHERIHTGEKPYTCPFCKTSYRQSSTYHRHMRTHEKITLPSVPSTPEAS.'), (671, 694, 'MCINMYASMYIPIVFIYLGYKI.'), (708, 710, 'M.'))
zscan4_orfs[(True, 3)]=\
((288, 319, 'MQGRNCKDFIGSFTHGCNQKSTARMKLFLY.'), (330, 336, 'MTKPV.'), (355, 359, 'MTA.'), (383, 393, 'MSLFISQNK.'), (393, 415, 'MPKPQEKQTWGHPPRLPKILP.'), (420, 437, 'MKMNKMAGTVLRKLLE.'), (437, 448, 'MKILLIKAIK.'), (490, 501, 'MESLSKVSLW.'), (523, 560, 'MREIPHVRYIRKDPMESKNHTNVKNAPRSLSISVTY.'), (567, 592, 'MRGHLFVPSVKKASSRYQTYGCIR.'), (617, 647, 'MRESTQEKSLIHVPFVRQATASHPHTTAI.'), (649, 670, 'MRKLPCQVFPPHQKLPKLLV.'), (676, 684, 'MQVCIFL.'), (697, 723, 'MLSIYCLASLKCKAKESMEFVSFVH.'))
zscan4_orfs[(False, 1)]=\
((68, 75, 'MISLYV.'), (221, 227, 'MECTP.'), (316, 324, 'MSSSKAS.'), (530, 544, 'MKLLSQRTEHRDP.'), (612, 628, 'MTTLEVGRGRGTVTN.'), (641, 677, 'MTTLEVGRGRGTEIMSQDMVVTRTLGSMSPPTPSS.'), (690, 703, 'MRCREVGPAVSL.'))
zscan4_orfs[(False, 2)]=\
((28, 37, 'MKSLVLTV.'), (43, 45, 'M.'), (72, 82, 'MYERMYKYV.'), (198, 214, 'MNFWNPVRSVNILKT.'))
zscan4_orfs[(False, 3)]=\
((73, 114, 'MNVCINMCNSLVVESFEDHTSLVNRPIKRVLRSIPPPYTY.'), (119, 146, 'MFSLYIFRKEDTPKRVLWRPTKTPTS.'), (147, 177, 'MCTTYTFRRKDTLNRLRGHPDYRPSSEKL.'), (246, 269, 'MWDEGSGIPVEPFTKVNTWEGL.'))

#=========================================================================
class TestModule( object ):
    student_module = None
    cgrades = 0
    bgrades = 0
    agrades = 0
    total_cgrades = 7
    total_bgrades = 3
    total_agrades = 1
    total_cpoints = 75
    total_bpoints = 12
    total_apoints = 13


    def __init__( self ):
        import os.path
        modulename, _ = os.path.splitext( sys.argv[1] )
        TestModule.student_module = importlib.import_module( modulename )

    @staticmethod
    def getMod():
        return TestModule.student_module

    @staticmethod
    def Report():
        grades = ['A', 'B', 'C']
        rptstr = "tests passed: {}, required: {}, percent {:.02f}. Total points {}, your points {:.01f}"

        total = 0
        for grade in grades[::-1]:
            print "Grade {} tests:".format( grade )
            passed = getattr( TestModule, "{}grades".format( grade.lower() ) )
            required = getattr( TestModule, "total_{}grades".format( grade.lower() ) )
            points = getattr( TestModule, "total_{}points".format( grade.lower() ) )
            fraction = float( passed ) / required
            points_awarded = fraction * points
            print rptstr.format( passed, required, fraction * 100, points, points_awarded )
            total += points_awarded
        print "Your grade: {:0.2f}".format( total )

        

#=========================================================================
class TestHW4DNAFunctionality( unittest.TestCase ):
    """All these test have to pass to get an A"""

    def setUp( self ):
        """Create a properly instantiated RNASequence for C-level tests"""

        self.stumod = TestModule.getMod()
        self.zscan4 = self.stumod.DNASequence.NewFromFastaFile( 'zscan4_dna.fasta' )
        self.errmsg_no_implement = "Tried to use {} on an instance of your class but I got a " +\
                     "TypeError. Either you forgot to implement the special function {}" +\
                     " or something is wrong with your implementation."
        self.errmsg_wrong_output = "Wrong output!!\n\nCalled:\n{}\n\nExpected output:\n{}\n\nYour method returned:\n{}"


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

        TestModule.cgrades += 1

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

        TestModule.cgrades += 1

    #============================================
    def test_repr( self ):
        """Check to see __repr__() was implemented"""
        try:
            self.zscan4.__repr__()
        except NotImplementedError:
            self.fail( "You forgot to implement {}!".format( '__repr__' ) )

        TestModule.cgrades += 1

    #============================================
    def test_in( self ):
        """Check to see "in" operator was implemented and returns correct output"""
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


        TestModule.cgrades += 1

    #============================================
    def test_count( self ):
        """Check to see count() was implemented and returns correct output"""
        try:
            count = self.zscan4.count('GGAA')
        except TypeError:
            self.fail( self.errmsg_no_implement.format( 'count()', 'count()' ) )
        except NotImplementedError:
            self.fail( "You forgot to implement {}!".format( 'count()' ) )

        try:
            self.assertEqual( 14, count )
        except AssertionError:
            self.fail( self.errmsg_wrong_output.format( "zscan4.count('GGAA')", 14, count )  )

        TestModule.cgrades += 1

    #============================================
    def test_IsValidSequence( self ):
        """Check to see IsValidSequence() was implemented and returns correct output"""
        try:
            isvalid = self.zscan4.IsValidSequence()
        except TypeError:
            self.fail( self.errmsg_no_implement.format( 'IsValidSequence()', 'IsValidSequence()' ) )
        except NotImplementedError:
            self.fail( "You forgot to implement {}!".format( 'IsValidSequence()' ) )

        try:
            self.assertEqual( isvalid, True )
        except AssertionError:
            self.fail( self.errmsg_wrong_output.format( "zscan4.IsValidSequence()", True, isvalid )  )

        TestModule.cgrades += 1

    #============================================
    def test_GCContent( self ):
        """Check to see GCContent() was implemented and returns correct output"""
        try:
            val = self.zscan4.GCContent()
        except TypeError:
            self.fail( self.errmsg_no_implement.format( 'GCContent()', 'GCContent()' ) )
        except NotImplementedError:
            self.fail( "You forgot to implement {}!".format( 'GCContent()' ) )

        try:
            self.assertAlmostEqual( val, 0.4137168 )
        except AssertionError:
            self.fail( self.errmsg_wrong_output.format( "zscan4.GCContent()", 0.4137168, val )  )


        TestModule.cgrades += 1
    # The B grade tests


    #============================================
    def test_NewFromFastaFila( self ):
        """Check to see IsValidSequence() was implemented and returns correct output"""
        try:
            zscan4 = self.stumod.DNASequence.NewFromFastaFile( 'zscan4_dna.fasta' )
        except TypeError:
            self.fail( self.errmsg_no_implement.format( 'NewFromFastaFile()', 'NewFromFastaFile()' ) )
        except NotImplementedError:
            self.fail( "You forgot to implement {}!".format( 'NewFromFastaFile()' ) )


        TestModule.bgrades += 1

    #============================================
    def test_TranslateToAA( self ):
        """Check to see TranslateToAA() was implemented and returns correct output"""

        reading_frames = ( (True, 1), (True, 2), (True, 3), (False, 1), (False, 2), (False, 3) )
        data = zip( reading_frames, zscan4_translated_aa.splitlines() )

        direction = None
        reading_frame = None
        try:
            for (direction, reading_frame), correct_aa in data:
                aa_chain = self.zscan4.TranslateToAA( direction, reading_frame )
                self.assertItemsEqual( aa_chain, correct_aa )
                self.assertEqual( aa_chain, correct_aa )
        except AssertionError as e:
            errmsg = "ERROR occurred when calling TranslateToAA() in the {} direction, reading frame {}:\n".format( "5'to3'" if direction else "3'to5'", reading_frame )
            import sys
            raise type(e), type(e)(errmsg + e.message), sys.exc_info()[2]


        TestModule.bgrades += 1
    # The A grade tests

    #============================================
    def test_OpenReadingFrames( self ):
        """Check to see OpenReadingFrames() was implemented and returns correct output"""
        reading_frames = ( (True, 1), (True, 2), (True, 3), (False, 1), (False, 2), (False, 3) )

        rf = None
        try:
            for rf in reading_frames:
                direction, reading_frame = rf
                val = self.zscan4.OpenReadingFrames( direction, reading_frame )
                self.assertTupleEqual( val, zscan4_orfs[rf] )
        except AssertionError as e:
            errmsg = "ERROR occurred when calling TranslateToAA() in the {} direction, reading frame {}:\n".format( "5'to3'" if direction else "3'to5'", reading_frame )
            import sys
            raise type(e), type(e)(errmsg + e.message), sys.exc_info()[2]


        TestModule.agrades += 1

#=========================================================================
class TestHW4DNADummyproofing( unittest.TestCase ):
    """All these test have to pass to get an A"""

    def setUp( self ):
        self.stumod = TestModule.getMod()
 
    #============================================
    def test_IsValidSequence_invalid( self ):
        """Check to see IsValidSequence() was implemented and returns correct output"""
        try: 
            self.assertRaises( ValueError, self.stumod.DNASequence.NewFromFastaFile, 
                'zscan4_dna_invalid_nt.fasta')
        except AssertionError:
                self.fail( "Your NewFromFastaFile did not raise a ValueError when importing "+\
                    'zscan4_dna_invalid_nt.fasta')


        TestModule.bgrades += 1


if __name__ == '__main__':


    module = TestModule()

    print "******************BIOF 309 HW4 TEST PROGRAM, version 1.0 *******************"

    del sys.argv[1:]
    try:
        unittest.main(verbosity=3)
    finally:
        module.Report()

