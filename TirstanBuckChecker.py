import os
import sys
previous_total_string = open("Total Binary String.txt", "r").read() if os.path.exists("Total Binary String.txt") else "Total Binary String.txt does not exist. Please pull the file from the github repo and paste it in the same folder as this script, and restart."
current_binary = input("Enter the current binary input: ")


if current_binary in previous_total_string:
    print("Binary string found in total string. Proceeding with verification...")
    # Generate the expected pin based on the binary string
    binary_integer = int(current_binary,2)
    print ("Binary Int =", binary_integer)
    secondary_factor = input("Do you have a secondary factor? (y/n): ")
if secondary_factor.lower() == "y":
    secondary_factor = int(input("Enter a secondary factor: "))
    pin_integer = binary_integer * secondary_factor
else:
    pin_integer = binary_integer * 1593
pin_integer = pin_integer % 10000  # Ensure it's a 4-digit number
print("Expected pin integer is:", pin_integer)
    # Reverse the pin and secondary number that the binary wants
user_pin = input("Enter your 4-digit pin: ")
if user_pin == str(pin_integer):
    print("Pin verified successfully! You can now proceed to use your Tirstan Buck.")
else:
    print("Error: Incorrect pin. Access denied.")