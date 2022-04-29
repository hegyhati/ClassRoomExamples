from imaplib import Int2AP
from sly import Parser
from lylexer import LilypondLexer

class LilypondParser(Parser):
    tokens = LilypondLexer.tokens

    def __init__(self, minoct=0, maxoct=1, notewidth=10, noteheight=80) -> None:
        super().__init__()
        self.minoct=minoct
        self.maxoct=maxoct
        self.notewidth=notewidth
        self.noteheight=noteheight
    
    def parse(self, tokens):
        self.pos=0
        return super().parse(tokens)
    
    @_(' "{" notes "}" ')
    def score(self, p):
        svg =  f'<svg viewBox = "{self.minoct*7*self.notewidth} {self.pos} {7*self.notewidth*(self.maxoct-self.minoct)} {-self.pos}" style="fill:rgb(0,0,255);stroke-width:1;stroke:rgb(0,0,0)">'
        for oct in range(self.minoct, self.maxoct):
            for pitch in range(0,8):
                x = (oct*7+pitch)*self.notewidth
                svg += f'<line x1="{x}" y1="{self.pos}" x2="{x}" y2="0" stroke="{"gray" if pitch == 0 else "lightgray"}" />'
        svg += p.notes
        svg += "<\svg>"
        return svg

    @_('note notes')
    def notes(self, p):
        return p.note + "\n\t" + p.notes
    
    @_(' ')
    def notes(self, p):
        return ""

    @_('pitch DURATION', 
       'pitch')
    def note(self, p):
        if hasattr(p,'DURATION'):
            self.prevduration = p.DURATION
        height = int(self.noteheight/self.prevduration)
        self.pos -= height
        return f'<rect x="{self.notewidth*p.pitch}" y="{self.pos}" width="{self.notewidth}" height="{height}" />'

    @_('PITCH MOD OCT', 
       'PITCH MOD ',
       'PITCH OCT',
       'PITCH')
    def pitch(self, p):
        base = p.PITCH
        base += 0 if not hasattr(p,'MOD') else -0.5 if p.MOD == 'es' else +0.5
        base += 0 if not hasattr(p,'OCT') else 8*p.OCT
        return base
    
    @_('REST ', 
       'REST DURATION ')
    def note(self, p):
        if hasattr(p,'DURATION'):
            self.prevduration = p.DURATION
        height = self.noteheight/self.prevduration
        self.pos -= height
        return ""

if __name__ == "__main__":
    lexer = LilypondLexer()
    parser = LilypondParser(minoct=-1, maxoct=3, noteheight=20)

    # text = '{c8 e c eis g4 g}'    
    text = ""
    with open('minimal.ly') as f:
        for line in  f.readlines():
            text += line
    result = parser.parse(lexer.tokenize(text))
    with open("minta.html","w") as file:
        file.write("<html><body>" + result + "</body></html>")
