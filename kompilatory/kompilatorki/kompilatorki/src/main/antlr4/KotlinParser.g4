parser grammar KotlinParser;

options { tokenVocab = KotlinLexer; }

startowy: classDeclaration* EOF;
condition: (Nazwa | Liczba_zmiennopoz) (EQUALS | NOT_EQUALS | SMALLER | BIGGER | SMALLER_OR_EQUAL | BIGGER_OR_EQUAL) (Nazwa | Liczba_zmiennopoz);
assignment: (variable | Nazwa) SPACE* ASSIGN SPACE* (Nazwa | Liczba_zmiennoprzecin | Liczba_zmiennopoz);
if_stat: IF_INIT SPACE* LEFT_BRACKET SPACE* condition SPACE* RIGHT_BRACKET SPACE* LEFT_CURVY_BRACKET instruction RIGHT_CURVY_BRACKET else_stat*;
else_stat: ELSE_INIT LEFT_CURVY_BRACKET instruction RIGHT_CURVY_BRACKET;
while_loop: WHILE_INIT LEFT_BRACKET condition RIGHT_BRACKET LEFT_CURVY_BRACKET instruction RIGHT_CURVY_BRACKET;
for_loop: FOR_INIT LEFT_BRACKET instruction RIGHT_BRACKET LEFT_CURVY_BRACKET instruction RIGHT_CURVY_BRACKET;
do_while_loop: DO_INIT LEFT_CURVY_BRACKET instruction RIGHT_CURVY_BRACKET while_loop;
function_body: NL* LEFT_CURVY_BRACKET (NL|SPACE)* instruction NL* RIGHT_CURVY_BRACKET;
function: FUN SPACE Nazwa LEFT_BRACKET variable* RIGHT_BRACKET NL* function_body?;
try_catch_stat: TRY_INIT LEFT_CURVY_BRACKET SPACE* instruction SPACE* RIGHT_CURVY_BRACKET CATCH_INIT LEFT_CURVY_BRACKET instruction RIGHT_CURVY_BRACKET;
import_stat: IMPORT SPACE* Nazwa;
return_stat: RETURN_INIT SPACE* (Nazwa | Liczba_zmiennoprzecin);
package_stat: PACKAGE SPACE* Nazwa;
komentarz_poj: DIVIDE DIVIDE String EscapedIdentifier;
komentarz_wiel: DIVIDE MULTIPLY String MULTIPLY DIVIDE;
instruction: (for_loop | if_stat | while_loop | Nazwa | variable | assignment | do_while_loop | function | try_catch_stat | komentarz_poj | komentarz_wiel|return_stat|NL |Nazwa SPACE* INCREMENT |SPACE)*;
classDeclaration: (PRIVATE | PUBLIC | PROTECTED | INTERNAL) SPACE CLASS SPACE Nazwa LEFT_BRACKET RIGHT_BRACKET NL* (function_body)?;
constructor: CONSTRUCTOR LEFT_BRACKET variable* RIGHT_BRACKET (LEFT_CURVY_BRACKET condition RIGHT_CURVY_BRACKET)*;
object: VAL_INIT Nazwa ASSIGN Nazwa LEFT_BRACKET variable* RIGHT_BRACKET;
variable: VAR_INIT SPACE Nazwa;