def main(input: str):
    try:
        parts = input.split()
        if len(parts) != 3:
            print("Неверный ввод")


        a = int(parts[0])
        op = parts[1]
        b = int(parts[2])


        if a < 1 or a > 10 or b < 1 or b > 10:
            raise ValueError("Числа должны быть от 1 до 10")

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            result = a // b
        else:
            raise ValueError("Неизвестная операция")

        return str(result)

    except Exception as e:
        return str(f'Произошоа ошибка: {e}')


if __name__ == "__main__":
    user_input = input("Введите арифметическое выражение: ")
    output = main(user_input)
    print("Результат:", output)