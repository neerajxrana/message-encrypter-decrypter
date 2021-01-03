import pyperclip
from tkinter import *

root = Tk()
root.title("Secret Whisperer")

canvas = Canvas(root, height=700, width=700)
canvas.pack()

filename = PhotoImage(
    file="C:\\Users\\NEERAJ RANA\\Desktop\\War Files\\Wall\\480537.png")
canvas.create_image(0, 0, image=filename, anchor=NW)

frame = Frame(root, bg="#0c8a27")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

message = Label(frame, text="Enter your message: ")
message.pack(anchor=W, padx=10, pady=10)

# ---------Entry field for accepting the message from the user---------
a = StringVar()
plaintext = Entry(frame, bd=5, textvariable=a, width=80)
plaintext.pack(anchor=NW, padx=10)


cipher_select = Label(frame, text="Choose your cipher: ")
cipher_select.pack(anchor=W, padx=10, pady=10)

# ---------Listbox for letting the user choose the cipher---------------
cipher = Listbox(frame)
cipher.insert(1, "Caesar Cipher")
cipher.insert(2, "Reverse Cipher")
cipher.insert(3, "Transposition Cipher")
cipher.insert(4, "Caesar Cipher Brute")
cipher.insert(5, "Affine Cipher")

cipher.pack(anchor=W, padx=10)

key_select = Label(frame, text="Enter your key: ")
key_select.pack(anchor=W, padx=10, pady=10)

# ---------Entry field for accepting the key from the user--------------
b = StringVar()
key = Entry(frame, bd=5, textvariable=b, width=10)
key.pack(anchor=NW, padx=10)

# ----------RadioButton for letting the user choose form enc and dec----
var = IntVar()
Radiobutton(frame, text="Encrpt", variable=var,
            value=1).pack(anchor=W, pady=10, padx=10)
Radiobutton(frame, text="Decrypt", variable=var,
            value=2).pack(anchor=W, padx=10)


'''output_text = Label(frame, text="Output: ")
output_text.pack(anchor=W, padx=10, pady=10)


output = Entry(frame, bd=5, width=80)
output.pack(anchor=NW, padx=10)'''

# xxxxxxxxxxxxxxxxxxx All Ciphers  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


def caesar_encryption(pv, kv):
    #message = input("Enter your message: ")
    #key = int(input("Enter your key: "))
    message = pv
    key = kv
    SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?_"
    translated = ""

    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex + key

            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    output.insert(0, translated)
    pyperclip.copy(translated)

def caesar_decryption(pv, kv):
	message = pv
	key = kv
	SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?_"
	translated = ""

	for symbol in message:
		if symbol in SYMBOLS:
			symbolIndex = SYMBOLS.find(symbol)
			translatedIndex = symbolIndex - key

			if translatedIndex >= len(SYMBOLS):
				translatedIndex = translatedIndex - len(SYMBOLS)
			elif translatedIndex < 0:
				translatedIndex = translatedIndex + len(SYMBOLS)

			translated = translated + SYMBOLS[translatedIndex]
		else:
			translated = translated + symbol
	output.insert(0, translated)
	pyperclip.copy(translated)
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


# =======================================================
# =======================================================
# -----------------THE MASTER COMMAND--------------------
def master_command(pv, cv, kv, edv):
    if(cv=="Caesar Cipher" and edv==1):
        caesar_encryption(pv, kv)
    elif(cv=="Caesar Cipher" and edv==2):
        caesar_decryption(pv, kv)


# -------------------------------------------------------
# =======================================================
# ======================================================


killswitch = Button(frame, text="Encrypt/Decrypt",
                    command=lambda: master_command(plaintext.get(), cipher.get(ACTIVE), int(key.get()), var.get()))
killswitch.pack()

output_text = Label(frame, text="Output: ")
output_text.pack(anchor=W, padx=10, pady=10)


output = Entry(frame, bd=5, width=80)
output.pack(anchor=NW, padx=10)


root.mainloop()
