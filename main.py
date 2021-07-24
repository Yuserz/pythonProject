from tkinter import *

root = Tk()
root.title("yusers")
root.geometry("416x550+500+40")

calc = Frame(root, bd=20, pady=5, bg='gainsboro', relief=RIDGE)
calc.grid()


class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.resul = False

    def number(self, num):
            selfresult = False
            firstname = txtDisplay.get()
            secondnum = str(num)
            if self.input_value:
                self.current = secondnum
                self.input_value = False
            else:
                if secondnum in firstname:
                        return
                self.current = firstname + secondnum
            self.Display(self.curent)

added_value = Calc()

txtDisplay = Entry(calc, font=('arial', 16, 'bold'), bd=20, width=28, justify = RIGHT)
txtDisplay.grid(row=0, columnspan=4, column=0, pady=1)

numberpad = "789456123"
i = 0
btn = []

for j in range(3,6):
    for k in range(3):
        btn.append(Button (calc, width = 6, height=2, font=('arial',16,'bold'), bd=4, text =numberpad[i]))
        btn[i].grid(row=j, column=k,pady=1)
        btn[i]["command"] = lambda x = numberpad[i]:added_value.numberEnter(x)
        i += 1

root.mainloop()
