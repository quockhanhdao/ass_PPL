# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u0250\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\5\f\u010b\n")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3#\3#")
        buf.write("\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3+\3+")
        buf.write("\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3<\7<\u01c6")
        buf.write("\n<\f<\16<\u01c9\13<\3<\3<\5<\u01cd\n<\3=\3=\3=\5=\u01d2")
        buf.write("\n=\3=\5=\u01d5\n=\3=\3=\3>\3>\3>\7>\u01dc\n>\f>\16>\u01df")
        buf.write("\13>\3>\5>\u01e2\n>\3?\3?\3?\3?\7?\u01e8\n?\f?\16?\u01eb")
        buf.write("\13?\3?\5?\u01ee\n?\3@\3@\5@\u01f2\n@\3@\3@\3@\7@\u01f7")
        buf.write("\n@\f@\16@\u01fa\13@\3@\5@\u01fd\n@\3A\3A\5A\u0201\nA")
        buf.write("\3A\3A\3A\3B\3B\6B\u0208\nB\rB\16B\u0209\3C\3C\3C\3D\3")
        buf.write("D\7D\u0211\nD\fD\16D\u0214\13D\3E\6E\u0217\nE\rE\16E\u0218")
        buf.write("\3E\3E\3F\3F\3F\3F\7F\u0221\nF\fF\16F\u0224\13F\3F\3F")
        buf.write("\3G\3G\3G\3G\7G\u022c\nG\fG\16G\u022f\13G\3G\3G\3G\3G")
        buf.write("\3G\3H\3H\3H\3I\3I\7I\u023b\nI\fI\16I\u023e\13I\3I\5I")
        buf.write("\u0241\nI\3I\3I\3J\3J\7J\u0247\nJ\fJ\16J\u024a\13J\3J")
        buf.write("\3J\3J\3J\3J\3\u022d\2K\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q:s;u<w=y>{\2}\2\177\2\u0081?\u0083")
        buf.write("\2\u0085\2\u0087@\u0089A\u008bB\u008dC\u008fD\u0091E\u0093")
        buf.write("F\3\2\16\3\2\62;\3\2\63;\4\2\62;aa\4\2GGgg\4\2--//\6\2")
        buf.write("\n\f\16\17$$^^\n\2$$))^^ddhhppttvv\5\2C\\aac|\6\2\62;")
        buf.write("C\\aac|\5\2\n\f\16\17\"\"\4\2\f\f\17\17\t\2$$^^ddhhpp")
        buf.write("ttvv\2\u0260\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2\u0081\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3")
        buf.write("\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2")
        buf.write("\2\u0091\3\2\2\2\2\u0093\3\2\2\2\3\u0095\3\2\2\2\5\u00a1")
        buf.write("\3\2\2\2\7\u00ae\3\2\2\2\t\u00b8\3\2\2\2\13\u00c3\3\2")
        buf.write("\2\2\r\u00cf\3\2\2\2\17\u00dc\3\2\2\2\21\u00e7\3\2\2\2")
        buf.write("\23\u00f3\3\2\2\2\25\u00f9\3\2\2\2\27\u010a\3\2\2\2\31")
        buf.write("\u010c\3\2\2\2\33\u0111\3\2\2\2\35\u0117\3\2\2\2\37\u011f")
        buf.write("\3\2\2\2!\u0124\3\2\2\2#\u012a\3\2\2\2%\u0130\3\2\2\2")
        buf.write("\'\u0136\3\2\2\2)\u013d\3\2\2\2+\u0141\3\2\2\2-\u0149")
        buf.write("\3\2\2\2/\u014d\3\2\2\2\61\u0154\3\2\2\2\63\u015d\3\2")
        buf.write("\2\2\65\u0160\3\2\2\2\67\u0169\3\2\2\29\u016e\3\2\2\2")
        buf.write(";\u0171\3\2\2\2=\u0176\3\2\2\2?\u0179\3\2\2\2A\u017f\3")
        buf.write("\2\2\2C\u0187\3\2\2\2E\u0189\3\2\2\2G\u018b\3\2\2\2I\u018d")
        buf.write("\3\2\2\2K\u018f\3\2\2\2M\u0191\3\2\2\2O\u0193\3\2\2\2")
        buf.write("Q\u0195\3\2\2\2S\u0198\3\2\2\2U\u019a\3\2\2\2W\u019d\3")
        buf.write("\2\2\2Y\u01a0\3\2\2\2[\u01a3\3\2\2\2]\u01a6\3\2\2\2_\u01a9")
        buf.write("\3\2\2\2a\u01ac\3\2\2\2c\u01ae\3\2\2\2e\u01b0\3\2\2\2")
        buf.write("g\u01b2\3\2\2\2i\u01b4\3\2\2\2k\u01b6\3\2\2\2m\u01b8\3")
        buf.write("\2\2\2o\u01ba\3\2\2\2q\u01bc\3\2\2\2s\u01be\3\2\2\2u\u01c0")
        buf.write("\3\2\2\2w\u01cc\3\2\2\2y\u01ce\3\2\2\2{\u01e1\3\2\2\2")
        buf.write("}\u01e3\3\2\2\2\177\u01ef\3\2\2\2\u0081\u01fe\3\2\2\2")
        buf.write("\u0083\u0207\3\2\2\2\u0085\u020b\3\2\2\2\u0087\u020e\3")
        buf.write("\2\2\2\u0089\u0216\3\2\2\2\u008b\u021c\3\2\2\2\u008d\u0227")
        buf.write("\3\2\2\2\u008f\u0235\3\2\2\2\u0091\u0238\3\2\2\2\u0093")
        buf.write("\u0244\3\2\2\2\u0095\u0096\7t\2\2\u0096\u0097\7g\2\2\u0097")
        buf.write("\u0098\7c\2\2\u0098\u0099\7f\2\2\u0099\u009a\7K\2\2\u009a")
        buf.write("\u009b\7p\2\2\u009b\u009c\7v\2\2\u009c\u009d\7g\2\2\u009d")
        buf.write("\u009e\7i\2\2\u009e\u009f\7g\2\2\u009f\u00a0\7t\2\2\u00a0")
        buf.write("\4\3\2\2\2\u00a1\u00a2\7r\2\2\u00a2\u00a3\7t\2\2\u00a3")
        buf.write("\u00a4\7k\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6\7v\2\2\u00a6")
        buf.write("\u00a7\7K\2\2\u00a7\u00a8\7p\2\2\u00a8\u00a9\7v\2\2\u00a9")
        buf.write("\u00aa\7g\2\2\u00aa\u00ab\7i\2\2\u00ab\u00ac\7g\2\2\u00ac")
        buf.write("\u00ad\7t\2\2\u00ad\6\3\2\2\2\u00ae\u00af\7t\2\2\u00af")
        buf.write("\u00b0\7g\2\2\u00b0\u00b1\7c\2\2\u00b1\u00b2\7f\2\2\u00b2")
        buf.write("\u00b3\7H\2\2\u00b3\u00b4\7n\2\2\u00b4\u00b5\7q\2\2\u00b5")
        buf.write("\u00b6\7c\2\2\u00b6\u00b7\7v\2\2\u00b7\b\3\2\2\2\u00b8")
        buf.write("\u00b9\7y\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb\7k\2\2\u00bb")
        buf.write("\u00bc\7v\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be\7H\2\2\u00be")
        buf.write("\u00bf\7n\2\2\u00bf\u00c0\7q\2\2\u00c0\u00c1\7c\2\2\u00c1")
        buf.write("\u00c2\7v\2\2\u00c2\n\3\2\2\2\u00c3\u00c4\7t\2\2\u00c4")
        buf.write("\u00c5\7g\2\2\u00c5\u00c6\7c\2\2\u00c6\u00c7\7f\2\2\u00c7")
        buf.write("\u00c8\7D\2\2\u00c8\u00c9\7q\2\2\u00c9\u00ca\7q\2\2\u00ca")
        buf.write("\u00cb\7n\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd\7c\2\2\u00cd")
        buf.write("\u00ce\7p\2\2\u00ce\f\3\2\2\2\u00cf\u00d0\7r\2\2\u00d0")
        buf.write("\u00d1\7t\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3\7p\2\2\u00d3")
        buf.write("\u00d4\7v\2\2\u00d4\u00d5\7D\2\2\u00d5\u00d6\7q\2\2\u00d6")
        buf.write("\u00d7\7q\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9\7g\2\2\u00d9")
        buf.write("\u00da\7c\2\2\u00da\u00db\7p\2\2\u00db\16\3\2\2\2\u00dc")
        buf.write("\u00dd\7t\2\2\u00dd\u00de\7g\2\2\u00de\u00df\7c\2\2\u00df")
        buf.write("\u00e0\7f\2\2\u00e0\u00e1\7U\2\2\u00e1\u00e2\7v\2\2\u00e2")
        buf.write("\u00e3\7t\2\2\u00e3\u00e4\7k\2\2\u00e4\u00e5\7p\2\2\u00e5")
        buf.write("\u00e6\7i\2\2\u00e6\20\3\2\2\2\u00e7\u00e8\7r\2\2\u00e8")
        buf.write("\u00e9\7t\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb\7p\2\2\u00eb")
        buf.write("\u00ec\7v\2\2\u00ec\u00ed\7U\2\2\u00ed\u00ee\7v\2\2\u00ee")
        buf.write("\u00ef\7t\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1\7p\2\2\u00f1")
        buf.write("\u00f2\7i\2\2\u00f2\22\3\2\2\2\u00f3\u00f4\7u\2\2\u00f4")
        buf.write("\u00f5\7w\2\2\u00f5\u00f6\7r\2\2\u00f6\u00f7\7g\2\2\u00f7")
        buf.write("\u00f8\7t\2\2\u00f8\24\3\2\2\2\u00f9\u00fa\7r\2\2\u00fa")
        buf.write("\u00fb\7t\2\2\u00fb\u00fc\7g\2\2\u00fc\u00fd\7x\2\2\u00fd")
        buf.write("\u00fe\7g\2\2\u00fe\u00ff\7p\2\2\u00ff\u0100\7v\2\2\u0100")
        buf.write("\u0101\7F\2\2\u0101\u0102\7g\2\2\u0102\u0103\7h\2\2\u0103")
        buf.write("\u0104\7c\2\2\u0104\u0105\7w\2\2\u0105\u0106\7n\2\2\u0106")
        buf.write("\u0107\7v\2\2\u0107\26\3\2\2\2\u0108\u010b\5\67\34\2\u0109")
        buf.write("\u010b\5\33\16\2\u010a\u0108\3\2\2\2\u010a\u0109\3\2\2")
        buf.write("\2\u010b\30\3\2\2\2\u010c\u010d\7c\2\2\u010d\u010e\7w")
        buf.write("\2\2\u010e\u010f\7v\2\2\u010f\u0110\7q\2\2\u0110\32\3")
        buf.write("\2\2\2\u0111\u0112\7h\2\2\u0112\u0113\7c\2\2\u0113\u0114")
        buf.write("\7n\2\2\u0114\u0115\7u\2\2\u0115\u0116\7g\2\2\u0116\34")
        buf.write("\3\2\2\2\u0117\u0118\7k\2\2\u0118\u0119\7p\2\2\u0119\u011a")
        buf.write("\7v\2\2\u011a\u011b\7g\2\2\u011b\u011c\7i\2\2\u011c\u011d")
        buf.write("\7g\2\2\u011d\u011e\7t\2\2\u011e\36\3\2\2\2\u011f\u0120")
        buf.write("\7x\2\2\u0120\u0121\7q\2\2\u0121\u0122\7k\2\2\u0122\u0123")
        buf.write("\7f\2\2\u0123 \3\2\2\2\u0124\u0125\7c\2\2\u0125\u0126")
        buf.write("\7t\2\2\u0126\u0127\7t\2\2\u0127\u0128\7c\2\2\u0128\u0129")
        buf.write("\7{\2\2\u0129\"\3\2\2\2\u012a\u012b\7d\2\2\u012b\u012c")
        buf.write("\7t\2\2\u012c\u012d\7g\2\2\u012d\u012e\7c\2\2\u012e\u012f")
        buf.write("\7m\2\2\u012f$\3\2\2\2\u0130\u0131\7h\2\2\u0131\u0132")
        buf.write("\7n\2\2\u0132\u0133\7q\2\2\u0133\u0134\7c\2\2\u0134\u0135")
        buf.write("\7v\2\2\u0135&\3\2\2\2\u0136\u0137\7t\2\2\u0137\u0138")
        buf.write("\7g\2\2\u0138\u0139\7v\2\2\u0139\u013a\7w\2\2\u013a\u013b")
        buf.write("\7t\2\2\u013b\u013c\7p\2\2\u013c(\3\2\2\2\u013d\u013e")
        buf.write("\7q\2\2\u013e\u013f\7w\2\2\u013f\u0140\7v\2\2\u0140*\3")
        buf.write("\2\2\2\u0141\u0142\7d\2\2\u0142\u0143\7q\2\2\u0143\u0144")
        buf.write("\7q\2\2\u0144\u0145\7n\2\2\u0145\u0146\7g\2\2\u0146\u0147")
        buf.write("\7c\2\2\u0147\u0148\7p\2\2\u0148,\3\2\2\2\u0149\u014a")
        buf.write("\7h\2\2\u014a\u014b\7q\2\2\u014b\u014c\7t\2\2\u014c.\3")
        buf.write("\2\2\2\u014d\u014e\7u\2\2\u014e\u014f\7v\2\2\u014f\u0150")
        buf.write("\7t\2\2\u0150\u0151\7k\2\2\u0151\u0152\7p\2\2\u0152\u0153")
        buf.write("\7i\2\2\u0153\60\3\2\2\2\u0154\u0155\7e\2\2\u0155\u0156")
        buf.write("\7q\2\2\u0156\u0157\7p\2\2\u0157\u0158\7v\2\2\u0158\u0159")
        buf.write("\7k\2\2\u0159\u015a\7p\2\2\u015a\u015b\7w\2\2\u015b\u015c")
        buf.write("\7g\2\2\u015c\62\3\2\2\2\u015d\u015e\7f\2\2\u015e\u015f")
        buf.write("\7q\2\2\u015f\64\3\2\2\2\u0160\u0161\7h\2\2\u0161\u0162")
        buf.write("\7w\2\2\u0162\u0163\7p\2\2\u0163\u0164\7e\2\2\u0164\u0165")
        buf.write("\7v\2\2\u0165\u0166\7k\2\2\u0166\u0167\7q\2\2\u0167\u0168")
        buf.write("\7p\2\2\u0168\66\3\2\2\2\u0169\u016a\7v\2\2\u016a\u016b")
        buf.write("\7t\2\2\u016b\u016c\7w\2\2\u016c\u016d\7g\2\2\u016d8\3")
        buf.write("\2\2\2\u016e\u016f\7q\2\2\u016f\u0170\7h\2\2\u0170:\3")
        buf.write("\2\2\2\u0171\u0172\7g\2\2\u0172\u0173\7n\2\2\u0173\u0174")
        buf.write("\7u\2\2\u0174\u0175\7g\2\2\u0175<\3\2\2\2\u0176\u0177")
        buf.write("\7k\2\2\u0177\u0178\7h\2\2\u0178>\3\2\2\2\u0179\u017a")
        buf.write("\7y\2\2\u017a\u017b\7j\2\2\u017b\u017c\7k\2\2\u017c\u017d")
        buf.write("\7n\2\2\u017d\u017e\7g\2\2\u017e@\3\2\2\2\u017f\u0180")
        buf.write("\7k\2\2\u0180\u0181\7p\2\2\u0181\u0182\7j\2\2\u0182\u0183")
        buf.write("\7g\2\2\u0183\u0184\7t\2\2\u0184\u0185\7k\2\2\u0185\u0186")
        buf.write("\7v\2\2\u0186B\3\2\2\2\u0187\u0188\7-\2\2\u0188D\3\2\2")
        buf.write("\2\u0189\u018a\7/\2\2\u018aF\3\2\2\2\u018b\u018c\7,\2")
        buf.write("\2\u018cH\3\2\2\2\u018d\u018e\7\61\2\2\u018eJ\3\2\2\2")
        buf.write("\u018f\u0190\7\'\2\2\u0190L\3\2\2\2\u0191\u0192\7#\2\2")
        buf.write("\u0192N\3\2\2\2\u0193\u0194\7>\2\2\u0194P\3\2\2\2\u0195")
        buf.write("\u0196\7>\2\2\u0196\u0197\7?\2\2\u0197R\3\2\2\2\u0198")
        buf.write("\u0199\7@\2\2\u0199T\3\2\2\2\u019a\u019b\7@\2\2\u019b")
        buf.write("\u019c\7?\2\2\u019cV\3\2\2\2\u019d\u019e\7?\2\2\u019e")
        buf.write("\u019f\7?\2\2\u019fX\3\2\2\2\u01a0\u01a1\7#\2\2\u01a1")
        buf.write("\u01a2\7?\2\2\u01a2Z\3\2\2\2\u01a3\u01a4\7<\2\2\u01a4")
        buf.write("\u01a5\7<\2\2\u01a5\\\3\2\2\2\u01a6\u01a7\7(\2\2\u01a7")
        buf.write("\u01a8\7(\2\2\u01a8^\3\2\2\2\u01a9\u01aa\7~\2\2\u01aa")
        buf.write("\u01ab\7~\2\2\u01ab`\3\2\2\2\u01ac\u01ad\7?\2\2\u01ad")
        buf.write("b\3\2\2\2\u01ae\u01af\7*\2\2\u01afd\3\2\2\2\u01b0\u01b1")
        buf.write("\7+\2\2\u01b1f\3\2\2\2\u01b2\u01b3\7]\2\2\u01b3h\3\2\2")
        buf.write("\2\u01b4\u01b5\7_\2\2\u01b5j\3\2\2\2\u01b6\u01b7\7}\2")
        buf.write("\2\u01b7l\3\2\2\2\u01b8\u01b9\7\177\2\2\u01b9n\3\2\2\2")
        buf.write("\u01ba\u01bb\7\60\2\2\u01bbp\3\2\2\2\u01bc\u01bd\7.\2")
        buf.write("\2\u01bdr\3\2\2\2\u01be\u01bf\7=\2\2\u01bft\3\2\2\2\u01c0")
        buf.write("\u01c1\7<\2\2\u01c1v\3\2\2\2\u01c2\u01cd\t\2\2\2\u01c3")
        buf.write("\u01c7\t\3\2\2\u01c4\u01c6\t\4\2\2\u01c5\u01c4\3\2\2\2")
        buf.write("\u01c6\u01c9\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c8\3")
        buf.write("\2\2\2\u01c8\u01ca\3\2\2\2\u01c9\u01c7\3\2\2\2\u01ca\u01cb")
        buf.write("\t\2\2\2\u01cb\u01cd\b<\2\2\u01cc\u01c2\3\2\2\2\u01cc")
        buf.write("\u01c3\3\2\2\2\u01cdx\3\2\2\2\u01ce\u01d4\5{>\2\u01cf")
        buf.write("\u01d5\5}?\2\u01d0\u01d2\5}?\2\u01d1\u01d0\3\2\2\2\u01d1")
        buf.write("\u01d2\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u01d5\5\177@")
        buf.write("\2\u01d4\u01cf\3\2\2\2\u01d4\u01d1\3\2\2\2\u01d5\u01d6")
        buf.write("\3\2\2\2\u01d6\u01d7\b=\3\2\u01d7z\3\2\2\2\u01d8\u01e2")
        buf.write("\t\2\2\2\u01d9\u01dd\t\3\2\2\u01da\u01dc\t\4\2\2\u01db")
        buf.write("\u01da\3\2\2\2\u01dc\u01df\3\2\2\2\u01dd\u01db\3\2\2\2")
        buf.write("\u01dd\u01de\3\2\2\2\u01de\u01e0\3\2\2\2\u01df\u01dd\3")
        buf.write("\2\2\2\u01e0\u01e2\t\2\2\2\u01e1\u01d8\3\2\2\2\u01e1\u01d9")
        buf.write("\3\2\2\2\u01e2|\3\2\2\2\u01e3\u01ed\7\60\2\2\u01e4\u01ee")
        buf.write("\t\2\2\2\u01e5\u01e9\t\2\2\2\u01e6\u01e8\t\4\2\2\u01e7")
        buf.write("\u01e6\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9\u01e7\3\2\2\2")
        buf.write("\u01e9\u01ea\3\2\2\2\u01ea\u01ec\3\2\2\2\u01eb\u01e9\3")
        buf.write("\2\2\2\u01ec\u01ee\t\2\2\2\u01ed\u01e4\3\2\2\2\u01ed\u01e5")
        buf.write("\3\2\2\2\u01ee~\3\2\2\2\u01ef\u01f1\t\5\2\2\u01f0\u01f2")
        buf.write("\t\6\2\2\u01f1\u01f0\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2")
        buf.write("\u01fc\3\2\2\2\u01f3\u01fd\t\2\2\2\u01f4\u01f8\t\2\2\2")
        buf.write("\u01f5\u01f7\t\4\2\2\u01f6\u01f5\3\2\2\2\u01f7\u01fa\3")
        buf.write("\2\2\2\u01f8\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fb")
        buf.write("\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fb\u01fd\t\2\2\2\u01fc")
        buf.write("\u01f3\3\2\2\2\u01fc\u01f4\3\2\2\2\u01fd\u0080\3\2\2\2")
        buf.write("\u01fe\u0200\7$\2\2\u01ff\u0201\5\u0083B\2\u0200\u01ff")
        buf.write("\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u0202\3\2\2\2\u0202")
        buf.write("\u0203\7$\2\2\u0203\u0204\bA\4\2\u0204\u0082\3\2\2\2\u0205")
        buf.write("\u0208\n\7\2\2\u0206\u0208\5\u0085C\2\u0207\u0205\3\2")
        buf.write("\2\2\u0207\u0206\3\2\2\2\u0208\u0209\3\2\2\2\u0209\u0207")
        buf.write("\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u0084\3\2\2\2\u020b")
        buf.write("\u020c\7^\2\2\u020c\u020d\t\b\2\2\u020d\u0086\3\2\2\2")
        buf.write("\u020e\u0212\t\t\2\2\u020f\u0211\t\n\2\2\u0210\u020f\3")
        buf.write("\2\2\2\u0211\u0214\3\2\2\2\u0212\u0210\3\2\2\2\u0212\u0213")
        buf.write("\3\2\2\2\u0213\u0088\3\2\2\2\u0214\u0212\3\2\2\2\u0215")
        buf.write("\u0217\t\13\2\2\u0216\u0215\3\2\2\2\u0217\u0218\3\2\2")
        buf.write("\2\u0218\u0216\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u021a")
        buf.write("\3\2\2\2\u021a\u021b\bE\5\2\u021b\u008a\3\2\2\2\u021c")
        buf.write("\u021d\7\61\2\2\u021d\u021e\7\61\2\2\u021e\u0222\3\2\2")
        buf.write("\2\u021f\u0221\n\f\2\2\u0220\u021f\3\2\2\2\u0221\u0224")
        buf.write("\3\2\2\2\u0222\u0220\3\2\2\2\u0222\u0223\3\2\2\2\u0223")
        buf.write("\u0225\3\2\2\2\u0224\u0222\3\2\2\2\u0225\u0226\bF\5\2")
        buf.write("\u0226\u008c\3\2\2\2\u0227\u0228\7\61\2\2\u0228\u0229")
        buf.write("\7,\2\2\u0229\u022d\3\2\2\2\u022a\u022c\13\2\2\2\u022b")
        buf.write("\u022a\3\2\2\2\u022c\u022f\3\2\2\2\u022d\u022e\3\2\2\2")
        buf.write("\u022d\u022b\3\2\2\2\u022e\u0230\3\2\2\2\u022f\u022d\3")
        buf.write("\2\2\2\u0230\u0231\7,\2\2\u0231\u0232\7\61\2\2\u0232\u0233")
        buf.write("\3\2\2\2\u0233\u0234\bG\5\2\u0234\u008e\3\2\2\2\u0235")
        buf.write("\u0236\13\2\2\2\u0236\u0237\bH\6\2\u0237\u0090\3\2\2\2")
        buf.write("\u0238\u023c\7$\2\2\u0239\u023b\5\u0083B\2\u023a\u0239")
        buf.write("\3\2\2\2\u023b\u023e\3\2\2\2\u023c\u023a\3\2\2\2\u023c")
        buf.write("\u023d\3\2\2\2\u023d\u0240\3\2\2\2\u023e\u023c\3\2\2\2")
        buf.write("\u023f\u0241\7\2\2\3\u0240\u023f\3\2\2\2\u0240\u0241\3")
        buf.write("\2\2\2\u0241\u0242\3\2\2\2\u0242\u0243\bI\7\2\u0243\u0092")
        buf.write("\3\2\2\2\u0244\u0248\7$\2\2\u0245\u0247\5\u0083B\2\u0246")
        buf.write("\u0245\3\2\2\2\u0247\u024a\3\2\2\2\u0248\u0246\3\2\2\2")
        buf.write("\u0248\u0249\3\2\2\2\u0249\u024b\3\2\2\2\u024a\u0248\3")
        buf.write("\2\2\2\u024b\u024c\7^\2\2\u024c\u024d\n\r\2\2\u024d\u024e")
        buf.write("\3\2\2\2\u024e\u024f\bJ\b\2\u024f\u0094\3\2\2\2\31\2\u010a")
        buf.write("\u01c7\u01cc\u01d1\u01d4\u01dd\u01e1\u01e9\u01ed\u01f1")
        buf.write("\u01f8\u01fc\u0200\u0207\u0209\u0212\u0218\u0222\u022d")
        buf.write("\u023c\u0240\u0248\t\3<\2\3=\3\3A\4\b\2\2\3H\5\3I\6\3")
        buf.write("J\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    BOOLLIT = 11
    AUTO = 12
    FALSE = 13
    INTEGER = 14
    VOID = 15
    ARRAY = 16
    BREAK = 17
    FLOAT = 18
    RETURN = 19
    OUT = 20
    BOOLEAN = 21
    FOR = 22
    STRING = 23
    CONTINUE = 24
    DO = 25
    FUNCTION = 26
    TRUE = 27
    OF = 28
    ELSE = 29
    IF = 30
    WHILE = 31
    INHERIT = 32
    ADD = 33
    SUB = 34
    MUL = 35
    DIV = 36
    MOD = 37
    NOT = 38
    SM = 39
    SME = 40
    BG = 41
    BGE = 42
    EQUAL = 43
    NEQUAL = 44
    CONCAT = 45
    AND = 46
    OR = 47
    EQ = 48
    LB1 = 49
    RB1 = 50
    LB2 = 51
    RB2 = 52
    LB3 = 53
    RB3 = 54
    DOT = 55
    COMMA = 56
    SEMI = 57
    COLON = 58
    INTLIT = 59
    FLOATLIT = 60
    STRINGLIT = 61
    ID = 62
    WS = 63
    LINE_COMMENT = 64
    BLOCK_COMMENT = 65
    ERROR_TOKEN = 66
    UNCLOSE_STRING = 67
    ILLEGAL_ESCAPE = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readInteger'", "'printInteger'", "'readFloat'", "'writeFloat'", 
            "'readBoolean'", "'printBoolean'", "'readString'", "'printString'", 
            "'super'", "'preventDefault'", "'auto'", "'false'", "'integer'", 
            "'void'", "'array'", "'break'", "'float'", "'return'", "'out'", 
            "'boolean'", "'for'", "'string'", "'continue'", "'do'", "'function'", 
            "'true'", "'of'", "'else'", "'if'", "'while'", "'inherit'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'<'", "'<='", "'>'", 
            "'>='", "'=='", "'!='", "'::'", "'&&'", "'||'", "'='", "'('", 
            "')'", "'['", "']'", "'{'", "'}'", "'.'", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLLIT", "AUTO", "FALSE", "INTEGER", "VOID", "ARRAY", "BREAK", 
            "FLOAT", "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", 
            "DO", "FUNCTION", "TRUE", "OF", "ELSE", "IF", "WHILE", "INHERIT", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "SM", "SME", "BG", 
            "BGE", "EQUAL", "NEQUAL", "CONCAT", "AND", "OR", "EQ", "LB1", 
            "RB1", "LB2", "RB2", "LB3", "RB3", "DOT", "COMMA", "SEMI", "COLON", 
            "INTLIT", "FLOATLIT", "STRINGLIT", "ID", "WS", "LINE_COMMENT", 
            "BLOCK_COMMENT", "ERROR_TOKEN", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "BOOLLIT", "AUTO", "FALSE", "INTEGER", 
                  "VOID", "ARRAY", "BREAK", "FLOAT", "RETURN", "OUT", "BOOLEAN", 
                  "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", "TRUE", 
                  "OF", "ELSE", "IF", "WHILE", "INHERIT", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "NOT", "SM", "SME", "BG", "BGE", 
                  "EQUAL", "NEQUAL", "CONCAT", "AND", "OR", "EQ", "LB1", 
                  "RB1", "LB2", "RB2", "LB3", "RB3", "DOT", "COMMA", "SEMI", 
                  "COLON", "INTLIT", "FLOATLIT", "INTPART", "DECPART", "EXPPART", 
                  "STRINGLIT", "CHARS", "ESCAPE", "ID", "WS", "LINE_COMMENT", 
                  "BLOCK_COMMENT", "ERROR_TOKEN", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[58] = self.INTLIT_action 
            actions[59] = self.FLOATLIT_action 
            actions[63] = self.STRINGLIT_action 
            actions[70] = self.ERROR_TOKEN_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:(len(self.text) - 1)]
     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	y = str(self.text)
            	raise UncloseString(y[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            	y = str(self.text)
            	raise IllegalEscape(y[1:])

     


