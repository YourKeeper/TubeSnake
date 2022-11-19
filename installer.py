import os
import tkinter
import tkinter.messagebox

class GUI:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry("425x300")
        self.window.title("TubeSnake Installer")
        self.icon = tkinter.PhotoImage(file = 'favicon.png')
        self.window.iconphoto(False, self.icon)
        self.canvas = tkinter.Canvas(self.window, width=200, height=200)
        self.button_frame = tkinter.Frame(self.window)
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)

        self.logo_img = tkinter.PhotoImage(file = 'logo.png')
        self.TSlabel = tkinter.Label(self.window, text="Welcome to TubeSnake! Select your OS!")
        self.install_windows_button = tkinter.Button(self.button_frame, text="Windows", width=12, height=1, bg="white", fg="black", command=self.install_windows)
        self.install_unix_button = tkinter.Button(self.button_frame, text="Mac/Linux/BSD", width=12, height=1, bg="white", fg="black", command=self.install_unix)
        self.close_button = tkinter.Button(self.window, text="Exit", width=12, height=1, bg="white", fg="black", command=self.window.destroy)

        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.pack()
        self.TSlabel.pack()
        self.install_windows_button.grid(row=0, column=0, sticky=tkinter.W+tkinter.E)
        self.install_unix_button.grid(row=0, column=1, sticky=tkinter.W+tkinter.E)
        self.button_frame.pack()
        self.close_button.pack()
        self.window.mainloop()

    def throw_error(self, error):
        error_msg = f"Errors have occured! Please examine the following Error output: {error} If you encounter this Error again and it is NOT your fault, please report it on our GitHub @ github.com/YourKeeper/TubeSnake"
        self.status_label.configure(text="Error!")
        tkinter.messagebox.showerror(title="An Error Occured!", message=error_msg)
        self.status_label.configure(text=" ")

    def throw_warning(self):
        warning_msg = "The TubeSnake Installer will reply with Not Responding while running, PLEASE do not worry or close the Installer for it is indeed installing your required modules. :)"
        tkinter.messagebox.showwarning(title="Warning!", message=warning_msg)

    def unix_pip_check(self):
        try:
            os.system('python3.10 -m pip install -r requirements.txt')
            return True
        except:
            pass
        try:
            os.system('python3.11 -m pip install -r requirements.txt')
            return True
        except:
            pass
        try:
            os.system('pip install -r requirements.txt')
            return True
        except:
            pass
        try:
            os.system('pip3 install -r requirements.txt')
            return True
        except:
            return False

    def install_windows(self):
        self.throw_warning()
        try:
            os.system('python -m pip install -r requirements.txt')
            tkinter.messagebox.showwarning(title="Install Completed!", message="Install completed! Thank you for using TubeSnake! :)")
        except Exception as error:
            self.throw_error(error)

    def install_unix(self):
        self.throw_warning()
        try:
            if self.unix_pip_check() == False:
                raise Exception("Pip not found")
            else:
                tkinter.messagebox.showwarning(title="Install Completed!", message="Install completed! Thank you for using TubeSnake! :)")
        except Exception as error:
            self.throw_error(error)

def main():
    app = GUI()

if __name__ == "__main__":
    main()