import tkinter as tk

def caesar_encrypt(plain_text, key):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

def caesar_decrypt(encrypted_text, key):
    return caesar_encrypt(encrypted_text, -key)

def encrypt_button_clicked():
    key = int(key_entry.get())
    plaintext = plaintext_entry.get()
    encrypted_text = caesar_encrypt(plaintext, key)
    encrypted_text_entry.delete(0, tk.END)
    encrypted_text_entry.insert(0, encrypted_text)

def decrypt_button_clicked():
    key = int(key_entry.get())
    encrypted_text = encrypted_text_entry.get()
    decrypted_text = caesar_decrypt(encrypted_text, key)
    decrypted_text_entry.delete(0, tk.END)
    decrypted_text_entry.insert(0, decrypted_text)

# Create the main application window
app = tk.Tk()
app.title("Caesar Cipher : Encryption and Decryption")

# Create widgets (labels, entries, buttons)
plaintext_label = tk.Label(app, text="Enter Plain Text:")
plaintext_label.grid(row=0, column=0)
plaintext_entry = tk.Entry(app)
plaintext_entry.grid(row=0, column=1, padx=5, pady=5)

key_label = tk.Label(app, text="Enter Key (Shift value):")
key_label.grid(row=1, column=0, padx=5, pady=5)
key_entry = tk.Entry(app)
key_entry.grid(row=1, column=1, padx=5, pady=5)

encrypt_button = tk.Button(app, text="Encrypt", command=encrypt_button_clicked)
encrypt_button.grid(row=2, column=0, padx=5, pady=5)

encrypted_text_label = tk.Label(app, text="Encrypted Text:")
encrypted_text_label.grid(row=3, column=0, padx=5, pady=5)
encrypted_text_entry = tk.Entry(app)
encrypted_text_entry.grid(row=3, column=1, padx=5, pady=5)

decrypt_button = tk.Button(app, text="Decrypt", command=decrypt_button_clicked)
decrypt_button.grid(row=4, column=0, padx=5, pady=5)

decrypted_text_label = tk.Label(app, text="Decrypted Text:")
decrypted_text_label.grid(row=5, column=0, padx=5, pady=5)
decrypted_text_entry = tk.Entry(app)
decrypted_text_entry.grid(row=5, column=1, padx=5, pady=5)

# Start the main event loop
app.mainloop()