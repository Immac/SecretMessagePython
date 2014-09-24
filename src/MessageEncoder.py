import itertools
import os


def encode_message_into_bitmap(message, path):
    extension = '.bmp'
    output_image_identifier = 'out'
    byte_to_skip = 64
    file_bytes = []
    last_char = chr(255)
    message += last_char
    if extension in path:
        temp_list = path.rsplit(extension)
        path = ''.join(temp_list)
    input_image_name = path + extension
    output_image_name = path + output_image_identifier + extension
    char_list = list(message)
    int_list = list(ord(x) for x in char_list)
    num_list = list([int(x) for x in list('{0:0b}'.format(num))] for num in int_list)
    for element in num_list:
        while len(element) < 8:
            element.insert(0, 0)
    merged_list = list(itertools.chain(*num_list))
    size = os.path.getsize(input_image_name) - byte_to_skip
    size_needed = len(merged_list)
    if size < size_needed:
        print("Not enough space in image!")
        exit()
    with open(input_image_name, "rb") as image_file:
        for i in range(byte_to_skip):
            file_bytes.append(ord(image_file.read(1)))
        byte = image_file.read(1)
        for item in merged_list:
            new_byte = ((ord(byte) & ~1) | item)
            file_bytes.append(new_byte)
            byte = image_file.read(1)
        while byte:
            file_bytes.append(ord(byte))
            byte = image_file.read(1)
    with open(output_image_name, "wb") as image_file:
        new_byte_array = bytes(file_bytes)
        image_file.write(new_byte_array)