from queries import Executing_queries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# class Data_visualisation:
#     @staticmethod
def present_data():

    object2 = Executing_queries()
    # object2.execute_command()
    time_taken_to_ship_orders, average_time_taken_per_month = object2.execute_command()
    df = pd.DataFrame()
    df["Average Time Taken To Ship Orders"] = time_taken_to_ship_orders
    df["Month Of Shipment"] = average_time_taken_per_month
    pd.set_option("display.max_rows", len(time_taken_to_ship_orders))
    print(df.head(len(time_taken_to_ship_orders)))

    plt.plot(average_time_taken_per_month, time_taken_to_ship_orders, '*') # bo stands for blue circle markers, x, v, <, >, *
    plt.title('Table Showing The Average Time Taken To Ship Order On a Monthly Basis ')
    plt.xlabel('Month Of Shipment')
    plt.ylabel('Time Taken To Ship Orders')
    plt.show()


