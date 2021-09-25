import tkinter as tk
import time

current_balance = 50000

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data = {'Balance':tk.IntVar()}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, MenuPage, Withdraw, Deposit, Balance):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        '''Test ATM'''
        frame = self.frames[page_name]
        frame.tkraise()


class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#2B547E')
        self.controller = controller

        self.controller.title('Crab Bank')
        self.controller.state('zoomed')
        self.controller.iconphoto(False,
                                  tk.PhotoImage(file='I:/lab 1/470 project/view/atm-machine.png'))
        heading_Label=tk.Label(self,
                               text='Crab Bank ATM',
                               font=('{Helvetica Nueve}',45,'bold'),
                               fg='white',
                               bg='#2B547E')
        heading_Label.pack(pady=20)

        space_label = tk.Label(self, height=4, bg='#2B547E')
        space_label.pack()

        pincode_label = tk.Label(self,
                                 text='Enter Pin code',
                                 font=('Helvetica', 13),
                                 bg='#2B547E',
                                 fg='white')
        pincode_label.pack(pady=12)

        pincode = tk.StringVar()
        pin_entry = tk.Entry(self,
                             textvariable=pincode,
                             font=('Helvetica', 12),
                             width=22)
        pin_entry.focus_set()
        pin_entry.pack(ipady=7)

        def handle_focus_in(_):
            pin_entry.configure(fg='black',show='*')

        pin_entry.bind('<FocusIn>', handle_focus_in)

        def check_pin():
            if pincode.get()=='6428':
                pincode.set('')
                wrong_pin['text']=''
                controller.show_frame('MenuPage')
            else:
                wrong_pin['text']='Incorrect Pin Code'

        login_button = tk.Button(self,
                          text='Log in',
                          command=check_pin,
                          relief='raised',
                          borderwidth = 3,
                          width = 20,
                          height = 1)
        login_button.pack(pady=10)

        wrong_pin = tk.Label(self,
                             text='',
                             font=('Bebas Neue', 13),
                             fg= '#FF0000',
                             bg= '#0d1e2e',
                             anchor='n')
        wrong_pin.pack(fill='both', expand=True)

        bottom_frame = tk.Frame(self,
                                relief='raised',
                                borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame,
                               font=('Helvetica', 12))
        time_label.pack(side='right')

        tick()


class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#728FCE')
        self.controller = controller

        heading_Label = tk.Label(self,
                                text='Crab Bank ATM',
                                font=('{Helvetica Nueve}', 45, 'bold'),
                                fg='white',
                                bg='#728FCE')
        heading_Label.pack(pady=20)

        menu_label = tk.Label(self,
                              text='Main Menu',
                              font=('Helvetica',13),
                              fg='white',
                              bg='#728FCE')
        menu_label.pack()

        selection_label = tk.Label(self,
                                   text='Choose an Option',
                                   font=('Helvetica',13),
                                   fg='white',
                                   bg='#728FCE',
                                   anchor='n')
        selection_label.pack(fill='x')

        button_frame = tk.Frame(self,bg='#284075')
        button_frame.pack(fill='both', expand=True)

        def withdraw():
            controller.show_frame('Withdraw')

        withdraw_button = tk.Button(button_frame,
                                    text= 'Withdraw',
                                    command=withdraw,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=5)
        withdraw_button.grid(row=0, column=0, pady=5)

        def deposit():
            controller.show_frame('Deposit')

        deposit_button = tk.Button(button_frame,
                                    text= 'Deposit',
                                    command=deposit,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=5)
        deposit_button.grid(row=1, column=0, pady=5)

        def balance():
            controller.show_frame('Balance')

        balance_button = tk.Button(button_frame,
                                    text= 'Balance',
                                    command=balance,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=5)
        balance_button.grid(row=2, column=0, pady=5)

        bottom_frame = tk.Frame(self,
                                relief='raised',
                                borderwidth=3)

        bottom_frame.pack(fill='x', side='bottom')

        def exit():
            controller.show_frame('HomePage')

        exit_button = tk.Button(button_frame,
                                    text= 'Exit',
                                    command=exit,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=5)
        exit_button.grid(row=3, column=0, pady=5)

        def tick():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame,
                              font=('Helvetica', 12))
        time_label.pack(side='right')

        tick()

