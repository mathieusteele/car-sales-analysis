import pandas

sold_items = pandas.read_csv('sold_items.csv')

sales_data_frame = pandas.DataFrame(sold_items)

#
# Question - Which Brand has on average been the most profitable for the car dealership?
#

# calculate average profit for each distinct make
average_profit_by_make = sales_data_frame.groupby('make').net.mean().sort_values(ascending=False)

print("Based on historical sales data, the overall average profit per car make in order is:")
print(average_profit_by_make)

# 
# Question - Has the average profit per vehicle improved over time?? What impact did Covid vehicle shortages have on profit?
# 

average_profit_by_year = sales_data_frame.groupby('sale_year').net.mean().sort_index(ascending=True)
print("\nThe average profit per vehicle per year in order is:")
print(average_profit_by_year)
print("\nCompared with the previous six years, 2021 and 2022 have shown a marked improvement in the average profit per sale.")

# Question - What car make spends the shortest amount of time on the lot, on average?
avg_days_on_lot = sales_data_frame.groupby('make').days_on_lot.mean().sort_values(ascending=False)
print(avg_days_on_lot)
# This is giving unexpected results. I don't think it is calculating it how I want it to.
