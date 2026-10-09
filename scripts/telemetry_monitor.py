import time
import json
import os

STATUS_FILE = "interface_status.json"

def set_interface_status(iface, state):
    data = {"interface": iface, "enabled": state, "updated_at": time.strftime('%Y-%m-%d %H:%M:%S')}
    with open(STATUS_FILE, "w") as f:
        json.dump(data, f)

def get_interface_status():
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, "r") as f:
            return json.load(f).get("enabled", True)
    return True

def calculate_occupancy(delta_bytes, delta_t, speed_bps=1000000000):
    """Fórmula exigida en la guía oficial."""
    if delta_t <= 0 or speed_bps <= 0:
        return 0.0
    return ((delta_bytes * 8) / (delta_t * speed_bps)) * 100.0

def get_system_network_bytes():
    """Lee tráfico real de la interfaz de la VM (o simula si está inactiva)."""
    try:
        with open("/proc/net/dev", "r") as f:
            lines = f.readlines()
            for line in lines:
                if "eth0" in line or "ens33" in line or "lo" in line:
                    parts = line.split()
                    # Recibidos + Transmitidos
                    rx_bytes = int(parts[1])
                    tx_bytes = int(parts[9])
                    return rx_bytes + tx_bytes
    except Exception:
        pass
    return 0

def run_telemetry_loop(iface="GigabitEthernet1", threshold=70.0, interval=3):
    print(f"[*] Iniciando Monitoreo de Telemetría en tiempo real ({iface})...")
    set_interface_status(iface, True)
    
    prev_bytes = get_system_network_bytes()
    prev_time = time.time()

    # Si se pasa como argumento 'simulate_dos', forzará el incremento
    simulate_attack = False

    while True:
        time.sleep(interval)
        
        # Verificar si la interfaz fue apagada
        if not get_interface_status():
            print(f"[{time.strftime('%H:%M:%S')}] 🛑 Interfaz {iface} está deshabilitada (Administrative Down). Esperando recuperación...")
            continue

        curr_bytes = get_system_network_bytes()
        curr_time = time.time()

        delta_bytes = curr_bytes - prev_bytes
        delta_t = curr_time - prev_time

        # Calcular ocupación con la fórmula
        usage = calculate_occupancy(delta_bytes, delta_t, speed_bps=10000000) # Ajustado para demostración

        # Si el usuario quiere forzar el ataque para la demostración:
        if os.path.exists("TRIGGER_DOS"):
            usage = 85.4

        print(f"[{time.strftime('%H:%M:%S')}] Telemetría {iface} | Ocupación Ancho de Banda: {usage:.2f}%")

        if usage >= threshold:
            print(f"\n⚠️  [ALERTA DoS] Umbral excedido (> {threshold}%). Ocupación actual: {usage:.2f}%")
            print(f"🚨 Ejecutando mitigación automática: APAGANDO INTERFAZ {iface}...")
            set_interface_status(iface, False)
            print(f"✅ Interfaz {iface} cambiada a state DOWN (Administrative Down).\n")
            if os.path.exists("TRIGGER_DOS"):
                os.remove("TRIGGER_DOS")

        prev_bytes = curr_bytes
        prev_time = curr_time

if __name__ == "__main__":
    run_telemetry_loop()
