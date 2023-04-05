import time
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from mypackages.Scan import *
window = Tk()
window.geometry("1200x750")
window.title('AntiBug')
# window.iconbitmap(r'C:\\AntiBug\\favicon.ico')

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
                    result = scan_malware(file_path)
                    # output.delete('1.0', 'end')  # clear previous contents of output widget
                    output.insert('end',"\n"+ message)
                    output.insert('end',"\n"+ result)
        # del message
        # del result
    
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
        


    #Scan
    def scan_directory():
        folder_path = choose_folder_and_scan()
        scan_directory_depth_first(folder_path)



    # width=1200, height=500,
    folderScanBtn = Button(scanFrame, text='Scan Folder', width=15, height=2, font=('Bold', 15),fg="white",
                           command=scan_directory)
    # folderScanBtn.grid(row=0, column=0, padx=10, pady=40)
    folderScanBtn.place(x=20, y=50, width=400)

    folderScanBtn.configure(bg='#800080')

    fileScanBtn = Button(scanFrame, text='Scan File', width=15,
                         height=2, font=('Bold', 15),fg="white", command=choose_file)
    fileScanBtn.place(x=450, y=50, width=400)
    # fileScanBtn.grid(row=0, column=5, padx=10, pady=40)
    fileScanBtn.configure(bg='#800080')

    
    output = Text(
            scanFrame,
            height=18,
            width=130,
            font=("bold",15)
            )
    
    output.pack(fill=ttk.X,expand=True)


    scanFrame.pack(pady=20)
    scanFrame.pack_propagate(False)

    



def quarPage():
    quarFrame = Frame(main_frame)
    quarFrame.pack(fill=ttk.BOTH, expand=True, padx=10, pady=10)
    frame_height = window.winfo_height()
    quarFrame.configure(height=frame_height,bg='#D9E3F1')
    
    def delete_file():
          # clear the textbox
        filepath = textbox.get("1.0", ttk.END).strip()
        # while True:
        #     try:
        #         os.remove(filepath)
        #         print(f"Deleted {filepath}")
        #         break
        #     except PermissionError:
        #         print(f"{filepath} is currently being used, waiting for 5 seconds...")
        #         time.sleep(5)
        #     except FileNotFoundError:
        #         print(f"{filepath} not found.")
        #         break
        # filename = os.path.basename(filepath)

        if os.path.exists(filepath):
            try:
                os.remove(filepath)
                textbox.delete("1.0", ttk.END)  # clear the textbox
                messagebox.showinfo("File Deleted", f"The file {filepath} has been deleted.")
            except Exception as e:
                messagebox.showerror("Error", f"Unable to delete file: {str(e)}")
            except OSError as e:
        # If the file is currently being used, wait for 5 seconds and try again
                # filename = os.path.basename(filepath)

                if e.errno == 32:
                    print(f"{filepath} is currently being used, waiting for 5 seconds...")
                    time.sleep(5)
                    delete_file(filepath)
        else:
            messagebox.showerror("Error", f"File does not exist: {filepath}")

    textbox = Text(
                quarFrame,
                height=1,
                font=("bold",15)
                )
    textbox.pack(fill=ttk.X,expand=True)

    deleteFileBtn = Button(quarFrame, text='Delete', font=('Bold', 20),fg="white", command=delete_file)
    deleteFileBtn.place(x=20.0, y=550,width=350)
    deleteFileBtn.configure(bg='#800080')

    
    
    restoreFileBtn = Button(quarFrame, text='Show', font=('Bold', 20),fg="white")
    restoreFileBtn.place(x=500, y=550,width=350)
    restoreFileBtn.configure(bg='#800080')

    quarFrame.pack(pady=20)
    quarFrame.pack_propagate(False)


