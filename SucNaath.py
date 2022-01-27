import os
import subprocess
import argparse


location_parser = argparse.ArgumentParser()       # Add an argument
location_parser.add_argument('--path', type=str, required=True)  # Parse the argument
args = location_parser.parse_args()
# Print "The Path to Password Files is " + the user input argument
print('The Path to Password Files is ', args.path)


print(" _______           _______  _  _        _______  _______ _________         ")
print("(  ____ \|\     /|(  ____ \( )( (    /|(  ___  )(  ___  )\__   __/|\     /|")
print("| (    \/| )   ( || (    \/|/ |  \  ( || (   ) || (   ) |   ) (   | )   ( |")
print("| (_____ | |   | || |         |   \ | || (___) || (___) |   | |   | (___) |")
print("(_____  )| |   | || |         | (\ \) ||  ___  ||  ___  |   | |   |  ___  |")
print("      ) || |   | || |         | | \   || (   ) || (   ) |   | |   | (   ) |")
print("/\____) || (___) || (____/\   | )  \  || )   ( || )   ( |   | |   | )   ( |")
print("\_______)(_______)(_______/   |/    )_)|/     \||/     \|   )_(   |/     \| version 1.0")
print("")
print("")


path = args.path
filenames = os.listdir(args.path)
bash_command = "cat Combined.txt | sort | uniq >> Deduped.txt"



with open("Combined.txt", "w") as outfile:              # Makes output file named Combined.txt
       for filename in filenames:                       # Loops through each file in directory
              if (filename != "SucNaath.py" and filename !="Combined.txt" and filename !="Deduped.txt"):               # Disregards script file if in same directory
                     print("Opening " + filename)
                     with open(path + filename) as infile:     # Opens the files within the loop
                            content = infile.read()     # Reads line and assigns it to "content variable"
                            outfile.write(content)      # Writes to the output file
                            infile.close()              # cLoSeS tHe fIlE (cAuSe wE aReN't mOnStErS)
       outfile.close()


subprocess.Popen(bash_command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)