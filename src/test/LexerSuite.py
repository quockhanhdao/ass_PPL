import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test0(self):
        testcase = '''1._2'''
        expect = '''1,.,_2,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 100))

    def test1(self):
        testcase = '''// This is a comment!!!'''
        expect = '''<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 101))

    def test2(self):
        testcase = '''"this is a string"'''
        expect = '''this is a string,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 102))

    def test3(self):
        testcase = '''"Escaped characters: \\\\ \\b \\f \\r \\n \\t \\' \\""'''
        expect = '''Escaped characters: \\\\ \\b \\f \\r \\n \\t \\' \\",<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 103))

    def test4(self):
        testcase = '''"A string with a double quote (\\") in it"'''
        expect = '''A string with a double quote (\\") in it,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 104))

    def test5(self):
        testcase = '''"A string with an endline \\n in it"'''
        expect = '''A string with an endline \\n in it,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 105))

    def test6(self):
        testcase = '''"Wrong string'''
        expect = '''Unclosed String: Wrong string'''
        self.assertTrue(TestLexer.test(testcase, expect, 106))

    def test7(self):
        testcase = '''mt22k20'''
        expect = '''mt22k20,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 107))

    def test8(self):
        testcase = '''"\\ "'''
        expect = '''Illegal Escape In String: \\ '''
        self.assertTrue(TestLexer.test(testcase, expect, 108))

    def test9(self):
        testcase = '''"String with an endline at the end\\n"'''
        expect = '''String with an endline at the end\\n,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 109))

    def test10(self):
        testcase = '''{1, 2, 3}'''
        expect = '''{,1,,,2,,,3,},<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 110))

    def test11(self):
        testcase = '''{1, 2, 3, 4, 5, 6, 7}'''
        expect = '''{,1,,,2,,,3,,,4,,,5,,,6,,,7,},<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 111))

    def test12(self):
        testcase = '''{"hello", "world"}'''
        expect = '''{,hello,,,world,},<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 112))

    def test13(self):
        testcase = '''"String with escape characters \\n \\t \\r \\b \\f \\a \\" "'''
        expect = '''Illegal Escape In String: String with escape characters \\n \\t \\r \\b \\f \\a'''
        self.assertTrue(TestLexer.test(testcase, expect, 113))

    def test14(self):
        testcase = '''{true, false, true, false}'''
        expect = '''{,true,,,false,,,true,,,false,},<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 114))

    def test15(self):
        testcase = '''{1.45, 2.1589, 12.8_9}'''
        expect = '''{,1.45,,,2.1589,,,12.89,},<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 115))

    def test16(self):
        testcase = '''{33, "pi", true, 3.14}'''
        expect = '''{,33,,,pi,,,true,,,3.14,},<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 116))

    def test17(self):
        testcase = '''GHIJKML8T'''
        expect = '''GHIJKML8T,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 117))

    def test18(self):
        testcase = '''"String unclosed'''
        expect = '''Unclosed String: String unclosed'''
        self.assertTrue(TestLexer.test(testcase, expect, 118))

    def test19(self):
        testcase = '''"int: %d\\n"'''
        expect = '''int: %d\\n,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 119))

    def test20(self):
        testcase = '''21312 3124 _234'''
        expect = '''21312,3124,_234,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 120))

    def test21(self):
        testcase = '''109.2002'''
        expect = '''109.2002,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 121))

    def test22(self):
        testcase = '''23e4'''
        expect = '''23e4,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 122))

    def test23(self):
        testcase = '''213.123.213'''
        expect = '''213.123,.,213,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 123))

    def test24(self):
        testcase = '''213.123e213'''
        expect = '''213.123e213,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 124))

    def test25(self):
        testcase = ''''''
        expect = '''<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 125))

    def test26(self):
        testcase = '''JK__3493k__lkdsfj'''
        expect = '''JK__3493k__lkdsfj,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 126))

    def test27(self):
        testcase = '''{1, 5, 7, 12} or {"Kangxi", "Yongzheng", "Qianlong"}.'''
        expect = '''{,1,,,5,,,7,,,12,},or,{,Kangxi,,,Yongzheng,,,Qianlong,},.,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 127))

    def test28(self):
        testcase = '''! && || == !='''
        expect = '''!,&&,||,==,!=,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 128))

    def test29(self):
        testcase = '''+ - * / %'''
        expect = '''+,-,*,/,%,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 129))

    def test30(self):
        testcase = '''== != > >= < <='''
        expect = '''==,!=,>,>=,<,<=,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 130))

    def test31(self):
        testcase = '''::'''
        expect = '''::,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 131))

    def test32(self):
        testcase = '''a[0, 0], a[0, 1], a[0, 2], a[1, 0], a[1, 1], a[1, 2]'''
        expect = '''a,[,0,,,0,],,,a,[,0,,,1,],,,a,[,0,,,2,],,,a,[,1,,,0,],,,a,[,1,,,1,],,,a,[,1,,,2,],<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 132))

    def test33(self):
        testcase = '''i : integer; a : array[1, 2] of integer;'''
        expect = '''i,:,integer,;,a,:,array,[,1,,,2,],of,integer,;,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 133))

    def test34(self):
        testcase = '''Test identify'''
        expect = '''Test,identify,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 134))
        
    def test35(self):
        testcase = '''/* Greedy or Non Greedy */ */'''
        expect = '''*,/,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 135))

    def test36(self):
        testcase = '''/*/**/greedy*/'''
        expect = '''greedy,*,/,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 136))

    def test37(self):
        testcase = '''6pNcLx1t_'''
        expect = '''6,pNcLx1t_,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 137))

    def test38(self):
        testcase = '''mN_5dYzF'''
        expect = '''mN_5dYzF,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 138))

    def test39(self):
        testcase = '''H6_7kL3yU'''
        expect = '''H6_7kL3yU,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 139))

    def test40(self):
        testcase = '''3CzjK9_1'''
        expect = '''3,CzjK9_1,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 140))

    def test41(self):
        testcase = '''_5S9vGKj'''
        expect = '''_5S9vGKj,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 141))

    def test42(self):
        testcase = '''Wxv_4tRm'''
        expect = '''Wxv_4tRm,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 142))

    def test43(self):
        testcase = '''eBpR7vYf'''
        expect = '''eBpR7vYf,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 143))

    def test44(self):
        testcase = '''whoami'''
        expect = '''whoami,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 144))

    def test45(self):
        testcase = '''333kk333k3k'''
        expect = '''333,kk333k3k,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 145))

    def test46(self):
        testcase = '''identify'''
        expect = '''identify,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 146))

    def test47(self):
        testcase = '''dKt8_7sA'''
        expect = '''dKt8_7sA,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 147))

    def test48(self):
        testcase = '''$k32j3'''
        expect = '''Error Token $'''
        self.assertTrue(TestLexer.test(testcase, expect, 148))

    def test49(self):
        testcase = '''Who am I'''
        expect = '''Who,am,I,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 149))

    def test50(self):
        testcase = '''+=+-=='''
        expect = '''+,=,+,-,==,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 150))

    def test51(self):
        testcase = '''== = = ====='''
        expect = '''==,=,=,==,==,=,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 151))

    def test52(self):
        testcase = '''-=-=----*&&&&'''
        expect = '''-,=,-,=,-,-,-,-,*,&&,&&,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 152))

    def test53(self):
        testcase = '''[] () }{{{}}}}}}'''
        expect = '''[,],(,),},{,{,{,},},},},},},<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 153))

    def test54(self):
        testcase = '''!= >= <= ?'''
        expect = '''!=,>=,<=,Error Token ?'''
        self.assertTrue(TestLexer.test(testcase, expect, 154))

    def test55(self):
        testcase = '''Test literals'''
        expect = '''Test,literals,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 155))

    def test56(self):
        testcase = '''integer'''
        expect = '''integer,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 156))

    def test57(self):
        testcase = '''0'''
        expect = '''0,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 157))

    def test58(self):
        testcase = '''HI'''
        expect = '''HI,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 158))

    def test59(self):
        testcase = '''3QbFmC_2'''
        expect = '''3,QbFmC_2,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 159))

    def test60(self):
        testcase = '''1'''
        expect = '''1,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 160))

    def test61(self):
        testcase = '''6EQJ5'''
        expect = '''6,EQJ5,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 161))

    def test62(self):
        testcase = '''30_04_1975'''
        expect = '''30041975,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 162))

    def test63(self):
        testcase = '''22_06'''
        expect = '''2206,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 163))

    def test64(self):
        testcase = '''0_0_0'''
        expect = '''0,_0_0,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 164))

    def test65(self):
        testcase = '''1_000_000'''
        expect = '''1000000,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 165))

    def test66(self):
        testcase = '''-42'''
        expect = '''-,42,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 166))

    def test67(self):
        testcase = '''-1_000'''
        expect = '''-,1000,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 167))

    def test68(self):
        testcase = '''-123_456_789'''
        expect = '''-,123456789,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 168))

    def test69(self):
        testcase = '''01'''
        expect = '''0,1,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 169))

    def test70(self):
        testcase = '''_'''
        expect = '''_,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 170))

    def test71(self):
        testcase = '''2k2'''
        expect = '''2,k2,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 171))

    def test72(self):
        testcase = '''1_2_3'''
        expect = '''123,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 172))

    def test73(self):
        testcase = '''1__2__3'''
        expect = '''123,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 173))

    def test74(self):
        testcase = '''123_'''
        expect = '''123,_,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 174))

    def test75(self):
        testcase = ''' --------- float'''
        expect = '''-,-,-,-,-,-,-,-,-,float,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 175))

    def test76(self):
        testcase = '''0.0'''
        expect = '''0.0,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 176))

    def test77(self):
        testcase = '''2.71828'''
        expect = '''2.71828,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 177))

    def test78(self):
        testcase = '''0.30103'''
        expect = '''0.30103,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 178))

    def test79(self):
        testcase = '''1.23e5'''
        expect = '''1.23e5,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 179))

    def test80(self):
        testcase = '''6.789e-2'''
        expect = '''6.789e-2,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 180))

    def test81(self):
        testcase = '''2'''
        expect = '''2,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 181))

    def test82(self):
        testcase = '''0.123_456'''
        expect = '''0.123456,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 182))

    def test83(self):
        testcase = '''9_8.76_5e4'''
        expect = '''98.765e4,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 183))

    def test84(self):
        testcase = '''1_000.0'''
        expect = '''1000.0,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 184))

    def test85(self):
        testcase = '''-1.23'''
        expect = '''-,1.23,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 185))

    def test86(self):
        testcase = '''1.23E10_'''
        expect = '''1.23E10,_,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 186))

    def test87(self):
        testcase = '''1_2.3'''
        expect = '''12.3,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 187))

    def test88(self):
        testcase = '''1.23E-10'''
        expect = '''1.23E-10,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 188))

    def test89(self):
        testcase = '''9_8.76_5e4'''
        expect = '''98.765e4,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 189))

    def test90(self):
        testcase = '''-1.23e-10'''
        expect = '''-,1.23e-10,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 190))

    def test91(self):
        testcase = '''123.456e7'''
        expect = '''123.456e7,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 191))

    def test92(self):
        testcase = '''_dk'''
        expect = '''_dk,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 192))

    def test93(self):
        testcase = '''123.456E-7'''
        expect = '''123.456E-7,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 193))

    def test94(self):
        testcase = '''.'''
        expect = '''.,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 194))

    def test95(self):
        testcase = '''df)2_$'''
        expect = '''df,),2,_,Error Token $'''
        self.assertTrue(TestLexer.test(testcase, expect, 195))

    def test96(self):
        testcase = '''1.'''
        expect = '''1,.,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 196))

    def test97(self):
        testcase = '''1e'''
        expect = '''1,e,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 197))

    def test98(self):
        testcase = '''1.e10'''
        expect = '''1,.,e10,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 198))

    def test99(self):
        testcase = '''1.23e-'''
        expect = '''1.23,e,-,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 199))