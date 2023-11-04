def make_grid(rows, cols):
    try:
        if rows < 1 or cols < 1:
            raise ValueError

        rectangle = []

        for row in range(rows):
            rectangle.append("+---" * cols + "+")
            rectangle.append("|   " * cols + "|")

        rectangle.append("+---" * cols + "+")

        return "\n".join(rectangle)
    except ValueError:
        print("Zle dane,Spróbuj ponownie.")
        
rectangle = make_grid(6, 4)

print(rectangle)