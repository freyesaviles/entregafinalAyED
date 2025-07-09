from memoria import Memoria
from bubble_sort import BubbleSort
from binary_search import BinarySearch

class Aplicacion:
    def __init__(self):
        self.ejecutar_menu()

    def ejecutar_menu(self):
        while True:
            print("\n--- MENÚ PRINCIPAL ---")
            print("1. Ejecutar Bubble Sort")
            print("2. Ejecutar Búsqueda Binaria")
            print("3. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                memoria = Memoria()
                bubble_sort = BubbleSort(memoria)
                bubble_sort.ejecutar()

            elif opcion == "2":
                memoria = Memoria(ordenado=True)
                memoria.mostrar()
                try:
                    objetivo = int(input("¿Qué número deseas buscar?: "))
                    binary_search = BinarySearch(memoria)
                    binary_search.ejecutar(objetivo)
                except ValueError:
                    print("Entrada inválida. Debes ingresar un número.")

            elif opcion == "3":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida.")

