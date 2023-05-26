import tkinter as tk


def answer():
    # Load the image file
    image = tk.PhotoImage(file="Python.png")
    resized_image = image.subsample(10)
    # Create a label to display the image
    image_label = tk.Label(root, image=resized_image)
    image_label.pack()
    root.mainloop()

root = tk.Tk()
root.title("Lior's window")     # title of window
root.geometry("600x400")
# place a label on the root window
message = tk.Label(root, text="What's my favorite programming language?", font=("Arial", 22))
message.pack()
button = tk.Button(root, text="Click to find out!", command=answer)
button.configure(bg="light blue")
button.pack()


root.mainloop()