from tkinter import *

#creating the window
root=Tk()

#setting the title of the window
root.title("Sanjana's Calculator")

#adding colour
root.config(background="dark grey")

#creating the input field and its dimensions
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#to ensure that the button will be displayed
def button_click(number):
    #gets the number that is clicked
    current=e.get()
    #delete the previous history
    e.delete(0,END)
    
    #inserting numbers to the input field when the respective button is clicked
    #with just this code the number is added at the front meaning that if i press 1,2,3 then i want it to be displayed as '123' but instead '321' is being shown
    #the last thing i click becomes the 1st thing that shows up 
    
    #need to convert to string as it is passed into as a integer
    e.insert(0,str(current)+str(number))
    
#define clear function
def button_clear():
    #delete the previous complete history
    e.delete(0,END)    
    
#define add function
def button_add():
    #pulling the number
    first_number=e.get()
    #make it a global function
    global f_num
    global math
    math='addition'
    f_num=int(first_number)
    #delete prior history
    e.delete(0,END)
    
#define equal function
def button_equal():
    #pull in whatever is in the secons variable in the box
    second_number=e.get()
    e.delete(0,END)
    
    if math=='addition':
        e.insert(0,f_num+int(second_number))    
    
    if math=='subtraction':
        e.insert(0,f_num-int(second_number))    
        
    if math=='multiplication':
        e.insert(0,f_num*int(second_number))    
    
    if math=='division':
        e.insert(0,f_num/int(second_number))    
            
    
    
#define subtract button
def button_subtract():
    #pulling the number
    first_number=e.get()
    #make it a global function
    global f_num
    global math
    math='subtraction'
    f_num=int(first_number)
    #delete prior history
    e.delete(0,END)

#define multiply button
def button_multiply():
    #pulling the number
    first_number=e.get()
    #make it a global function
    global f_num
    global math
    math='multiplication'
    f_num=int(first_number)
    #delete prior history
    e.delete(0,END)

#define divide button
def button_divide():
    #pulling the number
    first_number=e.get()
    #make it a global function
    global f_num
    global math
    math='division'
    f_num=int(first_number)
    #delete prior history
    e.delete(0,END)


#defining number button variables
#using lambda function as i cannot write the button_click() as if i do that the code won't run properly and will not display the right output
button_1=Button(root,text='1',padx=40,pady=20,command=lambda:button_click(1),font=("Courier New",16,'bold')) #passing the number that the button should respond with to the lambda function
button_2=Button(root,text='2',padx=40,pady=20,command=lambda:button_click(2),font=("Courier New",16,'bold'))
button_3=Button(root,text='3',padx=40,pady=20,command=lambda:button_click(3),font=("Courier New",16,'bold'))
button_4=Button(root,text='4',padx=40,pady=20,command=lambda:button_click(4),font=("Courier New",16,'bold'))
button_5=Button(root,text='5',padx=40,pady=20,command=lambda:button_click(5),font=("Courier New",16,'bold'))
button_6=Button(root,text='6',padx=40,pady=20,command=lambda:button_click(6),font=("Courier New",16,'bold'))
button_7=Button(root,text='7',padx=40,pady=20,command=lambda:button_click(7),font=("Courier New",16,'bold'))
button_8=Button(root,text='8',padx=40,pady=20,command=lambda:button_click(8),font=("Courier New",16,'bold'))
button_9=Button(root,text='9',padx=40,pady=20,command=lambda:button_click(9),font=("Courier New",16,'bold'))
button_0=Button(root,text='0',padx=39,pady=20,command=lambda:button_click(0),font=("Courier New",16,'bold'))

#defining other buttons
button_add=Button(root,text='+',padx=40,pady=20,command=button_add,font=("Courier New",16,'bold'))
button_subtract=Button(root,text='-',padx=41,pady=20,command=button_subtract,font=("Courier New",16,'bold'))
button_multiply=Button(root,text='*',padx=40,pady=20,command=button_multiply,font=("Courier New",16,'bold'))
button_divide=Button(root,text='/',padx=41,pady=20,command=button_divide,font=("Courier New",16,'bold'))

button_equal=Button(root,text='=',padx=99,pady=19,command=button_equal,font=("Courier New",16,'bold'))
button_clear=Button(root,text='Clear',padx=72,pady=20,command=button_clear,font=("Courier New",16,'bold'))


#displaying buttons on screen based on rows and columns
#buttons
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

#symbols
button_add.grid(row=5,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_equal.grid(row=5,column=1,columnspan=2)

button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)


root.mainloop()