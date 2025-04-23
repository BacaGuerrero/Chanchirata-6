from collections import deque

class Process:
    def __init__(self, pid, name, duration, priority):
        self.pid = pid
        self.name = name
        self.duration = duration
        self.priority = priority

    def __str__(self):
        return f"[PID:{self.pid} | {self.name} | {self.duration}s | Priority {self.priority}]"

class RoundRobinScheduler: 
    def __init__(self, quantum):
        self.quantum = quantum
        self.queues = {1: deque(), 2: deque(), 3: deque()}
        self.total_processes = 0

    def add_process(self, process):
        if process.priority not in self.queues:
            print(f"⚠️  Error: Prioridad {process.priority} no válida. Debe ser 1, 2 o 3.")
            return
        self.queues[process.priority].append(process)
        self.total_processes += 1
        print(f"✅ Proceso agregado: {process}")

    def run(self):
        if self.total_processes == 0:
            print("🚫 No hay procesos en cola. Ejecución cancelada.")
            return

        print("\n⏳ Iniciando planificación Round-Robin...\n")
        priorities = [1, 2, 3]
        while any(self.queues[p] for p in priorities):
            for p in priorities:
                if self.queues[p]:
                    process = self.queues[p].popleft()
                    run_time = min(self.quantum, process.duration)
                    process.duration -= run_time
                    print(f"⚙️ Ejecutando: {process} por {run_time}s")
                    if process.duration > 0:
                        self.queues[p].append(process)
                        print(f"🔁 Proceso {process.name} reinsertado en la cola (tiempo restante: {process.duration}s)")
                    else:
                        print(f"✅ Proceso {process.name} finalizado.")
        print("\n🏁 Todos los procesos han sido atendidos.")

# -------- INTERACCIÓN --------

try:
    quantum = int(input("Ingrese el quantum: "))
    scheduler = RoundRobinScheduler(quantum)

    num_processes = int(input("Ingrese el número de procesos: "))
    if num_processes <= 0:
        print("🚫 Número inválido. Debe ingresar al menos 1 proceso.")
    else:
        for i in range(num_processes):
            print(f"\n🧾 Proceso {i + 1}")
            pid = int(input("PID: "))
            name = input("Nombre: ")
            duration = int(input("Duración: "))
            priority = int(input("Prioridad (1-Alta, 2-Media, 3-Baja): "))
            scheduler.add_process(Process(pid, name, duration, priority))

        print("\n✅ Ejecutando planificación...\n")
        scheduler.run()
except ValueError:
    print("❌ Entrada inválida. Asegúrese de ingresar números enteros.")
