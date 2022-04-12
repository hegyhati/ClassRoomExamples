class Ember:
    vezeteknev = "Kovacs"
    keresztnev = "Bela"

    def __init__(self, vnev="Kovacs", knev="Bela"):
        self.vezeteknev = vnev
        self.keresztnev = knev

    def teljes_nev(self):
        return self.vezeteknev + " " + self.keresztnev
    
    def angol_nev(self):
        return self.keresztnev + " " + self.vezeteknev


sanyi = Ember()
sanyi.vezeteknev = "Toth"
sanyi.keresztnev = "Sandor"

jozsi = Ember()
jozsi.vezeteknev = "Orban"
jozsi.keresztnev = "Jozsef"

print( sanyi.teljes_nev() )
print( sanyi.angol_nev() )

marcsi = Ember(vnev = "Toth", knev = "Maria")
judit = Ember("Kiss","Judit")