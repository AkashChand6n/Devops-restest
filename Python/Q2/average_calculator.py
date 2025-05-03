# Author: Akash Chandran
# Description: Read a CSV file and calculate the average of a specified column.
 
import csv  # Import the CSV module to read CSV files
 
# Define a function to calculate average of a specific column in a CSV file
def calculate_average(filename, column_name):
    try:
        # Open the CSV file for reading
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)  # Read file into a dictionary per row
            values = []  
           
            for row in reader:
                # Check if the specified column exists in the current row
                if column_name in row:
                    try:
                        # Try converting the value to float and store it
                        value = float(row[column_name])
                        values.append(value)
                    except ValueError:
                        # If conversion fails, print warning and skip the value
                        print(f"Warning: Non-numeric value skipped in row: {row}")
                else:
                    # If column not found in row, show error and stop
                    print(f"Column '{column_name}' not found in row: {row}")
                    return
 
            # Check if we have collected any valid values
            if not values:
                print(f"No valid numeric data found in column '{column_name}'.")
                return
 
            # Calculate and print the average
            average = sum(values) / len(values)
            print(f"Average of column '{column_name}': {average}")
 
    except FileNotFoundError:
        # If the file doesn't exist
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")
 
# Entry point of the script
if __name__ == "__main__":
    # Call the function with the CSV filename and column name
    calculate_average('data.csv', 'score')