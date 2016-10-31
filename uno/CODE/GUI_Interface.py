import tkinter as tk
import tkinter.filedialog, tkinter.messagebox, os


#########################
#####   GUI window  #####
#########################

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ZUNO - THE GAME")

        #####
        # menu
        #####
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=GUI.new_game)
        self.filemenu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        #####
        # setup objects with buttons, options, ...
        #####
        self.send_message_text=tk.StringVar()

        # Player's frame
        self.playerframe = tk.Frame(self.root, relief='raised', bd=5, bg='lightgrey')
        self.playerframelabel = tk.Label(self.playerframe, text="Player's").grid(row=0, column=0)

        # ownframe
        self.ownframe = tk.Frame(self.root, relief='raised', bd=5, bg='orange')
        self.ownframelabel = tk.Label(self.ownframe, text="Your card's for the game").grid(row=0,column=0)


        # Messageframe
        self.messageframe = tk.Frame(self.root, relief='raised', bd=5, bg='lightgreen')
        self.send_message_entry = tk.Entry(self.messageframe,relief="raised", width=30, textvariable=self.send_message_text)
        self.send_message_entry.grid(row=0, column=0)  # must be in seperate line otherwise it will get a NoneType

        self.sendbutton = tk.Button(self.messageframe, text="send ",  bg="grey", fg="black",
            relief='raised', command=lambda: self.send_message(self.send_message_text), bd=5).grid(row=0, column=1)


        #####
        # draw frames into window
        #####
        self.playerframe.grid(row=0, column=0)
        self.ownframe.grid(row=1, column=0)

        self.messageframe.grid(row=4, column=0)


        # call window

        self.root.config(menu=self.menubar)
        self.root.mainloop()

    ##########
    def new_game(self):
        pass

    def send_message(self, argument):
        pass


if __name__ == "__main__":
    GUI()