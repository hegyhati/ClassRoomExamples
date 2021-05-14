import tkinter as tk
from wordchain import WordChain

class WordChainGUI(tk.Tk):

  def __init__(self, match_length:int=2):
    super().__init__()
    self.__setup_ui()
    self.model = WordChain(match_length)
    self.words.insert(0,self.model.chain[0])

  def __setup_ui(self):
    self.title("Wordchain")
    self.resizable(False,False)
    self.new_word = tk.StringVar(self)
    self.message = tk.StringVar(self)
    self.words = tk.Listbox(self)

    for widget in [
      tk.Entry(self,textvariable=self.new_word),
      tk.Button(self,text="ADD",command=self.add_word),
      tk.Label(self,textvariable=self.message),
      self.words
    ]: widget.pack(side=tk.TOP, fill=tk.X)

    self.bind('<Return>', self.add_word)
      
  def add_word(self, event=None):
    new_word=self.new_word.get()
    try:
      self.model.append(new_word)
      self.new_word.set("")
      self.words.insert(0,new_word)
      self.message.set(f"Score: {self.model.length()}")
    except Exception as e:
      self.message.set(e)

if __name__ == "__main__":
  WordChainGUI().mainloop()
  
