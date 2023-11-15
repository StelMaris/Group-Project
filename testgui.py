import tkinter as tk
# import tkinter.messagebox
#from testregistration import main


class MYGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title('Group Project')
        self.main_window.geometry('600x500')
        # frames
        self.frame1 = tk.Frame(self.main_window)
        self.frame2 = tk.Frame(self.main_window)
        self.frame3 = tk.Frame(self.main_window)

        # frame1
        self.login_label = tk.Label(self.frame1, text='Enter ID: ')
        self.login_entry = tk.Entry(self.frame1, width=10)
        self.login_label.pack(side='left')
        self.login_entry.pack(side='left')

        # frame2
        self.pin_label = tk.Label(self.frame1, text='Enter Pin: ')
        self.pin_entry = tk.Entry(self.frame1, width=10)
        self.pin_label.pack(side='left')
        self.pin_entry.pack(side='left')

        # frame3
        self.enter_button = tk.Button(self.frame3, text='Log In', command=self.login)
        self.quit_button = tk.Button(self.frame3, text='Quit', command=self.main_window.destroy)
        self.enter_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()

        tk.mainloop()

    def login(self):
        student_list = [('1001', '111'), ('1002', '222'),
                        ('1003', '333'), ('1004', '444'),
                        ('1005', '555'), ('1006', '666')]
        login = self.login_entry.get()
        pin = self.pin_entry.get()
        for user in student_list:
            if user[0] == login:
                if user[1] == pin:
                    print('ID and PIN verified')


if __name__ == '__main__':
    project = MYGUI()
