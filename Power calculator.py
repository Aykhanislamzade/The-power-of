#Imports
import tkinter as tk

#Variables
root = tk.Tk()


#Tkinter GUI setup basic
canvas = tk.Canvas(root, width= 400, height=400)
canvas.grid(columnspan=3, rowspan=120)

#Title
text = tk.Label(root, text="Calculating factorials", font="Raleway")
text.grid(column=1, row=1)

#Function
def start_calc():
    output_array = ["", ""]
    start_text.set("Loading...")
    i = 1
    global e1
    global e2
    output_array.clear()
    string = e1.get() 
    string2 = e2.get()
    integr = int(string)
    integr2 = int(string2)
    if string == "":
        error_message.set("Please enter correct numbers.")
    elif string2 == "":
        error_message.set("Please enter correct numbers.")
    else:
        while integr2 >= i:
            calc = integr ** i
            calcstr = (str(calc))
            output_array.append(calcstr)
            i += 1   
    start_text.set("Start!")
    output_array_str = (', '.join(output_array))
    # Change the output
    output_text.config(state="normal")
    # delete last output:
    output_text.delete("0.0", "end")
    # insert new output:
    output_text.insert("end", output_array_str)
    output_text.config(state="disabled")
    print(output_array_str) #This is just so I know if it's working or not in the terminal
    
    
#input
tk.Label(root, text="Number :").grid(row=10)
tk.Label(root, text="To the power of :").grid(row=11)
e1 = tk.Entry(root)
e2 = tk.Entry(root)
e1.grid(row=10, column=1)
e2.grid(row=11, column=1)

#Error message if the input is invalid
error_message = tk.StringVar()
error_text = tk.Label(root, textvariable=error_message, font="Raleway")
error_message.set(" ")
error_text.grid(column=1, row=12)

#Startbutton
start_text = tk.StringVar()
start_btn = tk.Button(root, textvariable=start_text, command=start_calc, font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
start_text.set("Start!")
start_btn.grid(column=1, row=13, pady=10)

#output
output_text = tk.Text(root, height=1, width=20, wrap="none", font="Raleway")
output_text.insert("end", "Output")
output_text.config(state="disabled")
output_text.grid(columnspan=3, column=0, row=14, sticky="news")

#Adding a scrollbar
scrollbar = tk.Scrollbar(root, orient="horizontal", command=output_text.xview)
scrollbar.grid(columnspan=3, column=0, row=15, sticky="news")
output_text.config(xscrollcommand=scrollbar.set)

#disclaimer message
disclaimer_text = tk.Label(root, text="Disclaimer: The results will be printed from the power of 1 to the power entered ")
disclaimer_text.grid(columnspan=3, column=0, row=110)

root.mainloop()