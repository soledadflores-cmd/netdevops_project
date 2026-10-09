import streamlit as st
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.recover_interface import recover_interface

st.set_page_config(page_title="NetDevOps SOC Dashboard", layout="wide")

st.title("🛡️ Centro de Operaciones y Telemetría NetDevOps")
st.markdown("---")

STATUS_FILE = "interface_status.json"

def get_status():
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, "r") as f:
            return json.load(f)
    return {"enabled": True, "interface": "GigabitEthernet1"}

status_data = get_status()
is_enabled = status_data.get("enabled", True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Estado de Telemetría")
    if is_enabled:
        st.success("🟢 Interfaz GigabitEthernet1: OPERACIONAL (UP)")
        st.metric(label="Uso de Ancho de Banda", value="18.5%", delta="Normal")
    else:
        st.error("🔴 Interfaz GigabitEthernet1: DESHABILITADA (ADMIN DOWN)")
        st.metric(label="Uso de Ancho de Banda", value="0.0%", delta="MITIGADO ANTE DoS", delta_color="inverse")

with col2:
    st.subheader("🛠️ Acciones de Mitigación y Simulación")
    
    if st.button("🔥 Simular Ataque DoS (>70% Tráfico)"):
        with open("TRIGGER_DOS", "w") as f:
            f.write("1")
        st.warning("Ataque simulado disparado. El script de telemetría apagará la interfaz en breve.")

    st.markdown("---")
    operator = st.text_input("ID del Administrador Autorizador:", value="admin_netdevops")
    
    if st.button("⚡ Reactivar Interfaz (No Shutdown)"):
        recover_interface("GigabitEthernet1", operator)
        st.success(f"Interfaz reactivada por {operator}. Refresca la página.")

st.markdown("---")
st.subheader("📋 Historial de Auditoría (recovery.log)")
try:
    with open("recovery.log", "r") as f:
        st.code(f.read(), language="text")
except FileNotFoundError:
    st.info("No se han registrado acciones de recuperación aún.")
