import sqlite3

# Connect to a database (or create one if it doesn't exist)
conn = sqlite3.connect('feedback_orders.db')
cursor = conn.cursor()

# Create Orders table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Orders (
        OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID INTEGER,
        OrderDetails TEXT,
        ExpectedDeliveryDate DATE,
        ActualDeliveryDate DATETIME,
        OrderStatus VARCHAR(50)
    )
''')

# Create Feedback table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Feedback (
        FeedbackID INTEGER PRIMARY KEY AUTOINCREMENT,
        OrderID INTEGER,
        UserID INTEGER,
        FeedbackText TEXT,
        Rating INTEGER,
        Timestamp DATETIME,
        FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Tables created successfully.")


"""
DB SCHEMA:-

Orders Table Schema:

OrderID: Integer (Primary Key, Auto Increment)
UserID: Integer
OrderDetails: Text
ExpectedDeliveryDate: Date
ActualDeliveryDate: DateTime
OrderStatus: VARCHAR(50)


Feedback Table Schema:

FeedbackID: Integer (Primary Key, Auto Increment)
OrderID: Integer (Foreign Key referencing Orders table)
UserID: Integer
FeedbackText: Text
Rating: Integer
Timestamp: DateTime (Timestamp of feedback submission)



"""