"""main.py: Configuration parameter GUI for a Calibre plugin that can read OPDS feeds"""

__author__    = "Steinar Bang"
__copyright__ = "Steinar Bang, 2015"
__credits__   = ["Steinar Bang"]
__license__   = "GPL v3"

from PyQt5.Qt import QWidget, QHBoxLayout, QLabel, QLineEdit

from calibre.utils.config import JSONConfig

prefs = JSONConfig('plugins/opds_client')

prefs.defaults['opds_url'] = 'http://localhost:8080/opds'
prefs.defaults['hideNewspapers'] = True
prefs.defaults['hideBooksAlreadyInLibrary'] = True

class ConfigWidget(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.opdsUrlLabel = QLabel('OPDS URL: ')
        self.layout.addWidget(self.opdsUrlLabel)

        self.opdsUrlEditor = QLineEdit(self)
        self.opdsUrlEditor.setText(prefs['opds_url'])
        self.layout.addWidget(self.opdsUrlEditor)
        self.opdsUrlLabel.setBuddy(self.opdsUrlEditor)

    def save_settings(self):
        prefs['opds_url'] = self.opdsUrlEditor.text()

            