def setPage():
    setFrame = Frame(main_frame)
    setFrame.pack(fill=ttk.BOTH, expand=True, padx=10, pady=10)
    frame_height = window.winfo_height()
    setFrame.configure(height=frame_height,bg='#D9E3F1')    
    
    lb = Label(setFrame, text='Select Machine Learning Algorithms',
               font=('Bold', 20))
    lb.grid(row=0, column=0, padx=10, pady=40)
    Checkbutton1 = IntVar()
    Checkbutton2 = IntVar()
    Checkbutton3 = IntVar()
    Checkbutton4 = IntVar()
    Checkbutton5 = IntVar()

    Button1 = Checkbutton(setFrame, text="Default(K-Nearest Neighbours)",
                          variable=Checkbutton1,
                          onvalue=1,
                          offvalue=0,
                          font=('Bold', 15),
                          height=2,
                          width=30)

    Button2 = Checkbutton(setFrame, text="Logistic Regression",
                          variable=Checkbutton2,
                          onvalue=1,
                          offvalue=0,
                          font=('Bold', 15),
                          justify=CENTER,
                          height=2,
                          width=30)

    Button3 = Checkbutton(setFrame, text="Decision Tree",
                          variable=Checkbutton3,
                          onvalue=1,
                          offvalue=0,
                          font=('Bold', 15),
                          justify=LEFT,
                          relief=FLAT,
                          height=2,
                          width=30)

    Button4 = Checkbutton(setFrame, text="Naive Bayes",
                          variable=Checkbutton4,
                          onvalue=1,
                          offvalue=0,
                          font=('Bold', 15),
                          height=2,
                          width=30)

    Button5 = Checkbutton(setFrame, text="Passive Aggresive",
                          variable=Checkbutton5,
                          onvalue=1,
                          offvalue=0,
                          height=2,
                          font=('Bold', 15),
                          width=30)

    Button1.grid(row=1, column=0, padx=10, pady=10)
    Button2.grid(row=2, column=0, padx=10, pady=10)
    Button3.grid(row=3, column=0, padx=10, pady=10)
    Button4.grid(row=4, column=0, padx=10, pady=10)
    Button5.grid(row=5, column=0, padx=10, pady=10)

    showbtn = Button(setFrame, text='Save', font=('Bold', 20), bg='green')
    showbtn.grid(row=6, column=0, padx=10, pady=20)
    showbtn.configure(bg='#800080')
    setFrame.pack(pady=20)
    setFrame.pack_propagate(False)


def hide_indicators():
    scan_indicate.config(bg='#4B7A0E')
    quar_indicate.config(bg='#4B7A0E')
    set_indicate.config(bg='#4B7A0E')


def deletePages():
    for frame in main_frame.winfo_children():
        frame.destroy()


def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#074A00')
    deletePages()
    page()


options_frame = Frame(window, bg='#c3c3c3')

# Designing Scan Buttons
scanphoto = PhotoImage(file=r"image/scan.png")
scanBtn = Button(options_frame, text='Scan', image=scanphoto, font=('Bold', 15), fg='#158aff', bg='#c3c3c3', bd=0,
                 command=lambda: indicate(scan_indicate, scanPage))
scanBtn.place(x=49.0, y=30.0, width=180.0, height=180.0)
scanBtn.configure(bg='#4B7A0E')


scan_indicate = Label(options_frame, text='', bg='#c3c3c3')
scan_indicate.place(x=3, y=30, width=5, height=150)

# Designing Quarantine Buttons
webphoto = PhotoImage(file=r"image/web.png")
quarBtn = Button(options_frame, text='Web', image=webphoto, font=('Bold', 15), fg='#158aff', bg='#c3c3c3', bd=0,
                 command=lambda: indicate(quar_indicate, quarPage))
quarBtn.place(x=49.0, y=250.0, width=180.0, height=180.0)
quarBtn.configure(bg='#4B7A0E')


quar_indicate = Label(options_frame, text='', bg='#c3c3c3')
quar_indicate.place(x=3, y=250, width=5, height=150)

# Designing settings Buttons
toolsphoto = PhotoImage(file=r"image/tools.png")
setBtn = Button(options_frame, text='Tools', image=toolsphoto, font=('Bold', 15), fg='#158aff', bg='#c3c3c3', bd=0,
                command=lambda: indicate(set_indicate, setPage))
setBtn.place(x=49.0, y=470.0, width=180.0, height=180.0)
setBtn.configure(bg='#4B7A0E')

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

# window.pack_propagate(False)
window.mainloop()
