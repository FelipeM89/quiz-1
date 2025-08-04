import time

numero_clientes = 5

cola = []

print(">>> SIMULACION DEL SISTEMA DE ATENCION DE CLIENTES <<<\n")

for i in range(1, numero_clientes + 1):
    print(f"Cliente {i} llego.")
    cola.append(i)
    time.sleep(1) 

print("\nSe lleno la cola\n")
time.sleep(1)

while cola:
    cliente_atendido = cola.pop(0)
    print(f"Atendiendo al cliente {cliente_atendido}")
    time.sleep(1)

print("\nTodos los clientes han sido atendidos.")
