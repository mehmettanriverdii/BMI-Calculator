from tkinter import *
FONT=("Arial", 10, "normal")

#window
window = Tk()
window.title("BMI Calculator")
window.minsize(width=250, height=250)
window.config(padx=10, pady=10)

#Kg label
label_kg = Label(text="Enter Your Weight (kg)", font=FONT, fg="black")
label_kg.pack()
label_kg.config(pady=10)

#kg entry
entry_kg = Entry(width=15)
entry_kg.pack()

#boy label
label_boy = Label(text="Enter Your Height (cm)", font=FONT, fg="black")
label_boy.pack()
label_boy.config(pady=10)

#boy entry
entry_boy = Entry(width=15)
entry_boy.pack()

def calculate_clicked():
    global result_bmi
    try:
        if entry_kg.get().strip() == "":
            raise TypeError("Enter both wight and height!")
        if entry_boy.get().strip() == "":
            raise TypeError("Enter both wight and height!")
        kg = float(entry_kg.get())
        boy = float(entry_boy.get()) / 100
        bmi = round((kg / (boy ** 2)), 2)
        if (bmi < 16.0):
            result_bmi.config(text=f"Your BMI is {bmi}. You are Severely Underweight")
            result_bmi.pack()
        elif (16.0 <= bmi <= 18.4):
            result_bmi.config(text=f"Your BMI is {bmi}. You are Underweight")
            result_bmi.pack()
        elif (18.5 <= bmi <= 24.9):
            result_bmi.config(text=f"Your BMI is {bmi}. You are Normal weight")
            result_bmi.pack()
        elif (25.0 <= bmi <= 29.9):
            result_bmi.config(text=f"Your BMI is {bmi}. You are Overweight")
            result_bmi.pack()
        elif (30.0 <= bmi <= 34.9):
            result_bmi.config(text=f"Your BMI is {bmi}. You are Moderately Obese")
            result_bmi.pack()
        elif (35.0 <= bmi <= 39.9):
            result_bmi.config(text=f"Your BMI is {bmi}. You are Severely Obese")
            result_bmi.pack()
        elif (bmi > 40.0):
            result_bmi.config(text=f"Your BMI is {bmi}. You are Morbidly Obese")
            result_bmi.pack()
        else:
            result_bmi.config(text="Error calculating.")
    except ValueError:
        result_bmi.config(text="Enter a valid number!", font=FONT, fg="black")
        result_bmi.pack()
    except ZeroDivisionError:
        result_bmi.config(text="Sıfıra bölme hatası.", font=FONT, fg="black")
        result_bmi.pack()
    except TypeError as error:
        result_bmi.config(text="Enter both wight and height!", font=FONT, fg="black")
        result_bmi.pack()

#calculate
calculate_button = Button(text="Calculate", command=calculate_clicked)
calculate_button.config(padx=5, pady=5)
calculate_button.pack(pady=10)

#result
result_bmi = Label(text="", font=FONT, fg="black")
result_bmi.pack()

window.mainloop()
