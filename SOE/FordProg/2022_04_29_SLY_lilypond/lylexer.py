from sly import Lexer

class LilypondLexer(Lexer):
    literals = {'{', '}'}
    tokens = { PITCH, DURATION, REST, MOD, OCT}

    
    PITCH  = r'[cdefgab]'
    REST = r'r'
    MOD = r'is|es'

    ignore = ' \t\n'

    @_(r'1|2|4|8|16|32|64')
    def DURATION(self, t):
        t.value = int(t.value)
        return t

    @_('[cdefgab]')
    def PITCH(self, t):
        t.value = "cdefgab".index(t.value)
        return t

    @_(r'\'+|\,+')
    def OCT(self,t):
        t.value = len(t.value) * (1 if t.value[0]=='\'' else -1)
        return t



if __name__ == '__main__':
    my_lexer = LilypondLexer()
    text = ""
    with open('minimal.ly') as f:
        for line in  f.readlines():
            text += line
    print(my_lexer.tokenize(text))
    for token in my_lexer.tokenize(text):
        print(token)