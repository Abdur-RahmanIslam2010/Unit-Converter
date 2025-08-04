import tkinter as tk
from conops import operationslu, operationstu, operationsdu, operationsmu

all_operations = {
    'length': operationslu,
    'temperature': operationstu,
    'mass': operationsmu,
    'data': operationsdu
}

lu = ["in.", "cm.", "m.", "ft.", "miles", "yards", "km"]
tu = ["°C", "°F", "K"]
mu = ['g', 'kg', 'lb', 'mg', 'oz', 'st', 't']
du = ["b", "B", "kB", "MB", "GB", "TB"]

def show_page2(parent):
    for widget in parent.winfo_children():
        widget.destroy()
    global lu, tu, mu, du, select_var, convert_var
    global dropdown, dropdown2, calc, result_label, input_box
    select_var = tk.StringVar(value="")
    convert_var = tk.StringVar(value="")
    si_label = tk.Label(window, text="Unit Conversion", font=("Arial", 15))
    si_label.grid(column=0, row=0, columnspan=4, padx=50, pady=15)
    input_box = tk.Entry(window, bd=2, relief="raised", font=(15))
    input_box.grid(column=0, row=1, padx=10, sticky='e')
    dropdown = tk.OptionMenu(window, select_var, *mu)
    dropdown.grid(column=1, row=1)
    to_label = tk.Label(window, text="to:", font=("Arial", 15))
    to_label.grid(column=2, row=1)
    dropdown2 = tk.OptionMenu(window, convert_var, *mu)
    dropdown2.grid(column=3, row=1)
    result_label = tk.Label(window, text="Result:", font=("Arial", 15), pady=10)
    result_label.grid(column=0, row=2)
    calc = tk.Button(window, text="Calculate", pady=10, command=calc_result)
    calc.grid(column=0, row=3)
    back = tk.Button(window, text="Back", width=7, pady=10, command=lambda: show_page1(window))
    back.grid(column=1, row=3)



def calc_result():
    try:
        input_num = float(input_box.get())
        from_unit = select_var.get()
        to_unit = convert_var.get()

        if from_unit in lu:
            conversion_type = 'length'
        elif from_unit in tu:
            conversion_type = 'temperature'
        elif from_unit in mu:
            conversion_type = 'mass'
        elif from_unit in du:
            conversion_type = 'data'
        else:
            result_label.config(text="Error: Invalid unit selected.")
            return

        operations = all_operations[conversion_type]

        if from_unit in operations and to_unit in operations[from_unit]:
            conversion_function = operations[from_unit][to_unit]
            converted_value = conversion_function(input_num)
            result_label.config(text=f"Result: {converted_value}")
        else:
            result_label.config(text="Error: Invalid conversion combination.")

    except ValueError:
        result_label.config(text="Error: Please enter a valid number.")
    except Exception as e:
        result_label.config(text=f"Error: An exception has occurred: {e}")
window = tk.Tk()
window.title("Unit Converter")
window.geometry('400x200')

def length_conver():
    global current_conversions
    current_conversions = lu
    menu = dropdown['menu']
    menu.delete(0, 'end')
    menu2 = dropdown2['menu']
    menu2.delete(0, 'end')
    for item in lu:
        menu.add_command(label=item, command=tk._setit(select_var, item))
        menu2.add_command(label=item, command=tk._setit(convert_var, item))
    
def data_conver():
    current_conversions = du
    menu = dropdown['menu']
    menu.delete(0, 'end')
    menu2 = dropdown2['menu']
    menu2.delete(0, 'end')
    for item in du:
        menu.add_command(label=item, command=tk._setit(select_var, item))
        menu2.add_command(label=item, command=tk._setit(convert_var, item))

def temp_conver():
    current_conversions = tu
    menu = dropdown['menu']
    menu.delete(0, 'end')
    menu2 = dropdown2['menu']
    menu2.delete(0, 'end')
    for item in tu:
        menu.add_command(label=item, command=tk._setit(select_var, item))
        menu2.add_command(label=item, command=tk._setit(convert_var, item))

def mass_conver():
    current_conversions = mu
    menu = dropdown['menu']
    menu.delete(0, 'end')
    menu2 = dropdown2['menu']
    menu2.delete(0, 'end')
    for item in mu:
        menu.add_command(label=item, command=tk._setit(select_var, item))
        menu2.add_command(label=item, command=tk._setit(convert_var, item))
    

def show_page1(parent):
    for widget in parent.winfo_children():
        widget.destroy()
    fi_label = tk.Label(window, text="Choose the type of conversion: ", font=("Arial", 15))
    fi_label.grid(column=0, row=0, columnspan=4, padx=50, pady=15)
    
    global length_b, temp_b, mass_b, data_b
    length_b = tk.Button(window, text="Length", width=10, padx=10, command=lambda: [show_page2(window), length_conver()])
    length_b.grid(row=1, column=0, padx=50, pady=15)
    temp_b = tk.Button(window, text="Temperature", width=10, padx=10, command=lambda: [show_page2(window), temp_conver()])
    temp_b.grid(row=1, column=1, padx=50, pady=15)
    mass_b = tk.Button(window, text="Mass", width=10, padx=10, command=lambda: [show_page2(window), mass_conver()])
    mass_b.grid(row=2, column=0, padx=50, pady=15)
    data_b = tk.Button(window, text="Data", width=10, padx=10, command=lambda: [show_page2(window), data_conver()])
    data_b.grid(row=2, column=1, padx=50, pady=15)

show_page1(window) 
window.mainloop()
