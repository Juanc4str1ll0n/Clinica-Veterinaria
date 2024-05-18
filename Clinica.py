import tkinter as tk
from tkinter import messagebox, ttk


class Persona:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

class Paciente(Persona):
    def __init__(self, nombre, direccion, telefono, historia_clinica):
        super().__init__(nombre, direccion, telefono)
        self.historia_clinica = historia_clinica


class Cita:
    def __init__(self, paciente, fecha, hora, motivo):
        self.paciente = paciente
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo

# Clase Medicamento
class Medicamento:
    def __init__(self, nombre, dosis, instrucciones):
        self.nombre = nombre
        self.dosis = dosis
        self.instrucciones = instrucciones

# Clase Propietario que hereda de Persona
class Propietario(Persona):
    def __init__(self, nombre, direccion, telefono, mascotas):
        super().__init__(nombre, direccion, telefono)
        self.mascotas = mascotas

# Clase para la gestión de la GUI
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión de Pacientes")
        self.geometry("800x800")
        self.configure(bg="#1e1e1e")
        
        # Configurar estilos
        style = ttk.Style(self)
        style.configure('TButton', font=('Helvetica', 14), padding=10)
        style.configure('TLabel', font=('Helvetica', 14), background='#1e1e1e', foreground='#ffffff')
        
        # Diccionarios para almacenar los datos
        self.pacientes = {}
        self.citas = {}
        self.medicamentos = {}
        
        self.create_widgets()

    def create_widgets(self):
        # Espacio para el logo en la esquina superior derecha
        self.logo = tk.PhotoImage(file="logo.png")  # Asegúrate de tener un archivo logo.png en el mismo directorio
        logo_label = tk.Label(self, image=self.logo, bg="#1e1e1e")
        logo_label.place(relx=0.9, rely=0.05, anchor="ne")

        ttk.Label(self, text="Sistema de Gestión de Pacientes", font=("Helvetica", 24, "bold")).pack(pady=20)

        ttk.Button(self, text="Gestión de Pacientes", command=self.gestion_pacientes).pack(pady=10)
        ttk.Button(self, text="Gestión de Citas", command=self.gestion_citas).pack(pady=10)
        ttk.Button(self, text="Gestión de Inventario", command=self.gestion_inventario).pack(pady=10)
        ttk.Button(self, text="Ver Datos", command=self.ver_datos).pack(pady=10)

    def gestion_pacientes(self):
        GestionPacientesWindow(self)

    def gestion_citas(self):
        GestionCitasWindow(self)

    def gestion_inventario(self):
        GestionInventarioWindow(self)

    def ver_datos(self):
        VerDatosWindow(self)

# Ventana para la gestión de pacientes
class GestionPacientesWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("Gestión de Pacientes")
        self.geometry("400x600")
        self.configure(bg="#2e2e2e")
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Nombre del Paciente:").pack(pady=5)
        self.nombre_entry = ttk.Entry(self)
        self.nombre_entry.pack(pady=5)
        
        ttk.Label(self, text="Dirección:").pack(pady=5)
        self.direccion_entry = ttk.Entry(self)
        self.direccion_entry.pack(pady=5)
        
        ttk.Label(self, text="Teléfono:").pack(pady=5)
        self.telefono_entry = ttk.Entry(self)
        self.telefono_entry.pack(pady=5)
        
        ttk.Label(self, text="Historia Clínica:").pack(pady=5)
        self.historia_entry = ttk.Entry(self)
        self.historia_entry.pack(pady=5)
        
        ttk.Button(self, text="Agregar Paciente", command=self.agregar_paciente).pack(pady=20)

    def agregar_paciente(self):
        nombre = self.nombre_entry.get()
        direccion = self.direccion_entry.get()
        telefono = self.telefono_entry.get()
        historia = self.historia_entry.get()
        paciente = Paciente(nombre, direccion, telefono, historia)
        
        # Agregar paciente al diccionario
        self.master.pacientes[nombre] = {
            "Nombre": nombre,
            "Dirección": direccion,
            "Teléfono": telefono,
            "Historia Clínica": historia
        }
        
        messagebox.showinfo("Paciente Agregado", f"Se ha agregado al paciente {nombre}.")
        self.destroy()

# Ventana para la gestión de citas
class GestionCitasWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("Gestión de Citas")
        self.geometry("400x500")
        self.configure(bg="#2e2e2e")
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Nombre del Paciente:").pack(pady=5)
        self.paciente_entry = ttk.Entry(self)
        self.paciente_entry.pack(pady=5)
        
        ttk.Label(self, text="Fecha (dd/mm/aaaa):").pack(pady=5)
        self.fecha_entry = ttk.Entry(self)
        self.fecha_entry.pack(pady=5)
        
        ttk.Label(self, text="Hora (HH:MM):").pack(pady=5)
        self.hora_entry = ttk.Entry(self)
        self.hora_entry.pack(pady=5)
        
        ttk.Label(self, text="Motivo:").pack(pady=5)
        self.motivo_entry = ttk.Entry(self)
        self.motivo_entry.pack(pady=5)
        
        ttk.Button(self, text="Agendar Cita", command=self.agendar_cita).pack(pady=20)

    def agendar_cita(self):
        paciente = self.paciente_entry.get()
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        motivo = self.motivo_entry.get()
        cita = Cita(paciente, fecha, hora, motivo)
        
        # Agregar cita al diccionario
        self.master.citas[f"{fecha} {hora}"] = {
            "Paciente": paciente,
            "Fecha": fecha,
            "Hora": hora,
            "Motivo": motivo
        }
        
        messagebox.showinfo("Cita Agendada", f"Se ha agendado la cita para {paciente} el {fecha} a las {hora}.")
        self.destroy()

