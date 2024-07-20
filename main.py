from rich.console import Console
from rich.table import Table

# Create a dictionary with example data
data = {
    "Field1": "Value1",
    "Field2": "Value2",
    "Field3": "Value3",
    "Field4": "Value4",
    "Field5": "Value5",
    "Field6": "Value6",
    "Field7": "Value7",
}

# Create a table
table = Table(title="Example Rich Table")

# Add columns
table.add_column("Field", style="cyan", no_wrap=True)
table.add_column("Value", style="magenta")

# Add rows
for field, value in data.items():
    table.add_row(field, value)

# Create a console object and print the table
console = Console()
console.print(table)
