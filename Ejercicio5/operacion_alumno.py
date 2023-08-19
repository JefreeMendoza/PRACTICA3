class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []
        pass
    def display(self):
        print(f"El nombre del alumno es, {self.nombre} y su numero de registro es, {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        else:
            print("Edad: No asignada")
        
        if self.notas:
            print("Notas:")
            for i, nota in enumerate(self.notas, start=1):
                print(f"Nota {i}: {nota}")
        else:
            print("Notas: No asignadas")

    def setAge(self, edad):
        self.edad = edad
    def setNota(self, notas):
        self.notas = notas