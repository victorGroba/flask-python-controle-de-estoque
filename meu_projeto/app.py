from flask import Flask, request, redirect, url_for, render_template, jsonify
import os
import datetime

app = Flask(__name__)

# Função para obter a data atual no formato 'YYYY-MM-DD'
def obter_data_atual():
    return datetime.datetime.now().strftime('%Y-%m-%d')

# Rota principal que renderiza o formulário
@app.route('/')
def form():
    return render_template('form.html')

# Rota para registrar um novo pedido
@app.route('/registrar', methods=['POST'])
def registrar():
    nome = request.form['nome']
    material = request.form['material']
    quantidade = request.form['quantidade']
    data_hora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Caminho para o arquivo onde os registros são armazenados
    arquivo_registro = 'registros.txt'

    # Escreve os dados no arquivo junto com a data e hora
    try:
        with open(arquivo_registro, 'a') as f:
            f.write(f'{data_hora} | Nome: {nome}, Material: {material}, Quantidade: {quantidade}\n')
        app.logger.info('Registro salvo com sucesso no arquivo.')
    except Exception as e:
        app.logger.error(f'Erro ao salvar registro no arquivo: {e}')

    # Retorna os dados registrados como resposta JSON
    registro = {
        'nome': nome,
        'material': material,
        'quantidade': quantidade,
        'data_hora': data_hora
    }
    
    return jsonify(registro)

# Rota para limpar os registros exibidos na página (opcional)
@app.route('/limpar_registros_exibidos', methods=['POST'])
def limpar_registros_exibidos():
    # Limpar os registros exibidos na página (se houver implementação)
    return 'Registros exibidos limpos com sucesso.'

# Rota para ver os registros do dia atual (opcional)
@app.route('/ver_registros')
def ver_registros():
    # Implementação para mostrar registros do dia atual (se houver)
    return 'Implementar visualização de registros do dia atual.'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
