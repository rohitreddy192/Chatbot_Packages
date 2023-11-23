import sqlite3

# We are fetching our Database record to provide information to our AI Agent to collect feedback..
class DBConnection:
    def getrecord(self, orderId):
        conn = sqlite3.Connection('feedback_orders.db')
        cursor = conn.cursor()
        sql_query = f'''SELECT OrderID, UserID, OrderDetails, DATE(ExpectedDeliveryDate), ActualDeliveryDate, OrderStatus FROM Orders where OrderID = {orderId} ORDER BY ActualDeliveryDate DESC LIMIT 1;'''    
        ans = None
        try:
            # Execute the SQL query
            cursor.execute(sql_query)

            # Fetch all results
            row = cursor.fetchone()
            rephrase_row = f'''
            Order is {row[2]}, which founds to ordered on {row[3]} and is {row[-1]}.
            '''
            print(row)
        except sqlite3.Error as e:
            # Handle any errors that occur during execution
            print("Error:", e)
            rephrase_row = 'No records exist'
        finally:
            # Close the database connection
            conn.close()
            return rephrase_row
            
