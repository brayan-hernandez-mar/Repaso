import matplotlib.pyplot as plt
# Función para crear el diagrama de ojiva
def crear_ojiva(marcas_clase, frecuencias, marcas_texto):
    datos_x = [0] + marcas_clase 
    datos_y = [0] + list(frecuencias)

    plt.figure(figsize=(12, 6))
    plt.plot(datos_x, datos_y, 
             linewidth=5, color="r", linestyle=":", 
             marker="v", markersize=15, markerfacecolor="y", markeredgecolor="b")

    plt.xticks(marcas_clase, marcas_texto, fontsize=15, rotation=45)
    plt.xlabel("Marcas de clase", fontsize=20)
    plt.ylabel("Frecuencias", fontsize=20)
    plt.title("Ojiva", fontsize=25)
    plt.grid(True)
    plt.show()