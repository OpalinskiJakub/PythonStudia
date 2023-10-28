def drawRectangle(rows, columns):
    try:
        if rows < 1 or columns < 1:
            raise ValueError

        rectangle = []

        for row in range(rows):
            rectangle.append("+---" * columns + "+")
            rectangle.append("|   " * columns + "|")

        rectangle.append("+---" * columns + "+")

        return "\n".join(rectangle)
    except ValueError:
        print("Zle dane,Spróbuj ponownie.")


rectangle = drawRectangle(6, 4)

print(rectangle)
