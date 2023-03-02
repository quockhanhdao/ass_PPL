// 2013452
// Dao Quoc Khanh

grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: decllist EOF;
decllist: decllistprime | ;
decllistprime: decllistprime decl | decl;
decl: vardecl | funcdecl | statement;

// Declaration
vardecl: idlist COLON typ SEMI
	| initialization SEMI;
initialization: ID COMMA initialization COMMA expression 
	| ID COLON typ EQ expression;
paramdecl: INHERIT? OUT? ID COLON typ;
funcdecl: prototype blockstmt;
prototype: ID COLON FUNCTION typ LB1 paramlist RB1 (INHERIT ID)?;

// Statement
statement: assignstmt SEMI
	| ifstmt 
	| forstmt 
	| whilestmt 
	| dowhilestmt SEMI
	| breakstmt SEMI
	| continuestmt SEMI
	| returnstmt SEMI
	| callstmt SEMI
	| blockstmt 
	| specfunc SEMI;
assignstmt: scalar EQ expression;
ifstmt: IF LB1 expression RB1 statement (ELSE statement)?;
forstmt: FOR LB1 scalar EQ expression COMMA expression COMMA assignstmt RB1 statement;
whilestmt: WHILE LB1 expression RB1 statement;
dowhilestmt: DO blockstmt WHILE LB1 expression RB1;
breakstmt: BREAK;
continuestmt: CONTINUE;
returnstmt: RETURN expression?;
callstmt: ID LB1 arglist RB1;
blockstmt: LB3 linelist RB3;
scalar: ID | idxop;

// Special function
specfunc: readInteger | printInteger | readFloat | writeFloat | readBoolean | printBoolean | readString | printString | sper | preventDefault;
readInteger: 'readInteger' LB1 RB1;
printInteger: 'printInteger' LB1 expression RB1;
readFloat: 'readFloat' LB1 RB1 SEMI;
writeFloat: 'writeFloat' LB1 expression RB1;
readBoolean: 'readBoolean' LB1 RB1;
printBoolean: 'printBoolean' LB1 expression RB1;
readString: 'readString' LB1 RB1;
printString: 'printString' LB1 expression RB1;
sper: 'super' LB1 expressionlist RB1;
preventDefault: 'preventDefault' LB1 RB1;

// Expression
expression: term1 CONCAT term1 | term1;
term1: term2 (EQUAL | NEQUAL | SM | SME | BG | BGE) term2 | term2;
term2: term2 (AND | OR) term3 | term3;
term3: term3 (ADD | SUB) term4 | term4;
term4: term4 (MUL | DIV | MOD) term5 | term5;
term5: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | arrlit 
	| ID | NOT ID | SUB ID 
	| call | idxop | subexpression | specfunc;
subexpression: LB1 expression RB1;
idxop: ID LB2 expressionlist RB2;
call: ID LB1 arglist RB1;
arrlit: LB3 expressionlist RB3;

// List
intlist: intlist COMMA INTLIT | INTLIT;
idlist: idlist COMMA ID | ID;
expressionlist: expressionlist COMMA expression | expression;
paramlist: paramlistprime | ;
paramlistprime: paramlistprime COMMA paramdecl | paramdecl;
arglist: arglistprime | ;
arglistprime: arglistprime COMMA expression | expression;
linelist: linelistprime | ;
linelistprime: linelistprime line | line;
line: statement | vardecl;

// Type
atomtyp: BOOLEAN | INTEGER | FLOAT | STRING;
arrtyp: ARRAY LB2 intlist RB2 OF atomtyp;
voidtyp: VOID;
autotyp: AUTO;
typ: atomtyp | arrtyp | voidtyp | autotyp;

// Literals
INTLIT: [0-9] | [1-9] [0-9_]* [0-9] {self.text = self.text.replace("_", "")};
BOOLLIT: TRUE | FALSE;
FLOATLIT: INTPART (DECPART | DECPART? EXPPART) {self.text = self.text.replace("_", "")};
fragment INTPART: [0-9] | [1-9] [0-9_]* [0-9];
fragment DECPART: '.' ([0-9] | [0-9] [0-9_]* [0-9]);
fragment EXPPART: ('e' | 'E') ('-' | '+')? ([0-9] | [0-9] [0-9_]* [0-9]);
STRINGLIT: '"' CHARS? '"' {self.text = self.text[1:(len(self.text) - 1)]};
fragment CHARS: (~["\\\b\f\r\n\t] | ESCAPE)+;
fragment ESCAPE: '\\' [bfrnt"'\\]; //'];

// Keywords;
AUTO: 'auto';
FALSE: 'false';
INTEGER: 'integer';
VOID: 'void';
ARRAY: 'array';
BREAK: 'break';
FLOAT: 'float';
RETURN: 'return';
OUT: 'out';
BOOLEAN: 'boolean';
FOR: 'for';
STRING: 'string';
CONTINUE: 'continue';
DO: 'do';
FUNCTION: 'function';
TRUE: 'true';
OF: 'of';
ELSE: 'else';
IF: 'if';
WHILE: 'while';
INHERIT: 'inherit';

// Operators:
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
SM: '<';
SME: '<=';
BG: '>';
BGE: '>=';
EQUAL: '==';
NEQUAL: '!=';
CONCAT: '::';
AND: '&&';
OR: '||';
EQ: '=';

// Seperators:
LB1: '(';
RB1: ')';
LB2: '[';
RB2: ']';
LB3: '{';
RB3: '}';
DOT: '.';
COMMA: ',';
SEMI: ';';
COLON: ':';

// Identifiers
ID: [A-Za-z_] [A-Za-z0-9_]*;

// Skip spaces and Comments
WS: [ \t\b\f\r\n]+ -> skip ; // skip spaces, tabs, newlines
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;

ERROR_TOKEN: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' CHARS* EOF? {
	y = str(self.text)
	raise UncloseString(y[1:])};
ILLEGAL_ESCAPE: '"' CHARS* ('\\' ~[bfrnt"\\]) {
	y = str(self.text)
	raise IllegalEscape(y[1:])
};