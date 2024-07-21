from rich.console import Console
from rich.syntax import Syntax

def main():
    console = Console()
    console.print("[bold green]Rich Syntax Highlighting Example[/bold green]\n")

    # Example Python code
    python_code = '''
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Print the first 10 Fibonacci numbers
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci(i)}")
'''

    # Highlight Python syntax
    syntax = Syntax(python_code, "python", theme="monokai", line_numbers=True)
    console.print(syntax)

    # Example JSON
    json_code = '''{
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "swimming", "coding"]
}'''

    # Highlight JSON syntax
    syntax = Syntax(json_code, "json", theme="monokai", line_numbers=True)
    console.print("\nJSON Example:")
    console.print(syntax)

if __name__ == "__main__":
    main()
