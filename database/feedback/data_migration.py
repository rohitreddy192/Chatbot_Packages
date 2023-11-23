migrate_rules = [
    '''CREATE TABLE Orders_New (
    OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INTEGER,
    OrderDetails TEXT,
    ExpectedDeliveryDate DATETIME,
    ActualDeliveryDate DATETIME,
    OrderStatus VARCHAR(50)
    );''',

    '''INSERT INTO Orders_New (OrderID, UserID, OrderDetails, ExpectedDeliveryDate, ActualDeliveryDate, OrderStatus)
    SELECT OrderID, UserID, OrderDetails, datetime(ExpectedDeliveryDate), datetime(ActualDeliveryDate), OrderStatus
    FROM Orders;''',

    '''DROP TABLE Orders;''',

    '''ALTER TABLE Orders_New RENAME TO Orders;''']

import sqlite3

# Connect to a database (or create one if it doesn't exist)
conn = sqlite3.connect('feedback_orders.db')
for i in migrate_rules:
    conn.execute(i)
    
conn.commit()
conn.close()




"""
-- Create a new table with the desired schema
CREATE TABLE Orders_New (
    OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INTEGER,
    OrderDetails TEXT,
    ExpectedDeliveryDate DATETIME,
    ActualDeliveryDate DATETIME,
    OrderStatus VARCHAR(50)
);

-- Copy data from the old table to the new table
INSERT INTO Orders_New (OrderID, UserID, OrderDetails, ExpectedDeliveryDate, ActualDeliveryDate, OrderStatus)
SELECT OrderID, UserID, OrderDetails, datetime(ExpectedDeliveryDate), datetime(ActualDeliveryDate), OrderStatus
FROM Orders;

-- Drop the old table
DROP TABLE Orders;

-- Rename the new table to match the old table name
ALTER TABLE Orders_New RENAME TO Orders;



"""