class Withdraw(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#71bd80')
        self.controller = controller

        heading_Label = tk.Label(self,
                                 text='Crab Bank ATM',
                                 font=('{Helvetica Nueve}', 45, 'bold'),
                                 fg='white',
                                 bg='#71bd80')
        heading_Label.pack(pady=20)

        bottom_frame = tk.Frame(self,
                                relief='raised',
                                borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame,
                              font=('Helvetica', 12))
        time_label.pack(side='right')

        tick()

        choose_amount = tk.Label(self,
                              text='How much you want to withdraw?',
                              font=('Helvetica', 13),
                              fg='white',
                              bg='#71bd80')
        choose_amount.pack()

        button_frame = tk.Frame(self,bg='#295c24')
        button_frame.pack(fill='both',expand=True)

        def withdraw(amount):
            global current_balance
            current_balance-= amount
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')

        def menu():
            controller.show_frame('MenuPage')

        menu_button = tk.Button(button_frame,
                                text='Menu',
                                command=menu,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        menu_button.grid(row=0, column=0, pady=5)

        hundred_button = tk.Button(button_frame,
                                  text='100',
                                  command=lambda: withdraw(100),
                                  relief='raised',
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        hundred_button.grid(row=1, column=0, pady=5)

        five_hundred_button = tk.Button(button_frame,
                                  text='500',
                                  command=lambda: withdraw(500),
                                  relief='raised',
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        five_hundred_button.grid(row=2, column=0, pady=5)

        one_k_button = tk.Button(button_frame,
                                  text='1000',
                                  command=lambda: withdraw(1000),
                                  relief='raised',
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        one_k_button.grid(row=0, column=1, pady=5, padx=555)

        five_k_button = tk.Button(button_frame,
                                 text='5000',
                                 command=lambda: withdraw(5000),
                                 relief='raised',
                                 borderwidth=3,
                                 width=50,
                                 height=5)
        five_k_button.grid(row=1, column=1, pady=5, padx=555)

        ten_k_button = tk.Button(button_frame,
                                 text='10000',
                                 command=lambda: withdraw(10000),
                                 relief='raised',
                                 borderwidth=3,
                                 width=50,
                                 height=5)
        ten_k_button.grid(row=2, column=1, pady=5, padx=555)

        cash = tk.StringVar
        other_button = tk.Entry(button_frame,
                                textvariable=cash,
                                width=59,
                                justify='right')
        other_button.grid(row=3, column=1, pady=5, ipady=30)


        def other_amount(_):
            global current_balance
            current_balance -= int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            cash.set('')
            controller.show_frame('MenuPage')

        other_button.bind('<Return>',other_amount)


class Deposit(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#14041c')
        self.controller = controller

        heading_Label = tk.Label(self,
                                 text='Crab Bank ATM',
                                 font=('{Helvetica Nueve}', 45, 'bold'),
                                 fg='white',
                                 bg='#14041c')
        heading_Label.pack(pady=20)

        space_label = tk.Label(self, height=4, bg='#14041c')
        space_label.pack()

        deposit_label = tk.Label(self,
                                 text='Enter Amount',
                                 font=('Helvetica', 13),
                                 bg='#14041c',
                                 fg='white')
        deposit_label.pack(pady=12)

        cash = tk.StringVar()
        deposit_entry = tk.Entry(self,
                                 textvariable=cash,
                                 font=('Helvetica',14),
                                 width=25)
        deposit_entry.pack()

        def deposit_cash():
            global current_balance
            current_balance+=int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')
            cash.set('')
        enter_button = tk.Button(self,
                                 text='Enter Amount',
                                 command=deposit_cash,
                                 relief='raised',
                                 borderwidth=3,
                                 height=3,
                                 width=40)
        enter_button.pack(pady=10)

        tone_label = tk.Label(self, bg='#0a030d')
        tone_label.pack(fill='both', expand=True)


        bottom_frame = tk.Frame(self,
                                relief='raised',
                                borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame,
                              font=('Helvetica', 12))
        time_label.pack(side='right')

        tick()



class Balance(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#14041c')
        self.controller = controller

        heading_Label = tk.Label(self,
                                 text='Crab Bank ATM',
                                 font=('{Helvetica Nueve}', 45, 'bold'),
                                 fg='white',
                                 bg='#14041c')
        heading_Label.pack(pady=20)


        global current_balance
        controller.shared_data['Balance'].set(current_balance)
        balance_label=tk.Label(self,
                               textvariable=controller.shared_data['Balance'],
                               font=('Helvetica',15),
                               fg='white',
                               bg='#14041c')
        balance_label.pack(fill='x')

        button_frame = tk.Frame(self, bg='#0a0207')
        button_frame.pack(fill='both',expand=True)

        def menu():
            controller.show_frame('MenuPage')
        menu_button = tk.Button(button_frame,
                                text='Menu',
                                command=menu,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        menu_button.grid(row=0,column=0,pady=5)

        def exit():
            controller.show_frame('HomePage')

        exit_button = tk.Button(button_frame,
                                text='Exit',
                                command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        exit_button.grid(row=1, column=0, pady=5)

        bottom_frame = tk.Frame(self,
                                relief='raised',
                                borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame,
                              font=('Helvetica', 12))
        time_label.pack(side='right')

        tick()



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()