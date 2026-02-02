import geometry
import function_file






def geometry_calc():
    while True:
        try:
            user = int(input("please enter a number 1 - 3: "))
            while user not in[1,2,3]:
                    user = int(input("please enter a number 1 - 3: "))
            if user == 1:
                length = float(input("please enter a number length: "))
                width = float(input("please enter a number width: "))
                return geometry.rectangle(length,width)
            elif user == 2:
                base_triangle = float(input("please enter a number base triangle: "))
                height_triangle = float(input("please enter a number height triangle: "))
                return geometry.triangle(base_triangle,height_triangle)
            elif user == 3:
                user1 = int(input("please enter a number 1 - 3: "))
                while user1 not in[1,2,3]:
                    user1 = int(input("please enter a number 1 - 3: "))
                if user1 == 1:
                     radius = float(input("please enter a number of radius: "))
                     return geometry.circle_area_from_radius(radius)
                elif user1 == 2:
                     diameter = float(input("please enter a number of diameter: "))
                     return geometry.circle_area_from_diameter(diameter)
                elif user1 == 3:
                     circumference = float(input("please enter a number of circumference: "))
                     return geometry.circle_area_from_circumference(circumference)
        except ValueError:
             print("Error! the value you entered is incorrect.")
        except ZeroDivisionError:
             print("Error! The value you entered is zero.")

def calc():
    while True:
        try:
            num1 = float(input("please enter a number: "))
            account_operation = input("please enter account operation, add = +, sub = -, multy = *, div = /, power = ** ,root = ***, absolute value = -+, : ")
            while account_operation not in["+","-","*","/","**","***","-+"]:
                account_operation = input("please enter account operation, add = +, sub = -, multy = *, div = /, power = ** ,root = ***, absolute value = -+, : ")
            if account_operation == "+":
                 num2 = float(input("please enter a number: "))
                 return function_file.add(num1,num2)
            elif account_operation == "-":
                 num2 = float(input("please enter a number: "))
                 return function_file.subtraction(num1,num2)
            elif account_operation == "*":
                 num2 = float(input("please enter a number: "))
                 return function_file.multiplication(num1,num2)
            elif account_operation == "/":
                 num2 = float(input("please enter a number: "))
                 return function_file.division(num1,num2)
            elif account_operation == "**":
                 num2 = float(input("please enter a number: "))
                 return function_file.power(num1,num2)
            elif account_operation == "***":
                 return function_file.root(num1)
            elif account_operation == "-+":
                 return function_file.Absolute_number(num1)
        except ValueError:
             print("Error! the value you entered is incorrect.")
        except ZeroDivisionError:
             print("Error! The value you entered is zero.")

def main():
    main_calc = input("please enter a number 1 or 2, 1=calculator, 2=geometry: ")
    while main_calc not in["1","2"]:
          main_calc = input("please enter a number 1 or 2, 1=calculator, 2=geometry: ")
    if main_calc == "1":
         return calc()
    elif main_calc == "2":
         return geometry_calc()


calculator = main()
print(calculator)
          
