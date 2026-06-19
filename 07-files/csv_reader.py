import csv # Module for handling CSV files

def read_csv_file(filename):
    """Read a CSV file and return its contact as a list of rows."""
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader) # Convert reader to list of rows
            return rows
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    
def display_table(rows):
    """Display rows as a formatted table with headers."""
    if not rows:
        return
    
    # Get headers (first row)
    headers = rows[0]
    # Calculate column widths
    col_widths = [len(header) for header in headers]
    
    # Find max width in each column
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(cell))
            
    # Print separator line
    separator = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"
    
    # Print headers
    print(separator)
    header_row = "|" + "|".join(f" {headers[i]:<{col_widths[i]}} " for i in range(len(headers))) + "|"
    print(header_row)
    print(separator)
    
    # Print data rows
    for row in rows[1:]: # Skip header row
        data_row = "|" + "|".join(f" {row[i]:<{col_widths[i]}} " if i < len(row) else " " * (col_widths[i] + 2) for i in range(len(headers))) + "|"
        print(data_row)
    print(separator)

def main():
    filename = input("Enter CSV filename (e.g., data.csv): ")
    data = read_csv_file(filename)
    
    if data:
        print(f"\n File '{filename}' loaded successfully!\n")
        display_table(data)
    else:
        print("Unalbe to read file.")
    
if __name__ == "__main__":
    main()