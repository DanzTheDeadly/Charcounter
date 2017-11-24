from tkinter import *
from tkinter.filedialog import askopenfilename
from os.path import basename
from charcounter import count


class my_gui(Frame):
    # interface construction
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        # base frames
        self.ButtonFrame = Frame(self)
        self.ButtonFrame.pack(side=BOTTOM, fill=X)
        self.LabelFrame = Frame(self)
        self.LabelFrame.pack(side=LEFT, anchor=W, fill=X)
        self.DataFrame = Frame(self)
        self.DataFrame.pack(side=RIGHT, anchor=E)
        # buttons
        Button(self.ButtonFrame, text='Open file', command=self.open_file).pack(side=LEFT, anchor=W)
        Button(self.ButtonFrame, text='Analyze', command=self.analyze).pack(side=LEFT, anchor=W)
        Button(self.ButtonFrame, text='Quit', command=quit).pack(side=RIGHT, anchor=E)
        # labels
        self.label_list = ['Name:',
                           'Characters:',
                           'Characters without spaces:',
                           'Words:',
                           'Pages (1800 chars):',
                           'Pages (1800 chars without spaces):',
                           'Pages (250 words):']
        for label in self.label_list:
            Label(self.LabelFrame, text=label).pack(anchor=W)
        # values
        self.name = Label(self.DataFrame, anchor=E)
        self.chars = Label(self.DataFrame, anchor=E)
        self.charsns = Label(self.DataFrame, anchor=E)
        self.words = Label(self.DataFrame, anchor=E)
        self.pgs = Label(self.DataFrame, anchor=E)
        self.pgsns = Label(self.DataFrame, anchor=E)
        self.pgsw = Label(self.DataFrame, anchor=E)
        self.name.pack(anchor=W)
        self.chars.pack(anchor=W)
        self.charsns.pack(anchor=W)
        self.words.pack(anchor=W)
        self.pgs.pack(anchor=W)
        self.pgsns.pack(anchor=W)
        self.pgsw.pack(anchor=W)
        # target file variable initialization
        self.file = None

    # default open file dialog
    # saves file into variable
    def open_file(self):
        self.file = askopenfilename()
        self.name['text'] = basename(self.file)
        self.chars['text'] = ''
        self.charsns['text'] = ''
        self.words['text'] = ''
        self.pgs['text'] = ''
        self.pgsns['text'] = ''
        self.pgsw['text'] = ''

    # core function imported from charcounter
    # analyzes file, that has been saved in variable
    # and shows results
    def analyze(self):
        data = count(self.file)
        if data:
            self.chars['text'] = data['Number of characters:']
            self.charsns['text'] = data['Number of characters without spaces:']
            self.words['text'] = data['Number of words:']
            self.pgs['text'] = data['Number of pages (1800 chars):']
            self.pgsns['text'] = data['Number of pages (1800 chars without spaces:']
            self.pgsw['text'] = data['Number of pages (250 words):']


root = Tk()
root.title('Charcounter')
my_gui(root)
mainloop()
