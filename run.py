
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

# --------- update Sales in Gsheet, add new row with the list user input data -----------
def update_sales_worksheet(data):
    
    print("updating sales worksheet ... \n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("sales worksheet updated with success ...\n")

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
    pprint (stock_row)
    # 2sd option using the len() method to get the length of the list and print the required   


def main():
    """
    Run all program
      functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    calculate_surplus_data(sales_data)
print("Welcome to Love Sandwiches Data Automation")


main()