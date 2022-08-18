import tkinter as tk
class RListBox(tk.Listbox):
  def __init__(self,*root,  **kwargs):
    super().__init__(*root,**kwargs)
    self.listData=list()

  def insertData(self,id,texto):
    self.insert(tk.END,texto)
    self.listData.append(id)


  def alunos_lista_Callback(self,event):
    print(self.get(tk.ANCHOR))
    print(self.listData[self.curselection()[0]])

  def prtlistData(self):
    print(self.listData)

  def clearData(self):
    self.delete(0,tk.END)
    self.listData.clear()

  def returnId(self):
    return self.listData[self.curselection()[0]]

