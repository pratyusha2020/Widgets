import tkinter as tk

def calculate_value():
    try:
        num1 = float(entry1.get())
        
        product = num1 * 2.54
        result_label.config(text=f" {product}"+"cm")
    except ValueError:
        result_label.config(text="Error: Invalid input. Please enter numbers.")

root = tk.Tk()
root.title("Length Converter App")

lbl= tk.Label(text= "Welcome to the length calculator app, this program converts lengths: in to cm!")
lbl.pack()
label1 = tk.Label(root, text="Enter your value in inches:",bg= "#e01868", fg= 'white')
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()



calculate_button = tk.Button(root, text="Calculate", command=calculate_value)
calculate_button.pack()

result_label = tk.Label()
result_label.pack()

root.mainloop()
