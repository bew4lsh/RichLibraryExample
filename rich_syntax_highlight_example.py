from rich.console import Console
from rich.syntax import Syntax
from rich.panel import Panel

def display_code_with_theme(console, code, language, theme):
    syntax = Syntax(code, language, theme=theme, line_numbers=True)
    console.print(Panel(syntax, title=f"{language.capitalize()} - {theme} theme", expand=False))

def main():
    console = Console()
    console.print("[bold green]Rich Syntax Highlighting Example with Themes[/bold green]\n")

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

    # Example JSON
    json_code = '''{
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "swimming", "coding"]
}'''

    # List of themes to demonstrate
    themes = ["monokai", "github-dark", "solarized-dark", "solarized-light", "dracula"]

    # Display Python code with different themes
    console.print("[bold]Python Examples:[/bold]")
    for theme in themes:
        display_code_with_theme(console, python_code, "python", theme)
        console.print()  # Add a blank line between examples

    # Display JSON code with different themes
    console.print("[bold]JSON Examples:[/bold]")
    for theme in themes:
        display_code_with_theme(console, json_code, "json", theme)
        console.print()  # Add a blank line between examples

if __name__ == "__main__":
    main()
