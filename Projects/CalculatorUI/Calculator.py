import tkinter as tk

def command(number1, number2, arg: str) -> None:
    number1 = number1_entry.get()
    number2 = number2_entry.get()
    value = None
    number1 = number1.replace(',', '.')
    number2 = number2.replace(',', '.')
    try:
        if '.' in number1 or '.' in number2:
            num1 = float(number1)
            num2 = float(number2)
        else:
            num1 = int(number1)
            num2 = int(number2)
    except (ValueError, TypeError) as e:
        value = "Error: wrong value of argument"
        answer_entry.delete(0, 'end')
        answer_entry.insert(0, value)
        return

    if arg == '+':
        value = num1 + num2
    elif arg == '-':
        value = num1 - num2
    elif arg == '*':
        value = num1 * num2
    elif arg == '/':
        if num2 == 0:
            value = "Error: division by zero"
        else:
            value = num1 / num2
    elif arg == '%':
        if num2 == 0:
            value = "Error: division by zero"
        else:
            value = num1 % num2
    elif arg == '//':
        if num2 == 0:
            value = "Error: division by zero"
        else:
            value = num1 // num2

    answer_entry.delete(0, 'end')
    answer_entry.config(state="normal")
    answer_entry.insert(0, value)
    answer_entry.config(state="readonly")


if __name__ == '__main__':
    window = tk.Tk()
    window.config(bg="#333333")
    window.title('Калькулятор')
    window.geometry("255x350")
    window.resizable(False, False)

    button_add = tk.Button(window, text="+", width=3, height=2, command=lambda: command(number1, number2, '+'), bg="#E85555", font=("Arial", 10, "bold"), fg="#FFFFFF")
    button_add.place(x=25, y=200)
    button_sub = tk.Button(window, text="-", width=3, height=2, command=lambda: command(number1, number2, '-'), bg="#E85555", font=("Arial", 10, "bold"), fg="#FFFFFF")
    button_sub.place(x=60, y=200)
    button_mul = tk.Button(window, text="*", width=3, height=2, command=lambda: command(number1, number2, '*'), bg="#E85555", font=("Arial", 10, "bold"), fg="#FFFFFF")
    button_mul.place(x=95, y=200)
    button_div = tk.Button(window, text="/", width=3, height=2, command=lambda: command(number1, number2, '/'), bg="#E85555", font=("Arial", 10, "bold"), fg="#FFFFFF")
    button_div.place(x=130, y=200)
    button_div = tk.Button(window, text="%", width=3, height=2, command=lambda: command(number1, number2, '%'), bg="#E85555", font=("Arial", 10, "bold"), fg="#FFFFFF")
    button_div.place(x=165, y=200)
    button_div = tk.Button(window, text="//", width=3, height=2, command=lambda: command(number1, number2, '//'), bg="#E85555", font=("Arial", 10, "bold"), fg="#FFFFFF")
    button_div.place(x=200, y=200)

    number1_entry = tk.Entry(window, width=29, bg="#DDDDDD", font=("Arial", 10, "bold"), fg="#000000")
    number1_entry.place(x=25, y=75)

    number2_entry = tk.Entry(window, width=29, bg="#DDDDDD", font=("Arial", 10, "bold"), fg="#000000")
    number2_entry.place(x=25, y=150)

    answer_entry = tk.Entry(window, width=29, state="readonly", bg="#E85555", font=("Arial", 10, "bold"), fg="#000000")
    answer_entry.insert(0, '')
    answer_entry.config(state="readonly")
    answer_entry.place(x=25, y=300)

    number1 = tk.Label(window, text="Введите первое число:            ", bg="#E85555", font=("Arial", 10, "bold"), fg="#FFFFFF")
    number1.place(x=25, y=50)
    number2 = tk.Label(window, text="Введите второе число:            ", bg="#E85555", font=("Arial", 10, "bold"), fg="#FFFFFF")
    number2.place(x=25, y=125)
    answer = tk.Label(window,  text="Ответ:                                        ", bg="#E85555", font=("Arial", 10, "bold"), fg="#FFFFFF")
    answer.place(x=25, y=275)


    window.mainloop()
