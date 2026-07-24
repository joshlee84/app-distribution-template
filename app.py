# --------------------------------------------------
# Import packages
# --------------------------------------------------

from analyticskit import *
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# --------------------------------------------------
# Obtain, validate, and load the CSV sales data
# --------------------------------------------------

while True:
    file_path = select_file("Please select the file to be used in this code.")
    if '.csv' in file_path.lower():
        sales = pd.read_csv(file_path)
        if 'Date' in sales.columns and 'Amount' in sales.columns:
            break

# --------------------------------------------------
# Ask the user if they want to save the image
# --------------------------------------------------

while True:
    save_file_input = single_input('Would you like to save the daily sales chart as a PNG? Y/N')
    if save_file_input.lower() in ['y','n','yes','no']:
        break
    else:
        show_message('Invalid Input', f'You entered "{save_file_input}". Please enter either Y or N.')

# --------------------------------------------------
# Extract the directory of the loaded file
# --------------------------------------------------

file_path = Path(file_path)
directory = str(file_path.parent)

# --------------------------------------------------
# Convert the Date column to a pandas datetime type.
# --------------------------------------------------

sales["Date"] = pd.to_datetime(sales["Date"])

# --------------------------------------------------
# Calculate daily total sales
# --------------------------------------------------

daily_sales = (sales.groupby("Date")["Amount"].sum().reset_index().sort_values("Date"))

# print("\nDaily Total Sales")
# print(daily_sales)

# --------------------------------------------------
# Chart: Daily total sales
# --------------------------------------------------

first_date = sales['Date'].min().strftime('%Y-%m-%d')
last_date = sales['Date'].max().strftime('%Y-%m-%d')
png_name = f'daily_sales {first_date} to {last_date}.png'

plt.figure(figsize=(10, 6))
plt.plot(daily_sales["Date"], daily_sales["Amount"], marker="o")
plt.title("Daily Total Sales")
plt.xlabel("Date")
plt.ylabel("Sales Amount ($)")
plt.xticks(rotation=90)
plt.tight_layout()
if save_file_input.lower() in ['y','yes']:
    plt.savefig(directory + '/' + png_name)
plt.show()
