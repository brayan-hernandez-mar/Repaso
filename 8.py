import matplotlib.pyplot as plt
def crear_poligono_frecuencias(marcas_clase, frecuencias, marcas_texto):
    # Ajustes necesarios para trazar el polígono
    datos_x = [0] + list(marcas_clase) + [7]
    datos_y = [0] + list(frecuencias) + [0]

    plt.figure(figsize=(12, 6))  # Ancho, alto de la figura

    # Trazar el polígono de frecuencias
    plt.plot(datos_x, datos_y, 
             linewidth=5, color="r", linestyle=":", 
             marker="v", markersize=15, markerfacecolor="y", markeredgecolor="b")

    # Configuraciones adicionales del gráfico
    plt.xticks(marcas_clase, marcas_texto, fontsize=15, rotation=45)
    plt.xlabel("Marcas de clase", fontsize=20)
    plt.ylabel("Frecuencias", fontsize=20)
    plt.title("Polígono de frecuencias", fontsize=25)
    plt.grid(True)  # Activar la cuadrícula