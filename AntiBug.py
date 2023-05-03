import subprocess
import time
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from matplotlib import pyplot as plt
from matplotlib.backend_bases import NavigationToolbar2
import psutil
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Details import fileInfo
from Details.fileInfo import extract_infos
from mypackages import Scan
from mypackages.Scan import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


window = Tk()
window.geometry("1200x750")
window.title('AntiBug')
window.iconbitmap(r'C:\AntiBug\AntiBug\favicon.ico')

def scanPage():

    scanFrame = Frame(main_frame)
    scanFrame.pack(fill=ttk.BOTH, expand=True, padx=10, pady=10)
    frame_height = window.winfo_height()
    scanFrame.configure(height=frame_height,bg='#D9E3F1')

    
    

    def scan_directory_depth_first(path):
        stack = [path]
        while stack:
            current_path = stack.pop()
            for filename in os.listdir(current_path):
                file_path = os.path.join(current_path, filename)
                if os.path.isdir(file_path):
                    stack.append(file_path)
                elif file_path.endswith(".exe"):
                    message = file_path
                    output.insert('end',"\n"+ message)
                    result = scan_malware(file_path)
                    output.insert('end',"\n"+ result)
                   
    
    def choose_folder_and_scan():
        # Show the "Choose Folder" dialog box
        global folder_path
        folder_path = filedialog.askdirectory()
        return folder_path

    #Choosing a file

    def choose_file():
        global file_path
        file_path = filedialog.askopenfilename()
        message = file_path
        output.insert('end',"\n"+ message)
        result = scan_malware(file_path)
        output.insert('end',"\n"+ result)
        
    output = Text(
            scanFrame,
            height=18,
            width=130,
            font=("bold",15)
            )
    
    output.pack(fill=ttk.X,expand=True)

    #Scan
    def scan_directory():
        folder_path = choose_folder_and_scan()
        scan_directory_depth_first(folder_path)



    folderScanBtn = Button(scanFrame, text='Scan Folder', width=15, height=2, font=('Bold', 15),fg="white",
                           command=scan_directory)
    folderScanBtn.place(x=0, y=50, width=400)

    folderScanBtn.configure(bg='#800080')

    fileScanBtn = Button(scanFrame, text='Scan File', width=15,
                         height=2, font=('Bold', 15),fg="white", command=choose_file)
    fileScanBtn.place(x=450, y=50, width=450)
    fileScanBtn.configure(bg='#800080')

    scanFrame.pack(pady=20)
    scanFrame.pack_propagate(False)


def quarPage():
    quarFrame = Frame(main_frame)
    quarFrame.pack(fill=ttk.BOTH, expand=True, padx=10, pady=10)
    frame_height = window.winfo_height()
    quarFrame.configure(height=frame_height,bg='#D9E3F1')
    

    textbox = Text(
                quarFrame,
                height=1,
                font=("bold",15)
                )
    textbox.place(x=10,y=10)

    def details():
        filepath = textbox.get("1.0", ttk.END).strip()
        fileDetails = extract_infos(filepath)
        strDetails = '\n'.join([f"{k}: {v}" for k, v in fileDetails.items()])
        detailBox.insert('1.0', strDetails)

    detailBox = Text(
                quarFrame,
                height=22,
                font=("bold",15),
                )
    detailBox.place(x=10,y=60)

    
    restoreFileBtn = Button(quarFrame, text='Show', font=('Bold', 20),fg="white", command=details)
    restoreFileBtn.place(x=300, y=650,width=250)
    restoreFileBtn.configure(bg='#800080')

    quarFrame.pack(pady=20)
    quarFrame.pack_propagate(False)


