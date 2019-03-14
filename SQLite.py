import sqlite3
import time
import datetime
import random

conn = sqlite3.connect("tutorial.db")
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL , datestamp TEXT , keyword TEXT , value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1451255552 , '2019-2-16' , 'python' , 8)") # putting in the value within the quotes
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():
    t = time.time()
    date = str(datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d'))
    keyword = "Python"
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot (unix , datestamp , keyword , value) VALUES(? , ? , ? , ?)" , (t , date , keyword , value)) # putting in the value from other variables
    conn.commit()

def read_from_database():


#create_table()
#data_entry()


dynamic_data_entry()
