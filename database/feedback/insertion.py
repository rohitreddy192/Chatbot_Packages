import sqlite3

conn = sqlite3.connect('feedback_orders.db')
cursor = conn.cursor()

records_to_insert = [
    (1, 'Pizza and Salad.', '2023-11-20 16:00:00', '2023-11-20 19:00:00', 'Delayed, Delivered'),
    (2, 'Pasta.', '2023-11-21 10:40:00', '2023-11-21 11:00:00', 'Delivered before Time'),
    (3, 'Sushi.', '2023-11-23 12:00:00', None, 'Still Didn\'t delivered.'),
    (4, 'Indian Curry.', '2023-11-23 18:00:00', '2023-11-23 18:30:00', 'Delivered in Time')
]

insert_query = '''
    INSERT INTO Orders (UserID, OrderDetails, ExpectedDeliveryDate, ActualDeliveryDate, OrderStatus)
    VALUES (?, ?, ?, ?, ?)
'''
for record in records_to_insert:
    cursor.execute(insert_query, record)

conn.commit()
conn.close()

print('Records Inserted!')
