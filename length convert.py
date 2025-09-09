from tkinter import*
from tkinter import messagebox
def convert_to_cm():
    try:
        inches=float(inches_entry.get())
        cm=inches*2.54
        messagebox.showinfo("Conversion Result",f"{inches} inches={cm:.2f}cm")
    except ValueError:
        messagebox.showerror("Invalid input","Please enter a valid number")
root=Tk()
root.title("Inches to Centimeters Converter")
Label(root,text="Lenght in inches:").grid(row=0,column=0,padx=10,pady=10)
inches_entry=Entry(root)
inches_entry.grid(row=0,column=1,padx=10,pady=10)
Button(root,text="Convert to cm",command= convert_to_cm).grid(row=1,column=0,columnspan=2,pady=10)
root.mainloop()