def get_secret_message(image_path):
    bytes_to_skip = 64
    with open(image_path, "rb") as image_file:
        image_file.read(bytes_to_skip)
        byte_array = []
        byte = image_file.read(1)
        while byte:
            byte_array.append((ord(byte)))
            byte = image_file.read(1)
    output_list = []
    list_item = ""
    counter = 0
    for item in byte_array:
        num = str(item % 2)
        list_item += num
        counter += 1
        if counter % 8 == 0:
            list_item_int = int(list_item, 2)
            if list_item_int > 128 or list_item_int == 0:
                break
            output_list.append(list_item_int)
            list_item = ""
    char_list = []
    for x in output_list:
        if x > 128 or x == 0:
            break
        char_list.append(chr(x))
    output = ''.join(char_list)
    return output