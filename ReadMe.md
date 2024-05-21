Projeto de UPX-III

Para rodar o código será necessário instalar as bibliotecas disponiveis em requirements.txt
O arquivo consiste num modelo incompleto de analise de consumo energético, incompleto pois
não há meios físicos disponiveis para efetuar de fato essa analise, por questões financeiras 
e outros problemas.

Função: Selecionar os dados disponíveis no banco de dados e com isso montar um gráfico para
ánalise de consumo diário e mensal, disponibilizando a comparação com outros meses.
O gráfico disponibilizado é do tipo interativo e é ativado ao clicar no botão "ativar", que
está disponível na aba de "Sistema", visualizada ao clicar no menu esquerdo.

Este projeto consiste numa conexão com o banco de dados usando MySql e seguindo a conexão
disponibilizada na documentação do Python. Foi usada a biblioteca Plotly para geração do
gráfico interativo, e do pandas para criar o dataframe.