import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # Carregando o arquivo .ui
        loader = QUiLoader()
        self.ui = loader.load("ui_main_window.ui")
        self.setCentralWidget(self.ui.centralwidget)

        # Ajustando o tamanho da janela para o tamanho do arquivo .ui
        self.resize(self.ui.size())

        # Adicionar funcionalidade se necessário
        self.setup_ui()

    def setup_ui(self):
        # Adicione código adicional de configuração aqui, se necessário
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())