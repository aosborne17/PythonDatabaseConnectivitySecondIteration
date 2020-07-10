from create_connection import database_OOP
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


class Executing_queries:

    def execute_command(self):

        object = database_OOP()
        cursor = object.establish_connection()
        query_result = """SELECT AVG(sq1.[Time Taken To Ship Orders]) AS "Average Time Taken Per Month"
                            ,sq1.[Date Of Delivery] "Month Of Delivery"
                            FROM (SELECT (DATEDIFF(d,OrderDate,ShippedDate)) AS "Time Taken To Ship Orders"
                            ,FORMAT(o.OrderDate, 'yy-MM') AS "Date Of Delivery"
                            FROM Orders o) sq1
                            GROUP BY sq1.[Date Of Delivery]
                            ORDER BY sq1.[Date Of Delivery]"""
        rows = cursor.execute(query_result)
        time_taken_to_ship_orders = []
        average_time_taken_per_month = []
        for keys, values in rows:
            time_taken_to_ship_orders.append(keys)
            average_time_taken_per_month.append(values)
        return time_taken_to_ship_orders, average_time_taken_per_month

    def execute_second_command(self):
        object = database_OOP()
        cursor = object.establish_connection()
        query_result = "SELECT FORMAT(AVG(UnitPrice), 'C') FROM Products"
        rows = cursor.execute(query_result)
        average_unit_price = []
        for row in rows:
            average_unit_price.append(row)
        print(average_unit_price)
        return average_unit_price

