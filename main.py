import tkinter as tk
from tkinter import filedialog

def caesar_cipher(text, shift, direction):
    """Encrypts or decrypts a text string using the Caesar cipher.

    Args:
        text (str): The text to be encrypted or decrypted.
        shift (int): The shift value for the cipher.
        direction (int): 1 for encryption, -1 for decryption.

    Returns:
        str: The encrypted or decrypted text.
    """
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            new_char = chr((ord(char) - ascii_offset + direction * shift) % 26 + ascii_offset)
            result += new_char
        else:
            result += char
    return result

def encrypt():
    """Encrypts the text from the text_entry widget using the shift value from the shift_entry widget."""
    text = text_entry.get()
    shift = shift_entry.get()
    if not text or not shift:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error: Both text and shift value must be provided.")
        return
    try:
        shift = int(shift)
        encrypted_text = caesar_cipher(text, shift, direction=1)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Encrypted Text: " + encrypted_text)
    except ValueError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error: Shift value must be an integer.")
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error: " + str(e))

def decrypt():
    """Decrypts the text from the text_entry widget using the shift value from the shift_entry widget."""
    text = text_entry.get()
    shift = shift_entry.get()
    if not text or not shift:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error: Both text and shift value must be provided.")
        return
    try:
        shift = int(shift)
        decrypted_text = caesar_cipher(text, shift, direction=-1)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Decrypted Text: " + decrypted_text)
    except ValueError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error: Shift value must be an integer.")
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error: " + str(e))
        
def clear():
    """Clears the text_entry, shift_entry, and result_text widgets."""
    text_entry.delete(0, tk.END)
    shift_entry.delete(0, tk.END)
    result_text.delete(1.0, tk.END)

def copy_to_clipboard():
    """Copies the contents of the result_text widget to the clipboard."""
    result = result_text.get(1.0, tk.END).strip()  # Get the result text and remove trailing newline
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(result) 
        
def save_to_file():
    """Saves the contents of the result_text widget to a file."""
    file_name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_name:
        with open(file_name, "w") as file:
            file.write(result_text.get(1.0, tk.END))

def load_from_file():
    """Loads the contents of a file into the text_entry widget."""
    file_name = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_name:
        with open(file_name, "r") as file:
            content = file.read()
            if "Encrypted Text: " in content:
                content = content.replace("Encrypted Text: ", "")
            elif "Decrypted Text: " in content:
                content = content.replace("Decrypted Text: ", "")
            text_entry.delete(0, tk.END)
            text_entry.insert(0, content)

root = tk.Tk()
root.geometry("500x350")    #Set the window size
root.title("Caesar Cipher")

# Create and pack all the widgets
text_label = tk.Label(root, text="Enter Text:")
text_label.pack()

text_entry = tk.Entry(root)
text_entry.pack()

shift_label = tk.Label(root, text="Enter Shift:")
shift_label.pack()

shift_entry = tk.Entry(root)
shift_entry.pack()

# Create a Frame to contain the buttons
button_frame1 = tk.Frame(root)
button_frame1.pack()

encrypt_button = tk.Button(button_frame1, text="Encrypt", command=encrypt)
encrypt_button.pack(side=tk.LEFT, padx=5) 


decrypt_button = tk.Button(button_frame1, text="Decrypt", command=decrypt)
decrypt_button.pack(side=tk.LEFT, padx=5)


clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.pack()

result_text = tk.Text(root, height=4, width=50)
result_text.pack()

button_frame2 = tk.Frame(root)
button_frame2.pack()

save_button = tk.Button(button_frame2, text="Save to File", command=save_to_file)
save_button.pack(side=tk.LEFT, padx=5)

load_button = tk.Button(button_frame2, text="Load from File", command=load_from_file)
load_button.pack(side=tk.LEFT, padx=5)

copy_button = tk.Button(button_frame2, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(side=tk.LEFT, padx=5)

root.mainloop() # Start the main loop