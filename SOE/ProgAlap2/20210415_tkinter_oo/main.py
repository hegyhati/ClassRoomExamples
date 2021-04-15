import model
import view

c = model.Character("characterdata.json")
c.vision=3
m = model.Map("mapdata_big.json")

gv = view.GameView(m,c)
gv.mainloop()
