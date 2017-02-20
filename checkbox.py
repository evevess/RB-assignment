import Tkinter
import csv
import operator


class MyGUI:

    def __init__(self):
        with open('data.csv') as csvfile:
            mydata = list(csv.reader(csvfile, delimiter=';'))

        # Create the main window.
        self.main_window = Tkinter.Tk()

        # Create two frames. One for the Radiobuttons
        # and another for the regular Button widgets.
        self.top_frame = Tkinter.Frame(self.main_window)
        self.bottom_frame = Tkinter.Frame(self.main_window)

        # Create an IntVar object to use with
        # the Radiobuttons.
        self.radio_var = Tkinter.IntVar()

        # Set the intVar object to 1.
        self.radio_var.set(1)

        # Create the Radiobutton widgets in the top_frame.
        self.rb1 = Tkinter.Radiobutton(self.top_frame, \
                                       text='name(alphabically)', variable=self.radio_var, \
                                       value=1)
        self.rb2 = Tkinter.Radiobutton(self.top_frame, \
                                       text='age(abscending)', variable=self.radio_var, \
                                       value=2)
        self.rb3 = Tkinter.Radiobutton(self.top_frame, \
                                       text='age(descending)', variable=self.radio_var, \
                                       value=3)
        self.rb4 = Tkinter.Radiobutton(self.top_frame, \
                                       text='salary(abscending)', variable=self.radio_var, \
                                       value=4)
        self.rb5 = Tkinter.Radiobutton(self.top_frame, \
                                       text='salary(descending)', variable=self.radio_var, \
                                       value=5)

        # Pack the Radiobuttons.
        self.rb1.pack(side='left')
        self.rb2.pack(side='left')
        self.rb3.pack(side='left')
        self.rb4.pack(side='left')
        self.rb5.pack(side='left')

        # Create an OK button and a Quit button.
        self.ok_button = Tkinter.Button(self.bottom_frame, \
                                        text='OK', command=self.show_choice)
        self.quit_button = Tkinter.Button(self.bottom_frame, \
                                          text='Cancel', command=self.main_window.destroy)

        # Pack the Buttons.
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # # Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Start the mainloop.
        Tkinter.mainloop()
    # The show_choice

    def show_choice(self):
        with open('data.csv') as csvfile:
            mydata = list(csv.reader(csvfile, delimiter=';'))

            sort=mydata
            from bottle import run, route, template

            @route('/original')
            def original():
                return template('disp_table', rows=sort)
        x=str(self.radio_var.get())
        print ('You selected option ' + \
        x)

        if x == '1':
            sort = sorted(mydata[1:], key=operator.itemgetter(0))
        else:
            if x == '2':
                sort = sorted(mydata[1:], key=operator.itemgetter(1))
            else:
                if x == '3':
                    sort = sorted(mydata[1:], key=operator.itemgetter(1), reverse=True)
                else:
                    if x == '4':
                       sort = sorted(mydata[1:], key=operator.itemgetter(2))
                    else:
                        if x == '5':
                             sort = sorted(mydata[1:], key=operator.itemgetter(2), reverse=True)

        mydata[1:]=sort

        @route('/sorting')

        def sorting():

            return template('disp_table', rows=mydata)
        run(port=8401,debug=True, update=True)
        self.main_window.destroy()

    def clear(self):
        self.input_text.delete(0, len(self.input_text.get()))
        self.label_result["text"] = "None"


def maincheck():
    # Create an instance of the MyGUI class.
    my_gui = MyGUI()

maincheck()
