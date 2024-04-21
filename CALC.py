import sys
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)


def calculate(operation, num1, num2):

    logging.info(f"{datetime.now()} - Operacja: {operation}, Argumenty: {num1}, {num2}")

    if operation == 1:
        result = num1 + num2
    elif operation == 2:
        result = num1 - num2
    elif operation == 3:
        result = num1 * num2
    elif operation == 4:
        result = num1 / num2
    
    return result

print("Podaj działanie, posługując się odpowiednią liczbą:")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")

operation = int(input("Wybierz operację: "))

num1 = float(input("Podaj pierwszą liczbę: "))
num2 = float(input("Podaj drugą liczbę: "))

print("Wynik:", calculate(operation, num1, num2))