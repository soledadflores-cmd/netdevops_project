import sys
import time
import json
import logging

logging.basicConfig(filename='recovery.log', level=logging.INFO, format='%(asctime)s - %(message)s')

STATUS_FILE = "interface_status.json"

def recover_interface(iface_name="GigabitEthernet1", authorized_by="admin_netdevops"):
    """Reactiva la interfaz (no shutdown) y guarda registro en recovery.log."""
    data = {"interface": iface_name, "enabled": True, "updated_at": time.strftime('%Y-%m-%d %H:%M:%S')}
    
    with open(STATUS_FILE, "w") as f:
        json.dump(data, f)
        
    log_msg = f"RECOVERY_SUCCESS | Interface: {iface_name} | Action: NO SHUTDOWN | Authorized By: {authorized_by}"
    logging.info(log_msg)
    print(f"✅ Interfaz {iface_name} reactivada por {authorized_by}. Registrado en recovery.log.")
    return True

if __name__ == "__main__":
    user = sys.argv[1] if len(sys.argv) > 1 else "operador_red"
    recover_interface("GigabitEthernet1", user)
