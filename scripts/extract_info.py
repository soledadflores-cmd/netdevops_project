import json
import random
import time

def get_cisco_info(ip="172.23.18.224"):
    """Simulación de extracción NETCONF / ietf-interfaces."""
    return {
        "device": "Cisco IOS-XE Switch",
        "ip": ip,
        "status": "Connected (Simulated)",
        "model_yang": "ietf-interfaces",
        "interfaces": [
            {"name": "GigabitEthernet1", "status": "up", "speed_bps": 1000000000},
            {"name": "GigabitEthernet2", "status": "up", "speed_bps": 1000000000},
            {"name": "GigabitEthernet3", "status": "down", "speed_bps": 1000000000}
        ]
    }

def get_fortigate_info(ip="172.23.18.225"):
    """Simulación de extracción REST API FortiOS."""
    return {
        "device": "FortiGate Firewall",
        "ip": ip,
        "interface": "wan1",
        "status": "up",
        "tx_bytes": 1254800,
        "rx_bytes": 4589200
    }

if __name__ == "__main__":
    print("=== INFORMACIÓN DE SWITCH CISCO (NETCONF / YANG) ===")
    print(json.dumps(get_cisco_info(), indent=2))
    print("\n=== INFORMACIÓN DE FORTIGATE WAN1 (REST API) ===")
    print(json.dumps(get_fortigate_info(), indent=2))
