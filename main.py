import geometry
import function_file


def main():
    main_calc = int(input("please enter a number 1 or 2, 1=calculator, 2=geometry: "))
    while main_calc not in[1,2]:
          main_calc = int(input("please enter a number 1 or 2, 1=calculator, 2=geometry: "))
    if main_calc == 1:
         calc()
    elif main_calc == 2:
         geometry_calc()

calculator = main()
print(calculator)

def geometry_calc():
    while True:
        try:
            user = int(input("please enter a number 1 - 3: "))
            while user not in[1,2,3]:
                    user = int(input("please enter a number 1 - 3: "))
            if user == 1:
                length = int(input("please enter a number length: "))
                width = int(input("please enter a number length: "))
                geometry.rectangle(length,width)
            elif user == 2:
                base_triangle = int(input("please enter a number base triangle: "))
                height_triangle = int(input("please enter a number height triangle: "))
                geometry.triangle(base_triangle,height_triangle)
            elif user == 3:
                user1 = int(input("please enter a number 1 - 3: "))
                while user1 not in[1,2,3]:
                    user1 = int(input("please enter a number 1 - 3: "))
                if user1 == 1:
                     radius = int(input("please enter a number base triangle: "))
                     geometry.circle_area_from_radius(radius)
                elif user1 == 2:
                     diameter = int(input("please enter a number of diameter: "))
                     geometry.circle_area_from_diameter(diameter)
                elif user1 == 3:
                     circumference = int(input("please enter a number of circumference: "))
                     geometry.circle_area_from_circumference(circumference)
        except ValueError:
             print("Error! the value you entered is incorrect.")
        except ZeroDivisionError:
             print("Error! The value you entered is zero.")

def calc():
    while True:
        try:
            num1 = int(input("please enter a number: "))
            account_operation = input("please enter account operation, add=+, sub=-, multy=*, div=/, power=** ,root=***, absolute value=-+, : ")
            while account_operation not in["+","-","*","/","**","***","-+"]:
                account_operation = input("please enter account operation, add=+, sub=-, multy=*, div=/, power=** ,root=***, absolute value=-+, : ")
            if account_operation == "+":
                 num2 = int(input("please enter a number: "))
                 function_file.add(num1,num2)
            elif account_operation == "-":
                 num2 = int(input("please enter a number: "))
                 function_file.subtraction(num1,num2)
            elif account_operation == "*":
                 num2 = int(input("please enter a number: "))
                 function_file.multiplication(num1,num2)
            elif account_operation == "/":
                 num2 = int(input("please enter a number: "))
                 function_file.division(num1,num2)
            elif account_operation == "**":
                 num2 = int(input("please enter a number: "))
                 function_file.power(num1,num2)
            elif account_operation == "***":
                 function_file.root(num1)
            elif account_operation == "-+":
                function_file.Absolute_number(num1)
        except ValueError:
             print("Error! the value you entered is incorrect.")
        except ZeroDivisionError:
             print("Error! The value you entered is zero.")
          
