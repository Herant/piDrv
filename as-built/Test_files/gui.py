from tkinter import *

Ti=0.15    # 0.15

class SliderDemo(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.pack()
        self.var = IntVar()
        Scale(self,label='Miles',
            command=self.onMove,
            variable = self.var,
            from_=1 , to=50 ,length=300,
            tickinterval=20).pack()
        Button(self , text='Read', command=self.readScale).pack(pady=10)

    def onMove(self, value):
        print('onMove = ' , value)

    def readScale(self):
        global Ti
        Ti = self.var.get()/100
        print('Ti = ' , Ti)
        return Ti


if __name__ == '__main__' :
    SliderDemo().mainloop()
    print(Ti)
