import tkinter as tk
from tkinter import filedialog



root=tk.Tk()
root.withdraw()

def getfilepath(file):  #function to get file path #file=name of the file
	print('\nSelect the file for %s .' %(file))
	file_path=filedialog.askopenfilename(title=("Plese select the file for "+file))
	print(file_path)
	return file_path


def getfolderpath(folder):  #function to get folder path
	print('\nSelect the folder for %s .' %(folder))
	folder_path=filedialog.askdirectory(title=("Plese select the folder for "+folder))
	print(folder_path)
	return folder_path