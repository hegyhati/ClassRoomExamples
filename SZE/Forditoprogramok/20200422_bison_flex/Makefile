a.out: lex.yy.c grammar.tab.c grammar.tab.h
	g++ lex.yy.c grammar.tab.c

lex.yy.c: tokens.l
	flex tokens.l

grammar.tab.c grammar.tab.h: grammar.y
	bison -d grammar.y
