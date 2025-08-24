import tkinter as tk
from datetime import date

def calculate_age():
        dob_str = entry_dob.get()
        try:
            
            dob_date = date.fromisoformat(dob_str) 
            today = date.today()

            years = today.year - dob_date.year
            months = today.month - dob_date.month
            days = today.day - dob_date.day

            
            if days < 0:
                months -= 1
                
                days += (date(today.year, today.month, 1) - date(today.year, today.month - 1, 1)).days 
            if months < 0:
                years -= 1
                months += 12

            
            result_label.config(text=f"You are {years} years, {months} months, and {days} days old.")
        except ValueError:
            result_label.config(text="Invalid date format. Please use YYYY-MM-DD.")
app = tk.Tk()
app.title("Age Calculator App")


label_prompt = tk.Label(app, text="Enter your date of birth (YYYY-MM-DD):", bg= "#552df3", fg= 'white')
label_prompt.pack(pady=10)

entry_dob = tk.Entry(app)
entry_dob.pack(padx=20, pady=5)

calculate_button = tk.Button(app, text="Calculate Age", command=calculate_age)
calculate_button.pack(pady=10)

result_label = tk.Label(app, text="")
result_label.pack(pady=10)

app.mainloop()