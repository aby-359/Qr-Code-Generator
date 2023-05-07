from tkinter import *
import pyqrcode
from PIL import ImageTk, Image
import time

root = Tk()
root.title("QR Code Generator")

# Set canvas dimensions and background color
canvas = Canvas(root, width=500, height=900, bg="#f7f7f7")
canvas.pack()

# Add title label with animation
title_text = "QR Code Generator"
title_label = Label(root, text="", font=("Courier New", 30), fg="#333333", bg="#f7f7f7")
canvas.create_window(250, 100, window=title_label)
for i in range(len(title_text)):
    title_label.configure(text=title_label.cget("text") + title_text[i])
    time.sleep(0.1)
    root.update()

# Add link name label
name_label = Label(root, text="Link Name:", font=("Courier New", 16), fg="#333333", bg="#f7f7f7")
canvas.create_window(250, 200, window=name_label)

# Add link name entry field
name_entry = Entry(root, font=("Courier New", 16), bg="#FFFFFF", borderwidth=2, relief="groove")
canvas.create_window(250, 240, window=name_entry)

# Add link label
link_label = Label(root, text="Link:", font=("Courier New", 16), fg="#333333", bg="#f7f7f7")
canvas.create_window(250, 300, window=link_label)

# Add link entry field
link_entry = Entry(root, font=("Courier New", 16), bg="#FFFFFF", borderwidth=2, relief="groove")
canvas.create_window(250, 340, window=link_entry)


# Define generate function
def generate():
    # Get link name and link from entry fields
    link_name = name_entry.get()
    link_link = link_entry.get()

    # Generate QR code and save to file
    file_name = link_name + ".png"
    url = pyqrcode.create(link_link)
    url.png(file_name, scale=8)

    # Display QR code image
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(250, 610, window=image_label)


# Add generate button
generate_button = Button(text="Generate QR Code", font=("Courier New", 16), bg="#4CAF50", fg="#FFFFFF", borderwidth=0,
                         command=generate)
canvas.create_window(250, 420, window=generate_button)

# Run main loop
root.mainloop()
