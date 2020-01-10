import sys
from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QSizePolicy, QTextEdit
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import requests
import sqlite3

# Стоп-слова, слова, которые обычно выкидываются из текста(артикли, союзы, междометия). Существует встроенный список,
# для дальнейшей работы с нимим
stop_words = stopwords.words("english") + ["'s", "'m", "'ve", "?", "!", ".", ",", "-", ";", ":"]

# Создание класса для Лемматизации слов. Лемматизация - преведение слова к каноничной форме, лемме.
lemmatizer = WordNetLemmatizer()

# Список слов, который, подразумевается, пользователь уже знает), берется из базы.
conn = sqlite3.connect("vocabulary.db")
cursor = conn.cursor()
n = []
cursor.execute("SELECT word_original FROM words")
for i in cursor.fetchall():
    n.append(i[0])

# Создание виджета, определение его параметров, окон, кнопок и т.д.
class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Learning_english")
        self.resize(1000, 900)
        self.move(100, 50)
        self.setStyleSheet("background-color:PeachPuff;")
        self.edit = QTextEdit("Текст")
        self.edit2 = QTextEdit("Вывод")
        self.button = QPushButton("Вывести неизвестные слова")
        self.button2 = QPushButton("Перевести неизвестные слова")
        self.button3 = QPushButton("Показать словарь")
        self.button4 = QPushButton("Очистить")
        self.edit.setStyleSheet("background-color:PapayaWhip;")
        self.edit2.setStyleSheet("background-color:PapayaWhip;")
        self.button.setStyleSheet("background-color:LightSalmon;")
        self.button2.setStyleSheet("background-color:LightSalmon;")
        self.button3.setStyleSheet("background-color:LightSalmon;")
        self.button4.setStyleSheet("background-color:LightSalmon;")
        layout = QGridLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.edit2)
        layout.addWidget(self.button, 2, 0)
        layout.addWidget(self.button2, 2, 1)
        layout.addWidget(self.button3, 3, 0)
        layout.addWidget(self.button4, 3, 1)
        self.edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.edit2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.button4.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.button2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.button3.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setLayout(layout)
        self.button.clicked.connect(self.tokenz)
        self.button2.clicked.connect(self.transl)
        self.button3.clicked.connect(self.dictr)
        self.button4.clicked.connect(self.clear)
    def clear(self): # Очищает поля ввода и вывода
        self.edit.setText("{}".format(""))
        self.edit2.setText("{}".format(""))
    def tokenz(self): # Выводит на экран неизвстные для пользователя слова, в инфинитиве
        l = self.edit.toPlainText()
        l = nltk.pos_tag(nltk.word_tokenize(l), tagset='universal')
        wd = []
        for i in range(len(l)):
            if l[i][1] == 'NOUN':
                wd.append(lemmatizer.lemmatize(l[i][0], wordnet.NOUN))
            elif l[i][1] == 'VERB':
                wd.append(lemmatizer.lemmatize(l[i][0], wordnet.VERB))
            elif l[i][1] == 'ADV':
                wd.append(lemmatizer.lemmatize(l[i][0], wordnet.ADV))
            elif l[i][1] == 'ADJ':
                wd.append(lemmatizer.lemmatize(l[i][0], wordnet.ADJ))
            else:
                wd.append(l[i][0])
        w = list(set(wd))
        words = []
        for i in range(len(w)):
            w[i] = (w[i]).lower()
            if w[i] not in stop_words:
                words.append(w[i])
        s = []
        for i in words:
            if i not in n:
                s.append(i)
        return self.edit2.setText("{}".format(s))
    def transl(self): # Выводит на экран неизвстные слова с переводом, и добавляе их в словарь пользователя
        URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
        KEY = 'trnsl.1.1.20200105T104005Z.5b922f3180fd0280.e302d49ea165afb64ca2c17cea9c45ac010809f9'
        l = self.edit.toPlainText()
        l = nltk.pos_tag(nltk.word_tokenize(l), tagset='universal')
        wd = []
        for i in range(len(l)):
            if l[i][1] == 'NOUN':
                wd.append(lemmatizer.lemmatize(l[i][0], wordnet.NOUN))
            elif l[i][1] == 'VERB':
                wd.append(lemmatizer.lemmatize(l[i][0], wordnet.VERB))
            elif l[i][1] == 'ADV':
                wd.append(lemmatizer.lemmatize(l[i][0], wordnet.ADV))
            elif l[i][1] == 'ADJ':
                wd.append(lemmatizer.lemmatize(l[i][0], wordnet.ADJ))
            else:
                wd.append(l[i][0])
        w = list(set(wd))
        words = []
        for i in range(len(w)):
            w[i] = (w[i]).lower()
            if w[i] not in stop_words:
                words.append(w[i])
        s = []
        for i in words:
            if i not in n:
                s.append(i)
        o = []
        for i in s:
            d = requests.post(URL, data={'key': KEY, 'text': i, 'lang': "ru"}).json()["text"][0]
            o.append((i, d))
        cursor.executemany(
            "INSERT OR IGNORE INTO words (word_original, translation) values (?, ?)", o)
        conn.commit()
        o = "\n ".join(str(x) for x in o)
        return self.edit2.setText("{}".format(o))
    def dictr(self): # Выводит на экран весь соварь пользователя (слово+перевод)
        cursor.execute("SELECT word_original, translation FROM words")
        u = "\n ".join(str(x) for x in cursor.fetchall())
        return self.edit2.setText("{}".format(u))


if __name__ == '__main__':
    app = QApplication()
    form = Form()
    form.show()
    sys.exit(app.exec_())