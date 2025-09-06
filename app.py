from flask import Flask, request, jsonify

app = Flask(__name__)

pacientes = []
profissionais = []
consultas = []
exames = []
prescricoes = []
usuarios = [
    {"id": 1, "login": "admin", "senha": "1234"}
]


# --- Paciente ---
@app.route("/pacientes", methods=["POST"])
def criar_paciente():
    paciente = request.json
    pacientes.append(paciente)
    return jsonify(paciente), 201

@app.route("/pacientes", methods=["GET"])
def listar_pacientes():
    return jsonify(pacientes)

# --- Profissional ---
@app.route("/profissionais", methods=["POST"])
def criar_profissional():
    prof = request.json
    profissionais.append(prof)
    return jsonify(prof), 201

@app.route("/profissionais", methods=["GET"])
def listar_profissionais():
    return jsonify(profissionais)

# --- Consulta ---
@app.route("/consultas", methods=["POST"])
def criar_consulta():
    consulta = request.json
    consultas.append(consulta)
    return jsonify(consulta), 201

@app.route("/consultas", methods=["GET"])
def listar_consultas():
    return jsonify(consultas)

# --- Exame ---
@app.route("/consultas/<int:consulta_id>/exames", methods=["POST"])
def criar_exame(consulta_id):
    exame = request.json
    exame["consulta_id"] = consulta_id
    exames.append(exame)
    return jsonify(exame), 201

@app.route("/consultas/<int:consulta_id>/exames", methods=["GET"])
def listar_exames(consulta_id):
    lista = [e for e in exames if e["consulta_id"] == consulta_id]
    return jsonify(lista)

# --- Prescricao ---
@app.route("/consultas/<int:consulta_id>/prescricoes", methods=["POST"])
def criar_prescricao(consulta_id):
    prescricao = request.json
    prescricao["consulta_id"] = consulta_id
    prescricoes.append(prescricao)
    return jsonify(prescricao), 201

@app.route("/consultas/<int:consulta_id>/prescricoes", methods=["GET"])
def listar_prescricoes(consulta_id):
    lista = [p for p in prescricoes if p["consulta_id"] == consulta_id]
    return jsonify(lista)


@app.route("/login", methods=["POST"])
def login():
    dados = request.json
    login = dados.get("login")
    senha = dados.get("senha")

    usuario = next((u for u in usuarios if u["login"] == login and u["senha"] == senha), None)

    if usuario:
        return jsonify({"message": "Login realizado com sucesso!", "id": usuario["id"]})
    else:
        return jsonify({"error": "Login ou senha incorretos"}), 401


if __name__ == "__main__":
    app.run(debug=True)
