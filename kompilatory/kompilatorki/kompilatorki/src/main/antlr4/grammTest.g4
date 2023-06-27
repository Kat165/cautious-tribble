grammar grammTest;

var_declaration :VAR ID COLON;

VAR: 'var';
ID: ALPHA ( ALPHA | DIGIT )*;

COLON: ':';
DIGIT: [0-9];
ALPHA: [a-zA-Z_];
WS: [ \n\t\r]+ -> skip;