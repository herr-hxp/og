import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# FLAVORS

cur.execute("INSERT INTO flavors (name, hourlyprice, monthlyprice) VALUES (?, ?, ?)",
            ('v1-micro-1', '0.10', '73')
            )

cur.execute("INSERT INTO flavors (name, hourlyprice, monthlyprice) VALUES (?, ?, ?)",
            ('v1-mini-1', '0.14', '102')
            )

cur.execute("INSERT INTO flavors (name, hourlyprice, monthlyprice) VALUES (?, ?, ?)",
            ('v1-small-1', '0.279', '204')
            )

cur.execute("INSERT INTO flavors (name, hourlyprice, monthlyprice) VALUES (?, ?, ?)",
            ('v1-standard-1', '0.560', '409')
            )

cur.execute("INSERT INTO flavors (name, hourlyprice, monthlyprice) VALUES (?, ?, ?)",
            ('v1-standard-2', '1.120', '818')
            )

cur.execute("INSERT INTO flavors (name, hourlyprice, monthlyprice) VALUES (?, ?, ?)",
            ('v1-standard-4', '2.240', '1635')
            )

cur.execute("INSERT INTO flavors (name, hourlyprice, monthlyprice) VALUES (?, ?, ?)",
            ('v1-standard-8', '4.479', '3270')
            )

cur.execute("INSERT INTO flavors (name, hourlyprice, monthlyprice) VALUES (?, ?, ?)",
            ('v1-dedicated-8', '5.411', '3950')
            )

cur.execute("INSERT INTO flavors (name, hourlyprice, monthlyprice) VALUES (?, ?, ?)",
            ('v2-dedicated-8', '8.151', '5950')
            )

cur.execute("INSERT INTO flavors (name, hourlyprice, monthlyprice) VALUES (?, ?, ?)",
            ('d2-dedicated-8', '11.30', '8249')
            )

# STORAGE

cur.execute("INSERT INTO storage (name, hourlyprice, monthlyprice) VALUES (?, ?, ?)",
            ('Swift Object Storage, 1GB', '0.0007', '0.50')
            )

cur.execute("INSERT INTO storage (name, hourlyprice, monthlyprice) VALUES (?, ?, ?)",
            ('Volume 4000 IOPS SSD, 1GB', '0.0049', '3.60')
            )

cur.execute("INSERT INTO storage (name, hourlyprice, monthlyprice) VALUES (?, ?, ?)",
            ('Volume 8000 IOPS SSD, 1GB', '0.0074', '5.40')
            )

cur.execute("INSERT INTO storage (name, hourlyprice, monthlyprice) VALUES (?, ?, ?)",
            ('Volume 16000 IOPS SSD, 1GB', '0.0099', '7.20')
            )

cur.execute("INSERT INTO storage (name, hourlyprice, monthlyprice) VALUES (?, ?, ?)",
            ('Volume Snapshop, 1GB', '0.001', '0.73')
            )

cur.execute("INSERT INTO storage (name, hourlyprice, monthlyprice) VALUES (?, ?, ?)",
            ('Barbican Key Manager Secret', '0.13', '95')
            )

# NETWORK

cur.execute("INSERT INTO network (name, hourlyprice, monthlyprice) VALUES (?, ?, ?)",
            ('Router', '0.68', '495')
            )

cur.execute("INSERT INTO network (name, hourlyprice, monthlyprice) VALUES (?, ?, ?)",
            ('Load Balancer as a Service (instance is added)', '0.34', '245')
            )

cur.execute("INSERT INTO network (name, hourlyprice, monthlyprice) VALUES (?, ?, ?)",
            ('SSL certificate for LBaaS', '0.20', '145')
            )

cur.execute("INSERT INTO network (name, hourlyprice, monthlyprice) VALUES (?, ?, ?)",
            ('Public IP', '0.08', '58')
            )

cur.execute("INSERT INTO network (name, hourlyprice, monthlyprice) VALUES (?, ?, ?)",
            ('Bandwidth per GB', '0', '0.50')
            )


# LICENCES

cur.execute("INSERT INTO licenses (name, hourlyprice, monthlyprice) VALUES (?, ?, ?)",
            ('Windows Server license', '0.05', '36')
            )

cur.execute("INSERT INTO licenses (name, hourlyprice, monthlyprice) VALUES (?, ?, ?)",
            ('Windows SQL Standard Server license', '0.27', '195')
            )


connection.commit()
connection.close()
