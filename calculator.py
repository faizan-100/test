def main():

    calc = str(input("Enter your calculation in the format : '45 + 55' or '45 ^2' or '45 - 2' or '45 * 2' or '45 ^3'"))


    for i in range(len(calc)):
        if calc[i] == "-":
            def subtraction(x,y):
                sub = x - y
                return sub
            print(subtraction())

        elif calc[i] == "^3":
            def cube_numbers(x):
                cubed = x * x * x
                return cubed
            print(cube_numbers())

        elif calc[i] == "^2":
            def squared_numbers(x):
                sqr = x * x
                return sqr
            print(squared_numbers())

        elif calc[i] == "+":
            def add_numbers(x,y):
                total = x + y
                return total
            print(add_numbers(4,5))

main()