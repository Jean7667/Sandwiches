import gspread

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
    print("please input sales data")
    print("expected format 6 numbers separated by commas")
    print("Example: 1,11,22,24,1,21\n")  
    
    data_str = input("enter your numbers here: ")
    
    #print(f"you gave the following numbers {data_str}")

    sales_data = data_str.split(",")
    #call fct to check format
    validate_data(sales_data)
    #print(sales_data)

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
#e shorthand error python - review
# data type input always a str ''        



#call fct
get_sales_data()
    