# Proyecto NetDevOps - Monitoreo, Telemetría y Automatización

Este proyecto implementa un entorno de automatización de red y servicios NetDevOps.

## Estructura del Proyecto
- `scripts/extract_info.py`: Extracción de información (NETCONF / REST API).
- `scripts/telemetry_monitor.py`: Monitoreo de uso de ancho de banda y mitigación automática de DoS (>70%).
- `scripts/recover_interface.py`: Script de reactivación de interfaz con log de auditoría.
- `dashboard/app.py`: Panel web para supervisión y mitigación.
- `ansible/site.yml`: Playbook para despliegue de servicios (Web, FTP, Mail, DNS).

## Modo de Uso
1. Ejecutar extracción de datos:
   `python3 scripts/extract_info.py`

2. Ejecutar monitoreo de telemetría:
   `python3 scripts/telemetry_monitor.py`

3. Ejecutar Dashboard Web:
   `streamlit run dashboard/app.py`

4. Ejecutar Playbook de Ansible:
   `ansible-playbook ansible/site.yml`
