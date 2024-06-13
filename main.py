from flask import Flask, render_template, request, redirect

app = Flask(__name__)

contatos = []
agendas = []
idade_humana_ = []
doses = []
soros = []

@app.route('/')
def index():
    return render_template('index.html', contatos=contatos, agenda=agendas, dose=doses, soro=soros)

@app.route('/sobrenos', methods=['GET', 'POST'])
def sobrenos():
    return render_template('sobrenos.html', contatos=contatos)

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    return render_template('contato.html', contatos=contatos)

@app.route('/servicos')
def servicos():
    return render_template('servicos.html', contatos=contatos)

@app.route('/agenda', methods=['GET', 'POST'])
def agenda():
    return render_template('agenda.html', agenda=agendas, contatos=contatos)

@app.route('/soro_e_dose', methods=['GET', 'POST'])
def soro_e_dose():
    return render_template('soro_e_dose.html', soro=soros, dose=doses, contatos=contatos)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        especie = request.form['especie']
        raca = request.form['raca']
        peso = float(request.form['peso'])
        nome_tutor = request.form['nome_tutor']
        telefone = request.form['telefone']
        codigo = len(contatos)
        contatos.append([codigo, nome, especie, raca, peso, nome_tutor, telefone])
        return redirect('/')
    else:
        return render_template('cadastro.html', contatos=contatos)

@app.route('/editar_usuario/<int:codigo>', methods=['GET', 'POST'])
def editar_usuario(codigo):
    if request.method == 'POST':
        nome = request.form['nome']
        especie = request.form['especie']
        raca = request.form['raca']
        peso = float(request.form['peso'])
        nome_tutor = request.form['nome_tutor']
        telefone = request.form['telefone']
        contatos[codigo] = [codigo, nome, especie, raca, peso, nome_tutor, telefone, contatos[codigo][6]]
        return redirect('/')
    else:
        contato = contatos[codigo]
        return render_template('editar_usuario.html', contato=contato, contatos=contatos)

# --------------------------------------------------------------------------------------------------------------------

@app.route('/adicionar_agendamento', methods=['GET', 'POST'])
def adicionar_agendamento():
    if request.method == 'POST':
        nome = request.form['nome']
        nome_tutor = request.form['nome_tutor']
        data = request.form['data']
        sintomas = request.form['sintomas']
        codigo = len(agendas)
        agendas.append([codigo, nome, nome_tutor, data, sintomas])
        return redirect('/agenda')
    else:
        return render_template('adicionar_agendamento.html', agenda=agendas, contatos=contatos)

@app.route('/editar_agendamento/<int:codigo>', methods=['GET', 'POST'])
def editar_agendamento(codigo):
    if request.method == 'POST':
        nome = request.form['nome']
        nome_tutor = request.form['nome_tutor']
        data = request.form['data']
        sintomas = request.form['sintomas']
        agendas[codigo] = [codigo, nome, nome_tutor, data, sintomas, agendas[codigo][4]]
        return redirect('/agenda')
    else:
        agenda = agendas[codigo]
        return render_template('editar_agendamento.html', agenda=agenda, contatos=contatos)

@app.route('/apagar_agendamento/<int:codigo>')
def apagar_agendamento(codigo):
    del agendas[codigo]
    return redirect('/agenda')


# ---------------------------------------------------------------------------------------------------------------------

@app.route('/calcular_idade', methods=['GET', 'POST'])
def calcular_idade():
    if request.method == 'POST':
        nome = request.form['nome']
        especie_animal = request.form['especie_animal']
        idade = int(request.form['idade'])

        if especie_animal.lower() == 'cachorro':
            if idade == 1:
                idade_humana = 15
            elif idade == 2:
                idade_humana = 24
            elif idade == 3:
                idade_humana = 28
            elif idade == 4:
                idade_humana = 32
            elif idade == 5:
                idade_humana = 36
            elif idade == 6:
                idade_humana = 40
            elif idade == 7:
                idade_humana = 44
            else:
                idade_humana = 44 + (idade - 7) * 5

        elif especie_animal.lower() == 'gato':
            if idade == 1:
                idade_humana = 15
            elif idade == 2:
                idade_humana = 24
            elif idade == 3:
                idade_humana = 28
            elif idade == 4:
                idade_humana = 32
            elif idade == 5:
                idade_humana = 36
            else:
                idade_humana = 36 + (idade - 5) * 4

        else:
            idade_humana = 'Espécie inválida! Escolha entre "cachorro" ou "gato".'
        idade_humana_.append(idade_humana)

        return redirect('/calcular_idade')

    else:
        return render_template('calcular_idade.html', idade_humana=idade_humana_, contatos=contatos)

# ----------------------------------------------------------------------------------------------------------------------


@app.route('/calcular_dose', methods=['GET', 'POST'])
def calcular_dose():
    if request.method == 'POST':
        nome = request.form['nome']
        peso = float(request.form['peso'])
        dose_rec = int(request.form['dose'])
        dose = peso * dose_rec
        codigo = len(doses)
        doses.append((dose))
        return redirect('/soro_e_dose')
    else:
        return render_template('soro_e_dose.html', dose=doses, contatos=contatos)



# ---------------------------------------------------------------------------------------------------------------------
@app.route('/calcular_soro', methods=['GET', 'POST'])
def calcular_soro():
    if request.method == 'POST':
        soro = None
        nome = request.form['nome']
        grau = request.form['grau']
        peso = float(request.form['peso'])
        if grau.capitalize() == 'Leve':
            soro = 50 * peso
        elif grau.capitalize() == 'Moderada':
            soro = 75 * peso
        elif grau.capitalize() == 'Grave':
            soro = 100 * peso

        soros.append((soro))
        return redirect('/soro_e_dose')

    else:
        return render_template('soro_e_dose.html', soro=soros, contatos=contatos)



if __name__ == '__main__':
    app.run(debug=True)