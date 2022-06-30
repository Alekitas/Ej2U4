from email.mime import message
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk


class Aplicacion(tk.Tk):
    __preciobase = None
    __grabado = None
    __iva = None
    __precioconiva = None

    def __init__(self):
        super().__init__()
        self.title('CALCULADORA DE IVA')
        self.config(padx=10, pady=10)

        self.__grabado = IntVar()
        self.__preciobase = StringVar()
        self.__iva = StringVar()
        self.__precioconiva = StringVar()

        ttk.Label(self, text="Precio sin IVA: ").grid(column=0, row=0)
        self.entrypreciobase = ttk.Entry(self, width=10, textvariable=self.__preciobase)
        self.entrypreciobase.grid(column=1, row=0)

        ttk.Radiobutton(self, text="IVA 21%", value=0, variable=self.__grabado).grid(
            column=0, row=1, sticky='W')
        ttk.Radiobutton(self, text="IVA 10.5%", value=1, variable=self.__grabado).grid(
            column=0, row=2, sticky='W')

        ttk.Label(self, text="IVA: ").grid(column=0, row=3)
        ttk.Label(self, textvariable=self.__iva).grid(column=1, row=3)

        ttk.Label(self, text="Precio con IVA: ").grid(column=0, row=4)
        ttk.Label(self, textvariable=self.__precioconiva).grid(column=1, row=4)

        ttk.Button(self, text="Calcular", command=self.Calcular).grid(column=0, row=5, sticky='W', padx=3)
        ttk.Button(self, text="Salir", command=self.destroy).grid(column=2, row=5, sticky='E', padx=3)

        self.__grabado.set(-1)

    def Calcular(self):
        if self.entrypreciobase != '' and self.__grabado != -1:
            try:
                IVA = 0
                preciobase = float(self.entrypreciobase.get())
                if self.__grabado.get() == 0:
                    IVA = preciobase*(10.5/100)
                elif self.__grabado.get() == 1:
                    IVA = preciobase*(21/100)
                self.__iva.set(IVA)
                self.__precioconiva.set(IVA+preciobase)
            except ValueError:
                messagebox.showerror(title="Valor Incorrecto", message="Solo ingresar valores numericos")
                self.__preciobase.set('')
                self.entrypreciobase.focus()
