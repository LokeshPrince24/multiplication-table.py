# Open the input file in read mode and output file in write mode
with open('input.txt', 'r') as infile, open('output9.txt', 'w') as outfile:
    # Read the numbers from the input file
    numbers = [int(num.strip()) for num in infile.readlines()]

    for num in numbers:
        outfile.write("Multiplication table for " + str(num) + ":\n")
        i = 0
        k = 1
        while k <= 10:
            outfile.write(str(num) + " * " + str(k) + " = " + str(num * k) + "\n")
            k = k + 1
        outfile.write("\n")
