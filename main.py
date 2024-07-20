# Import necessary components from the Rich library
from rich.console import Console  # For creating a console object to print rich text
from rich.table import Table  # For creating and manipulating tables

# Create a dictionary with example data
# This dictionary will be used to populate the table
data = {
    "Field1": "Value1",
    "Field2": "Value2",
    "Field3": "Value3",
    "Field4": "Value4",
    "Field5": "Value5",
    "Field6": "Value6",
    "Field7": "Value7",
}

# Create a table object with a title
table = Table(title="Example Rich Table")

# Add two columns to the table
# The "Field" column will be cyan and won't wrap text
table.add_column("Field", style="cyan", no_wrap=True)
# The "Value" column will be magenta
table.add_column("Value", style="magenta")

# Iterate through the dictionary items
for field, value in data.items():
    # Add each key-value pair as a row in the table
    table.add_row(field, value)

# Create a console object for rich text output
console = Console()
# Print the table to the console
console.print(table)