# Ventana para la gestión de inventario
class GestionInventarioWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("Gestión de Inventario")
        self.geometry("400x300")
        self.configure(bg="#2e2e2e")
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Nombre del Medicamento:").pack(pady=5)
        self.nombre_entry = ttk.Entry(self)
        self.nombre_entry.pack(pady=5)
        
        ttk.Label(self, text="Dosis:").pack(pady=5)
        self.dosis_entry = ttk.Entry(self)
        self.dosis_entry.pack(pady=5)
        
        ttk.Label(self, text="Instrucciones:").pack(pady=5)
        self.instrucciones_entry = ttk.Entry(self)
        self.instrucciones_entry.pack(pady=5)
        
        ttk.Button(self, text="Agregar Medicamento", command=self.agregar_medicamento).pack(pady=20)

    def agregar_medicamento(self):
        nombre = self.nombre_entry.get()
        dosis = self.dosis_entry.get()
        instrucciones = self.instrucciones_entry.get()
        medicamento = Medicamento(nombre, dosis, instrucciones)
        
        # Agregar medicamento al diccionario
        self.master.medicamentos[nombre] = {
            "Nombre": nombre,
            "Dosis": dosis,
            "Instrucciones": instrucciones
        }
        
        messagebox.showinfo("Medicamento Agregado", f"Se ha agregado el medicamento {nombre}.")
        self.destroy()

# Ventana para ver los datos guardados
class VerDatosWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Datos Guardados")
        self.geometry("600x400")
        self.configure(bg="#2e2e2e")
        self.create_widgets()

    def create_widgets(self):
        # Crear tabs para pacientes, citas y medicamentos
        tab_control = ttk.Notebook(self)
        tab_pacientes = ttk.Frame(tab_control)
        tab_citas = ttk.Frame(tab_control)
        tab_medicamentos = ttk.Frame(tab_control)
        
        tab_control.add(tab_pacientes, text='Pacientes')
        tab_control.add(tab_citas, text='Citas')
        tab_control.add(tab_medicamentos, text='Medicamentos')
        tab_control.pack(expand=1, fill='both')
        
        # Listado de Pacientes
        self.pacientes_tree = ttk.Treeview(tab_pacientes, columns=("Nombre", "Dirección", "Teléfono", "Historia Clínica"), show='headings')
        self.pacientes_tree.heading("Nombre", text="Nombre")
        self.pacientes_tree.heading("Dirección", text="Dirección")
        self.pacientes_tree.heading("Teléfono", text="Teléfono")
        self.pacientes_tree.heading("Historia Clínica", text="Historia Clínica")
        self.pacientes_tree.pack(expand=1, fill='both')
        
        for paciente in self.master.pacientes.values():
            self.pacientes_tree.insert('', tk.END, values=(paciente["Nombre"], paciente["Dirección"], paciente["Teléfono"], paciente["Historia Clínica"]))
        
        # Listado de Citas
        self.citas_tree = ttk.Treeview(tab_citas, columns=("Paciente", "Fecha", "Hora", "Motivo"), show='headings')
        self.citas_tree.heading("Paciente", text="Paciente")
        self.citas_tree.heading("Fecha", text="Fecha")
        self.citas_tree.heading("Hora", text="Hora")
        self.citas_tree.heading("Motivo", text="Motivo")
        self.citas_tree.pack(expand=1, fill='both')
        
        for cita in self.master.citas.values():
            self.citas_tree.insert('', tk.END, values=(cita["Paciente"], cita["Fecha"], cita["Hora"], cita["Motivo"]))
        
        # Listado de Medicamentos
        self.medicamentos_tree = ttk.Treeview(tab_medicamentos, columns=("Nombre", "Dosis", "Instrucciones"), show='headings')
        self.medicamentos_tree.heading("Nombre", text="Nombre")
        self.medicamentos_tree.heading("Dosis", text="Dosis")
        self.medicamentos_tree.heading("Instrucciones", text="Instrucciones")
        self.medicamentos_tree.pack(expand=1, fill='both')
        
        for medicamento in self.master.medicamentos.values():
            self.medicamentos_tree.insert('', tk.END, values=(medicamento["Nombre"], medicamento["Dosis"], medicamento["Instrucciones"]))

# Ejecutar la aplicación
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
