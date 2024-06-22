# FUNCION PARA CREAR EL HISTOGRAMA
import matplotlib.pyplot as plt
# Función para crear el histograma
def crear_histograma(marcas_clase, frecuencias):
    plt.figure(figsize=(12, 6))
    plt.bar(marcas_clase, frecuencias,
           width=1, edgecolor="k",
           color=["#EF90F1", "#90E7F1", "#D8B4EF", "#C7EFB4", "#EFB4C7", "#EFE4B4"])
    
    plt.xlabel("Marcas de clase", fontsize=20)
    plt.ylabel("Frecuencias", fontsize=20)
    plt.title("Histograma", fontsize=25)
    plt.show()