import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import messagebox

if __name__ == '__main__':
    import tkinter as tk
    from PIL import Image, ImageTk

    # --- constants ---

    WIDTH = 800
    HEIGHT = 600

    # --- main ---

    root = tk.Tk()

    c = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    c.pack()

    # only GIF and PGM/PPM
    # photo = tk.PhotoImage(file='test.gif')

    # other formats
    image = Image.open('new_background_img.png')
    photo = ImageTk.PhotoImage(image)
    # use in functions - solution for "garbage collector" problem
    c.image = photo

    i = c.create_image((WIDTH // 2, HEIGHT // 2), image=photo)
    t = c.create_text((WIDTH // 2, HEIGHT // 4), text='Hello World')

    root.mainloop()

