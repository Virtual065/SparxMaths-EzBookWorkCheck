import datetime

import os

if not os.path.exists("output"):
    os.mkdir("Saves")

time = datetime.datetime.now().strftime("%d-%m-%Y    %Hh %Mm %Ss")

file = open(f"Saves/{time}.txt", "w")

counter = 1

number = 1

while True:
    text = input(f"{number}{chr(96 + counter)} = ")
    
    if text.lower() == "quit":
        break
    
    if text.lower() == "next":
        number += 1
        counter = 1
        file.write("\n")
        continue
    
    file.write(f"{number}{chr(96 + counter)} = {text}\n")
    
    counter += 1

file.close()
