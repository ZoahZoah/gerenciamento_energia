import sys
import plotly.express as px
import pandas as pd
import config
from QrcFiles.ui_main_window import Ui_Widget
from data_base import BancoDeDados
from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication, QUrl
from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsProxyWidget, QWidget
from QrcFiles.ui_main_window import Ui_Widget
from PySide6.QtWebEngineWidgets import QWebEngineView

class Graficos:
    def __init__(self, banco_dados):
        self.bd = banco_dados

    
    # Carrega o gráfico HTML no PyQt
    def load_html_chart(self, item):
        web_view = QWebEngineView()
        file_path = f"/home/ivan/Python/gerenciamento_energia/grafico_{item}.html"
        web_view.load(QUrl.fromLocalFile(file_path))
        return web_view

    # Função para gerar o gráfico interativo do consumo do mês
    def grafico_consumo_diario(self, item):
        self.bd.mycursor.execute(f"""
            SELECT 
                ano,
                mes,
                dia,
                consumo_diario
            FROM (
                SELECT 
                    YEAR(data_verificacao) AS ano,
                    MONTH(data_verificacao) AS mes,
                    DAY(data_verificacao) AS dia,
                    AVG(consumo_energia) AS consumo_diario
                FROM 
                    leituras
                WHERE 
                    YEAR(data_verificacao) = YEAR(CURDATE()) AND
                    MONTH(data_verificacao) = MONTH(CURDATE()) AND
                    caminho = '{item}'
                GROUP BY 
                    ano, mes, dia
            ) AS consumos_diarios
            ORDER BY 
                ano, mes, dia;
        """)

        resultados = self.bd.mycursor.fetchall()
        return resultados

    # Função para gerar o consumo diario de todos os meses do ano
    def grafico_diario_anual(self, item):
        self.bd.mycursor.execute(f"""
            SELECT 
                    ano,
                    mes,
                    dia,
                    consumo_diario
                FROM (
                    SELECT 
                        YEAR(data_verificacao) AS ano,
                        MONTH(data_verificacao) AS mes,
                        DAY(data_verificacao) AS dia,
                        AVG(consumo_energia) AS consumo_diario
                    FROM 
                        leituras
                    WHERE 
                        data_verificacao >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
                        AND caminho = '{item}'
                    GROUP BY 
                        ano, mes, dia
                ) AS consumos_diarios
                ORDER BY 
                    ano, mes, dia;
                    """)

        resultados = self.bd.mycursor.fetchall()
        return resultados


    def gerar_grafico(self, dados, item):
        df = pd.DataFrame(dados, columns=['ano', 'mes', 'dia', 'consumo_energia'])
        df = df.drop(columns=['ano'])  # Remover a coluna 'ano'
        
        # Pivotar o DataFrame para ter os meses como colunas e os dias como índices das linhas
        df_pivot = df.pivot_table(index='dia', columns='mes', values='consumo_energia', aggfunc='mean')
        
        # Plotar o gráfico
        fig = px.line(df_pivot)
        fig.update_layout(
            xaxis_title='Dia',
            yaxis_title='Consumo de Energia Médio',
            title_font_color='black',
            title_font_size=22,
            title={
                'text': 'Consumo diário de energia do item 1',
                'x': 0.5,
                'xanchor': 'center'
            }
        )
        return fig.write_html(f'/home/ivan/Python/gerenciamento_energia/grafico_{item}.html')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())