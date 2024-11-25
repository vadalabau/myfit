
Bautista Vadalá Miranda <vadala.bautistaet36@gmail.com>
mar, 1 oct, 16:04
para vitocordobaet36

import tkinter as tk
from tkinter import messagebox

class GestionBarras:
    def __init__(self, root):
        self.root = root
        self.root.title("My Fit")
        
        # Inicializar el control de ventas
        self.ventas = {'1.20m': 0, '2m': 0}
        
        # Variables para entradas
        self.stock_6m_var = tk.StringVar()
        self.barras_1_2m_var = tk.StringVar()
        self.barras_2m_var = tk.StringVar()
        self.venta_1_2m_var = tk.StringVar()
        self.venta_2m_var = tk.StringVar()

        # Crear la interfaz
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Etiquetas y campos de entrada
        tk.Label(self.root, text="Stock de barras de 6 metros:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.stock_6m_var).grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self.root, text="Cantidad de barras de 1.20m a producir:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.barras_1_2m_var).grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(self.root, text="Cantidad de barras de 2m a producir:").grid(row=2, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.barras_2m_var).grid(row=2, column=1, padx=10, pady=10)

        # Botón para producir barras
        tk.Button(self.root, text="Producir Barras", command=self.producir_barras).grid(row=3, column=0, columnspan=2, pady=10)

        # Etiquetas y campos de venta
        tk.Label(self.root, text="Cantidad vendida de barras de 1.20m:").grid(row=4, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.venta_1_2m_var).grid(row=4, column=1, padx=10, pady=10)
        
        tk.Label(self.root, text="Cantidad vendida de barras de 2m:").grid(row=5, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.venta_2m_var).grid(row=5, column=1, padx=10, pady=10)

        # Botón para registrar ventas
        tk.Button(self.root, text="Registrar Ventas", command=self.registrar_ventas).grid(row=6, column=0, columnspan=2, pady=10)

        # Área de resumen
        self.resumen_text = tk.Text(self.root, height=10, width=40)
        self.resumen_text.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def producir_barras(self):
        try:
            stock_6m = int(self.stock_6m_var.get())
            barras_1_2m = int(self.barras_1_2m_var.get())
            barras_2m = int(self.barras_2m_var.get())

            # Calcular si es posible producir
            total_necesario_1_2m = barras_1_2m * 1.2
            total_necesario_2m = barras_2m * 2
            total_necesario = total_necesario_1_2m + total_necesario_2m
            barras_necesarias = total_necesario / 6

            if barras_necesarias <= stock_6m:
                # Actualizar stock disponible
                self.stock_control_1_2m = barras_1_2m
                self.stock_control_2m = barras_2m
                stock_restante = stock_6m - barras_necesarias
                self.mostrar_resumen(f"Producción exitosa:\n{barras_1_2m} barras de 1.20m\n{barras_2m} barras de 2m\nStock restante de barras de 6m: {stock_restante:.2f}")
            else:
                messagebox.showerror("Error", "No hay suficiente stock para producir la cantidad deseada.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

    def registrar_ventas(self):
        try:
            venta_1_2m = int(self.venta_1_2m_var.get())
            venta_2m = int(self.venta_2m_var.get())

            if venta_1_2m > self.stock_control_1_2m or venta_2m > self.stock_control_2m:
                messagebox.showerror("Error", "No hay suficiente stock para realizar la venta.")
            else:
                # Actualizar ventas y stock
                self.ventas['1.20m'] += venta_1_2m
                self.ventas['2m'] += venta_2m
                self.stock_control_1_2m -= venta_1_2m
                self.stock_control_2m -= venta_2m
                self.mostrar_resumen(f"Ventas registradas:\nVentas totales: {self.ventas['1.20m']} barras de 1.20m y {self.ventas['2m']} barras de 2m\nStock restante de barras de 1.20m: {self.stock_control_1_2m}\nStock restante de barras de 2m: {self.stock_control_2m}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

    def mostrar_resumen(self, mensaje):
        self.resumen_text.delete(1.0, tk.END)
        self.resumen_text.insert(tk.END, mensaje)

# Crear la ventana principal
root = tk.Tk()
app = GestionBarras(root)
root.mainloop()
