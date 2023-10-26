def productopunto2(vector1, vector2) -> float:
    producto_punto = (vector1[0] * vector2[0]) + (vector1[1] * vector2[1])
    return producto_punto

if __name__ == "__main__":
    vector1 = [4, 9]
    vector2 = [6, 8]

    producto_punto = productopunto2(vector1, vector2)

    print(f"El producto punto entre los vectores a y b es {producto_punto}.")