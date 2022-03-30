import tkinter as tk
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from numberLinesClass import LineNumbers
from editorClass import IDE

# Colors
editorBg = "#363636"
editorText = "#9AD7DD"

class Editor (tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.__text = IDE(self)
        self.__vsb = tk.Scrollbar(self, orient = "vertical", command = self.__text.yview)
        self.__lineNumbers = LineNumbers(self, width = 30)
        self.__codeOutput = tk.Text()
        self.__filePath = ''
        self.__StartUp()

    def __OnChange(self, event):
        self.__lineNumbers.redraw()

    def __OpenFile(self):
        path = askopenfilename(filetypes = [('Tambarduine files', '*.tam')])
        self.__codeOutput.delete('1.0', END)

        if path.endswith('.tam'):
            with open(path, 'r') as file:
                code = file.read()
                self.__text.delete('1.0', END)
                self.__text.insert('1.0', code)
                self.__SetFilePath(path)
                self.__codeOutput.insert('1.0', "\"" + path + "\"")
        else:
            self.__codeOutput.insert('1.0' ,"##########################\n"
                                            "File format not supported\n"
                                            "##########################\n"
                                            "Try a '.tam' file\n"
                                            "##########################")

    def GetFilePath(self):
        path = self.__filePath
        return path

    def __SetFilePath(self, path):
        self.__filePath = path

    def __SaveAs(self):
        path = asksaveasfilename(filetypes = [('Tambarduine files', '*.tam')])
        self.__codeOutput.delete('1.0', END)

        if path.endswith('.tam'):
            with open(path, 'w') as file:
                code = self.__text.get('1.0', END)
                file.write(code)
                self.__SetFilePath(path)
                self.__codeOutput.insert('1.0', "File saved: \"" + path + "\"")
        else:
            self.__codeOutput.insert('1.0', "##############################################\n"
                                            "File not saved\n"
                                            "##############################################\n"
                                            "Try adding '.tam' at the end of the file name\n"
                                            "##############################################")

    def __Save(self):
        self.__codeOutput.delete('1.0', END)
        if self.__filePath == '':
            path = asksaveasfilename(filetypes = [('Tambarduine files', '*.tam')])
        else:
            path = self.__filePath

        if path.endswith('.tam'):
            with open(path, 'w') as file:
                code = self.__text.get('1.0', END)
                file.write(code)
                self.__SetFilePath(path)
                self.__codeOutput.insert('1.0', "File saved: \"" + path + "\"")
        else:
            self.__codeOutput.insert('1.0', "##############################################\n"
                                            "File not saved\n"
                                            "##############################################\n"
                                            "Try adding '.tam' at the end of the file name\n"
                                            "##############################################")

    def __Compile(self):
        path = self.__filePath

        if path == '':
            self.__Save()


    def __Run(self):
        path = self.__filePath

        if path == '':
            self.__Save()

    def __StartUp(self):
        self.__text.configure(yscrollcommand = self.__vsb.set)
        self.__lineNumbers.attach(self.__text)

        self.__vsb.pack(side = "right", fill = "y")
        self.__lineNumbers.pack(side = "left", fill = "y")
        self.__text.pack(side = "right", fill = "both", expand = True)


        self.__text.bind("<<Change>>", self.__OnChange)
        self.__text.bind("<<Configure>>", self.__OnChange)

    def SetGUI(self, window):
        self.__codeOutput.__init__(height= 10, width = 192)
        # self.__text.configure(bg = editorBg, fg = editorText)
        # self.__codeOutput.configure(bg = editorBg, fg = editorText)
        menuBar = tk.Menu(window)
        fileMenu = tk.Menu(menuBar, tearoff=0)
        runBar = tk.Menu(menuBar, tearoff = 0)
        window.title("Tambarduine IDE")
        fileMenu.add_command(label = 'Open', command = self.__OpenFile)
        fileMenu.add_command(label = 'Save', command = self.__Save)
        fileMenu.add_command(label = 'Save As', command = self.__SaveAs)
        fileMenu.add_command(label = 'Exit', command = exit)
        runBar.add_command(label = 'Compile', command = self.__Compile)
        runBar.add_command(label = ' Compile and Run', command = self.__Run)
        menuBar.add_cascade(label = 'File', menu = fileMenu)
        menuBar.add_cascade(label = 'Run', menu = runBar)
        window.config(menu = menuBar)
        window.state('zoomed')
        self.__codeOutput.pack()