def setPage():
    setFrame = Frame(main_frame)
    setFrame.pack(fill=ttk.BOTH, expand=True, padx=10, pady=10)
    frame_height = window.winfo_height()
    setFrame.configure(height=frame_height,bg='#D9E3F1')    


    
    def graph():

        filepath = textbox.get("1.0", ttk.END).strip()
        fileDetails = extract_infos(filepath)
        x = list(fileDetails.keys())
        y = list(fileDetails.values())
        # Create bar plot
        fig = plt.Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.bar(x, y)

        # Add labels and title
        ax.set_xlabel('Atrributes')
        ax.set_ylabel('Values')
        ax.set_title('Graph of file values')

        # Create Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=text)
        canvas.draw()

        # Get size of canvas widget
        canvas_width = canvas.get_tk_widget().winfo_width()
        canvas_height = canvas.get_tk_widget().winfo_height()

        # Insert canvas widget into Text widget
        text.window_create(ttk.END, window=canvas.get_tk_widget())
        enlarge = Button(setFrame, text='Enlarge', font=('Bold', 20),fg='white', bg='green',command=lambda: enlarge_graph(fig))
        enlarge.place(x=5, y=650,width=350)
        enlarge.configure(bg='#800080')


    textbox = Text(
                setFrame,
                height=1,
                font=("bold",15)
                )
    textbox.place(x=10,y=10)  

    text = ttk.Text(setFrame,height=24,font=("bold",15),fg="black")
    text.place(x=10,y=50) 

    def enlarge_graph(fig):
        # Create new window
        new_window = Toplevel(setFrame)

        # Create new canvas for enlarged graph
        canvas = FigureCanvasTkAgg(fig, master=new_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=ttk.TOP, fill=ttk.BOTH, expand=1)

        # Add toolbar for zooming and saving options
        toolbar = NavigationToolbar2(canvas, new_window)
        toolbar.update()
        canvas.get_tk_widget().pack(side=ttk.TOP, fill=ttk.BOTH, expand=1)

    


    showbtn = Button(setFrame, text='Graph', font=('Bold', 20),fg='white', bg='green',command=graph)
    showbtn.place(x=550, y=650,width=350)
    showbtn.configure(bg='#800080')
    setFrame.pack(pady=20)
    setFrame.pack_propagate(False)


def hide_indicators():
    scan_indicate.config(bg='#C59EE2')
    quar_indicate.config(bg='#C59EE2')
    set_indicate.config(bg='#C59EE2')


def deletePages():
    for frame in main_frame.winfo_children():
        frame.destroy()


def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#800080')
    deletePages()
    page()


options_frame = Frame(window, bg='#c3c3c3')

# Designing Scan Buttons
scanphoto = PhotoImage(file=r"image/scann.png")
scanBtn = Button(options_frame, text='Scan', image=scanphoto, font=('Bold', 15), fg='#158aff', bg='#c3c3c3', bd=0,
                 command=lambda: indicate(scan_indicate, scanPage))
scanBtn.place(x=49.0, y=30.0, width=150.0, height=150.0)
scanBtn.configure(bg='#D9E3F1')


scan_indicate = Label(options_frame, text='', bg='#c3c3c3')
scan_indicate.place(x=3, y=30, width=5, height=150)

# Designing Quarantine Buttons
webphoto = PhotoImage(file=r"image/details.png")
quarBtn = Button(options_frame, text='Web', image=webphoto, font=('Bold', 15), fg='#158aff', bg='#c3c3c3', bd=0,
                 command=lambda: indicate(quar_indicate, quarPage))
quarBtn.place(x=49.0, y=250.0, width=150.0, height=150.0)
quarBtn.configure(bg='#D9E3F1')


quar_indicate = Label(options_frame, text='', bg='#c3c3c3')
quar_indicate.place(x=3, y=250, width=5, height=150)

# Designing settings Buttons
toolsphoto = PhotoImage(file=r"image/graph.png")
setBtn = Button(options_frame, text='Tools', image=toolsphoto, font=('Bold', 15), fg='#158aff', bg='#c3c3c3', bd=0,
                command=lambda: indicate(set_indicate, setPage))
setBtn.place(x=49.0, y=470.0, width=150.0, height=150.0)
setBtn.configure(bg='#D9E3F1')

set_indicate = Label(options_frame, text='', bg='#c3c3c3')
set_indicate.place(x=3, y=470, width=5, height=150)

options_frame.pack(side=LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=300, height=1000, bg="#D9E3F1")


main_frame = Frame(window, highlightbackground='black', highlightthickness=2)

main_frame.pack(side=LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=900, height=750,bg='#D9E3F1')

indicate(scan_indicate, scanPage)

window.mainloop()