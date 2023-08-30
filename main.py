import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QListWidget, QWidget, QVBoxLayout

class AppListaTarefa(QWidget):
    def __init__(self):
        super().__init__()

        self.tarefas = []

        #Configuração da janela principal
        self.setWindowTitle('To do List')
        self.setGeometry(100,100,400,600)

        #Widgets da interface
        self.txt_tarefa = QLineEdit()
        self.btn_adicionar = QPushButton('Adicionar')
        self.btn_concluir = QPushButton('Concluir')
        self.btn_editar = QPushButton('Editar')
        self.btn_remover = QPushButton('Remover')

        self.lst_tarefa = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.txt_tarefa)
        layout.addWidget(self.btn_adicionar)
        layout.addWidget(self.btn_editar)
        layout.addWidget(self.btn_concluir)
        layout.addWidget(self.btn_remover)
        layout.addWidget(self.lst_tarefa)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication()
    app_lista_tarefa = AppListaTarefa()
    app_lista_tarefa.show()
    sys.exit(app.exec())


