message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = ""
for ch in message:
    pos = ord(ch)
    if (pos <= 90) and (pos >= 65):
        pos = ord(ch) - ord('A')
        pos = (pos + offset) % 26
        encoded_message = encoded_message + chr(pos + ord('A'))
    elif (pos >= 97) and (pos <= 122):
        pos = ord(ch) - ord('a')
        pos = (pos + offset) % 26
        encoded_message = encoded_message + chr(pos + ord('a'))
    else:
        encoded_message = encoded_message + ch
