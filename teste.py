import sys
import plotly.express as px
import datetime
import pandas as pd
from QrcFiles.ui_main_window import Ui_Widget
from data_base import BancoDeDados
from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication, QUrl
from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsProxyWidget, QWidget
from QrcFiles.ui_main_window import Ui_Widget
from PySide6.QtWebEngineWidgets import QWebEngineView

bd = BancoDeDados('localhost', 'root', 'Euamochocotone1998!!', 'dados_energia')

def load_html_chart():
    web_view = QWebEngineView()
    # Certifique-se de fornecer o caminho absoluto correto para o arquivo HTML
    file_path = "/home/ivan/Python/gerenciamento_energia/grafico_caminho1.html"
    web_view.load(QUrl.fromLocalFile(file_path))
    return web_view

# Função para gerar o gráfico interativo
def grafico_consumo_diario():
    bd.mycursor.execute("""
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
                caminho = 'caminho1'
            GROUP BY 
                ano, mes, dia
        ) AS consumos_diarios
        ORDER BY 
            ano, mes, dia;
    """)

    resultados = bd.mycursor.fetchall()
    return resultados

def grafico_diario_anual():
    bd.mycursor.execute("""
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
                    AND caminho = 'caminho1'
                GROUP BY 
                    ano, mes, dia
            ) AS consumos_diarios
            ORDER BY 
                ano, mes, dia;
                """)

    resultados = bd.mycursor.fetchall()
    return resultados


def gerar_grafico(dados):
    df = pd.DataFrame(dados, columns=['ano', 'mes', 'dia', 'consumo_energia'])
    df = df.drop(columns=['ano'])  # Remover a coluna 'ano'
    
    # Pivotar o DataFrame para ter os meses como colunas e os dias como índices das linhas
    df_pivot = df.pivot_table(index='dia', columns='mes', values='consumo_energia', aggfunc='mean')
    
    
    # Plotar o gráfico
    fig = px.line(df_pivot, title='Consumo diário de energia do item 1')
    fig.update_layout(
        xaxis_title='Dia',
        yaxis_title='Consumo de Energia Médio',
        title_font_color='black',
        title_font_size=22,
    )
    return fig.write_html('/home/ivan/Python/gerenciamento_energia/grafico_caminho1.html')

dados = grafico_diario_anual()
grafico = gerar_grafico(dados)


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.bd = BancoDeDados('localhost', 'root', 'Euamochocotone1998!!', 'dados_energia')
        titulo_janela = 'Blink'

        self.ui = Ui_Widget()   
        self.ui.setupUi(self)               # set widget setup
        self.setWindowTitle(titulo_janela)  # set window title
        self.ui.btn_toggle.clicked.connect(self.leftMenu)       # toggle_button


        # Paginas do sistema
        self.ui.button_home.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.pg_home))
        self.ui.butto_contato.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.pg_contatos))
        self.ui.button_sobre.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.pg_sobre))
        self.ui.button_gerenciar.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.pg_gerenciamento))

        scene = QGraphicsScene()
        self.ui.graphicsView.setScene(scene)

        html_char_view = load_html_chart()
                
        proxy = QGraphicsProxyWidget()
        proxy.setWidget(html_char_view)

        # Adicionar o QGraphicsProxyWidget à QGraphicsScene
        scene.addItem(proxy)

        # Ajustar a visualização para o tamanho do gráfico
        #self.ui.graphicsView.fitInView(scene.sceneRect())
        #self.ui.graphicsView.show()




    def leftMenu(self):
        width = self.ui.left_container.width()

        if width == 1:
            newWidth = 200
        else:
            newWidth = 1

        self.ui.animation = QtCore.QPropertyAnimation(self.ui.left_container, b'maximumWidth')
        self.ui.animation.setDuration(500)
        self.ui.animation.setStartValue(width)
        self.ui.animation.setEndValue(newWidth)
        self.ui.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.ui.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())