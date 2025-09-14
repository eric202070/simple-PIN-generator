import random
import time as tm


def generate_pin(length=7):
    if length < 1:
        print("Type at least 1 length")
        return False
    pin = random.choices("0123456789", k=length)
    return "".join(pin)

if __name__ == "__main__":
    input_value = int(input("Enter the length of the pin: "))
    if generate_pin(input_value) is False:
      print("Valor invalido, gerando senha aleatoriade 7 digitos")
      input_value = 7
    pin = generate_pin(input_value)
    print(pin)
    tm.sleep(2)
    save = input("Want to save? (y/n)").lower()
    if save == 'y':
        with open("./python_projects/random_pin/pin.txt", "a") as f:
            f.write(pin)
        print("Added to pin.txt")
    else:
        print("Alright, not saved.")