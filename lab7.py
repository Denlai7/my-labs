import tkinter as tk

def columnar_encrypt(text, height):
    text = text.replace(" ", "")
    return ''.join(text[i::height] for i in range(height))

def columnar_decrypt(ciphertext, height):
    width = -(-len(ciphertext) // height)
    return ''.join(ciphertext[i::width] for i in range(width))

def encrypt_decrypt():
    input_text = entry_text.get()
    column_height = int(entry_height.get())

    ciphertext = columnar_encrypt(input_text, column_height)
    label_result.config(text="Зашифровано: " + ciphertext)

    decryption = columnar_decrypt(ciphertext, column_height)
    label_decryption.config(text="Розшифровано: " + decryption)

root = tk.Tk()
root.title("Шифр Частоколу")

label_text = tk.Label(root, text="Введіть текст для шифрування:")
label_text.pack()

entry_text = tk.Entry(root)
entry_text.pack()

label_height = tk.Label(root, text="Введіть висоту стовпчика (column_height):")
label_height.pack()

entry_height = tk.Entry(root)
entry_height.pack()

button_encrypt = tk.Button(root, text="Зашифрувати та розшифрувати", command=encrypt_decrypt)
button_encrypt.pack()

label_result = tk.Label(root, text="")
label_result.pack()

label_decryption = tk.Label(root, text="")
label_decryption.pack()

root.mainloop()
