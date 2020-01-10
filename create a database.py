import sqlite3
# Создание базы, в которой будут храниться слова, создается один раз
conn = sqlite3.connect("vocabulary.db")
cursor = conn.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS words (word_original text NOT NULL PRIMARY KEY, translation text); """)
conn.commit()



