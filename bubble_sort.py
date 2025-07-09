import time

class BubbleSort:
    def __init__(self, memoria):
        self.memoria = memoria

    def ejecutar(self):
        arr = self.memoria.obtener_datos()
        n = len(arr)
        print("\n--- Iniciando Bubble Sort ---")
        inicio = time.time()

        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(f"Pasada {i + 1}: {arr}")  # Mostrar todos los elementos
            time.sleep(0.3)

        fin = time.time()
        print(f"--- Bubble Sort terminado en {fin - inicio:.4f} segundos ---")
