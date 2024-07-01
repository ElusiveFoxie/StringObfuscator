import argparse
import random
import string
from random import randrange

def obfuscate_string(input_string, mode):

    # Revers original
    input_string = input_string[::-1]
    # Split the input string according to the pattern
    pattern = []
    i = 0
    take_two = False
    while i < len(input_string):
        if take_two and i + 1 < len(input_string):
            pattern.append(input_string[i:i+2])
            i += 2
        else:
            pattern.append(input_string[i])
            i += 1
        take_two = not take_two  # Toggle between taking 1 or 2 characters




    # Create random strings for each element in the pattern
    randoms = []
    for _ in pattern:
        random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
        randoms.append(random_str)

    # Concatenate all random strings to form the obfuscated string
    obfuscated_string = ''.join(randoms)

    # var length

    var_length = randrange(2,10)

    if mode == "powershell":
         powershell(pattern, randoms, var_length)
    elif mode == "csharp":
        csharp(pattern, randoms, var_length)

    return obfuscated_string



def powershell(pattern, randoms, var_length):

    print("Paste this in powershell:\n")

    obfuscated_string = ''.join(randoms)

    variable = ''.join(random.choices(string.ascii_letters, k=var_length))
    print ("$" + variable + "=\"" + obfuscated_string + "\"" )

    for i in range(len(pattern)):
        print("$" + variable + " = $" + variable + ".Replace('" + randoms[i] +"','"+ pattern[i] + "')")

    print("$" + variable + " = " + "$" + variable + "[-1..-$" + variable + ".Length] -join ''")

    print("$" + variable)

def csharp(pattern, randoms, var_length):
    print("Paste this in C# environment:\n")

    obfuscated_string = ''.join(randoms)

    variable = ''.join(random.choices(string.ascii_letters, k=var_length))
    print("var " + variable + " = \"" + obfuscated_string + "\";")
    for i in range(len(pattern)):
        print(variable + " = " + variable + ".Replace(\"" + randoms[i] + "\", \"" + pattern[i] + "\");")


    charArray = ''.join(random.choices(string.ascii_letters, k=randrange(2,10)))
    temp = ''.join(random.choices(string.ascii_letters, k=randrange(2,10)))

    print("char[] " + charArray + " = "+variable+".ToCharArray();")

    print("for (int i = 0, j = " + charArray +".Length - 1; i < j; i++, j--)")
    print("{char "+temp+" ="+charArray+"[i];" + charArray + "[i] = " + charArray + "[j];" + charArray + "[j] = " + temp + ";}")
    print(variable + "= new string(" +charArray + ");" )

    print("Console.WriteLine(" + variable + ");")

def main():
    parser = argparse.ArgumentParser(description="Obfuscate a string by interleaving random alphanumeric characters.")
    parser.add_argument("-s", "--string", required=True, help="Input string to obfuscate.")
    parser.add_argument("-m", "--mode", required=True, help="Mode (powershell or csharp)")
    
    args = parser.parse_args()

    # Obfuscate the input string
    obfuscated_string = obfuscate_string(args.string,args.mode)

if __name__ == "__main__":
    main()
