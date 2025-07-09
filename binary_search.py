import time

class BinarySearch:
    def __init__(self, memoria):
        self.memoria = memoria

    def ejecutar(self, objetivo):
        arr = self.memoria.obtener_datos()
        izquierda, derecha = 0, len(arr) - 1
        print(f"\n--- Iniciando búsqueda binaria de {objetivo} ---")
        inicio = time.time()

        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            print(f"Array: {arr}")
            print(f"Verificando posición {medio} (valor: {arr[medio]})")
            time.sleep(0.3)

            if arr[medio] == objetivo:
                fin = time.time()
                print(f"Elemento {objetivo} encontrado en la posición {medio}.")
                print(f"--- Búsqueda terminada en {fin - inicio:.4f} segundos ---")
                return medio
            elif arr[medio] < objetivo:
                izquierda = medio + 1
                print(f"Ir a la derecha (nuevo rango: {izquierda} a {derecha})")
            else:
                derecha = medio - 1
                print(f"Ir a la izquierda (nuevo rango: {izquierda} a {derecha})")

        fin = time.time()
        print(f"Elemento {objetivo} no encontrado.")
        print(f"--- Búsqueda terminada en {fin - inicio:.4f} segundos ---")
        return -1
