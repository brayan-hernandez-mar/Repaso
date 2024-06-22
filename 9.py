# Función para crear gráfico de pastel
import matplotlib.pyplot as plt
def crear_grafico_pastel(datos, marcas_texto):
    separaciones = [0] * len(datos)  # Lista de ceros del mismo tamaño que datos
    plt.figure(figsize=(8, 8))
    plt.pie(datos, 
            explode=separaciones,  
            counterclock=False, 
            startangle=90, 
            autopct="%0.1f%%", 
            pctdistance=0.8, 
            colors=["#EF90F1", "#90E7F1", "#D8B4EF", "#C7EFB4", "#EFB4C7", "#EFE4B4"], 
            labels=marcas_texto)
    plt.title("Grafico de pastel", fontsize=20)
    plt.show()

# Uso de la función
datos = frecuencias
marcas_texto = clases_ordenadas