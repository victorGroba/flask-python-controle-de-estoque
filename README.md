# 📊 **Aplicação Web para Gestão de Dados de Temperatura e Pedidos**

## 🚀 **Visão Geral**

Esta aplicação web combina duas funcionalidades principais:
1. **Gestão de Dados de Temperatura**: Registra e gera relatórios sobre dados de temperatura de equipamentos.
2. **Registro de Pedidos**: Permite registrar e visualizar pedidos, armazenando informações em um arquivo de texto.

Utiliza **Flask** para o backend, **pandas** e **openpyxl** para manipulação de dados e Excel, além de técnicas de logging para rastreamento de atividades.

## 🛠️ **Recursos**

### 1. **Gestão de Dados de Temperatura**
- **Formulário de Registro**: Entrada de dados sobre equipamentos e temperaturas.
- **Geração de Relatórios**: Relatórios detalhados agrupados por mês e ano.
- **Relatórios Individuais**: Acesso a relatórios específicos por equipamento e período.

### 2. **Registro de Pedidos**
- **Formulário de Registro de Pedidos**: Registra nome, material e quantidade, com data e hora.
- **Armazenamento de Dados**: Dados são armazenados em um arquivo de texto (`registros.txt`).
- **Visualização de Registros**: Funcionalidade opcional para visualizar registros do dia atual.
- **Limpeza de Registros**: Funcionalidade opcional para limpar registros exibidos.

## 🌟 **Tecnologias Utilizadas**

- **Flask**: Framework web para construção da aplicação.
- **pandas**: Biblioteca para manipulação e análise de dados (somente para gestão de dados de temperatura).
- **openpyxl**: Biblioteca para leitura e escrita de arquivos Excel (somente para gestão de dados de temperatura).
- **HTML/CSS**: Para criação das interfaces web.
- **Logging**: Para rastreamento e registro de erros e informações importantes.

## 📂 **Como Funciona**

### **Gestão de Dados de Temperatura**

1. **Registro de Dados**: Preencha o formulário com detalhes sobre o equipamento e temperaturas.
2. **Geração de Relatórios**: Visualize relatórios na web, agrupados por mês e ano.
3. **Relatórios Individuais**: Acesse e imprima relatórios específicos por equipamento.

### **Registro de Pedidos**

1. **Registro de Pedidos**: Preencha o formulário com informações sobre pedidos.
2. **Armazenamento e Visualização**: Os pedidos são armazenados em um arquivo de texto e podem ser visualizados opcionalmente.
3. **Limpeza de Registros**: Opcionalmente, limpe registros exibidos.

## 📥 **Como Começar**

1. Clone o repositório:
    ```bash
    git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute a aplicação:
    ```bash
    python app.py
    ```


## 🤝 **Contribuições**

Sinta-se à vontade para contribuir com melhorias e sugestões. Abra uma issue ou envie um pull request!

## 📧 **Contato**

Para dúvidas ou sugestões, entre em contato pelo e-mail: [victorgroba2@gmail.com](mailto:victorgroba2@gmail.com)
