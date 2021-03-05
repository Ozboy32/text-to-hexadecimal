input_text = input("Input:")
convert = list(input_text)
for x in convert:
    output_1 = ord(x)
    output_2 = hex(output_1)
    print(output_2, end=' ')
