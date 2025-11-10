from flask import Flask, jsonify
import os
import platform
import psutil

# Lista com os nomes completos dos integrantes (edite aqui)
xnome_integrantes = [
    "Julia Machado Kociolek",
    "Antonio Bernardo Zilio Tomasi",
    "Gustavo Lona Grespan"
]

# Instância Flask requisitada pelo Render (gunicorn app:APP)
APP = Flask(__name__)

# Função interna para coletar métricas do processo
def xget_metricas():
    proc = psutil.Process(os.getpid())
    pid = proc.pid
    memoria_mb = proc.memory_info().rss / (1024 * 1024)
    cpu_percent = proc.cpu_percent(interval=0.1)
    so = platform.system()
    return {
        "Nome": " e ".join(xnome_integrantes),
        "PID": pid,
        "Memória usada (MB)": round(memoria_mb, 2),
        "CPU (%)": round(cpu_percent, 2),  
        "Sistema Operacional": so
    }

# Rota /info — exibe somente os nomes dos integrantes (JSON)
@APP.route('/info')
def xinfo():
    return jsonify({"Nome": " e ".join(xnome_integrantes)})

# Rota /metricas — retorna as informações pedidas em JSON
@APP.route('/metricas')
def xmetricas():
    dados = xget_metricas()
    return jsonify(dados)

# Rota raiz opcional para ver algo no navegador
@APP.route('/')
def xindex():
    return (
        "<pre>Servidor Flask ativo. Rotas:\n"
        "/info -> nomes dos integrantes\n"
        "/metricas -> métricas do servidor (JSON)</pre>"
    )

if __name__ == '__main__':
    # Para execução local durante desenvolvimento
    APP.run(host='0.0.0.0', port=5000, debug=True)
