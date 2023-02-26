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
        buf.write("\u0203\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\7\3{\n\3\f\3\16\3~\13\3\3\4\3\4\3")
        buf.write("\4\5\4\u0083\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u008d")
        buf.write("\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6\u009b\n\6\3\7\5\7\u009e\n\7\3\7\5\7\u00a1\n\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\5\t\u00b3\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\5\n\u00c0\n\n\3\13\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\22\3\22\5\22\u00f1\n\22\3\22\3\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\5\25\u0101\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\5\26\u010d\n\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3!\3!\3!\3!\3!\5!\u0154\n!\3\"\3\"\3\"\3")
        buf.write("\"\3\"\5\"\u015b\n\"\3#\3#\3#\3#\3#\3#\7#\u0163\n#\f#")
        buf.write("\16#\u0166\13#\3$\3$\3$\3$\3$\3$\7$\u016e\n$\f$\16$\u0171")
        buf.write("\13$\3%\3%\3%\3%\3%\3%\7%\u0179\n%\f%\16%\u017c\13%\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u018b\n&\3\'")
        buf.write("\3\'\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3")
        buf.write("*\3+\3+\3+\3+\3+\3+\7+\u01a5\n+\f+\16+\u01a8\13+\3,\3")
        buf.write(",\3,\3,\3,\3,\7,\u01b0\n,\f,\16,\u01b3\13,\3-\3-\3-\3")
        buf.write("-\3-\3-\7-\u01bb\n-\f-\16-\u01be\13-\3.\3.\5.\u01c2\n")
        buf.write(".\3/\3/\3/\3/\3/\3/\7/\u01ca\n/\f/\16/\u01cd\13/\3\60")
        buf.write("\3\60\5\60\u01d1\n\60\3\61\3\61\3\61\3\61\3\61\3\61\7")
        buf.write("\61\u01d9\n\61\f\61\16\61\u01dc\13\61\3\62\3\62\5\62\u01e0")
        buf.write("\n\62\3\63\3\63\3\63\3\63\3\63\7\63\u01e7\n\63\f\63\16")
        buf.write("\63\u01ea\13\63\3\64\3\64\5\64\u01ee\n\64\3\65\3\65\3")
        buf.write("\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\38\38\39\3")
        buf.write("9\39\39\59\u0201\n9\39\2\f\4DFHTVX\\`d:\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bdfhjlnp\2\7\3\2,\61\3\2\63\64\3\2&\'\3")
        buf.write("\2(*\6\2\23\23\27\27\32\32\34\34\2\u0203\2r\3\2\2\2\4")
        buf.write("u\3\2\2\2\6\u0082\3\2\2\2\b\u008c\3\2\2\2\n\u009a\3\2")
        buf.write("\2\2\f\u009d\3\2\2\2\16\u00a6\3\2\2\2\20\u00a9\3\2\2\2")
        buf.write("\22\u00bf\3\2\2\2\24\u00c1\3\2\2\2\26\u00c6\3\2\2\2\30")
        buf.write("\u00ce\3\2\2\2\32\u00da\3\2\2\2\34\u00e0\3\2\2\2\36\u00e8")
        buf.write("\3\2\2\2 \u00eb\3\2\2\2\"\u00ee\3\2\2\2$\u00f4\3\2\2\2")
        buf.write("&\u00fa\3\2\2\2(\u0100\3\2\2\2*\u010c\3\2\2\2,\u010e\3")
        buf.write("\2\2\2.\u0113\3\2\2\2\60\u011b\3\2\2\2\62\u0121\3\2\2")
        buf.write("\2\64\u0129\3\2\2\2\66\u012e\3\2\2\28\u0136\3\2\2\2:\u013b")
        buf.write("\3\2\2\2<\u0143\3\2\2\2>\u0149\3\2\2\2@\u0153\3\2\2\2")
        buf.write("B\u015a\3\2\2\2D\u015c\3\2\2\2F\u0167\3\2\2\2H\u0172\3")
        buf.write("\2\2\2J\u018a\3\2\2\2L\u018c\3\2\2\2N\u0190\3\2\2\2P\u0195")
        buf.write("\3\2\2\2R\u019a\3\2\2\2T\u019e\3\2\2\2V\u01a9\3\2\2\2")
        buf.write("X\u01b4\3\2\2\2Z\u01c1\3\2\2\2\\\u01c3\3\2\2\2^\u01d0")
        buf.write("\3\2\2\2`\u01d2\3\2\2\2b\u01df\3\2\2\2d\u01e1\3\2\2\2")
        buf.write("f\u01ed\3\2\2\2h\u01ef\3\2\2\2j\u01f1\3\2\2\2l\u01f8\3")
        buf.write("\2\2\2n\u01fa\3\2\2\2p\u0200\3\2\2\2rs\5\4\3\2st\7\2\2")
        buf.write("\3t\3\3\2\2\2uv\b\3\1\2vw\5\6\4\2w|\3\2\2\2xy\f\4\2\2")
        buf.write("y{\5\6\4\2zx\3\2\2\2{~\3\2\2\2|z\3\2\2\2|}\3\2\2\2}\5")
        buf.write("\3\2\2\2~|\3\2\2\2\177\u0083\5\b\5\2\u0080\u0083\5\16")
        buf.write("\b\2\u0081\u0083\5\22\n\2\u0082\177\3\2\2\2\u0082\u0080")
        buf.write("\3\2\2\2\u0082\u0081\3\2\2\2\u0083\7\3\2\2\2\u0084\u0085")
        buf.write("\5V,\2\u0085\u0086\7?\2\2\u0086\u0087\5p9\2\u0087\u0088")
        buf.write("\7>\2\2\u0088\u008d\3\2\2\2\u0089\u008a\5\n\6\2\u008a")
        buf.write("\u008b\7>\2\2\u008b\u008d\3\2\2\2\u008c\u0084\3\2\2\2")
        buf.write("\u008c\u0089\3\2\2\2\u008d\t\3\2\2\2\u008e\u008f\7@\2")
        buf.write("\2\u008f\u0090\7=\2\2\u0090\u0091\5\n\6\2\u0091\u0092")
        buf.write("\7=\2\2\u0092\u0093\5@!\2\u0093\u009b\3\2\2\2\u0094\u0095")
        buf.write("\7@\2\2\u0095\u0096\7?\2\2\u0096\u0097\5p9\2\u0097\u0098")
        buf.write("\7\65\2\2\u0098\u0099\5@!\2\u0099\u009b\3\2\2\2\u009a")
        buf.write("\u008e\3\2\2\2\u009a\u0094\3\2\2\2\u009b\13\3\2\2\2\u009c")
        buf.write("\u009e\7%\2\2\u009d\u009c\3\2\2\2\u009d\u009e\3\2\2\2")
        buf.write("\u009e\u00a0\3\2\2\2\u009f\u00a1\7\31\2\2\u00a0\u009f")
        buf.write("\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2")
        buf.write("\u00a3\7@\2\2\u00a3\u00a4\7?\2\2\u00a4\u00a5\5p9\2\u00a5")
        buf.write("\r\3\2\2\2\u00a6\u00a7\5\20\t\2\u00a7\u00a8\5&\24\2\u00a8")
        buf.write("\17\3\2\2\2\u00a9\u00aa\7@\2\2\u00aa\u00ab\7?\2\2\u00ab")
        buf.write("\u00ac\7\37\2\2\u00ac\u00ad\5p9\2\u00ad\u00ae\7\66\2\2")
        buf.write("\u00ae\u00af\5Z.\2\u00af\u00b2\7\67\2\2\u00b0\u00b1\7")
        buf.write("%\2\2\u00b1\u00b3\7@\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3")
        buf.write("\3\2\2\2\u00b3\21\3\2\2\2\u00b4\u00c0\5\24\13\2\u00b5")
        buf.write("\u00c0\5\26\f\2\u00b6\u00c0\5\30\r\2\u00b7\u00c0\5\32")
        buf.write("\16\2\u00b8\u00c0\5\34\17\2\u00b9\u00c0\5\36\20\2\u00ba")
        buf.write("\u00c0\5 \21\2\u00bb\u00c0\5\"\22\2\u00bc\u00c0\5$\23")
        buf.write("\2\u00bd\u00c0\5&\24\2\u00be\u00c0\5*\26\2\u00bf\u00b4")
        buf.write("\3\2\2\2\u00bf\u00b5\3\2\2\2\u00bf\u00b6\3\2\2\2\u00bf")
        buf.write("\u00b7\3\2\2\2\u00bf\u00b8\3\2\2\2\u00bf\u00b9\3\2\2\2")
        buf.write("\u00bf\u00ba\3\2\2\2\u00bf\u00bb\3\2\2\2\u00bf\u00bc\3")
        buf.write("\2\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00be\3\2\2\2\u00c0\23")
        buf.write("\3\2\2\2\u00c1\u00c2\5(\25\2\u00c2\u00c3\7\65\2\2\u00c3")
        buf.write("\u00c4\5@!\2\u00c4\u00c5\7>\2\2\u00c5\25\3\2\2\2\u00c6")
        buf.write("\u00c7\7#\2\2\u00c7\u00c8\7\66\2\2\u00c8\u00c9\5@!\2\u00c9")
        buf.write("\u00ca\7\67\2\2\u00ca\u00cb\5\22\n\2\u00cb\u00cc\7\"\2")
        buf.write("\2\u00cc\u00cd\5\22\n\2\u00cd\27\3\2\2\2\u00ce\u00cf\7")
        buf.write("\33\2\2\u00cf\u00d0\7\66\2\2\u00d0\u00d1\5(\25\2\u00d1")
        buf.write("\u00d2\7\65\2\2\u00d2\u00d3\5@!\2\u00d3\u00d4\7=\2\2\u00d4")
        buf.write("\u00d5\5@!\2\u00d5\u00d6\7=\2\2\u00d6\u00d7\5\22\n\2\u00d7")
        buf.write("\u00d8\7\67\2\2\u00d8\u00d9\5\22\n\2\u00d9\31\3\2\2\2")
        buf.write("\u00da\u00db\7$\2\2\u00db\u00dc\7\66\2\2\u00dc\u00dd\5")
        buf.write("@!\2\u00dd\u00de\7\67\2\2\u00de\u00df\5\22\n\2\u00df\33")
        buf.write("\3\2\2\2\u00e0\u00e1\7\36\2\2\u00e1\u00e2\5&\24\2\u00e2")
        buf.write("\u00e3\7$\2\2\u00e3\u00e4\7\66\2\2\u00e4\u00e5\5@!\2\u00e5")
        buf.write("\u00e6\7\67\2\2\u00e6\u00e7\7>\2\2\u00e7\35\3\2\2\2\u00e8")
        buf.write("\u00e9\7\26\2\2\u00e9\u00ea\7>\2\2\u00ea\37\3\2\2\2\u00eb")
        buf.write("\u00ec\7\35\2\2\u00ec\u00ed\7>\2\2\u00ed!\3\2\2\2\u00ee")
        buf.write("\u00f0\7\30\2\2\u00ef\u00f1\5@!\2\u00f0\u00ef\3\2\2\2")
        buf.write("\u00f0\u00f1\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\7")
        buf.write(">\2\2\u00f3#\3\2\2\2\u00f4\u00f5\7@\2\2\u00f5\u00f6\7")
        buf.write("\66\2\2\u00f6\u00f7\5^\60\2\u00f7\u00f8\7\67\2\2\u00f8")
        buf.write("\u00f9\7>\2\2\u00f9%\3\2\2\2\u00fa\u00fb\7:\2\2\u00fb")
        buf.write("\u00fc\5b\62\2\u00fc\u00fd\7;\2\2\u00fd\'\3\2\2\2\u00fe")
        buf.write("\u0101\7@\2\2\u00ff\u0101\5N(\2\u0100\u00fe\3\2\2\2\u0100")
        buf.write("\u00ff\3\2\2\2\u0101)\3\2\2\2\u0102\u010d\5,\27\2\u0103")
        buf.write("\u010d\5.\30\2\u0104\u010d\5\60\31\2\u0105\u010d\5\62")
        buf.write("\32\2\u0106\u010d\5\64\33\2\u0107\u010d\5\66\34\2\u0108")
        buf.write("\u010d\58\35\2\u0109\u010d\5:\36\2\u010a\u010d\5<\37\2")
        buf.write("\u010b\u010d\5> \2\u010c\u0102\3\2\2\2\u010c\u0103\3\2")
        buf.write("\2\2\u010c\u0104\3\2\2\2\u010c\u0105\3\2\2\2\u010c\u0106")
        buf.write("\3\2\2\2\u010c\u0107\3\2\2\2\u010c\u0108\3\2\2\2\u010c")
        buf.write("\u0109\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010b\3\2\2\2")
        buf.write("\u010d+\3\2\2\2\u010e\u010f\7\3\2\2\u010f\u0110\7\66\2")
        buf.write("\2\u0110\u0111\7\67\2\2\u0111\u0112\7>\2\2\u0112-\3\2")
        buf.write("\2\2\u0113\u0114\7\4\2\2\u0114\u0115\7\66\2\2\u0115\u0116")
        buf.write("\7@\2\2\u0116\u0117\7?\2\2\u0117\u0118\7\23\2\2\u0118")
        buf.write("\u0119\7\67\2\2\u0119\u011a\7>\2\2\u011a/\3\2\2\2\u011b")
        buf.write("\u011c\7\5\2\2\u011c\u011d\7\66\2\2\u011d\u011e\7\67\2")
        buf.write("\2\u011e\u011f\7>\2\2\u011f\u0120\7>\2\2\u0120\61\3\2")
        buf.write("\2\2\u0121\u0122\7\6\2\2\u0122\u0123\7\66\2\2\u0123\u0124")
        buf.write("\7@\2\2\u0124\u0125\7?\2\2\u0125\u0126\7\27\2\2\u0126")
        buf.write("\u0127\7\67\2\2\u0127\u0128\7>\2\2\u0128\63\3\2\2\2\u0129")
        buf.write("\u012a\7\7\2\2\u012a\u012b\7\66\2\2\u012b\u012c\7\67\2")
        buf.write("\2\u012c\u012d\7>\2\2\u012d\65\3\2\2\2\u012e\u012f\7\b")
        buf.write("\2\2\u012f\u0130\7\66\2\2\u0130\u0131\7@\2\2\u0131\u0132")
        buf.write("\7?\2\2\u0132\u0133\7\32\2\2\u0133\u0134\7\67\2\2\u0134")
        buf.write("\u0135\7>\2\2\u0135\67\3\2\2\2\u0136\u0137\7\t\2\2\u0137")
        buf.write("\u0138\7\66\2\2\u0138\u0139\7\67\2\2\u0139\u013a\7>\2")
        buf.write("\2\u013a9\3\2\2\2\u013b\u013c\7\n\2\2\u013c\u013d\7\66")
        buf.write("\2\2\u013d\u013e\7@\2\2\u013e\u013f\7?\2\2\u013f\u0140")
        buf.write("\7\34\2\2\u0140\u0141\7\67\2\2\u0141\u0142\7>\2\2\u0142")
        buf.write(";\3\2\2\2\u0143\u0144\7\13\2\2\u0144\u0145\7\66\2\2\u0145")
        buf.write("\u0146\5X-\2\u0146\u0147\7\67\2\2\u0147\u0148\7>\2\2\u0148")
        buf.write("=\3\2\2\2\u0149\u014a\7\f\2\2\u014a\u014b\7\66\2\2\u014b")
        buf.write("\u014c\7\67\2\2\u014c\u014d\7>\2\2\u014d?\3\2\2\2\u014e")
        buf.write("\u014f\5B\"\2\u014f\u0150\7\62\2\2\u0150\u0151\5B\"\2")
        buf.write("\u0151\u0154\3\2\2\2\u0152\u0154\5B\"\2\u0153\u014e\3")
        buf.write("\2\2\2\u0153\u0152\3\2\2\2\u0154A\3\2\2\2\u0155\u0156")
        buf.write("\5D#\2\u0156\u0157\t\2\2\2\u0157\u0158\5D#\2\u0158\u015b")
        buf.write("\3\2\2\2\u0159\u015b\5D#\2\u015a\u0155\3\2\2\2\u015a\u0159")
        buf.write("\3\2\2\2\u015bC\3\2\2\2\u015c\u015d\b#\1\2\u015d\u015e")
        buf.write("\5F$\2\u015e\u0164\3\2\2\2\u015f\u0160\f\4\2\2\u0160\u0161")
        buf.write("\t\3\2\2\u0161\u0163\5F$\2\u0162\u015f\3\2\2\2\u0163\u0166")
        buf.write("\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165")
        buf.write("E\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u0168\b$\1\2\u0168")
        buf.write("\u0169\5H%\2\u0169\u016f\3\2\2\2\u016a\u016b\f\4\2\2\u016b")
        buf.write("\u016c\t\4\2\2\u016c\u016e\5H%\2\u016d\u016a\3\2\2\2\u016e")
        buf.write("\u0171\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2\2")
        buf.write("\u0170G\3\2\2\2\u0171\u016f\3\2\2\2\u0172\u0173\b%\1\2")
        buf.write("\u0173\u0174\5J&\2\u0174\u017a\3\2\2\2\u0175\u0176\f\4")
        buf.write("\2\2\u0176\u0177\t\5\2\2\u0177\u0179\5J&\2\u0178\u0175")
        buf.write("\3\2\2\2\u0179\u017c\3\2\2\2\u017a\u0178\3\2\2\2\u017a")
        buf.write("\u017b\3\2\2\2\u017bI\3\2\2\2\u017c\u017a\3\2\2\2\u017d")
        buf.write("\u018b\7\r\2\2\u017e\u018b\7\17\2\2\u017f\u018b\7\16\2")
        buf.write("\2\u0180\u018b\7\20\2\2\u0181\u018b\5R*\2\u0182\u018b")
        buf.write("\7@\2\2\u0183\u0184\7+\2\2\u0184\u018b\7@\2\2\u0185\u0186")
        buf.write("\7\'\2\2\u0186\u018b\7@\2\2\u0187\u018b\5P)\2\u0188\u018b")
        buf.write("\5N(\2\u0189\u018b\5L\'\2\u018a\u017d\3\2\2\2\u018a\u017e")
        buf.write("\3\2\2\2\u018a\u017f\3\2\2\2\u018a\u0180\3\2\2\2\u018a")
        buf.write("\u0181\3\2\2\2\u018a\u0182\3\2\2\2\u018a\u0183\3\2\2\2")
        buf.write("\u018a\u0185\3\2\2\2\u018a\u0187\3\2\2\2\u018a\u0188\3")
        buf.write("\2\2\2\u018a\u0189\3\2\2\2\u018bK\3\2\2\2\u018c\u018d")
        buf.write("\7\66\2\2\u018d\u018e\5@!\2\u018e\u018f\7\67\2\2\u018f")
        buf.write("M\3\2\2\2\u0190\u0191\7@\2\2\u0191\u0192\78\2\2\u0192")
        buf.write("\u0193\5X-\2\u0193\u0194\79\2\2\u0194O\3\2\2\2\u0195\u0196")
        buf.write("\7@\2\2\u0196\u0197\7\66\2\2\u0197\u0198\5^\60\2\u0198")
        buf.write("\u0199\7\67\2\2\u0199Q\3\2\2\2\u019a\u019b\7:\2\2\u019b")
        buf.write("\u019c\5X-\2\u019c\u019d\7;\2\2\u019dS\3\2\2\2\u019e\u019f")
        buf.write("\b+\1\2\u019f\u01a0\7\r\2\2\u01a0\u01a6\3\2\2\2\u01a1")
        buf.write("\u01a2\f\4\2\2\u01a2\u01a3\7=\2\2\u01a3\u01a5\7\r\2\2")
        buf.write("\u01a4\u01a1\3\2\2\2\u01a5\u01a8\3\2\2\2\u01a6\u01a4\3")
        buf.write("\2\2\2\u01a6\u01a7\3\2\2\2\u01a7U\3\2\2\2\u01a8\u01a6")
        buf.write("\3\2\2\2\u01a9\u01aa\b,\1\2\u01aa\u01ab\7@\2\2\u01ab\u01b1")
        buf.write("\3\2\2\2\u01ac\u01ad\f\4\2\2\u01ad\u01ae\7=\2\2\u01ae")
        buf.write("\u01b0\7@\2\2\u01af\u01ac\3\2\2\2\u01b0\u01b3\3\2\2\2")
        buf.write("\u01b1\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2W\3\2\2")
        buf.write("\2\u01b3\u01b1\3\2\2\2\u01b4\u01b5\b-\1\2\u01b5\u01b6")
        buf.write("\5@!\2\u01b6\u01bc\3\2\2\2\u01b7\u01b8\f\4\2\2\u01b8\u01b9")
        buf.write("\7=\2\2\u01b9\u01bb\5@!\2\u01ba\u01b7\3\2\2\2\u01bb\u01be")
        buf.write("\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd")
        buf.write("Y\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf\u01c2\5\\/\2\u01c0")
        buf.write("\u01c2\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c0\3\2\2\2")
        buf.write("\u01c2[\3\2\2\2\u01c3\u01c4\b/\1\2\u01c4\u01c5\5\f\7\2")
        buf.write("\u01c5\u01cb\3\2\2\2\u01c6\u01c7\f\4\2\2\u01c7\u01c8\7")
        buf.write("=\2\2\u01c8\u01ca\5\f\7\2\u01c9\u01c6\3\2\2\2\u01ca\u01cd")
        buf.write("\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc")
        buf.write("]\3\2\2\2\u01cd\u01cb\3\2\2\2\u01ce\u01d1\5`\61\2\u01cf")
        buf.write("\u01d1\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01cf\3\2\2\2")
        buf.write("\u01d1_\3\2\2\2\u01d2\u01d3\b\61\1\2\u01d3\u01d4\5@!\2")
        buf.write("\u01d4\u01da\3\2\2\2\u01d5\u01d6\f\4\2\2\u01d6\u01d7\7")
        buf.write("=\2\2\u01d7\u01d9\5@!\2\u01d8\u01d5\3\2\2\2\u01d9\u01dc")
        buf.write("\3\2\2\2\u01da\u01d8\3\2\2\2\u01da\u01db\3\2\2\2\u01db")
        buf.write("a\3\2\2\2\u01dc\u01da\3\2\2\2\u01dd\u01e0\5d\63\2\u01de")
        buf.write("\u01e0\3\2\2\2\u01df\u01dd\3\2\2\2\u01df\u01de\3\2\2\2")
        buf.write("\u01e0c\3\2\2\2\u01e1\u01e2\b\63\1\2\u01e2\u01e3\5f\64")
        buf.write("\2\u01e3\u01e8\3\2\2\2\u01e4\u01e5\f\4\2\2\u01e5\u01e7")
        buf.write("\5f\64\2\u01e6\u01e4\3\2\2\2\u01e7\u01ea\3\2\2\2\u01e8")
        buf.write("\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9e\3\2\2\2\u01ea")
        buf.write("\u01e8\3\2\2\2\u01eb\u01ee\5\22\n\2\u01ec\u01ee\5\b\5")
        buf.write("\2\u01ed\u01eb\3\2\2\2\u01ed\u01ec\3\2\2\2\u01eeg\3\2")
        buf.write("\2\2\u01ef\u01f0\t\6\2\2\u01f0i\3\2\2\2\u01f1\u01f2\7")
        buf.write("\25\2\2\u01f2\u01f3\78\2\2\u01f3\u01f4\5T+\2\u01f4\u01f5")
        buf.write("\79\2\2\u01f5\u01f6\7!\2\2\u01f6\u01f7\5h\65\2\u01f7k")
        buf.write("\3\2\2\2\u01f8\u01f9\7\24\2\2\u01f9m\3\2\2\2\u01fa\u01fb")
        buf.write("\7\21\2\2\u01fbo\3\2\2\2\u01fc\u0201\5h\65\2\u01fd\u0201")
        buf.write("\5j\66\2\u01fe\u0201\5l\67\2\u01ff\u0201\5n8\2\u0200\u01fc")
        buf.write("\3\2\2\2\u0200\u01fd\3\2\2\2\u0200\u01fe\3\2\2\2\u0200")
        buf.write("\u01ff\3\2\2\2\u0201q\3\2\2\2\36|\u0082\u008c\u009a\u009d")
        buf.write("\u00a0\u00b2\u00bf\u00f0\u0100\u010c\u0153\u015a\u0164")
        buf.write("\u016f\u017a\u018a\u01a6\u01b1\u01bc\u01c1\u01cb\u01d0")
        buf.write("\u01da\u01df\u01e8\u01ed\u0200")
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
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_initialization = 4
    RULE_paramdecl = 5
    RULE_funcdecl = 6
    RULE_prototype = 7
    RULE_statement = 8
    RULE_assignstmt = 9
    RULE_ifstmt = 10
    RULE_forstmt = 11
    RULE_whilestmt = 12
    RULE_dowhilestmt = 13
    RULE_breakstmt = 14
    RULE_continuestmt = 15
    RULE_returnstmt = 16
    RULE_callstmt = 17
    RULE_blockstmt = 18
    RULE_scalar = 19
    RULE_specfunc = 20
    RULE_readInteger = 21
    RULE_printInteger = 22
    RULE_readFloat = 23
    RULE_writeFloat = 24
    RULE_readBoolean = 25
    RULE_printBoolean = 26
    RULE_readString = 27
    RULE_printString = 28
    RULE_sper = 29
    RULE_preventDefault = 30
    RULE_expression = 31
    RULE_term1 = 32
    RULE_term2 = 33
    RULE_term3 = 34
    RULE_term4 = 35
    RULE_term5 = 36
    RULE_subexpression = 37
    RULE_idxop = 38
    RULE_call = 39
    RULE_arrlit = 40
    RULE_intlist = 41
    RULE_idlist = 42
    RULE_expressionlist = 43
    RULE_paramlist = 44
    RULE_paramlistprime = 45
    RULE_arglist = 46
    RULE_arglistprime = 47
    RULE_linelist = 48
    RULE_linelistprime = 49
    RULE_line = 50
    RULE_atomtyp = 51
    RULE_arrtyp = 52
    RULE_voidtyp = 53
    RULE_autotyp = 54
    RULE_typ = 55

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "initialization", 
                   "paramdecl", "funcdecl", "prototype", "statement", "assignstmt", 
                   "ifstmt", "forstmt", "whilestmt", "dowhilestmt", "breakstmt", 
                   "continuestmt", "returnstmt", "callstmt", "blockstmt", 
                   "scalar", "specfunc", "readInteger", "printInteger", 
                   "readFloat", "writeFloat", "readBoolean", "printBoolean", 
                   "readString", "printString", "sper", "preventDefault", 
                   "expression", "term1", "term2", "term3", "term4", "term5", 
                   "subexpression", "idxop", "call", "arrlit", "intlist", 
                   "idlist", "expressionlist", "paramlist", "paramlistprime", 
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
            self.state = 112
            self.decllist(0)
            self.state = 113
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

        def decl(self):
            return self.getTypedRuleContext(MT22Parser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(MT22Parser.DecllistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)



    def decllist(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.DecllistContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_decllist, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.decl()
            self._ctx.stop = self._input.LT(-1)
            self.state = 122
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.DecllistContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_decllist)
                    self.state = 118
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 119
                    self.decl() 
                self.state = 124
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

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
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.funcdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 127
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
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.idlist(0)
                self.state = 131
                self.match(MT22Parser.COLON)
                self.state = 132
                self.typ()
                self.state = 133
                self.match(MT22Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.initialization()
                self.state = 136
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
        self.enterRule(localctx, 8, self.RULE_initialization)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(MT22Parser.ID)
                self.state = 141
                self.match(MT22Parser.COMMA)
                self.state = 142
                self.initialization()
                self.state = 143
                self.match(MT22Parser.COMMA)
                self.state = 144
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.match(MT22Parser.ID)
                self.state = 147
                self.match(MT22Parser.COLON)
                self.state = 148
                self.typ()
                self.state = 149
                self.match(MT22Parser.EQ)
                self.state = 150
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
        self.enterRule(localctx, 10, self.RULE_paramdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 154
                self.match(MT22Parser.INHERIT)


            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.OUT:
                self.state = 157
                self.match(MT22Parser.OUT)


            self.state = 160
            self.match(MT22Parser.ID)
            self.state = 161
            self.match(MT22Parser.COLON)
            self.state = 162
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
        self.enterRule(localctx, 12, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.prototype()
            self.state = 165
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
        self.enterRule(localctx, 14, self.RULE_prototype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(MT22Parser.ID)
            self.state = 168
            self.match(MT22Parser.COLON)
            self.state = 169
            self.match(MT22Parser.FUNCTION)
            self.state = 170
            self.typ()
            self.state = 171
            self.match(MT22Parser.LB1)
            self.state = 172
            self.paramlist()
            self.state = 173
            self.match(MT22Parser.RB1)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 174
                self.match(MT22Parser.INHERIT)
                self.state = 175
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
        self.enterRule(localctx, 16, self.RULE_statement)
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.assignstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.ifstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 180
                self.forstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 181
                self.whilestmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 182
                self.dowhilestmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 183
                self.breakstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 184
                self.continuestmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 185
                self.returnstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 186
                self.callstmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 187
                self.blockstmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 188
                self.specfunc()
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


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = MT22Parser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.scalar()
            self.state = 192
            self.match(MT22Parser.EQ)
            self.state = 193
            self.expression()
            self.state = 194
            self.match(MT22Parser.SEMI)
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
        self.enterRule(localctx, 20, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(MT22Parser.IF)
            self.state = 197
            self.match(MT22Parser.LB1)
            self.state = 198
            self.expression()
            self.state = 199
            self.match(MT22Parser.RB1)
            self.state = 200
            self.statement()

            self.state = 201
            self.match(MT22Parser.ELSE)
            self.state = 202
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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementContext,i)


        def RB1(self):
            return self.getToken(MT22Parser.RB1, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = MT22Parser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(MT22Parser.FOR)
            self.state = 205
            self.match(MT22Parser.LB1)
            self.state = 206
            self.scalar()
            self.state = 207
            self.match(MT22Parser.EQ)
            self.state = 208
            self.expression()
            self.state = 209
            self.match(MT22Parser.COMMA)
            self.state = 210
            self.expression()
            self.state = 211
            self.match(MT22Parser.COMMA)
            self.state = 212
            self.statement()
            self.state = 213
            self.match(MT22Parser.RB1)
            self.state = 214
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
        self.enterRule(localctx, 24, self.RULE_whilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(MT22Parser.WHILE)
            self.state = 217
            self.match(MT22Parser.LB1)
            self.state = 218
            self.expression()
            self.state = 219
            self.match(MT22Parser.RB1)
            self.state = 220
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

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_dowhilestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDowhilestmt" ):
                return visitor.visitDowhilestmt(self)
            else:
                return visitor.visitChildren(self)




    def dowhilestmt(self):

        localctx = MT22Parser.DowhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_dowhilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(MT22Parser.DO)
            self.state = 223
            self.blockstmt()
            self.state = 224
            self.match(MT22Parser.WHILE)
            self.state = 225
            self.match(MT22Parser.LB1)
            self.state = 226
            self.expression()
            self.state = 227
            self.match(MT22Parser.RB1)
            self.state = 228
            self.match(MT22Parser.SEMI)
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

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = MT22Parser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(MT22Parser.BREAK)
            self.state = 231
            self.match(MT22Parser.SEMI)
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

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = MT22Parser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(MT22Parser.CONTINUE)
            self.state = 234
            self.match(MT22Parser.SEMI)
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

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

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
        self.enterRule(localctx, 32, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(MT22Parser.RETURN)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTLIT) | (1 << MT22Parser.BOOLLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.STRINGLIT) | (1 << MT22Parser.SUB) | (1 << MT22Parser.NOT) | (1 << MT22Parser.LB1) | (1 << MT22Parser.LB3) | (1 << MT22Parser.ID))) != 0):
                self.state = 237
                self.expression()


            self.state = 240
            self.match(MT22Parser.SEMI)
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

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_callstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




    def callstmt(self):

        localctx = MT22Parser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(MT22Parser.ID)
            self.state = 243
            self.match(MT22Parser.LB1)
            self.state = 244
            self.arglist()
            self.state = 245
            self.match(MT22Parser.RB1)
            self.state = 246
            self.match(MT22Parser.SEMI)
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
        self.enterRule(localctx, 36, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(MT22Parser.LB3)
            self.state = 249
            self.linelist()
            self.state = 250
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
        self.enterRule(localctx, 38, self.RULE_scalar)
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.match(MT22Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
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
        self.enterRule(localctx, 40, self.RULE_specfunc)
        try:
            self.state = 266
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.readInteger()
                pass
            elif token in [MT22Parser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.printInteger()
                pass
            elif token in [MT22Parser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.readFloat()
                pass
            elif token in [MT22Parser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 259
                self.writeFloat()
                pass
            elif token in [MT22Parser.T__4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 260
                self.readBoolean()
                pass
            elif token in [MT22Parser.T__5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 261
                self.printBoolean()
                pass
            elif token in [MT22Parser.T__6]:
                self.enterOuterAlt(localctx, 7)
                self.state = 262
                self.readString()
                pass
            elif token in [MT22Parser.T__7]:
                self.enterOuterAlt(localctx, 8)
                self.state = 263
                self.printString()
                pass
            elif token in [MT22Parser.T__8]:
                self.enterOuterAlt(localctx, 9)
                self.state = 264
                self.sper()
                pass
            elif token in [MT22Parser.T__9]:
                self.enterOuterAlt(localctx, 10)
                self.state = 265
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

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_readInteger

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadInteger" ):
                return visitor.visitReadInteger(self)
            else:
                return visitor.visitChildren(self)




    def readInteger(self):

        localctx = MT22Parser.ReadIntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_readInteger)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(MT22Parser.T__0)
            self.state = 269
            self.match(MT22Parser.LB1)
            self.state = 270
            self.match(MT22Parser.RB1)
            self.state = 271
            self.match(MT22Parser.SEMI)
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

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def RB1(self):
            return self.getToken(MT22Parser.RB1, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_printInteger

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintInteger" ):
                return visitor.visitPrintInteger(self)
            else:
                return visitor.visitChildren(self)




    def printInteger(self):

        localctx = MT22Parser.PrintIntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_printInteger)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(MT22Parser.T__1)
            self.state = 274
            self.match(MT22Parser.LB1)
            self.state = 275
            self.match(MT22Parser.ID)
            self.state = 276
            self.match(MT22Parser.COLON)
            self.state = 277
            self.match(MT22Parser.INTEGER)
            self.state = 278
            self.match(MT22Parser.RB1)
            self.state = 279
            self.match(MT22Parser.SEMI)
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

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.SEMI)
            else:
                return self.getToken(MT22Parser.SEMI, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_readFloat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadFloat" ):
                return visitor.visitReadFloat(self)
            else:
                return visitor.visitChildren(self)




    def readFloat(self):

        localctx = MT22Parser.ReadFloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_readFloat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(MT22Parser.T__2)
            self.state = 282
            self.match(MT22Parser.LB1)
            self.state = 283
            self.match(MT22Parser.RB1)
            self.state = 284
            self.match(MT22Parser.SEMI)
            self.state = 285
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

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def RB1(self):
            return self.getToken(MT22Parser.RB1, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_writeFloat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteFloat" ):
                return visitor.visitWriteFloat(self)
            else:
                return visitor.visitChildren(self)




    def writeFloat(self):

        localctx = MT22Parser.WriteFloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_writeFloat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(MT22Parser.T__3)
            self.state = 288
            self.match(MT22Parser.LB1)
            self.state = 289
            self.match(MT22Parser.ID)
            self.state = 290
            self.match(MT22Parser.COLON)
            self.state = 291
            self.match(MT22Parser.FLOAT)
            self.state = 292
            self.match(MT22Parser.RB1)
            self.state = 293
            self.match(MT22Parser.SEMI)
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

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_readBoolean

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadBoolean" ):
                return visitor.visitReadBoolean(self)
            else:
                return visitor.visitChildren(self)




    def readBoolean(self):

        localctx = MT22Parser.ReadBooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_readBoolean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(MT22Parser.T__4)
            self.state = 296
            self.match(MT22Parser.LB1)
            self.state = 297
            self.match(MT22Parser.RB1)
            self.state = 298
            self.match(MT22Parser.SEMI)
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

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def RB1(self):
            return self.getToken(MT22Parser.RB1, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_printBoolean

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintBoolean" ):
                return visitor.visitPrintBoolean(self)
            else:
                return visitor.visitChildren(self)




    def printBoolean(self):

        localctx = MT22Parser.PrintBooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_printBoolean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(MT22Parser.T__5)
            self.state = 301
            self.match(MT22Parser.LB1)
            self.state = 302
            self.match(MT22Parser.ID)
            self.state = 303
            self.match(MT22Parser.COLON)
            self.state = 304
            self.match(MT22Parser.BOOLEAN)
            self.state = 305
            self.match(MT22Parser.RB1)
            self.state = 306
            self.match(MT22Parser.SEMI)
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

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_readString

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadString" ):
                return visitor.visitReadString(self)
            else:
                return visitor.visitChildren(self)




    def readString(self):

        localctx = MT22Parser.ReadStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_readString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(MT22Parser.T__6)
            self.state = 309
            self.match(MT22Parser.LB1)
            self.state = 310
            self.match(MT22Parser.RB1)
            self.state = 311
            self.match(MT22Parser.SEMI)
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

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def RB1(self):
            return self.getToken(MT22Parser.RB1, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_printString

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintString" ):
                return visitor.visitPrintString(self)
            else:
                return visitor.visitChildren(self)




    def printString(self):

        localctx = MT22Parser.PrintStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_printString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(MT22Parser.T__7)
            self.state = 314
            self.match(MT22Parser.LB1)
            self.state = 315
            self.match(MT22Parser.ID)
            self.state = 316
            self.match(MT22Parser.COLON)
            self.state = 317
            self.match(MT22Parser.STRING)
            self.state = 318
            self.match(MT22Parser.RB1)
            self.state = 319
            self.match(MT22Parser.SEMI)
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

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_sper

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSper" ):
                return visitor.visitSper(self)
            else:
                return visitor.visitChildren(self)




    def sper(self):

        localctx = MT22Parser.SperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_sper)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(MT22Parser.T__8)
            self.state = 322
            self.match(MT22Parser.LB1)
            self.state = 323
            self.expressionlist(0)
            self.state = 324
            self.match(MT22Parser.RB1)
            self.state = 325
            self.match(MT22Parser.SEMI)
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

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_preventDefault

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreventDefault" ):
                return visitor.visitPreventDefault(self)
            else:
                return visitor.visitChildren(self)




    def preventDefault(self):

        localctx = MT22Parser.PreventDefaultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_preventDefault)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(MT22Parser.T__9)
            self.state = 328
            self.match(MT22Parser.LB1)
            self.state = 329
            self.match(MT22Parser.RB1)
            self.state = 330
            self.match(MT22Parser.SEMI)
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
        self.enterRule(localctx, 62, self.RULE_expression)
        try:
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.term1()
                self.state = 333
                self.match(MT22Parser.CONCAT)
                self.state = 334
                self.term1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
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
        self.enterRule(localctx, 64, self.RULE_term1)
        self._la = 0 # Token type
        try:
            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.term2(0)
                self.state = 340
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.SM) | (1 << MT22Parser.SME) | (1 << MT22Parser.BG) | (1 << MT22Parser.BGE) | (1 << MT22Parser.EQUAL) | (1 << MT22Parser.NEQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 341
                self.term2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
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
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_term2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.term3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 354
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Term2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term2)
                    self.state = 349
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 350
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.AND or _la==MT22Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 351
                    self.term3(0) 
                self.state = 356
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_term3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.term4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 365
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Term3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term3)
                    self.state = 360
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 361
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ADD or _la==MT22Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 362
                    self.term4(0) 
                self.state = 367
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_term4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.term5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 376
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Term4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term4)
                    self.state = 371
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 372
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MUL) | (1 << MT22Parser.DIV) | (1 << MT22Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 373
                    self.term5() 
                self.state = 378
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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


        def getRuleIndex(self):
            return MT22Parser.RULE_term5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm5" ):
                return visitor.visitTerm5(self)
            else:
                return visitor.visitChildren(self)




    def term5(self):

        localctx = MT22Parser.Term5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_term5)
        try:
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.match(MT22Parser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 380
                self.match(MT22Parser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 381
                self.match(MT22Parser.BOOLLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 382
                self.match(MT22Parser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 383
                self.arrlit()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 384
                self.match(MT22Parser.ID)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 385
                self.match(MT22Parser.NOT)
                self.state = 386
                self.match(MT22Parser.ID)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 387
                self.match(MT22Parser.SUB)
                self.state = 388
                self.match(MT22Parser.ID)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 389
                self.call()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 390
                self.idxop()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 391
                self.subexpression()
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
        self.enterRule(localctx, 74, self.RULE_subexpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(MT22Parser.LB1)
            self.state = 395
            self.expression()
            self.state = 396
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
        self.enterRule(localctx, 76, self.RULE_idxop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.match(MT22Parser.ID)
            self.state = 399
            self.match(MT22Parser.LB2)
            self.state = 400
            self.expressionlist(0)
            self.state = 401
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
        self.enterRule(localctx, 78, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(MT22Parser.ID)
            self.state = 404
            self.match(MT22Parser.LB1)
            self.state = 405
            self.arglist()
            self.state = 406
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
        self.enterRule(localctx, 80, self.RULE_arrlit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(MT22Parser.LB3)
            self.state = 409
            self.expressionlist(0)
            self.state = 410
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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_intlist, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.match(MT22Parser.INTLIT)
            self._ctx.stop = self._input.LT(-1)
            self.state = 420
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.IntlistContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_intlist)
                    self.state = 415
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 416
                    self.match(MT22Parser.COMMA)
                    self.state = 417
                    self.match(MT22Parser.INTLIT) 
                self.state = 422
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_idlist, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(MT22Parser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 431
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.IdlistContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_idlist)
                    self.state = 426
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 427
                    self.match(MT22Parser.COMMA)
                    self.state = 428
                    self.match(MT22Parser.ID) 
                self.state = 433
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expressionlist, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 442
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.ExpressionlistContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expressionlist)
                    self.state = 437
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 438
                    self.match(MT22Parser.COMMA)
                    self.state = 439
                    self.expression() 
                self.state = 444
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        self.enterRule(localctx, 88, self.RULE_paramlist)
        try:
            self.state = 447
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.OUT, MT22Parser.INHERIT, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 445
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
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_paramlistprime, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.paramdecl()
            self._ctx.stop = self._input.LT(-1)
            self.state = 457
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.ParamlistprimeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_paramlistprime)
                    self.state = 452
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 453
                    self.match(MT22Parser.COMMA)
                    self.state = 454
                    self.paramdecl() 
                self.state = 459
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        self.enterRule(localctx, 92, self.RULE_arglist)
        try:
            self.state = 462
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INTLIT, MT22Parser.BOOLLIT, MT22Parser.FLOATLIT, MT22Parser.STRINGLIT, MT22Parser.SUB, MT22Parser.NOT, MT22Parser.LB1, MT22Parser.LB3, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
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
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_arglistprime, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 472
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.ArglistprimeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arglistprime)
                    self.state = 467
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 468
                    self.match(MT22Parser.COMMA)
                    self.state = 469
                    self.expression() 
                self.state = 474
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
        self.enterRule(localctx, 96, self.RULE_linelist)
        try:
            self.state = 477
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.T__0, MT22Parser.T__1, MT22Parser.T__2, MT22Parser.T__3, MT22Parser.T__4, MT22Parser.T__5, MT22Parser.T__6, MT22Parser.T__7, MT22Parser.T__8, MT22Parser.T__9, MT22Parser.BREAK, MT22Parser.RETURN, MT22Parser.FOR, MT22Parser.CONTINUE, MT22Parser.DO, MT22Parser.IF, MT22Parser.WHILE, MT22Parser.LB3, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 475
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
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_linelistprime, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.line()
            self._ctx.stop = self._input.LT(-1)
            self.state = 486
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.LinelistprimeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_linelistprime)
                    self.state = 482
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 483
                    self.line() 
                self.state = 488
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
        self.enterRule(localctx, 100, self.RULE_line)
        try:
            self.state = 491
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 490
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
        self.enterRule(localctx, 102, self.RULE_atomtyp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
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
        self.enterRule(localctx, 104, self.RULE_arrtyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.match(MT22Parser.ARRAY)
            self.state = 496
            self.match(MT22Parser.LB2)
            self.state = 497
            self.intlist(0)
            self.state = 498
            self.match(MT22Parser.RB2)
            self.state = 499
            self.match(MT22Parser.OF)
            self.state = 500
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
        self.enterRule(localctx, 106, self.RULE_voidtyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
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
        self.enterRule(localctx, 108, self.RULE_autotyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
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
        self.enterRule(localctx, 110, self.RULE_typ)
        try:
            self.state = 510
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INTEGER, MT22Parser.FLOAT, MT22Parser.BOOLEAN, MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 506
                self.atomtyp()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 507
                self.arrtyp()
                pass
            elif token in [MT22Parser.VOID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 508
                self.voidtyp()
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 4)
                self.state = 509
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
        self._predicates[1] = self.decllist_sempred
        self._predicates[33] = self.term2_sempred
        self._predicates[34] = self.term3_sempred
        self._predicates[35] = self.term4_sempred
        self._predicates[41] = self.intlist_sempred
        self._predicates[42] = self.idlist_sempred
        self._predicates[43] = self.expressionlist_sempred
        self._predicates[45] = self.paramlistprime_sempred
        self._predicates[47] = self.arglistprime_sempred
        self._predicates[49] = self.linelistprime_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def decllist_sempred(self, localctx:DecllistContext, predIndex:int):
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
         




