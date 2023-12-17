import tkinter as tk
import random

def draw(canvas, result):
   
    canvas.delete("all")
    
    w = 300
    h = 300
    padding = 40
    
    points = {
        1: [(w // 2, h // 2)],
        2: [(padding, padding), (w - padding, h - padding)],
        3: [(padding, padding), (w // 2, h // 2), (w - padding, h - padding)],
        4: [(padding, padding), (w - padding, padding), (padding, h - padding), (w - padding, h - padding)],
        5: [(padding, padding), (w - padding, padding), (w // 2, h // 2), (padding, h - padding), (w - padding, h - padding)],
        6: [(padding, padding), (w - padding, padding), (padding, h - padding), (w - padding, h - padding),
            (padding, h // 2), (w - padding, h // 2)]
    }
    
    for point in points[result]:
        x, y = point
        canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill='black')

def throw_cube():
    
    result = random.randint(1, 6)
    
    
    wynik_label.configure(text=f"Wynik rzutu: {result}")
    
    
    draw(canvas, result)


root = tk.Tk()
root.title("Symulator rzutu kostką")


rzut_button = tk.Button(root, text="Rzuć kostką", command=throw_cube)
rzut_button.pack(pady=10)


wynik_label = tk.Label(root, text="Wynik rzutu: ")
wynik_label.pack(pady=20)


canvas = tk.Canvas(root, width=300, height=300, bg='white')
canvas.pack()


root.mainloop()
