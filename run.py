
import gspread
from pprint import pprint
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


print ("something")

CREDS = Credentials.from_service_account_file('cred.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

#check access to data API connection
""" sales = SHEET.worksheet('sales')
data = sales.get_all_values()
print(data)
 """

#fct get sales data from the user
def get_sales_data():
    while True:

        print("please input sales data from the last market")
        print("expected format 6 numbers separated by commas")
        print("Example: 1,11,22,24,1,21\n")  
        
        data_str = input("enter your numbers here: ")
        
        #print(f"you gave the following numbers {data_str}")

        sales_data = data_str.split(",")
        #call fct to check format
        validate_data(sales_data)
        #print(sales_data)

        if validate_data(sales_data):
            print ("Data is valid")
            break

    return sales_data

def validate_data(values):
    """
    check format of data
    converts all strings values into int 
    raises value erroe if strings cannont be converted
    """
    #print(values)
    try:
        #convert st into int
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(  
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True
#e shorthand error python - review
# data type input always a str ''        

# print(data) check

def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")




""" # --------- update Sales in Gsheet, add new row with the list user input data -----------
def update_sales_worksheet(data):
    
    print("updating sales worksheet ... \n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("sales worksheet updated with success ...\n") """

def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.
    The surplus is defined as the sales figure subtracted from the stock:
    Positive surplus indicates waste
    Negative surplus indicates extra made when stock was sold out.
    """
    print("calculating surplus \n")
    stock = SHEET.worksheet("stock").get_all_values()
    # pprint(stock) check the values
    # square brackets with list index of -1
    # to slice the final item from the list 
    stock_row = stock[-1]
    #pprint (stock_row)
    # 2sd option using the len() method to get the length of the list and print the required   
    #print (f"stock_row:{stock_row}")
    #print (f"sales_row:{sales_row}")
    ############## where I left  convert data into int and perform calcul through the list
    #Using the Python zip() Function for Parallel Iteration
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
        #print(surplus_data)
    return surplus_data
"""
update our surplus worksheet with the surplus data.
"""

""" def update_surplus_worksheet(data):
    print("updating surplus worksheet ... \n")
    surplus_worksheet = SHEET.worksheet("surplus")
    surplus_worksheet.append_row(data)
    print("surplus worksheet updated with success ...\n") """

def get_last_5_entries_sales():
    """
    Collects columns of data from sales worksheet, collecting
    the last 5 entries for each sandwich and returns the data
    as a list of lists.
    """
    sales = SHEET.worksheet("sales")
    columns = []
    #print our column variable and see values - make range adjustement to skip 0
    for ind in range(1, 7):
        column = sales.col_values(ind)
        #to get the 5 last lines (slice method)
        columns.append(column[-5:]) 
    return columns

def calculate_stock_data(data):
    """
    Calculate the average stock for each item type, adding 10%
    """
    print("Calculating stock data...\n")
    new_stock_data = []

    for column in data:
        int_column = [int(num) for num in column]
        #using the length method make possible change in the list (add columns)
        average = sum(int_column) / len(int_column)
        #adding 10%
        stock_num = average * 1.1
        #round the data
        new_stock_data.append(round(stock_num))
    # print (new_stock_data) - to check the output
    return new_stock_data

def main():
    """
    Run all program functions
    """

    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, "surplus")
    #print(new_surplus_data)
    sales_columns = get_last_5_entries_sales()
    stock_data = calculate_stock_data(sales_columns)
    #print (stock_data)
    update_worksheet(stock_data,"stock")
print("Welcome to Love Sandwiches Data Automation")

main()


