input_string = input()
hex_representation = ''.join([hex(ord(char))[2:] for char in input_string])
print(hex_representation)

hex_string = hex_representation
decoded_string = bytes.fromhex(hex_string[2:]).decode('utf-8')
print(decoded_string)
