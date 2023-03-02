# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\u0200\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\3\2\3")
        buf.write("\2\3\2\3\3\3\3\5\3z\n\3\3\4\3\4\3\4\3\4\3\4\7\4\u0081")
        buf.write("\n\4\f\4\16\4\u0084\13\4\3\5\3\5\3\5\5\5\u0089\n\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0093\n\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00a1\n\7\3\b")
        buf.write("\5\b\u00a4\n\b\3\b\5\b\u00a7\n\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00b9\n")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u00d4\n\13\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00e1\n\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\5\23\u0102\n\23\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\5\26")
        buf.write("\u010f\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\5\27\u011b\n\27\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\5\"\u0150\n\"")
        buf.write("\3#\3#\3#\3#\3#\5#\u0157\n#\3$\3$\3$\3$\3$\3$\7$\u015f")
        buf.write("\n$\f$\16$\u0162\13$\3%\3%\3%\3%\3%\3%\7%\u016a\n%\f%")
        buf.write("\16%\u016d\13%\3&\3&\3&\3&\3&\3&\7&\u0175\n&\f&\16&\u0178")
        buf.write("\13&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\5\'\u0188\n\'\3(\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*")
        buf.write("\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\7,\u01a2\n,\f")
        buf.write(",\16,\u01a5\13,\3-\3-\3-\3-\3-\3-\7-\u01ad\n-\f-\16-\u01b0")
        buf.write("\13-\3.\3.\3.\3.\3.\3.\7.\u01b8\n.\f.\16.\u01bb\13.\3")
        buf.write("/\3/\5/\u01bf\n/\3\60\3\60\3\60\3\60\3\60\3\60\7\60\u01c7")
        buf.write("\n\60\f\60\16\60\u01ca\13\60\3\61\3\61\5\61\u01ce\n\61")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\7\62\u01d6\n\62\f\62\16")
        buf.write("\62\u01d9\13\62\3\63\3\63\5\63\u01dd\n\63\3\64\3\64\3")
        buf.write("\64\3\64\3\64\7\64\u01e4\n\64\f\64\16\64\u01e7\13\64\3")
        buf.write("\65\3\65\5\65\u01eb\n\65\3\66\3\66\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\38\38\39\39\3:\3:\3:\3:\5:\u01fe\n:\3")
        buf.write(":\2\f\6FHJVXZ^bf;\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln")
        buf.write("pr\2\7\3\2,\61\3\2\63\64\3\2&\'\3\2(*\6\2\23\23\27\27")
        buf.write("\32\32\34\34\2\u0202\2t\3\2\2\2\4y\3\2\2\2\6{\3\2\2\2")
        buf.write("\b\u0088\3\2\2\2\n\u0092\3\2\2\2\f\u00a0\3\2\2\2\16\u00a3")
        buf.write("\3\2\2\2\20\u00ac\3\2\2\2\22\u00af\3\2\2\2\24\u00d3\3")
        buf.write("\2\2\2\26\u00d5\3\2\2\2\30\u00d9\3\2\2\2\32\u00e2\3\2")
        buf.write("\2\2\34\u00ee\3\2\2\2\36\u00f4\3\2\2\2 \u00fb\3\2\2\2")
        buf.write("\"\u00fd\3\2\2\2$\u00ff\3\2\2\2&\u0103\3\2\2\2(\u0108")
        buf.write("\3\2\2\2*\u010e\3\2\2\2,\u011a\3\2\2\2.\u011c\3\2\2\2")
        buf.write("\60\u0120\3\2\2\2\62\u0125\3\2\2\2\64\u012a\3\2\2\2\66")
        buf.write("\u012f\3\2\2\28\u0133\3\2\2\2:\u0138\3\2\2\2<\u013c\3")
        buf.write("\2\2\2>\u0141\3\2\2\2@\u0146\3\2\2\2B\u014f\3\2\2\2D\u0156")
        buf.write("\3\2\2\2F\u0158\3\2\2\2H\u0163\3\2\2\2J\u016e\3\2\2\2")
        buf.write("L\u0187\3\2\2\2N\u0189\3\2\2\2P\u018d\3\2\2\2R\u0192\3")
        buf.write("\2\2\2T\u0197\3\2\2\2V\u019b\3\2\2\2X\u01a6\3\2\2\2Z\u01b1")
        buf.write("\3\2\2\2\\\u01be\3\2\2\2^\u01c0\3\2\2\2`\u01cd\3\2\2\2")
        buf.write("b\u01cf\3\2\2\2d\u01dc\3\2\2\2f\u01de\3\2\2\2h\u01ea\3")
        buf.write("\2\2\2j\u01ec\3\2\2\2l\u01ee\3\2\2\2n\u01f5\3\2\2\2p\u01f7")
        buf.write("\3\2\2\2r\u01fd\3\2\2\2tu\5\4\3\2uv\7\2\2\3v\3\3\2\2\2")
        buf.write("wz\5\6\4\2xz\3\2\2\2yw\3\2\2\2yx\3\2\2\2z\5\3\2\2\2{|")
        buf.write("\b\4\1\2|}\5\b\5\2}\u0082\3\2\2\2~\177\f\4\2\2\177\u0081")
        buf.write("\5\b\5\2\u0080~\3\2\2\2\u0081\u0084\3\2\2\2\u0082\u0080")
        buf.write("\3\2\2\2\u0082\u0083\3\2\2\2\u0083\7\3\2\2\2\u0084\u0082")
        buf.write("\3\2\2\2\u0085\u0089\5\n\6\2\u0086\u0089\5\20\t\2\u0087")
        buf.write("\u0089\5\24\13\2\u0088\u0085\3\2\2\2\u0088\u0086\3\2\2")
        buf.write("\2\u0088\u0087\3\2\2\2\u0089\t\3\2\2\2\u008a\u008b\5X")
        buf.write("-\2\u008b\u008c\7?\2\2\u008c\u008d\5r:\2\u008d\u008e\7")
        buf.write(">\2\2\u008e\u0093\3\2\2\2\u008f\u0090\5\f\7\2\u0090\u0091")
        buf.write("\7>\2\2\u0091\u0093\3\2\2\2\u0092\u008a\3\2\2\2\u0092")
        buf.write("\u008f\3\2\2\2\u0093\13\3\2\2\2\u0094\u0095\7@\2\2\u0095")
        buf.write("\u0096\7=\2\2\u0096\u0097\5\f\7\2\u0097\u0098\7=\2\2\u0098")
        buf.write("\u0099\5B\"\2\u0099\u00a1\3\2\2\2\u009a\u009b\7@\2\2\u009b")
        buf.write("\u009c\7?\2\2\u009c\u009d\5r:\2\u009d\u009e\7\65\2\2\u009e")
        buf.write("\u009f\5B\"\2\u009f\u00a1\3\2\2\2\u00a0\u0094\3\2\2\2")
        buf.write("\u00a0\u009a\3\2\2\2\u00a1\r\3\2\2\2\u00a2\u00a4\7%\2")
        buf.write("\2\u00a3\u00a2\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a6")
        buf.write("\3\2\2\2\u00a5\u00a7\7\31\2\2\u00a6\u00a5\3\2\2\2\u00a6")
        buf.write("\u00a7\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a9\7@\2\2")
        buf.write("\u00a9\u00aa\7?\2\2\u00aa\u00ab\5r:\2\u00ab\17\3\2\2\2")
        buf.write("\u00ac\u00ad\5\22\n\2\u00ad\u00ae\5(\25\2\u00ae\21\3\2")
        buf.write("\2\2\u00af\u00b0\7@\2\2\u00b0\u00b1\7?\2\2\u00b1\u00b2")
        buf.write("\7\37\2\2\u00b2\u00b3\5r:\2\u00b3\u00b4\7\66\2\2\u00b4")
        buf.write("\u00b5\5\\/\2\u00b5\u00b8\7\67\2\2\u00b6\u00b7\7%\2\2")
        buf.write("\u00b7\u00b9\7@\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b9\3")
        buf.write("\2\2\2\u00b9\23\3\2\2\2\u00ba\u00bb\5\26\f\2\u00bb\u00bc")
        buf.write("\7>\2\2\u00bc\u00d4\3\2\2\2\u00bd\u00d4\5\30\r\2\u00be")
        buf.write("\u00d4\5\32\16\2\u00bf\u00d4\5\34\17\2\u00c0\u00c1\5\36")
        buf.write("\20\2\u00c1\u00c2\7>\2\2\u00c2\u00d4\3\2\2\2\u00c3\u00c4")
        buf.write("\5 \21\2\u00c4\u00c5\7>\2\2\u00c5\u00d4\3\2\2\2\u00c6")
        buf.write("\u00c7\5\"\22\2\u00c7\u00c8\7>\2\2\u00c8\u00d4\3\2\2\2")
        buf.write("\u00c9\u00ca\5$\23\2\u00ca\u00cb\7>\2\2\u00cb\u00d4\3")
        buf.write("\2\2\2\u00cc\u00cd\5&\24\2\u00cd\u00ce\7>\2\2\u00ce\u00d4")
        buf.write("\3\2\2\2\u00cf\u00d4\5(\25\2\u00d0\u00d1\5,\27\2\u00d1")
        buf.write("\u00d2\7>\2\2\u00d2\u00d4\3\2\2\2\u00d3\u00ba\3\2\2\2")
        buf.write("\u00d3\u00bd\3\2\2\2\u00d3\u00be\3\2\2\2\u00d3\u00bf\3")
        buf.write("\2\2\2\u00d3\u00c0\3\2\2\2\u00d3\u00c3\3\2\2\2\u00d3\u00c6")
        buf.write("\3\2\2\2\u00d3\u00c9\3\2\2\2\u00d3\u00cc\3\2\2\2\u00d3")
        buf.write("\u00cf\3\2\2\2\u00d3\u00d0\3\2\2\2\u00d4\25\3\2\2\2\u00d5")
        buf.write("\u00d6\5*\26\2\u00d6\u00d7\7\65\2\2\u00d7\u00d8\5B\"\2")
        buf.write("\u00d8\27\3\2\2\2\u00d9\u00da\7#\2\2\u00da\u00db\7\66")
        buf.write("\2\2\u00db\u00dc\5B\"\2\u00dc\u00dd\7\67\2\2\u00dd\u00e0")
        buf.write("\5\24\13\2\u00de\u00df\7\"\2\2\u00df\u00e1\5\24\13\2\u00e0")
        buf.write("\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\31\3\2\2\2\u00e2")
        buf.write("\u00e3\7\33\2\2\u00e3\u00e4\7\66\2\2\u00e4\u00e5\5*\26")
        buf.write("\2\u00e5\u00e6\7\65\2\2\u00e6\u00e7\5B\"\2\u00e7\u00e8")
        buf.write("\7=\2\2\u00e8\u00e9\5B\"\2\u00e9\u00ea\7=\2\2\u00ea\u00eb")
        buf.write("\5\26\f\2\u00eb\u00ec\7\67\2\2\u00ec\u00ed\5\24\13\2\u00ed")
        buf.write("\33\3\2\2\2\u00ee\u00ef\7$\2\2\u00ef\u00f0\7\66\2\2\u00f0")
        buf.write("\u00f1\5B\"\2\u00f1\u00f2\7\67\2\2\u00f2\u00f3\5\24\13")
        buf.write("\2\u00f3\35\3\2\2\2\u00f4\u00f5\7\36\2\2\u00f5\u00f6\5")
        buf.write("(\25\2\u00f6\u00f7\7$\2\2\u00f7\u00f8\7\66\2\2\u00f8\u00f9")
        buf.write("\5B\"\2\u00f9\u00fa\7\67\2\2\u00fa\37\3\2\2\2\u00fb\u00fc")
        buf.write("\7\26\2\2\u00fc!\3\2\2\2\u00fd\u00fe\7\35\2\2\u00fe#\3")
        buf.write("\2\2\2\u00ff\u0101\7\30\2\2\u0100\u0102\5B\"\2\u0101\u0100")
        buf.write("\3\2\2\2\u0101\u0102\3\2\2\2\u0102%\3\2\2\2\u0103\u0104")
        buf.write("\7@\2\2\u0104\u0105\7\66\2\2\u0105\u0106\5`\61\2\u0106")
        buf.write("\u0107\7\67\2\2\u0107\'\3\2\2\2\u0108\u0109\7:\2\2\u0109")
        buf.write("\u010a\5d\63\2\u010a\u010b\7;\2\2\u010b)\3\2\2\2\u010c")
        buf.write("\u010f\7@\2\2\u010d\u010f\5P)\2\u010e\u010c\3\2\2\2\u010e")
        buf.write("\u010d\3\2\2\2\u010f+\3\2\2\2\u0110\u011b\5.\30\2\u0111")
        buf.write("\u011b\5\60\31\2\u0112\u011b\5\62\32\2\u0113\u011b\5\64")
        buf.write("\33\2\u0114\u011b\5\66\34\2\u0115\u011b\58\35\2\u0116")
        buf.write("\u011b\5:\36\2\u0117\u011b\5<\37\2\u0118\u011b\5> \2\u0119")
        buf.write("\u011b\5@!\2\u011a\u0110\3\2\2\2\u011a\u0111\3\2\2\2\u011a")
        buf.write("\u0112\3\2\2\2\u011a\u0113\3\2\2\2\u011a\u0114\3\2\2\2")
        buf.write("\u011a\u0115\3\2\2\2\u011a\u0116\3\2\2\2\u011a\u0117\3")
        buf.write("\2\2\2\u011a\u0118\3\2\2\2\u011a\u0119\3\2\2\2\u011b-")
        buf.write("\3\2\2\2\u011c\u011d\7\3\2\2\u011d\u011e\7\66\2\2\u011e")
        buf.write("\u011f\7\67\2\2\u011f/\3\2\2\2\u0120\u0121\7\4\2\2\u0121")
        buf.write("\u0122\7\66\2\2\u0122\u0123\5B\"\2\u0123\u0124\7\67\2")
        buf.write("\2\u0124\61\3\2\2\2\u0125\u0126\7\5\2\2\u0126\u0127\7")
        buf.write("\66\2\2\u0127\u0128\7\67\2\2\u0128\u0129\7>\2\2\u0129")
        buf.write("\63\3\2\2\2\u012a\u012b\7\6\2\2\u012b\u012c\7\66\2\2\u012c")
        buf.write("\u012d\5B\"\2\u012d\u012e\7\67\2\2\u012e\65\3\2\2\2\u012f")
        buf.write("\u0130\7\7\2\2\u0130\u0131\7\66\2\2\u0131\u0132\7\67\2")
        buf.write("\2\u0132\67\3\2\2\2\u0133\u0134\7\b\2\2\u0134\u0135\7")
        buf.write("\66\2\2\u0135\u0136\5B\"\2\u0136\u0137\7\67\2\2\u0137")
        buf.write("9\3\2\2\2\u0138\u0139\7\t\2\2\u0139\u013a\7\66\2\2\u013a")
        buf.write("\u013b\7\67\2\2\u013b;\3\2\2\2\u013c\u013d\7\n\2\2\u013d")
        buf.write("\u013e\7\66\2\2\u013e\u013f\5B\"\2\u013f\u0140\7\67\2")
        buf.write("\2\u0140=\3\2\2\2\u0141\u0142\7\13\2\2\u0142\u0143\7\66")
        buf.write("\2\2\u0143\u0144\5Z.\2\u0144\u0145\7\67\2\2\u0145?\3\2")
        buf.write("\2\2\u0146\u0147\7\f\2\2\u0147\u0148\7\66\2\2\u0148\u0149")
        buf.write("\7\67\2\2\u0149A\3\2\2\2\u014a\u014b\5D#\2\u014b\u014c")
        buf.write("\7\62\2\2\u014c\u014d\5D#\2\u014d\u0150\3\2\2\2\u014e")
        buf.write("\u0150\5D#\2\u014f\u014a\3\2\2\2\u014f\u014e\3\2\2\2\u0150")
        buf.write("C\3\2\2\2\u0151\u0152\5F$\2\u0152\u0153\t\2\2\2\u0153")
        buf.write("\u0154\5F$\2\u0154\u0157\3\2\2\2\u0155\u0157\5F$\2\u0156")
        buf.write("\u0151\3\2\2\2\u0156\u0155\3\2\2\2\u0157E\3\2\2\2\u0158")
        buf.write("\u0159\b$\1\2\u0159\u015a\5H%\2\u015a\u0160\3\2\2\2\u015b")
        buf.write("\u015c\f\4\2\2\u015c\u015d\t\3\2\2\u015d\u015f\5H%\2\u015e")
        buf.write("\u015b\3\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2")
        buf.write("\u0160\u0161\3\2\2\2\u0161G\3\2\2\2\u0162\u0160\3\2\2")
        buf.write("\2\u0163\u0164\b%\1\2\u0164\u0165\5J&\2\u0165\u016b\3")
        buf.write("\2\2\2\u0166\u0167\f\4\2\2\u0167\u0168\t\4\2\2\u0168\u016a")
        buf.write("\5J&\2\u0169\u0166\3\2\2\2\u016a\u016d\3\2\2\2\u016b\u0169")
        buf.write("\3\2\2\2\u016b\u016c\3\2\2\2\u016cI\3\2\2\2\u016d\u016b")
        buf.write("\3\2\2\2\u016e\u016f\b&\1\2\u016f\u0170\5L\'\2\u0170\u0176")
        buf.write("\3\2\2\2\u0171\u0172\f\4\2\2\u0172\u0173\t\5\2\2\u0173")
        buf.write("\u0175\5L\'\2\u0174\u0171\3\2\2\2\u0175\u0178\3\2\2\2")
        buf.write("\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177K\3\2\2")
        buf.write("\2\u0178\u0176\3\2\2\2\u0179\u0188\7\r\2\2\u017a\u0188")
        buf.write("\7\17\2\2\u017b\u0188\7\16\2\2\u017c\u0188\7\20\2\2\u017d")
        buf.write("\u0188\5T+\2\u017e\u0188\7@\2\2\u017f\u0180\7+\2\2\u0180")
        buf.write("\u0188\7@\2\2\u0181\u0182\7\'\2\2\u0182\u0188\7@\2\2\u0183")
        buf.write("\u0188\5R*\2\u0184\u0188\5P)\2\u0185\u0188\5N(\2\u0186")
        buf.write("\u0188\5,\27\2\u0187\u0179\3\2\2\2\u0187\u017a\3\2\2\2")
        buf.write("\u0187\u017b\3\2\2\2\u0187\u017c\3\2\2\2\u0187\u017d\3")
        buf.write("\2\2\2\u0187\u017e\3\2\2\2\u0187\u017f\3\2\2\2\u0187\u0181")
        buf.write("\3\2\2\2\u0187\u0183\3\2\2\2\u0187\u0184\3\2\2\2\u0187")
        buf.write("\u0185\3\2\2\2\u0187\u0186\3\2\2\2\u0188M\3\2\2\2\u0189")
        buf.write("\u018a\7\66\2\2\u018a\u018b\5B\"\2\u018b\u018c\7\67\2")
        buf.write("\2\u018cO\3\2\2\2\u018d\u018e\7@\2\2\u018e\u018f\78\2")
        buf.write("\2\u018f\u0190\5Z.\2\u0190\u0191\79\2\2\u0191Q\3\2\2\2")
        buf.write("\u0192\u0193\7@\2\2\u0193\u0194\7\66\2\2\u0194\u0195\5")
        buf.write("`\61\2\u0195\u0196\7\67\2\2\u0196S\3\2\2\2\u0197\u0198")
        buf.write("\7:\2\2\u0198\u0199\5Z.\2\u0199\u019a\7;\2\2\u019aU\3")
        buf.write("\2\2\2\u019b\u019c\b,\1\2\u019c\u019d\7\r\2\2\u019d\u01a3")
        buf.write("\3\2\2\2\u019e\u019f\f\4\2\2\u019f\u01a0\7=\2\2\u01a0")
        buf.write("\u01a2\7\r\2\2\u01a1\u019e\3\2\2\2\u01a2\u01a5\3\2\2\2")
        buf.write("\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4W\3\2\2")
        buf.write("\2\u01a5\u01a3\3\2\2\2\u01a6\u01a7\b-\1\2\u01a7\u01a8")
        buf.write("\7@\2\2\u01a8\u01ae\3\2\2\2\u01a9\u01aa\f\4\2\2\u01aa")
        buf.write("\u01ab\7=\2\2\u01ab\u01ad\7@\2\2\u01ac\u01a9\3\2\2\2\u01ad")
        buf.write("\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2")
        buf.write("\u01afY\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u01b2\b.\1\2")
        buf.write("\u01b2\u01b3\5B\"\2\u01b3\u01b9\3\2\2\2\u01b4\u01b5\f")
        buf.write("\4\2\2\u01b5\u01b6\7=\2\2\u01b6\u01b8\5B\"\2\u01b7\u01b4")
        buf.write("\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9")
        buf.write("\u01ba\3\2\2\2\u01ba[\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bc")
        buf.write("\u01bf\5^\60\2\u01bd\u01bf\3\2\2\2\u01be\u01bc\3\2\2\2")
        buf.write("\u01be\u01bd\3\2\2\2\u01bf]\3\2\2\2\u01c0\u01c1\b\60\1")
        buf.write("\2\u01c1\u01c2\5\16\b\2\u01c2\u01c8\3\2\2\2\u01c3\u01c4")
        buf.write("\f\4\2\2\u01c4\u01c5\7=\2\2\u01c5\u01c7\5\16\b\2\u01c6")
        buf.write("\u01c3\3\2\2\2\u01c7\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2")
        buf.write("\u01c8\u01c9\3\2\2\2\u01c9_\3\2\2\2\u01ca\u01c8\3\2\2")
        buf.write("\2\u01cb\u01ce\5b\62\2\u01cc\u01ce\3\2\2\2\u01cd\u01cb")
        buf.write("\3\2\2\2\u01cd\u01cc\3\2\2\2\u01cea\3\2\2\2\u01cf\u01d0")
        buf.write("\b\62\1\2\u01d0\u01d1\5B\"\2\u01d1\u01d7\3\2\2\2\u01d2")
        buf.write("\u01d3\f\4\2\2\u01d3\u01d4\7=\2\2\u01d4\u01d6\5B\"\2\u01d5")
        buf.write("\u01d2\3\2\2\2\u01d6\u01d9\3\2\2\2\u01d7\u01d5\3\2\2\2")
        buf.write("\u01d7\u01d8\3\2\2\2\u01d8c\3\2\2\2\u01d9\u01d7\3\2\2")
        buf.write("\2\u01da\u01dd\5f\64\2\u01db\u01dd\3\2\2\2\u01dc\u01da")
        buf.write("\3\2\2\2\u01dc\u01db\3\2\2\2\u01dde\3\2\2\2\u01de\u01df")
        buf.write("\b\64\1\2\u01df\u01e0\5h\65\2\u01e0\u01e5\3\2\2\2\u01e1")
        buf.write("\u01e2\f\4\2\2\u01e2\u01e4\5h\65\2\u01e3\u01e1\3\2\2\2")
        buf.write("\u01e4\u01e7\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6\3")
        buf.write("\2\2\2\u01e6g\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e8\u01eb")
        buf.write("\5\24\13\2\u01e9\u01eb\5\n\6\2\u01ea\u01e8\3\2\2\2\u01ea")
        buf.write("\u01e9\3\2\2\2\u01ebi\3\2\2\2\u01ec\u01ed\t\6\2\2\u01ed")
        buf.write("k\3\2\2\2\u01ee\u01ef\7\25\2\2\u01ef\u01f0\78\2\2\u01f0")
        buf.write("\u01f1\5V,\2\u01f1\u01f2\79\2\2\u01f2\u01f3\7!\2\2\u01f3")
        buf.write("\u01f4\5j\66\2\u01f4m\3\2\2\2\u01f5\u01f6\7\24\2\2\u01f6")
        buf.write("o\3\2\2\2\u01f7\u01f8\7\21\2\2\u01f8q\3\2\2\2\u01f9\u01fe")
        buf.write("\5j\66\2\u01fa\u01fe\5l\67\2\u01fb\u01fe\5n8\2\u01fc\u01fe")
        buf.write("\5p9\2\u01fd\u01f9\3\2\2\2\u01fd\u01fa\3\2\2\2\u01fd\u01fb")
        buf.write("\3\2\2\2\u01fd\u01fc\3\2\2\2\u01fes\3\2\2\2 y\u0082\u0088")
        buf.write("\u0092\u00a0\u00a3\u00a6\u00b8\u00d3\u00e0\u0101\u010e")
        buf.write("\u011a\u014f\u0156\u0160\u016b\u0176\u0187\u01a3\u01ae")
        buf.write("\u01b9\u01be\u01c8\u01cd\u01d7\u01dc\u01e5\u01ea\u01fd")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'readInteger'", "'printInteger'", "'readFloat'", 
                     "'writeFloat'", "'readBoolean'", "'printBoolean'", 
                     "'readString'", "'printString'", "'super'", "'preventDefault'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'auto'", "'false'", "'integer'", "'void'", "'array'", 
                     "'break'", "'float'", "'return'", "'out'", "'boolean'", 
                     "'for'", "'string'", "'continue'", "'do'", "'function'", 
                     "'true'", "'of'", "'else'", "'if'", "'while'", "'inherit'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'<'", "'<='", 
                     "'>'", "'>='", "'=='", "'!='", "'::'", "'&&'", "'||'", 
                     "'='", "'('", "')'", "'['", "']'", "'{'", "'}'", "'.'", 
                     "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INTLIT", "BOOLLIT", 
                      "FLOATLIT", "STRINGLIT", "AUTO", "FALSE", "INTEGER", 
                      "VOID", "ARRAY", "BREAK", "FLOAT", "RETURN", "OUT", 
                      "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", 
                      "TRUE", "OF", "ELSE", "IF", "WHILE", "INHERIT", "ADD", 
                      "SUB", "MUL", "DIV", "MOD", "NOT", "SM", "SME", "BG", 
                      "BGE", "EQUAL", "NEQUAL", "CONCAT", "AND", "OR", "EQ", 
                      "LB1", "RB1", "LB2", "RB2", "LB3", "RB3", "DOT", "COMMA", 
                      "SEMI", "COLON", "ID", "WS", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "ERROR_TOKEN", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decllistprime = 2
    RULE_decl = 3
    RULE_vardecl = 4
    RULE_initialization = 5
    RULE_paramdecl = 6
    RULE_funcdecl = 7
    RULE_prototype = 8
    RULE_statement = 9
    RULE_assignstmt = 10
    RULE_ifstmt = 11
    RULE_forstmt = 12
    RULE_whilestmt = 13
    RULE_dowhilestmt = 14
    RULE_breakstmt = 15
    RULE_continuestmt = 16
    RULE_returnstmt = 17
    RULE_callstmt = 18
    RULE_blockstmt = 19
    RULE_scalar = 20
    RULE_specfunc = 21
    RULE_readInteger = 22
    RULE_printInteger = 23
    RULE_readFloat = 24
    RULE_writeFloat = 25
    RULE_readBoolean = 26
    RULE_printBoolean = 27
    RULE_readString = 28
    RULE_printString = 29
    RULE_sper = 30
    RULE_preventDefault = 31
    RULE_expression = 32
    RULE_term1 = 33
    RULE_term2 = 34
    RULE_term3 = 35
    RULE_term4 = 36
    RULE_term5 = 37
    RULE_subexpression = 38
    RULE_idxop = 39
    RULE_call = 40
    RULE_arrlit = 41
    RULE_intlist = 42
    RULE_idlist = 43
    RULE_expressionlist = 44
    RULE_paramlist = 45
    RULE_paramlistprime = 46
    RULE_arglist = 47
    RULE_arglistprime = 48
    RULE_linelist = 49
    RULE_linelistprime = 50
    RULE_line = 51
    RULE_atomtyp = 52
    RULE_arrtyp = 53
    RULE_voidtyp = 54
    RULE_autotyp = 55
    RULE_typ = 56

    ruleNames =  [ "program", "decllist", "decllistprime", "decl", "vardecl", 
                   "initialization", "paramdecl", "funcdecl", "prototype", 
                   "statement", "assignstmt", "ifstmt", "forstmt", "whilestmt", 
                   "dowhilestmt", "breakstmt", "continuestmt", "returnstmt", 
                   "callstmt", "blockstmt", "scalar", "specfunc", "readInteger", 
                   "printInteger", "readFloat", "writeFloat", "readBoolean", 
                   "printBoolean", "readString", "printString", "sper", 
                   "preventDefault", "expression", "term1", "term2", "term3", 
                   "term4", "term5", "subexpression", "idxop", "call", "arrlit", 
                   "intlist", "idlist", "expressionlist", "paramlist", "paramlistprime", 
                   "arglist", "arglistprime", "linelist", "linelistprime", 
                   "line", "atomtyp", "arrtyp", "voidtyp", "autotyp", "typ" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    INTLIT=11
    BOOLLIT=12
    FLOATLIT=13
    STRINGLIT=14
    AUTO=15
    FALSE=16
    INTEGER=17
    VOID=18
    ARRAY=19
    BREAK=20
    FLOAT=21
    RETURN=22
    OUT=23
    BOOLEAN=24
    FOR=25
    STRING=26
    CONTINUE=27
    DO=28
    FUNCTION=29
    TRUE=30
    OF=31
    ELSE=32
    IF=33
    WHILE=34
    INHERIT=35
    ADD=36
    SUB=37
    MUL=38
    DIV=39
    MOD=40
    NOT=41
    SM=42
    SME=43
    BG=44
    BGE=45
    EQUAL=46
    NEQUAL=47
    CONCAT=48
    AND=49
    OR=50
    EQ=51
    LB1=52
    RB1=53
    LB2=54
    RB2=55
    LB3=56
    RB3=57
    DOT=58
    COMMA=59
    SEMI=60
    COLON=61
    ID=62
    WS=63
    LINE_COMMENT=64
    BLOCK_COMMENT=65
    ERROR_TOKEN=66
    UNCLOSE_STRING=67
    ILLEGAL_ESCAPE=68

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decllist(self):
            return self.getTypedRuleContext(MT22Parser.DecllistContext,0)


        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.decllist()
            self.state = 115
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decllistprime(self):
            return self.getTypedRuleContext(MT22Parser.DecllistprimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = MT22Parser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.T__0, MT22Parser.T__1, MT22Parser.T__2, MT22Parser.T__3, MT22Parser.T__4, MT22Parser.T__5, MT22Parser.T__6, MT22Parser.T__7, MT22Parser.T__8, MT22Parser.T__9, MT22Parser.BREAK, MT22Parser.RETURN, MT22Parser.FOR, MT22Parser.CONTINUE, MT22Parser.DO, MT22Parser.IF, MT22Parser.WHILE, MT22Parser.LB3, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.decllistprime(0)
                pass
            elif token in [MT22Parser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MT22Parser.DeclContext,0)


        def decllistprime(self):
            return self.getTypedRuleContext(MT22Parser.DecllistprimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decllistprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllistprime" ):
                return visitor.visitDecllistprime(self)
            else:
                return visitor.visitChildren(self)



    def decllistprime(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.DecllistprimeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_decllistprime, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.decl()
            self._ctx.stop = self._input.LT(-1)
            self.state = 128
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.DecllistprimeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_decllistprime)
                    self.state = 124
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 125
                    self.decl() 
                self.state = 130
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MT22Parser.FuncdeclContext,0)


        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MT22Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl)
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.funcdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 133
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(MT22Parser.TypContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def initialization(self):
            return self.getTypedRuleContext(MT22Parser.InitializationContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MT22Parser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardecl)
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.idlist(0)
                self.state = 137
                self.match(MT22Parser.COLON)
                self.state = 138
                self.typ()
                self.state = 139
                self.match(MT22Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.initialization()
                self.state = 142
                self.match(MT22Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def initialization(self):
            return self.getTypedRuleContext(MT22Parser.InitializationContext,0)


        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(MT22Parser.TypContext,0)


        def EQ(self):
            return self.getToken(MT22Parser.EQ, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_initialization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialization" ):
                return visitor.visitInitialization(self)
            else:
                return visitor.visitChildren(self)




    def initialization(self):

        localctx = MT22Parser.InitializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_initialization)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(MT22Parser.ID)
                self.state = 147
                self.match(MT22Parser.COMMA)
                self.state = 148
                self.initialization()
                self.state = 149
                self.match(MT22Parser.COMMA)
                self.state = 150
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.match(MT22Parser.ID)
                self.state = 153
                self.match(MT22Parser.COLON)
                self.state = 154
                self.typ()
                self.state = 155
                self.match(MT22Parser.EQ)
                self.state = 156
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(MT22Parser.TypContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def OUT(self):
            return self.getToken(MT22Parser.OUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_paramdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamdecl" ):
                return visitor.visitParamdecl(self)
            else:
                return visitor.visitChildren(self)




    def paramdecl(self):

        localctx = MT22Parser.ParamdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_paramdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 160
                self.match(MT22Parser.INHERIT)


            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.OUT:
                self.state = 163
                self.match(MT22Parser.OUT)


            self.state = 166
            self.match(MT22Parser.ID)
            self.state = 167
            self.match(MT22Parser.COLON)
            self.state = 168
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prototype(self):
            return self.getTypedRuleContext(MT22Parser.PrototypeContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MT22Parser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.prototype()
            self.state = 171
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrototypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def typ(self):
            return self.getTypedRuleContext(MT22Parser.TypContext,0)


        def LB1(self):
            return self.getToken(MT22Parser.LB1, 0)

        def paramlist(self):
            return self.getTypedRuleContext(MT22Parser.ParamlistContext,0)


        def RB1(self):
            return self.getToken(MT22Parser.RB1, 0)

        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_prototype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrototype" ):
                return visitor.visitPrototype(self)
            else:
                return visitor.visitChildren(self)




    def prototype(self):

        localctx = MT22Parser.PrototypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_prototype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(MT22Parser.ID)
            self.state = 174
            self.match(MT22Parser.COLON)
            self.state = 175
            self.match(MT22Parser.FUNCTION)
            self.state = 176
            self.typ()
            self.state = 177
            self.match(MT22Parser.LB1)
            self.state = 178
            self.paramlist()
            self.state = 179
            self.match(MT22Parser.RB1)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 180
                self.match(MT22Parser.INHERIT)
                self.state = 181
                self.match(MT22Parser.ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignstmt(self):
            return self.getTypedRuleContext(MT22Parser.AssignstmtContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def ifstmt(self):
            return self.getTypedRuleContext(MT22Parser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(MT22Parser.ForstmtContext,0)


        def whilestmt(self):
            return self.getTypedRuleContext(MT22Parser.WhilestmtContext,0)


        def dowhilestmt(self):
            return self.getTypedRuleContext(MT22Parser.DowhilestmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(MT22Parser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(MT22Parser.ContinuestmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(MT22Parser.ReturnstmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(MT22Parser.CallstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def specfunc(self):
            return self.getTypedRuleContext(MT22Parser.SpecfuncContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MT22Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.assignstmt()
                self.state = 185
                self.match(MT22Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.ifstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 188
                self.forstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 189
                self.whilestmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 190
                self.dowhilestmt()
                self.state = 191
                self.match(MT22Parser.SEMI)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 193
                self.breakstmt()
                self.state = 194
                self.match(MT22Parser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 196
                self.continuestmt()
                self.state = 197
                self.match(MT22Parser.SEMI)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 199
                self.returnstmt()
                self.state = 200
                self.match(MT22Parser.SEMI)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 202
                self.callstmt()
                self.state = 203
                self.match(MT22Parser.SEMI)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 205
                self.blockstmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 206
                self.specfunc()
                self.state = 207
                self.match(MT22Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar(self):
            return self.getTypedRuleContext(MT22Parser.ScalarContext,0)


        def EQ(self):
            return self.getToken(MT22Parser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = MT22Parser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.scalar()
            self.state = 212
            self.match(MT22Parser.EQ)
            self.state = 213
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MT22Parser.IF, 0)

        def LB1(self):
            return self.getToken(MT22Parser.LB1, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RB1(self):
            return self.getToken(MT22Parser.RB1, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementContext,i)


        def ELSE(self):
            return self.getToken(MT22Parser.ELSE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = MT22Parser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(MT22Parser.IF)
            self.state = 216
            self.match(MT22Parser.LB1)
            self.state = 217
            self.expression()
            self.state = 218
            self.match(MT22Parser.RB1)
            self.state = 219
            self.statement()
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 220
                self.match(MT22Parser.ELSE)
                self.state = 221
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MT22Parser.FOR, 0)

        def LB1(self):
            return self.getToken(MT22Parser.LB1, 0)

        def scalar(self):
            return self.getTypedRuleContext(MT22Parser.ScalarContext,0)


        def EQ(self):
            return self.getToken(MT22Parser.EQ, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def assignstmt(self):
            return self.getTypedRuleContext(MT22Parser.AssignstmtContext,0)


        def RB1(self):
            return self.getToken(MT22Parser.RB1, 0)

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = MT22Parser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(MT22Parser.FOR)
            self.state = 225
            self.match(MT22Parser.LB1)
            self.state = 226
            self.scalar()
            self.state = 227
            self.match(MT22Parser.EQ)
            self.state = 228
            self.expression()
            self.state = 229
            self.match(MT22Parser.COMMA)
            self.state = 230
            self.expression()
            self.state = 231
            self.match(MT22Parser.COMMA)
            self.state = 232
            self.assignstmt()
            self.state = 233
            self.match(MT22Parser.RB1)
            self.state = 234
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LB1(self):
            return self.getToken(MT22Parser.LB1, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RB1(self):
            return self.getToken(MT22Parser.RB1, 0)

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_whilestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhilestmt" ):
                return visitor.visitWhilestmt(self)
            else:
                return visitor.visitChildren(self)




    def whilestmt(self):

        localctx = MT22Parser.WhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_whilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(MT22Parser.WHILE)
            self.state = 237
            self.match(MT22Parser.LB1)
            self.state = 238
            self.expression()
            self.state = 239
            self.match(MT22Parser.RB1)
            self.state = 240
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DowhilestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MT22Parser.DO, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LB1(self):
            return self.getToken(MT22Parser.LB1, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RB1(self):
            return self.getToken(MT22Parser.RB1, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_dowhilestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDowhilestmt" ):
                return visitor.visitDowhilestmt(self)
            else:
                return visitor.visitChildren(self)




    def dowhilestmt(self):

        localctx = MT22Parser.DowhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_dowhilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(MT22Parser.DO)
            self.state = 243
            self.blockstmt()
            self.state = 244
            self.match(MT22Parser.WHILE)
            self.state = 245
            self.match(MT22Parser.LB1)
            self.state = 246
            self.expression()
            self.state = 247
            self.match(MT22Parser.RB1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MT22Parser.BREAK, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = MT22Parser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(MT22Parser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MT22Parser.CONTINUE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = MT22Parser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(MT22Parser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MT22Parser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = MT22Parser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(MT22Parser.RETURN)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.T__0) | (1 << MT22Parser.T__1) | (1 << MT22Parser.T__2) | (1 << MT22Parser.T__3) | (1 << MT22Parser.T__4) | (1 << MT22Parser.T__5) | (1 << MT22Parser.T__6) | (1 << MT22Parser.T__7) | (1 << MT22Parser.T__8) | (1 << MT22Parser.T__9) | (1 << MT22Parser.INTLIT) | (1 << MT22Parser.BOOLLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.STRINGLIT) | (1 << MT22Parser.SUB) | (1 << MT22Parser.NOT) | (1 << MT22Parser.LB1) | (1 << MT22Parser.LB3) | (1 << MT22Parser.ID))) != 0):
                self.state = 254
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LB1(self):
            return self.getToken(MT22Parser.LB1, 0)

        def arglist(self):
            return self.getTypedRuleContext(MT22Parser.ArglistContext,0)


        def RB1(self):
            return self.getToken(MT22Parser.RB1, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_callstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




    def callstmt(self):

        localctx = MT22Parser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(MT22Parser.ID)
            self.state = 258
            self.match(MT22Parser.LB1)
            self.state = 259
            self.arglist()
            self.state = 260
            self.match(MT22Parser.RB1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB3(self):
            return self.getToken(MT22Parser.LB3, 0)

        def linelist(self):
            return self.getTypedRuleContext(MT22Parser.LinelistContext,0)


        def RB3(self):
            return self.getToken(MT22Parser.RB3, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = MT22Parser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(MT22Parser.LB3)
            self.state = 263
            self.linelist()
            self.state = 264
            self.match(MT22Parser.RB3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def idxop(self):
            return self.getTypedRuleContext(MT22Parser.IdxopContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_scalar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar" ):
                return visitor.visitScalar(self)
            else:
                return visitor.visitChildren(self)




    def scalar(self):

        localctx = MT22Parser.ScalarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_scalar)
        try:
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(MT22Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.idxop()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def readInteger(self):
            return self.getTypedRuleContext(MT22Parser.ReadIntegerContext,0)


        def printInteger(self):
            return self.getTypedRuleContext(MT22Parser.PrintIntegerContext,0)


        def readFloat(self):
            return self.getTypedRuleContext(MT22Parser.ReadFloatContext,0)


        def writeFloat(self):
            return self.getTypedRuleContext(MT22Parser.WriteFloatContext,0)


        def readBoolean(self):
            return self.getTypedRuleContext(MT22Parser.ReadBooleanContext,0)


        def printBoolean(self):
            return self.getTypedRuleContext(MT22Parser.PrintBooleanContext,0)


        def readString(self):
            return self.getTypedRuleContext(MT22Parser.ReadStringContext,0)


        def printString(self):
            return self.getTypedRuleContext(MT22Parser.PrintStringContext,0)


        def sper(self):
            return self.getTypedRuleContext(MT22Parser.SperContext,0)


        def preventDefault(self):
            return self.getTypedRuleContext(MT22Parser.PreventDefaultContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_specfunc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecfunc" ):
                return visitor.visitSpecfunc(self)
            else:
                return visitor.visitChildren(self)




    def specfunc(self):

        localctx = MT22Parser.SpecfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_specfunc)
        try:
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.readInteger()
                pass
            elif token in [MT22Parser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.printInteger()
                pass
            elif token in [MT22Parser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 272
                self.readFloat()
                pass
            elif token in [MT22Parser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 273
                self.writeFloat()
                pass
            elif token in [MT22Parser.T__4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 274
                self.readBoolean()
                pass
            elif token in [MT22Parser.T__5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 275
                self.printBoolean()
                pass
            elif token in [MT22Parser.T__6]:
                self.enterOuterAlt(localctx, 7)
                self.state = 276
                self.readString()
                pass
            elif token in [MT22Parser.T__7]:
                self.enterOuterAlt(localctx, 8)
                self.state = 277
                self.printString()
                pass
            elif token in [MT22Parser.T__8]:
                self.enterOuterAlt(localctx, 9)
                self.state = 278
                self.sper()
                pass
            elif token in [MT22Parser.T__9]:
                self.enterOuterAlt(localctx, 10)
                self.state = 279
                self.preventDefault()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadIntegerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB1(self):
            return self.getToken(MT22Parser.LB1, 0)

        def RB1(self):
            return self.getToken(MT22Parser.RB1, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_readInteger

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadInteger" ):
                return visitor.visitReadInteger(self)
            else:
                return visitor.visitChildren(self)




    def readInteger(self):

        localctx = MT22Parser.ReadIntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_readInteger)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(MT22Parser.T__0)
            self.state = 283
            self.match(MT22Parser.LB1)
            self.state = 284
            self.match(MT22Parser.RB1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintIntegerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB1(self):
            return self.getToken(MT22Parser.LB1, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RB1(self):
            return self.getToken(MT22Parser.RB1, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_printInteger

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintInteger" ):
                return visitor.visitPrintInteger(self)
            else:
                return visitor.visitChildren(self)




    def printInteger(self):

        localctx = MT22Parser.PrintIntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_printInteger)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(MT22Parser.T__1)
            self.state = 287
            self.match(MT22Parser.LB1)
            self.state = 288
            self.expression()
            self.state = 289
            self.match(MT22Parser.RB1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadFloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB1(self):
            return self.getToken(MT22Parser.LB1, 0)

        def RB1(self):
            return self.getToken(MT22Parser.RB1, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_readFloat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadFloat" ):
                return visitor.visitReadFloat(self)
            else:
                return visitor.visitChildren(self)




    def readFloat(self):

        localctx = MT22Parser.ReadFloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_readFloat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(MT22Parser.T__2)
            self.state = 292
            self.match(MT22Parser.LB1)
            self.state = 293
            self.match(MT22Parser.RB1)
            self.state = 294
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteFloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB1(self):
            return self.getToken(MT22Parser.LB1, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RB1(self):
            return self.getToken(MT22Parser.RB1, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_writeFloat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteFloat" ):
                return visitor.visitWriteFloat(self)
            else:
                return visitor.visitChildren(self)




    def writeFloat(self):

        localctx = MT22Parser.WriteFloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_writeFloat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(MT22Parser.T__3)
            self.state = 297
            self.match(MT22Parser.LB1)
            self.state = 298
            self.expression()
            self.state = 299
            self.match(MT22Parser.RB1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadBooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB1(self):
            return self.getToken(MT22Parser.LB1, 0)

        def RB1(self):
            return self.getToken(MT22Parser.RB1, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_readBoolean

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadBoolean" ):
                return visitor.visitReadBoolean(self)
            else:
                return visitor.visitChildren(self)




    def readBoolean(self):

        localctx = MT22Parser.ReadBooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_readBoolean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(MT22Parser.T__4)
            self.state = 302
            self.match(MT22Parser.LB1)
            self.state = 303
            self.match(MT22Parser.RB1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintBooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB1(self):
            return self.getToken(MT22Parser.LB1, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RB1(self):
            return self.getToken(MT22Parser.RB1, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_printBoolean

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintBoolean" ):
                return visitor.visitPrintBoolean(self)
            else:
                return visitor.visitChildren(self)




    def printBoolean(self):

        localctx = MT22Parser.PrintBooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_printBoolean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(MT22Parser.T__5)
            self.state = 306
            self.match(MT22Parser.LB1)
            self.state = 307
            self.expression()
            self.state = 308
            self.match(MT22Parser.RB1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB1(self):
            return self.getToken(MT22Parser.LB1, 0)

        def RB1(self):
            return self.getToken(MT22Parser.RB1, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_readString

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadString" ):
                return visitor.visitReadString(self)
            else:
                return visitor.visitChildren(self)




    def readString(self):

        localctx = MT22Parser.ReadStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_readString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(MT22Parser.T__6)
            self.state = 311
            self.match(MT22Parser.LB1)
            self.state = 312
            self.match(MT22Parser.RB1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB1(self):
            return self.getToken(MT22Parser.LB1, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RB1(self):
            return self.getToken(MT22Parser.RB1, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_printString

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintString" ):
                return visitor.visitPrintString(self)
            else:
                return visitor.visitChildren(self)




    def printString(self):

        localctx = MT22Parser.PrintStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_printString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(MT22Parser.T__7)
            self.state = 315
            self.match(MT22Parser.LB1)
            self.state = 316
            self.expression()
            self.state = 317
            self.match(MT22Parser.RB1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SperContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB1(self):
            return self.getToken(MT22Parser.LB1, 0)

        def expressionlist(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionlistContext,0)


        def RB1(self):
            return self.getToken(MT22Parser.RB1, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_sper

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSper" ):
                return visitor.visitSper(self)
            else:
                return visitor.visitChildren(self)




    def sper(self):

        localctx = MT22Parser.SperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_sper)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(MT22Parser.T__8)
            self.state = 320
            self.match(MT22Parser.LB1)
            self.state = 321
            self.expressionlist(0)
            self.state = 322
            self.match(MT22Parser.RB1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreventDefaultContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB1(self):
            return self.getToken(MT22Parser.LB1, 0)

        def RB1(self):
            return self.getToken(MT22Parser.RB1, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_preventDefault

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreventDefault" ):
                return visitor.visitPreventDefault(self)
            else:
                return visitor.visitChildren(self)




    def preventDefault(self):

        localctx = MT22Parser.PreventDefaultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_preventDefault)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(MT22Parser.T__9)
            self.state = 325
            self.match(MT22Parser.LB1)
            self.state = 326
            self.match(MT22Parser.RB1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Term1Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Term1Context,i)


        def CONCAT(self):
            return self.getToken(MT22Parser.CONCAT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MT22Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expression)
        try:
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.term1()
                self.state = 329
                self.match(MT22Parser.CONCAT)
                self.state = 330
                self.term1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.term1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Term2Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Term2Context,i)


        def EQUAL(self):
            return self.getToken(MT22Parser.EQUAL, 0)

        def NEQUAL(self):
            return self.getToken(MT22Parser.NEQUAL, 0)

        def SM(self):
            return self.getToken(MT22Parser.SM, 0)

        def SME(self):
            return self.getToken(MT22Parser.SME, 0)

        def BG(self):
            return self.getToken(MT22Parser.BG, 0)

        def BGE(self):
            return self.getToken(MT22Parser.BGE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_term1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm1" ):
                return visitor.visitTerm1(self)
            else:
                return visitor.visitChildren(self)




    def term1(self):

        localctx = MT22Parser.Term1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_term1)
        self._la = 0 # Token type
        try:
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.term2(0)
                self.state = 336
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.SM) | (1 << MT22Parser.SME) | (1 << MT22Parser.BG) | (1 << MT22Parser.BGE) | (1 << MT22Parser.EQUAL) | (1 << MT22Parser.NEQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 337
                self.term2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.term2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term3(self):
            return self.getTypedRuleContext(MT22Parser.Term3Context,0)


        def term2(self):
            return self.getTypedRuleContext(MT22Parser.Term2Context,0)


        def AND(self):
            return self.getToken(MT22Parser.AND, 0)

        def OR(self):
            return self.getToken(MT22Parser.OR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_term2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm2" ):
                return visitor.visitTerm2(self)
            else:
                return visitor.visitChildren(self)



    def term2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Term2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_term2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.term3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 350
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Term2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term2)
                    self.state = 345
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 346
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.AND or _la==MT22Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 347
                    self.term3(0) 
                self.state = 352
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Term3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term4(self):
            return self.getTypedRuleContext(MT22Parser.Term4Context,0)


        def term3(self):
            return self.getTypedRuleContext(MT22Parser.Term3Context,0)


        def ADD(self):
            return self.getToken(MT22Parser.ADD, 0)

        def SUB(self):
            return self.getToken(MT22Parser.SUB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_term3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm3" ):
                return visitor.visitTerm3(self)
            else:
                return visitor.visitChildren(self)



    def term3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Term3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_term3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.term4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 361
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Term3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term3)
                    self.state = 356
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 357
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ADD or _la==MT22Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 358
                    self.term4(0) 
                self.state = 363
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Term4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term5(self):
            return self.getTypedRuleContext(MT22Parser.Term5Context,0)


        def term4(self):
            return self.getTypedRuleContext(MT22Parser.Term4Context,0)


        def MUL(self):
            return self.getToken(MT22Parser.MUL, 0)

        def DIV(self):
            return self.getToken(MT22Parser.DIV, 0)

        def MOD(self):
            return self.getToken(MT22Parser.MOD, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_term4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm4" ):
                return visitor.visitTerm4(self)
            else:
                return visitor.visitChildren(self)



    def term4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Term4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_term4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.term5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 372
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Term4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term4)
                    self.state = 367
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 368
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MUL) | (1 << MT22Parser.DIV) | (1 << MT22Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 369
                    self.term5() 
                self.state = 374
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Term5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MT22Parser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(MT22Parser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MT22Parser.STRINGLIT, 0)

        def arrlit(self):
            return self.getTypedRuleContext(MT22Parser.ArrlitContext,0)


        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def NOT(self):
            return self.getToken(MT22Parser.NOT, 0)

        def SUB(self):
            return self.getToken(MT22Parser.SUB, 0)

        def call(self):
            return self.getTypedRuleContext(MT22Parser.CallContext,0)


        def idxop(self):
            return self.getTypedRuleContext(MT22Parser.IdxopContext,0)


        def subexpression(self):
            return self.getTypedRuleContext(MT22Parser.SubexpressionContext,0)


        def specfunc(self):
            return self.getTypedRuleContext(MT22Parser.SpecfuncContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_term5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm5" ):
                return visitor.visitTerm5(self)
            else:
                return visitor.visitChildren(self)




    def term5(self):

        localctx = MT22Parser.Term5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_term5)
        try:
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.match(MT22Parser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                self.match(MT22Parser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 377
                self.match(MT22Parser.BOOLLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 378
                self.match(MT22Parser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 379
                self.arrlit()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 380
                self.match(MT22Parser.ID)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 381
                self.match(MT22Parser.NOT)
                self.state = 382
                self.match(MT22Parser.ID)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 383
                self.match(MT22Parser.SUB)
                self.state = 384
                self.match(MT22Parser.ID)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 385
                self.call()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 386
                self.idxop()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 387
                self.subexpression()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 388
                self.specfunc()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB1(self):
            return self.getToken(MT22Parser.LB1, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RB1(self):
            return self.getToken(MT22Parser.RB1, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_subexpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexpression" ):
                return visitor.visitSubexpression(self)
            else:
                return visitor.visitChildren(self)




    def subexpression(self):

        localctx = MT22Parser.SubexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_subexpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(MT22Parser.LB1)
            self.state = 392
            self.expression()
            self.state = 393
            self.match(MT22Parser.RB1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdxopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LB2(self):
            return self.getToken(MT22Parser.LB2, 0)

        def expressionlist(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionlistContext,0)


        def RB2(self):
            return self.getToken(MT22Parser.RB2, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_idxop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdxop" ):
                return visitor.visitIdxop(self)
            else:
                return visitor.visitChildren(self)




    def idxop(self):

        localctx = MT22Parser.IdxopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_idxop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(MT22Parser.ID)
            self.state = 396
            self.match(MT22Parser.LB2)
            self.state = 397
            self.expressionlist(0)
            self.state = 398
            self.match(MT22Parser.RB2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LB1(self):
            return self.getToken(MT22Parser.LB1, 0)

        def arglist(self):
            return self.getTypedRuleContext(MT22Parser.ArglistContext,0)


        def RB1(self):
            return self.getToken(MT22Parser.RB1, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = MT22Parser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(MT22Parser.ID)
            self.state = 401
            self.match(MT22Parser.LB1)
            self.state = 402
            self.arglist()
            self.state = 403
            self.match(MT22Parser.RB1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrlitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB3(self):
            return self.getToken(MT22Parser.LB3, 0)

        def expressionlist(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionlistContext,0)


        def RB3(self):
            return self.getToken(MT22Parser.RB3, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_arrlit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrlit" ):
                return visitor.visitArrlit(self)
            else:
                return visitor.visitChildren(self)




    def arrlit(self):

        localctx = MT22Parser.ArrlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_arrlit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(MT22Parser.LB3)
            self.state = 406
            self.expressionlist(0)
            self.state = 407
            self.match(MT22Parser.RB3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def intlist(self):
            return self.getTypedRuleContext(MT22Parser.IntlistContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_intlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntlist" ):
                return visitor.visitIntlist(self)
            else:
                return visitor.visitChildren(self)



    def intlist(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.IntlistContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_intlist, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(MT22Parser.INTLIT)
            self._ctx.stop = self._input.LT(-1)
            self.state = 417
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.IntlistContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_intlist)
                    self.state = 412
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 413
                    self.match(MT22Parser.COMMA)
                    self.state = 414
                    self.match(MT22Parser.INTLIT) 
                self.state = 419
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)



    def idlist(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.IdlistContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_idlist, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(MT22Parser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 428
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.IdlistContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_idlist)
                    self.state = 423
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 424
                    self.match(MT22Parser.COMMA)
                    self.state = 425
                    self.match(MT22Parser.ID) 
                self.state = 430
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExpressionlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def expressionlist(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionlistContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expressionlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionlist" ):
                return visitor.visitExpressionlist(self)
            else:
                return visitor.visitChildren(self)



    def expressionlist(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.ExpressionlistContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_expressionlist, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 439
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.ExpressionlistContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expressionlist)
                    self.state = 434
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 435
                    self.match(MT22Parser.COMMA)
                    self.state = 436
                    self.expression() 
                self.state = 441
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramlistprime(self):
            return self.getTypedRuleContext(MT22Parser.ParamlistprimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = MT22Parser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_paramlist)
        try:
            self.state = 444
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.OUT, MT22Parser.INHERIT, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.paramlistprime(0)
                pass
            elif token in [MT22Parser.RB1]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramdecl(self):
            return self.getTypedRuleContext(MT22Parser.ParamdeclContext,0)


        def paramlistprime(self):
            return self.getTypedRuleContext(MT22Parser.ParamlistprimeContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_paramlistprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlistprime" ):
                return visitor.visitParamlistprime(self)
            else:
                return visitor.visitChildren(self)



    def paramlistprime(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.ParamlistprimeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_paramlistprime, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.paramdecl()
            self._ctx.stop = self._input.LT(-1)
            self.state = 454
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.ParamlistprimeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_paramlistprime)
                    self.state = 449
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 450
                    self.match(MT22Parser.COMMA)
                    self.state = 451
                    self.paramdecl() 
                self.state = 456
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArglistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arglistprime(self):
            return self.getTypedRuleContext(MT22Parser.ArglistprimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arglist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArglist" ):
                return visitor.visitArglist(self)
            else:
                return visitor.visitChildren(self)




    def arglist(self):

        localctx = MT22Parser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_arglist)
        try:
            self.state = 459
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.T__0, MT22Parser.T__1, MT22Parser.T__2, MT22Parser.T__3, MT22Parser.T__4, MT22Parser.T__5, MT22Parser.T__6, MT22Parser.T__7, MT22Parser.T__8, MT22Parser.T__9, MT22Parser.INTLIT, MT22Parser.BOOLLIT, MT22Parser.FLOATLIT, MT22Parser.STRINGLIT, MT22Parser.SUB, MT22Parser.NOT, MT22Parser.LB1, MT22Parser.LB3, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.arglistprime(0)
                pass
            elif token in [MT22Parser.RB1]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArglistprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def arglistprime(self):
            return self.getTypedRuleContext(MT22Parser.ArglistprimeContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_arglistprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArglistprime" ):
                return visitor.visitArglistprime(self)
            else:
                return visitor.visitChildren(self)



    def arglistprime(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.ArglistprimeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_arglistprime, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 469
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.ArglistprimeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arglistprime)
                    self.state = 464
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 465
                    self.match(MT22Parser.COMMA)
                    self.state = 466
                    self.expression() 
                self.state = 471
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LinelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def linelistprime(self):
            return self.getTypedRuleContext(MT22Parser.LinelistprimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_linelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLinelist" ):
                return visitor.visitLinelist(self)
            else:
                return visitor.visitChildren(self)




    def linelist(self):

        localctx = MT22Parser.LinelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_linelist)
        try:
            self.state = 474
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.T__0, MT22Parser.T__1, MT22Parser.T__2, MT22Parser.T__3, MT22Parser.T__4, MT22Parser.T__5, MT22Parser.T__6, MT22Parser.T__7, MT22Parser.T__8, MT22Parser.T__9, MT22Parser.BREAK, MT22Parser.RETURN, MT22Parser.FOR, MT22Parser.CONTINUE, MT22Parser.DO, MT22Parser.IF, MT22Parser.WHILE, MT22Parser.LB3, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 472
                self.linelistprime(0)
                pass
            elif token in [MT22Parser.RB3]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinelistprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self):
            return self.getTypedRuleContext(MT22Parser.LineContext,0)


        def linelistprime(self):
            return self.getTypedRuleContext(MT22Parser.LinelistprimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_linelistprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLinelistprime" ):
                return visitor.visitLinelistprime(self)
            else:
                return visitor.visitChildren(self)



    def linelistprime(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.LinelistprimeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 100
        self.enterRecursionRule(localctx, 100, self.RULE_linelistprime, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.line()
            self._ctx.stop = self._input.LT(-1)
            self.state = 483
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.LinelistprimeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_linelistprime)
                    self.state = 479
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 480
                    self.line() 
                self.state = 485
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_line

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = MT22Parser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_line)
        try:
            self.state = 488
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 486
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
                self.vardecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomtypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_atomtyp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomtyp" ):
                return visitor.visitAtomtyp(self)
            else:
                return visitor.visitChildren(self)




    def atomtyp(self):

        localctx = MT22Parser.AtomtypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_atomtyp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTEGER) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrtypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def LB2(self):
            return self.getToken(MT22Parser.LB2, 0)

        def intlist(self):
            return self.getTypedRuleContext(MT22Parser.IntlistContext,0)


        def RB2(self):
            return self.getToken(MT22Parser.RB2, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def atomtyp(self):
            return self.getTypedRuleContext(MT22Parser.AtomtypContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arrtyp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrtyp" ):
                return visitor.visitArrtyp(self)
            else:
                return visitor.visitChildren(self)




    def arrtyp(self):

        localctx = MT22Parser.ArrtypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_arrtyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.match(MT22Parser.ARRAY)
            self.state = 493
            self.match(MT22Parser.LB2)
            self.state = 494
            self.intlist(0)
            self.state = 495
            self.match(MT22Parser.RB2)
            self.state = 496
            self.match(MT22Parser.OF)
            self.state = 497
            self.atomtyp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidtypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_voidtyp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVoidtyp" ):
                return visitor.visitVoidtyp(self)
            else:
                return visitor.visitChildren(self)




    def voidtyp(self):

        localctx = MT22Parser.VoidtypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_voidtyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.match(MT22Parser.VOID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AutotypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_autotyp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAutotyp" ):
                return visitor.visitAutotyp(self)
            else:
                return visitor.visitChildren(self)




    def autotyp(self):

        localctx = MT22Parser.AutotypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_autotyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.match(MT22Parser.AUTO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomtyp(self):
            return self.getTypedRuleContext(MT22Parser.AtomtypContext,0)


        def arrtyp(self):
            return self.getTypedRuleContext(MT22Parser.ArrtypContext,0)


        def voidtyp(self):
            return self.getTypedRuleContext(MT22Parser.VoidtypContext,0)


        def autotyp(self):
            return self.getTypedRuleContext(MT22Parser.AutotypContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = MT22Parser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_typ)
        try:
            self.state = 507
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INTEGER, MT22Parser.FLOAT, MT22Parser.BOOLEAN, MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 503
                self.atomtyp()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 504
                self.arrtyp()
                pass
            elif token in [MT22Parser.VOID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 505
                self.voidtyp()
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 4)
                self.state = 506
                self.autotyp()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.decllistprime_sempred
        self._predicates[34] = self.term2_sempred
        self._predicates[35] = self.term3_sempred
        self._predicates[36] = self.term4_sempred
        self._predicates[42] = self.intlist_sempred
        self._predicates[43] = self.idlist_sempred
        self._predicates[44] = self.expressionlist_sempred
        self._predicates[46] = self.paramlistprime_sempred
        self._predicates[48] = self.arglistprime_sempred
        self._predicates[50] = self.linelistprime_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def decllistprime_sempred(self, localctx:DecllistprimeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def term2_sempred(self, localctx:Term2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term3_sempred(self, localctx:Term3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def term4_sempred(self, localctx:Term4Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def intlist_sempred(self, localctx:IntlistContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def idlist_sempred(self, localctx:IdlistContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def expressionlist_sempred(self, localctx:ExpressionlistContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def paramlistprime_sempred(self, localctx:ParamlistprimeContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def arglistprime_sempred(self, localctx:ArglistprimeContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

    def linelistprime_sempred(self, localctx:LinelistprimeContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         




