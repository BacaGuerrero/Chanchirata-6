class LogBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.index = 0
        self.size = 0

    def add_log(self, entry):
        if self.size == self.capacity:
            overwritten = self.buffer[self.index]
            print(f"⚠️  El buffer está lleno. Se sobreescribirá: '{overwritten}'")
        self.buffer[self.index] = entry
        self.index = (self.index + 1) % self.capacity
        self.size = min(self.size + 1, self.capacity)
        print(f"✅ Log guardado: '{entry}'")

    def get_logs(self):
        start = (self.index - self.size) % self.capacity
        return [self.buffer[(start + i) % self.capacity] for i in range(self.size)]


# -------- INTERACCIÓN --------

try:
    size = int(input("Ingrese el tamaño del buffer: "))
    if size <= 0:
        print("🚫 Tamaño inválido. El buffer debe ser mayor que cero.")
    else:
        buffer = LogBuffer(size)
        print("📝 Ingrese los logs (escriba 'fin' para terminar):")

        while True:
            entry = input("> ")
            if entry.lower() == 'fin':
                break
            buffer.add_log(entry)

        if buffer.size == 0:
            print("📭 No se ingresaron logs.")
        else:
            print("\n📋 Logs actuales en el buffer:")
            for log in buffer.get_logs():
                print("-", log)
except ValueError:
    print("❌ Entrada inválida. Asegúrese de ingresar un número entero.")
