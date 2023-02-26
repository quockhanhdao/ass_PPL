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
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\7\f\u010c")
        buf.write("\n\f\f\f\16\f\u010f\13\f\3\f\3\f\5\f\u0113\n\f\3\r\3\r")
        buf.write("\5\r\u0117\n\r\3\16\3\16\3\16\5\16\u011c\n\16\3\16\5\16")
        buf.write("\u011f\n\16\3\16\3\16\3\17\3\17\3\17\7\17\u0126\n\17\f")
        buf.write("\17\16\17\u0129\13\17\3\17\5\17\u012c\n\17\3\20\3\20\3")
        buf.write("\20\3\20\7\20\u0132\n\20\f\20\16\20\u0135\13\20\3\20\5")
        buf.write("\20\u0138\n\20\3\21\3\21\5\21\u013c\n\21\3\21\3\21\3\21")
        buf.write("\7\21\u0141\n\21\f\21\16\21\u0144\13\21\3\21\5\21\u0147")
        buf.write("\n\21\3\22\3\22\5\22\u014b\n\22\3\22\3\22\3\22\3\23\3")
        buf.write("\23\6\23\u0152\n\23\r\23\16\23\u0153\3\24\3\24\3\24\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3")
        buf.write("%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\38\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3")
        buf.write("@\3@\3A\3A\3B\3B\3C\3C\3D\3D\7D\u0211\nD\fD\16D\u0214")
        buf.write("\13D\3E\6E\u0217\nE\rE\16E\u0218\3E\3E\3F\3F\3F\3F\7F")
        buf.write("\u0221\nF\fF\16F\u0224\13F\3F\3F\3G\3G\3G\3G\7G\u022c")
        buf.write("\nG\fG\16G\u022f\13G\3G\3G\3G\3G\3G\3H\3H\3H\3I\3I\7I")
        buf.write("\u023b\nI\fI\16I\u023e\13I\3I\5I\u0241\nI\3I\3I\3J\3J")
        buf.write("\7J\u0247\nJ\fJ\16J\u024a\13J\3J\3J\3J\3J\3J\3\u022d\2")
        buf.write("K\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\2\37\2!\2#\20%\2\'\2)\21+\22-\23/\24\61\25")
        buf.write("\63\26\65\27\67\309\31;\32=\33?\34A\35C\36E\37G I!K\"")
        buf.write("M#O$Q%S&U\'W(Y)[*]+_,a-c.e/g\60i\61k\62m\63o\64q\65s\66")
        buf.write("u\67w8y9{:};\177<\u0081=\u0083>\u0085?\u0087@\u0089A\u008b")
        buf.write("B\u008dC\u008fD\u0091E\u0093F\3\2\16\3\2\62;\3\2\63;\4")
        buf.write("\2\62;aa\4\2GGgg\4\2--//\6\2\n\f\16\17$$^^\n\2$$))^^d")
        buf.write("dhhppttvv\5\2C\\aac|\6\2\62;C\\aac|\5\2\n\f\16\17\"\"")
        buf.write("\4\2\f\f\17\17\t\2$$^^ddhhppttvv\2\u0260\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2#\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2")
        buf.write("\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2")
        buf.write("\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\3\u0095\3\2\2\2\5\u00a1\3\2\2\2\7\u00ae\3\2\2")
        buf.write("\2\t\u00b8\3\2\2\2\13\u00c3\3\2\2\2\r\u00cf\3\2\2\2\17")
        buf.write("\u00dc\3\2\2\2\21\u00e7\3\2\2\2\23\u00f3\3\2\2\2\25\u00f9")
        buf.write("\3\2\2\2\27\u0112\3\2\2\2\31\u0116\3\2\2\2\33\u0118\3")
        buf.write("\2\2\2\35\u012b\3\2\2\2\37\u012d\3\2\2\2!\u0139\3\2\2")
        buf.write("\2#\u0148\3\2\2\2%\u0151\3\2\2\2\'\u0155\3\2\2\2)\u0158")
        buf.write("\3\2\2\2+\u015d\3\2\2\2-\u0163\3\2\2\2/\u016b\3\2\2\2")
        buf.write("\61\u0170\3\2\2\2\63\u0176\3\2\2\2\65\u017c\3\2\2\2\67")
        buf.write("\u0182\3\2\2\29\u0189\3\2\2\2;\u018d\3\2\2\2=\u0195\3")
        buf.write("\2\2\2?\u0199\3\2\2\2A\u01a0\3\2\2\2C\u01a9\3\2\2\2E\u01ac")
        buf.write("\3\2\2\2G\u01b5\3\2\2\2I\u01ba\3\2\2\2K\u01bd\3\2\2\2")
        buf.write("M\u01c2\3\2\2\2O\u01c5\3\2\2\2Q\u01cb\3\2\2\2S\u01d3\3")
        buf.write("\2\2\2U\u01d5\3\2\2\2W\u01d7\3\2\2\2Y\u01d9\3\2\2\2[\u01db")
        buf.write("\3\2\2\2]\u01dd\3\2\2\2_\u01df\3\2\2\2a\u01e1\3\2\2\2")
        buf.write("c\u01e4\3\2\2\2e\u01e6\3\2\2\2g\u01e9\3\2\2\2i\u01ec\3")
        buf.write("\2\2\2k\u01ef\3\2\2\2m\u01f2\3\2\2\2o\u01f5\3\2\2\2q\u01f8")
        buf.write("\3\2\2\2s\u01fa\3\2\2\2u\u01fc\3\2\2\2w\u01fe\3\2\2\2")
        buf.write("y\u0200\3\2\2\2{\u0202\3\2\2\2}\u0204\3\2\2\2\177\u0206")
        buf.write("\3\2\2\2\u0081\u0208\3\2\2\2\u0083\u020a\3\2\2\2\u0085")
        buf.write("\u020c\3\2\2\2\u0087\u020e\3\2\2\2\u0089\u0216\3\2\2\2")
        buf.write("\u008b\u021c\3\2\2\2\u008d\u0227\3\2\2\2\u008f\u0235\3")
        buf.write("\2\2\2\u0091\u0238\3\2\2\2\u0093\u0244\3\2\2\2\u0095\u0096")
        buf.write("\7t\2\2\u0096\u0097\7g\2\2\u0097\u0098\7c\2\2\u0098\u0099")
        buf.write("\7f\2\2\u0099\u009a\7K\2\2\u009a\u009b\7p\2\2\u009b\u009c")
        buf.write("\7v\2\2\u009c\u009d\7g\2\2\u009d\u009e\7i\2\2\u009e\u009f")
        buf.write("\7g\2\2\u009f\u00a0\7t\2\2\u00a0\4\3\2\2\2\u00a1\u00a2")
        buf.write("\7r\2\2\u00a2\u00a3\7t\2\2\u00a3\u00a4\7k\2\2\u00a4\u00a5")
        buf.write("\7p\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7\7K\2\2\u00a7\u00a8")
        buf.write("\7p\2\2\u00a8\u00a9\7v\2\2\u00a9\u00aa\7g\2\2\u00aa\u00ab")
        buf.write("\7i\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad\7t\2\2\u00ad\6")
        buf.write("\3\2\2\2\u00ae\u00af\7t\2\2\u00af\u00b0\7g\2\2\u00b0\u00b1")
        buf.write("\7c\2\2\u00b1\u00b2\7f\2\2\u00b2\u00b3\7H\2\2\u00b3\u00b4")
        buf.write("\7n\2\2\u00b4\u00b5\7q\2\2\u00b5\u00b6\7c\2\2\u00b6\u00b7")
        buf.write("\7v\2\2\u00b7\b\3\2\2\2\u00b8\u00b9\7y\2\2\u00b9\u00ba")
        buf.write("\7t\2\2\u00ba\u00bb\7k\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd")
        buf.write("\7g\2\2\u00bd\u00be\7H\2\2\u00be\u00bf\7n\2\2\u00bf\u00c0")
        buf.write("\7q\2\2\u00c0\u00c1\7c\2\2\u00c1\u00c2\7v\2\2\u00c2\n")
        buf.write("\3\2\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6")
        buf.write("\7c\2\2\u00c6\u00c7\7f\2\2\u00c7\u00c8\7D\2\2\u00c8\u00c9")
        buf.write("\7q\2\2\u00c9\u00ca\7q\2\2\u00ca\u00cb\7n\2\2\u00cb\u00cc")
        buf.write("\7g\2\2\u00cc\u00cd\7c\2\2\u00cd\u00ce\7p\2\2\u00ce\f")
        buf.write("\3\2\2\2\u00cf\u00d0\7r\2\2\u00d0\u00d1\7t\2\2\u00d1\u00d2")
        buf.write("\7k\2\2\u00d2\u00d3\7p\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5")
        buf.write("\7D\2\2\u00d5\u00d6\7q\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8")
        buf.write("\7n\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da\7c\2\2\u00da\u00db")
        buf.write("\7p\2\2\u00db\16\3\2\2\2\u00dc\u00dd\7t\2\2\u00dd\u00de")
        buf.write("\7g\2\2\u00de\u00df\7c\2\2\u00df\u00e0\7f\2\2\u00e0\u00e1")
        buf.write("\7U\2\2\u00e1\u00e2\7v\2\2\u00e2\u00e3\7t\2\2\u00e3\u00e4")
        buf.write("\7k\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7i\2\2\u00e6\20")
        buf.write("\3\2\2\2\u00e7\u00e8\7r\2\2\u00e8\u00e9\7t\2\2\u00e9\u00ea")
        buf.write("\7k\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed")
        buf.write("\7U\2\2\u00ed\u00ee\7v\2\2\u00ee\u00ef\7t\2\2\u00ef\u00f0")
        buf.write("\7k\2\2\u00f0\u00f1\7p\2\2\u00f1\u00f2\7i\2\2\u00f2\22")
        buf.write("\3\2\2\2\u00f3\u00f4\7u\2\2\u00f4\u00f5\7w\2\2\u00f5\u00f6")
        buf.write("\7r\2\2\u00f6\u00f7\7g\2\2\u00f7\u00f8\7t\2\2\u00f8\24")
        buf.write("\3\2\2\2\u00f9\u00fa\7r\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc")
        buf.write("\7g\2\2\u00fc\u00fd\7x\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff")
        buf.write("\7p\2\2\u00ff\u0100\7v\2\2\u0100\u0101\7F\2\2\u0101\u0102")
        buf.write("\7g\2\2\u0102\u0103\7h\2\2\u0103\u0104\7c\2\2\u0104\u0105")
        buf.write("\7w\2\2\u0105\u0106\7n\2\2\u0106\u0107\7v\2\2\u0107\26")
        buf.write("\3\2\2\2\u0108\u0113\t\2\2\2\u0109\u010d\t\3\2\2\u010a")
        buf.write("\u010c\t\4\2\2\u010b\u010a\3\2\2\2\u010c\u010f\3\2\2\2")
        buf.write("\u010d\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u0110\3")
        buf.write("\2\2\2\u010f\u010d\3\2\2\2\u0110\u0111\t\2\2\2\u0111\u0113")
        buf.write("\b\f\2\2\u0112\u0108\3\2\2\2\u0112\u0109\3\2\2\2\u0113")
        buf.write("\30\3\2\2\2\u0114\u0117\5G$\2\u0115\u0117\5+\26\2\u0116")
        buf.write("\u0114\3\2\2\2\u0116\u0115\3\2\2\2\u0117\32\3\2\2\2\u0118")
        buf.write("\u011e\5\35\17\2\u0119\u011f\5\37\20\2\u011a\u011c\5\37")
        buf.write("\20\2\u011b\u011a\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u011d")
        buf.write("\3\2\2\2\u011d\u011f\5!\21\2\u011e\u0119\3\2\2\2\u011e")
        buf.write("\u011b\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0121\b\16\3")
        buf.write("\2\u0121\34\3\2\2\2\u0122\u012c\t\2\2\2\u0123\u0127\t")
        buf.write("\3\2\2\u0124\u0126\t\4\2\2\u0125\u0124\3\2\2\2\u0126\u0129")
        buf.write("\3\2\2\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128")
        buf.write("\u012a\3\2\2\2\u0129\u0127\3\2\2\2\u012a\u012c\t\2\2\2")
        buf.write("\u012b\u0122\3\2\2\2\u012b\u0123\3\2\2\2\u012c\36\3\2")
        buf.write("\2\2\u012d\u0137\7\60\2\2\u012e\u0138\t\2\2\2\u012f\u0133")
        buf.write("\t\2\2\2\u0130\u0132\t\4\2\2\u0131\u0130\3\2\2\2\u0132")
        buf.write("\u0135\3\2\2\2\u0133\u0131\3\2\2\2\u0133\u0134\3\2\2\2")
        buf.write("\u0134\u0136\3\2\2\2\u0135\u0133\3\2\2\2\u0136\u0138\t")
        buf.write("\2\2\2\u0137\u012e\3\2\2\2\u0137\u012f\3\2\2\2\u0138 ")
        buf.write("\3\2\2\2\u0139\u013b\t\5\2\2\u013a\u013c\t\6\2\2\u013b")
        buf.write("\u013a\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u0146\3\2\2\2")
        buf.write("\u013d\u0147\t\2\2\2\u013e\u0142\t\2\2\2\u013f\u0141\t")
        buf.write("\4\2\2\u0140\u013f\3\2\2\2\u0141\u0144\3\2\2\2\u0142\u0140")
        buf.write("\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0145\3\2\2\2\u0144")
        buf.write("\u0142\3\2\2\2\u0145\u0147\t\2\2\2\u0146\u013d\3\2\2\2")
        buf.write("\u0146\u013e\3\2\2\2\u0147\"\3\2\2\2\u0148\u014a\7$\2")
        buf.write("\2\u0149\u014b\5%\23\2\u014a\u0149\3\2\2\2\u014a\u014b")
        buf.write("\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014d\7$\2\2\u014d")
        buf.write("\u014e\b\22\4\2\u014e$\3\2\2\2\u014f\u0152\n\7\2\2\u0150")
        buf.write("\u0152\5\'\24\2\u0151\u014f\3\2\2\2\u0151\u0150\3\2\2")
        buf.write("\2\u0152\u0153\3\2\2\2\u0153\u0151\3\2\2\2\u0153\u0154")
        buf.write("\3\2\2\2\u0154&\3\2\2\2\u0155\u0156\7^\2\2\u0156\u0157")
        buf.write("\t\b\2\2\u0157(\3\2\2\2\u0158\u0159\7c\2\2\u0159\u015a")
        buf.write("\7w\2\2\u015a\u015b\7v\2\2\u015b\u015c\7q\2\2\u015c*\3")
        buf.write("\2\2\2\u015d\u015e\7h\2\2\u015e\u015f\7c\2\2\u015f\u0160")
        buf.write("\7n\2\2\u0160\u0161\7u\2\2\u0161\u0162\7g\2\2\u0162,\3")
        buf.write("\2\2\2\u0163\u0164\7k\2\2\u0164\u0165\7p\2\2\u0165\u0166")
        buf.write("\7v\2\2\u0166\u0167\7g\2\2\u0167\u0168\7i\2\2\u0168\u0169")
        buf.write("\7g\2\2\u0169\u016a\7t\2\2\u016a.\3\2\2\2\u016b\u016c")
        buf.write("\7x\2\2\u016c\u016d\7q\2\2\u016d\u016e\7k\2\2\u016e\u016f")
        buf.write("\7f\2\2\u016f\60\3\2\2\2\u0170\u0171\7c\2\2\u0171\u0172")
        buf.write("\7t\2\2\u0172\u0173\7t\2\2\u0173\u0174\7c\2\2\u0174\u0175")
        buf.write("\7{\2\2\u0175\62\3\2\2\2\u0176\u0177\7d\2\2\u0177\u0178")
        buf.write("\7t\2\2\u0178\u0179\7g\2\2\u0179\u017a\7c\2\2\u017a\u017b")
        buf.write("\7m\2\2\u017b\64\3\2\2\2\u017c\u017d\7h\2\2\u017d\u017e")
        buf.write("\7n\2\2\u017e\u017f\7q\2\2\u017f\u0180\7c\2\2\u0180\u0181")
        buf.write("\7v\2\2\u0181\66\3\2\2\2\u0182\u0183\7t\2\2\u0183\u0184")
        buf.write("\7g\2\2\u0184\u0185\7v\2\2\u0185\u0186\7w\2\2\u0186\u0187")
        buf.write("\7t\2\2\u0187\u0188\7p\2\2\u01888\3\2\2\2\u0189\u018a")
        buf.write("\7q\2\2\u018a\u018b\7w\2\2\u018b\u018c\7v\2\2\u018c:\3")
        buf.write("\2\2\2\u018d\u018e\7d\2\2\u018e\u018f\7q\2\2\u018f\u0190")
        buf.write("\7q\2\2\u0190\u0191\7n\2\2\u0191\u0192\7g\2\2\u0192\u0193")
        buf.write("\7c\2\2\u0193\u0194\7p\2\2\u0194<\3\2\2\2\u0195\u0196")
        buf.write("\7h\2\2\u0196\u0197\7q\2\2\u0197\u0198\7t\2\2\u0198>\3")
        buf.write("\2\2\2\u0199\u019a\7u\2\2\u019a\u019b\7v\2\2\u019b\u019c")
        buf.write("\7t\2\2\u019c\u019d\7k\2\2\u019d\u019e\7p\2\2\u019e\u019f")
        buf.write("\7i\2\2\u019f@\3\2\2\2\u01a0\u01a1\7e\2\2\u01a1\u01a2")
        buf.write("\7q\2\2\u01a2\u01a3\7p\2\2\u01a3\u01a4\7v\2\2\u01a4\u01a5")
        buf.write("\7k\2\2\u01a5\u01a6\7p\2\2\u01a6\u01a7\7w\2\2\u01a7\u01a8")
        buf.write("\7g\2\2\u01a8B\3\2\2\2\u01a9\u01aa\7f\2\2\u01aa\u01ab")
        buf.write("\7q\2\2\u01abD\3\2\2\2\u01ac\u01ad\7h\2\2\u01ad\u01ae")
        buf.write("\7w\2\2\u01ae\u01af\7p\2\2\u01af\u01b0\7e\2\2\u01b0\u01b1")
        buf.write("\7v\2\2\u01b1\u01b2\7k\2\2\u01b2\u01b3\7q\2\2\u01b3\u01b4")
        buf.write("\7p\2\2\u01b4F\3\2\2\2\u01b5\u01b6\7v\2\2\u01b6\u01b7")
        buf.write("\7t\2\2\u01b7\u01b8\7w\2\2\u01b8\u01b9\7g\2\2\u01b9H\3")
        buf.write("\2\2\2\u01ba\u01bb\7q\2\2\u01bb\u01bc\7h\2\2\u01bcJ\3")
        buf.write("\2\2\2\u01bd\u01be\7g\2\2\u01be\u01bf\7n\2\2\u01bf\u01c0")
        buf.write("\7u\2\2\u01c0\u01c1\7g\2\2\u01c1L\3\2\2\2\u01c2\u01c3")
        buf.write("\7k\2\2\u01c3\u01c4\7h\2\2\u01c4N\3\2\2\2\u01c5\u01c6")
        buf.write("\7y\2\2\u01c6\u01c7\7j\2\2\u01c7\u01c8\7k\2\2\u01c8\u01c9")
        buf.write("\7n\2\2\u01c9\u01ca\7g\2\2\u01caP\3\2\2\2\u01cb\u01cc")
        buf.write("\7k\2\2\u01cc\u01cd\7p\2\2\u01cd\u01ce\7j\2\2\u01ce\u01cf")
        buf.write("\7g\2\2\u01cf\u01d0\7t\2\2\u01d0\u01d1\7k\2\2\u01d1\u01d2")
        buf.write("\7v\2\2\u01d2R\3\2\2\2\u01d3\u01d4\7-\2\2\u01d4T\3\2\2")
        buf.write("\2\u01d5\u01d6\7/\2\2\u01d6V\3\2\2\2\u01d7\u01d8\7,\2")
        buf.write("\2\u01d8X\3\2\2\2\u01d9\u01da\7\61\2\2\u01daZ\3\2\2\2")
        buf.write("\u01db\u01dc\7\'\2\2\u01dc\\\3\2\2\2\u01dd\u01de\7#\2")
        buf.write("\2\u01de^\3\2\2\2\u01df\u01e0\7>\2\2\u01e0`\3\2\2\2\u01e1")
        buf.write("\u01e2\7>\2\2\u01e2\u01e3\7?\2\2\u01e3b\3\2\2\2\u01e4")
        buf.write("\u01e5\7@\2\2\u01e5d\3\2\2\2\u01e6\u01e7\7@\2\2\u01e7")
        buf.write("\u01e8\7?\2\2\u01e8f\3\2\2\2\u01e9\u01ea\7?\2\2\u01ea")
        buf.write("\u01eb\7?\2\2\u01ebh\3\2\2\2\u01ec\u01ed\7#\2\2\u01ed")
        buf.write("\u01ee\7?\2\2\u01eej\3\2\2\2\u01ef\u01f0\7<\2\2\u01f0")
        buf.write("\u01f1\7<\2\2\u01f1l\3\2\2\2\u01f2\u01f3\7(\2\2\u01f3")
        buf.write("\u01f4\7(\2\2\u01f4n\3\2\2\2\u01f5\u01f6\7~\2\2\u01f6")
        buf.write("\u01f7\7~\2\2\u01f7p\3\2\2\2\u01f8\u01f9\7?\2\2\u01f9")
        buf.write("r\3\2\2\2\u01fa\u01fb\7*\2\2\u01fbt\3\2\2\2\u01fc\u01fd")
        buf.write("\7+\2\2\u01fdv\3\2\2\2\u01fe\u01ff\7]\2\2\u01ffx\3\2\2")
        buf.write("\2\u0200\u0201\7_\2\2\u0201z\3\2\2\2\u0202\u0203\7}\2")
        buf.write("\2\u0203|\3\2\2\2\u0204\u0205\7\177\2\2\u0205~\3\2\2\2")
        buf.write("\u0206\u0207\7\60\2\2\u0207\u0080\3\2\2\2\u0208\u0209")
        buf.write("\7.\2\2\u0209\u0082\3\2\2\2\u020a\u020b\7=\2\2\u020b\u0084")
        buf.write("\3\2\2\2\u020c\u020d\7<\2\2\u020d\u0086\3\2\2\2\u020e")
        buf.write("\u0212\t\t\2\2\u020f\u0211\t\n\2\2\u0210\u020f\3\2\2\2")
        buf.write("\u0211\u0214\3\2\2\2\u0212\u0210\3\2\2\2\u0212\u0213\3")
        buf.write("\2\2\2\u0213\u0088\3\2\2\2\u0214\u0212\3\2\2\2\u0215\u0217")
        buf.write("\t\13\2\2\u0216\u0215\3\2\2\2\u0217\u0218\3\2\2\2\u0218")
        buf.write("\u0216\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u021a\3\2\2\2")
        buf.write("\u021a\u021b\bE\5\2\u021b\u008a\3\2\2\2\u021c\u021d\7")
        buf.write("\61\2\2\u021d\u021e\7\61\2\2\u021e\u0222\3\2\2\2\u021f")
        buf.write("\u0221\n\f\2\2\u0220\u021f\3\2\2\2\u0221\u0224\3\2\2\2")
        buf.write("\u0222\u0220\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0225\3")
        buf.write("\2\2\2\u0224\u0222\3\2\2\2\u0225\u0226\bF\5\2\u0226\u008c")
        buf.write("\3\2\2\2\u0227\u0228\7\61\2\2\u0228\u0229\7,\2\2\u0229")
        buf.write("\u022d\3\2\2\2\u022a\u022c\13\2\2\2\u022b\u022a\3\2\2")
        buf.write("\2\u022c\u022f\3\2\2\2\u022d\u022e\3\2\2\2\u022d\u022b")
        buf.write("\3\2\2\2\u022e\u0230\3\2\2\2\u022f\u022d\3\2\2\2\u0230")
        buf.write("\u0231\7,\2\2\u0231\u0232\7\61\2\2\u0232\u0233\3\2\2\2")
        buf.write("\u0233\u0234\bG\5\2\u0234\u008e\3\2\2\2\u0235\u0236\13")
        buf.write("\2\2\2\u0236\u0237\bH\6\2\u0237\u0090\3\2\2\2\u0238\u023c")
        buf.write("\7$\2\2\u0239\u023b\5%\23\2\u023a\u0239\3\2\2\2\u023b")
        buf.write("\u023e\3\2\2\2\u023c\u023a\3\2\2\2\u023c\u023d\3\2\2\2")
        buf.write("\u023d\u0240\3\2\2\2\u023e\u023c\3\2\2\2\u023f\u0241\7")
        buf.write("\2\2\3\u0240\u023f\3\2\2\2\u0240\u0241\3\2\2\2\u0241\u0242")
        buf.write("\3\2\2\2\u0242\u0243\bI\7\2\u0243\u0092\3\2\2\2\u0244")
        buf.write("\u0248\7$\2\2\u0245\u0247\5%\23\2\u0246\u0245\3\2\2\2")
        buf.write("\u0247\u024a\3\2\2\2\u0248\u0246\3\2\2\2\u0248\u0249\3")
        buf.write("\2\2\2\u0249\u024b\3\2\2\2\u024a\u0248\3\2\2\2\u024b\u024c")
        buf.write("\7^\2\2\u024c\u024d\n\r\2\2\u024d\u024e\3\2\2\2\u024e")
        buf.write("\u024f\bJ\b\2\u024f\u0094\3\2\2\2\31\2\u010d\u0112\u0116")
        buf.write("\u011b\u011e\u0127\u012b\u0133\u0137\u013b\u0142\u0146")
        buf.write("\u014a\u0151\u0153\u0212\u0218\u0222\u022d\u023c\u0240")
        buf.write("\u0248\t\3\f\2\3\16\3\3\22\4\b\2\2\3H\5\3I\6\3J\7")
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
    INTLIT = 11
    BOOLLIT = 12
    FLOATLIT = 13
    STRINGLIT = 14
    AUTO = 15
    FALSE = 16
    INTEGER = 17
    VOID = 18
    ARRAY = 19
    BREAK = 20
    FLOAT = 21
    RETURN = 22
    OUT = 23
    BOOLEAN = 24
    FOR = 25
    STRING = 26
    CONTINUE = 27
    DO = 28
    FUNCTION = 29
    TRUE = 30
    OF = 31
    ELSE = 32
    IF = 33
    WHILE = 34
    INHERIT = 35
    ADD = 36
    SUB = 37
    MUL = 38
    DIV = 39
    MOD = 40
    NOT = 41
    SM = 42
    SME = 43
    BG = 44
    BGE = 45
    EQUAL = 46
    NEQUAL = 47
    CONCAT = 48
    AND = 49
    OR = 50
    EQ = 51
    LB1 = 52
    RB1 = 53
    LB2 = 54
    RB2 = 55
    LB3 = 56
    RB3 = 57
    DOT = 58
    COMMA = 59
    SEMI = 60
    COLON = 61
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
            "INTLIT", "BOOLLIT", "FLOATLIT", "STRINGLIT", "AUTO", "FALSE", 
            "INTEGER", "VOID", "ARRAY", "BREAK", "FLOAT", "RETURN", "OUT", 
            "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", "TRUE", 
            "OF", "ELSE", "IF", "WHILE", "INHERIT", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "NOT", "SM", "SME", "BG", "BGE", "EQUAL", "NEQUAL", 
            "CONCAT", "AND", "OR", "EQ", "LB1", "RB1", "LB2", "RB2", "LB3", 
            "RB3", "DOT", "COMMA", "SEMI", "COLON", "ID", "WS", "LINE_COMMENT", 
            "BLOCK_COMMENT", "ERROR_TOKEN", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "INTLIT", "BOOLLIT", "FLOATLIT", 
                  "INTPART", "DECPART", "EXPPART", "STRINGLIT", "CHARS", 
                  "ESCAPE", "AUTO", "FALSE", "INTEGER", "VOID", "ARRAY", 
                  "BREAK", "FLOAT", "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", 
                  "CONTINUE", "DO", "FUNCTION", "TRUE", "OF", "ELSE", "IF", 
                  "WHILE", "INHERIT", "ADD", "SUB", "MUL", "DIV", "MOD", 
                  "NOT", "SM", "SME", "BG", "BGE", "EQUAL", "NEQUAL", "CONCAT", 
                  "AND", "OR", "EQ", "LB1", "RB1", "LB2", "RB2", "LB3", 
                  "RB3", "DOT", "COMMA", "SEMI", "COLON", "ID", "WS", "LINE_COMMENT", 
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
            actions[10] = self.INTLIT_action 
            actions[12] = self.FLOATLIT_action 
            actions[16] = self.STRINGLIT_action 
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

     


