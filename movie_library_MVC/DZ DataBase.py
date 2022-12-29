import sqlite3 as sq

techics = [('iphone', 'xs', 43000),
           ('iphone', 'xr', 44000),
           ('iphone', '11', 48000),
           ('iphone', '11 Pro', 64000),
           ('iphone', '13', 76000),
           ('samsung', 's7', 54000),
           ('samsung', 's8', 63000),
           ('honor', 'zx2', 23000),
           ('huawei', 'ww3', 32000)
           ]

with sq.connect('smartfon.db') as con:
    cur = con.cursor()
    cur.executescript("""
    CREATE TABLE IF NOT EXISTS telephone(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firm TEXT,
    model TEXT,
    price INTEGER
    )
    """)
    cur.executemany('INSERT INTO telephone VALUES(NULL,?,?,?)', techics)
