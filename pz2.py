print("Счетчик среднего значения")      

class Number:
    def get_average(self, *args):
        if len(args) == 0:
            raise ValueError("Ошибка значений нету")
        return sum(args) / len(args)



def main():
    number = []
    while True:
        s = input("Введите число или Enter чтобы закончить программу ")
        
        if s == "":
            break

        try:
            number.append(float(s))

        except ValueError:
            print("Произошла ошибка повторите попытку")

    if not number:
        print("Не одного числа не было введено")
        return


    calc = Number()
    try:
        avg = calc.get_average(*number)
        print(f"Среднее значение {avg}")

    except ValueError as e:
        print(f"Ошибка{e}")


if __name__ == "__main__":
    main()






