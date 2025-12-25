import os
import random
import sys

print("It has started")
# Name input
previous_total_string = open("Total Binary String.txt", "r").read() if os.path.exists("Total Binary String.txt") else "Total Binary String.txt does not exist. Please pull the file from the github repo and paste it in the same folder as this script, and restart."
user_name = input("Enter your name to register under: ")
num_combinatons = previous_total_string.count("/")
print("Hello, " + user_name + "!")
#Generate a binary string of length 9 with random 0s and 1s
def generate_binary_string(length=9):
    return ''.join(random.choice('01') for _ in range(length))
#Split the previous total string by forward slashes to get existing binary strings
existing_binaries = previous_total_string.split("/") if previous_total_string != "Total Binary String.txt" else []# Check if the binary string exists in the previous total string
binary_string = generate_binary_string()

if binary_string in existing_binaries:
    print("You have successfully generated an unique binary string. Your brinary string is:", binary_string)
else:
    print("The string generated exists, you must regenerate. You might check to see if you have every single possible binary string of length 9 already generated.")
    print("There are", num_combinatons, "unique binary strings in the total string.")
    def restart_script(): os.execv(sys.executable, ['python'] + sys.argv)
    restart_script()
total_string = previous_total_string + binary_string + "/"
open("Total Binary String.txt", "w").write(total_string)
print("Total string:", total_string)
# Create a txt file and make the user_name string the file name
file_name = user_name + ".txt"
with open(file_name, "w") as file:
    file.write(binary_string)
print("Binary string saved to file:", file_name)
print("This file is kept inside the same folder as this script under your name. Commit it into the github repo to be able to use your dollar later.")

print("Generating pin...")

# First Convert Binary String to Integer
binary_integer = int(binary_string, 2)
# Then multiply binary_integer by the number of number of forward slashes in total_string
num_slashes = total_string.count("/")
pin_integer = binary_integer * num_slashes
# Multiply the Pin by a constant factor to ensure it's a larger number 
secondary_factor = input("Would you like to enter a secondary factor to increase pin complexity? (y/n): ")
if secondary_factor.lower() == "y":
    secondary_factor = int(input("Enter a secondary factor: "))
    pin_integer = pin_integer * secondary_factor
else:
    pin_integer = pin_integer * 1593
pin_integer = pin_integer % 9999  # Ensure it's a 4-digit number
# Format the pin to be exactly 4 digits, padding with leading zeros if necessary
pin_string = f"{pin_integer:04d}"
print("Generated 4-digit pin:", pin_string, "(Keep this pin safe, to be able to cash use your dollar. You will need it later.)")
print("Thank you for using your Tirstan Buck Generator! Your buck has been created, make sure to commit your file into the github repo to be able to use it later.")
final_info = input("Almost Complete! Would you like to save your pin, secondary factor and binary onto another txt document outside of this folder? (y/n): ")
if final_info.lower() == "y":
    # Save pin, secondary factor, and binary string to a new text file outside of this folder
    save_path = input("Enter the full path where you would like to save the file (including filename.txt): ")
    with open(save_path, "w") as save_file:
        save_file.write(f"User Name: {user_name}\n")
        save_file.write(f"Binary String: {binary_string}\n")
        save_file.write(f"Pin: {pin_string}\n")
        save_file.write(f"Secondary Factor: {secondary_factor if secondary_factor.lower() == 'y' else 'N/A'}\n")
    print(f"Information saved to {save_path}")
else: print("Goodbye!")