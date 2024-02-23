import tkinter
from tkinter import filedialog
import os
screen = tkinter.Tk()
screen.title("iguana notepad")
screen.geometry("500x500")
def salvar():
	arquivoDir = input("diretorio do arquivo :")
	arquivoNome = input("nome do arquivo :")
	os.chdir(arquivoDir)
	with open(arquivoNome, "w") as userFile:
		userFile.write(text.get("1.0", "end"))
def abrir():
	arquivo = filedialog.askopenfilename()
	if arquivo:
		with open(arquivo, "r") as fileNam:
			fileContent = fileNam.read()
			text.delete("1.0", "end")
			text.insert("1.0", fileContent)
	else:
		print("arquivo nao selecionado")
text = tkinter.Text(screen)
text.pack()
saveFile = tkinter.Button(screen, text="salvar", command=salvar)
saveFile.pack()
openFile = tkinter.Button(screen, text="abrir", command=abrir)
openFile.pack()
screen.mainloop()
