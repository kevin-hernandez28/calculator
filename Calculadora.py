import tkinter as tk  # Para crear la interfaz gráfica
from tkinter import messagebox  # Para mostrar mensajes emergentes como errores o alertas
import ttkbootstrap as ttk  # Para mejorar la apariencia de la interfaz con temas modernos
import numpy as np  # Para funciones matemáticas avanzadas como trigonometría
import math  # Para realizar cálculos matemáticos como sqrt

# ttkbootstrap:
# Ventajas: Esta biblioteca proporciona un tema moderno y atractivo para las interfaces gráficas,
# haciendo que los widgets de tkinter se vean más profesionales y fáciles de usar.
# Simplificación: Facilita la personalización de los elementos de la interfaz, permitiendo un diseño
# más atractivo sin esfuerzo adicional.

# Función para realizar los cálculos
def calcular():
    try:
        exp = entrada.get()

        # Reemplazar 'sin', 'cos' y 'tan' para que el cálculo sea correcto
        if "sin" in exp or "cos" in exp or "tan" in exp:
            exp = exp.replace("sin", "np.sin(np.radians")
            exp = exp.replace("cos", "np.cos(np.radians")
            exp = exp.replace("tan", "np.tan(np.radians")
            exp += ")"

        # Evaluar la expresión
        resultado = eval(exp)
        entrada.delete(0, tk.END)  # Limpiar la entrada
        entrada.insert(tk.END, str(resultado))  # Mostrar el resultado
    except Exception as e:
        messagebox.showerror("Error", "Hubo un error en la operación")  # Mostrar mensaje de error

# Función para borrar la entrada
def borrar():
    entrada.delete(0, tk.END)

# Función para realizar la raíz cuadrada
def raiz_cuadrada():
    try:
        exp = entrada.get()
        resultado = math.sqrt(float(exp))  # Realizar la raíz cuadrada
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        messagebox.showerror("Error", "Por favor ingrese un número válido.")

# numpy:
# Ventajas: Permite trabajar con operaciones matemáticas avanzadas, como las funciones trigonométricas
# (sin, cos, tan) y la creación de rangos numéricos (linspace).
# Simplificación: Al integrar numpy, el código se simplifica al hacer uso de funciones optimizadas para
# operaciones matemáticas complejas.

# Crear la ventana principal con un tema moderno
ventana = ttk.Window(themename="darkly")
ventana.title("Calculadora Científica")
ventana.geometry("500x600")  # Ajustar el tamaño de la ventana para que se vean todos los botones
ventana.resizable(False, False)

# Centrar la ventana en la pantalla
ventana.update_idletasks()
window_width = ventana.winfo_width()
window_height = ventana.winfo_height()
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
ventana.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Campo de entrada para mostrar la operación
entrada = ttk.Entry(ventana, width=35, font=("Arial", 20), justify='right', bootstyle="info")
entrada.pack(pady=20)

# Etiqueta para mostrar el resultado
salida = ttk.Label(ventana, text="Resultado:", font=("Arial", 16), bootstyle="success")
salida.pack(pady=5)

# Estilo de botones más llamativos y con bordes redondeados
button_style = {
    "width": 8,  # Aumentar el tamaño de los botones
    "height": 3,  # Aumentar la altura de los botones
    "font": ('Arial', 16, 'bold'),  # Aumentar el tamaño de la fuente
    "relief": "raised",
    "bd": 3,
    "fg": "#fff",
    "bg": "#1ABC9C",  # Color verde brillante
    "activebackground": "#16A085",
    "activeforeground": "#fff",
    "highlightbackground": "#16A085",  # Sombra sutil
    "highlightcolor": "#1ABC9C",
    "borderwidth": 2,
}

# matplotlib:
# Ventajas: Permite crear gráficos de manera sencilla y altamente personalizable.
# En este caso, se utiliza para graficar las funciones trigonométricas.
# Simplificación: Hace que la visualización de datos complejos sea accesible con solo unas pocas líneas de código,
# mejorando la comprensión visual de las funciones.

# Botones de la calculadora
tabla_botones = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
    ('sin', 'cos', 'tan', '('),
    (')', 'pi', 'e', '√'),
    ('←', 'C', '^')
]

# Crear un marco para contener los botones
frame_botones = ttk.Frame(ventana)

# Recorrer la tabla de botones y agregarlos a la interfaz
for fila in tabla_botones:
    fila_frame = ttk.Frame(frame_botones)
    for btn_text in fila:
        if btn_text == '=':
            boton = ttk.Button(fila_frame, text=btn_text, command=calcular, bootstyle="success solid")
        elif btn_text == 'C':
            boton = ttk.Button(fila_frame, text=btn_text, command=borrar, bootstyle="danger solid")
        elif btn_text == '√':
            boton = ttk.Button(fila_frame, text=btn_text, command=raiz_cuadrada, bootstyle="warning solid")
        elif btn_text == '←':
            boton = ttk.Button(fila_frame, text=btn_text, command=lambda: entrada.delete(len(entrada.get()) - 1, tk.END), bootstyle="danger outline")
        elif btn_text == 'pi':
            boton = ttk.Button(fila_frame, text=btn_text, command=lambda: entrada.insert(tk.END, str(math.pi)), bootstyle="primary outline")
        elif btn_text == 'e':
            boton = ttk.Button(fila_frame, text=btn_text, command=lambda: entrada.insert(tk.END, str(math.e)), bootstyle="primary outline")
        else:
            boton = ttk.Button(fila_frame, text=btn_text, command=lambda t=btn_text: entrada.insert(tk.END, t), bootstyle="primary outline")
        boton.pack(side=tk.LEFT, padx=8, pady=8)  # Aumentar el espaciado entre botones
    fila_frame.pack()

# Posicionar los botones en la ventana
frame_botones.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
