import tkinter as tk

class LineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.__editor = None

    def attach(self, editor):
        self.__editor = editor

    def redraw(self, *args):
        self.delete("all")

        i = self.__editor.index("@0,0")

        while True:
            dline = self.__editor.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            lineNum = str(i).split(".")[0]
            self.create_text(2, y, anchor = "nw", text = lineNum)
            i = self.__editor.index("%s+1line" % i)