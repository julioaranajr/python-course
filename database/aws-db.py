# Import and Define pandas as pd
import pandas as pd

# # Increase the maximum number of rows to display the entire DataFrame:
# pd.options.display.max_rows = 9999
# # Load the CSV into a DataFrame 
# aws_db = pd.read_csv('~/src/Talent-Academy/Projects/aws_services_db/database/aws.csv')
# # - Tip: use to_string() to print the entire DataFrame.
# print(aws_db.head()) 
# print(aws_db.info()) 
# print(aws_db.value_counts()) 


aws_services=pd.read_csv('~/src/Talent-Academy/Projects/aws_services_db/database/aws.csv')

# Create a list with tha data inside of the csv file (lisy-of-list)
list_values = aws_services.values.tolist()

