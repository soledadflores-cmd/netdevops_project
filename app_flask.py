from flask import Flask, render_template_string, redirect, url_for
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>NetDevOps DoS Dashboard</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; }
        .card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 20px; }
        .btn { background-color: #28a745; color: white; padding: 12px 20px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; text-decoration: none; display: inline-block; }
        .btn:hover { background-color: #218838; }
        .status { font-weight: bold; color: #007bff; }
    </style>
</head>
<body>
    <h1>🛡️ NetDevOps DoS Mitigation & Telemetry Dashboard</h1>
    <div class="card">
        <h2>Estado de la Interfaz: <span class="status">GigabitEthernet1</span></h2>
        <p><strong>Monitoreo:</strong> Activo (Actualización automática cada 5s)</p>
        <p><strong>Umbral DoS:</strong> > 70% Ancho de Banda</p>
    </div>
    <div class="card">
        <h2>Control de Recuperación (Requerimiento 5)</h2>
        <a href="/recover" class="btn">⚡ Rearmar Interfaz (NO SHUTDOWN)</a>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/recover')
def recover():
    os.system("python3 ~/netdevops_project/scripts/recover_interface.py")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8501)
