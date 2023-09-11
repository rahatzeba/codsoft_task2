from tkinter import *
import string
import random
from PIL import ImageTk, Image

root = Tk()
root.title("Password Generator")
root.geometry("900x600")
root.resizable(False, False)

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

s = []

def genPass():
    try:
        P_length = int(T.get())
        if P_length > 30 or P_length < 1:
            result.config(text="length must be from 1 to 30")
    
        else:
            s.extend(list(s1))
            s.extend(list(s2))
            s.extend(list(s3))
            s.extend(list(s4))
            random.shuffle(s)
            password = "".join(random.sample(s, P_length))
            result.config(text=password)
    except ValueError:
        result.config(text="Length is empty")

# background_image
path = "D:/python/codsoft Internship work/Task2/img.jpg"
img = ImageTk.PhotoImage(Image.open(path))
Label(root, image=img).pack(fill="both", expand="no")

l = Label(root, text="Enter the Length of Password:")
l.config(font=("Courier", 14))
l.place(x=300, y=30)

# textbox
T = Entry(root, width="10")
T.place(x=700, y=30)

result = Label(root, text='***********************',font=("arial",25))
result.place(x=450, y=400)

# Generate Password
button = Button(text="Generate Password", font="arial 15 bold", bg="white", fg="purple", bd=2, command=genPass)
button.place(x=300, y=500)

root.mainloop()

'''
s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits
s4=string.punctuation
P_length=int(input("Please enter length of your password :"))
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
random.shuffle(s)
#print("".join(s[0:P_length]))
print("".join(random.sample(s,P_length)))
'''
