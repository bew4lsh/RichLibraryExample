# Import necessary components from the Rich library
from rich.console import Console  # For creating a console object to print rich text
from rich.table import Table  # For creating and manipulating tables
from rich.panel import Panel  # For creating panels to display detailed information
from rich.prompt import Prompt  # For creating interactive prompts

# Create a dictionary with example data
# This dictionary will be used to populate the table
data = {
    "Field1": {"value": "Value1", "description": "This is a detailed description of Field1"},
    "Field2": {"value": "Value2", "description": "This is a detailed description of Field2"},
    "Field3": {"value": "Value3", "description": "This is a detailed description of Field3"},
    "Field4": {"value": "Value4", "description": "This is a detailed description of Field4"},
    "Field5": {"value": "Value5", "description": "This is a detailed description of Field5"},
    "Field6": {"value": "Value6", "description": "This is a detailed description of Field6"},
    "Field7": {"value": "Value7", "description": "This is a detailed description of Field7"},
}

def display_details(field, details):
    """Display detailed information about a selected field."""
    console.print(Panel(f"[bold]{field}[/bold]\n\nValue: {details['value']}\n\nDescription: {details['description']}"))

# Create a table object with a title
table = Table(title="Example Rich Table")

# Add two columns to the table
# The "Field" column will be cyan and won't wrap text
table.add_column("Field", style="cyan", no_wrap=True)
# The "Value" column will be magenta
table.add_column("Value", style="magenta")

# Iterate through the dictionary items
for field, details in data.items():
    # Add each key-value pair as a row in the table
    table.add_row(field, details['value'])

# Create a console object for rich text output
console = Console()
# Print the table to the console
console.print(table)

# Prompt the user to select a field
selected_field = Prompt.ask("Enter a field name to see more details", choices=list(data.keys()))

# Display the details of the selected field
display_details(selected_field, data[selected_field])
