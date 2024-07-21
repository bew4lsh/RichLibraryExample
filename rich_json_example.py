from rich.console import Console
from rich.json import JSON
import json

def main():
    console = Console()

    # Sample JSON data
    sample_data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York",
        "interests": ["programming", "reading", "traveling"],
        "education": {
            "degree": "Bachelor's",
            "major": "Computer Science",
            "university": "Example University"
        },
        "work_experience": [
            {
                "company": "Tech Corp",
                "position": "Software Engineer",
                "years": 3
            },
            {
                "company": "Innovative Startup",
                "position": "Senior Developer",
                "years": 2
            }
        ]
    }

    # Convert the Python dictionary to a JSON string
    json_str = json.dumps(sample_data, indent=2)

    console.print("[bold green]Rich JSON Output Example[/bold green]")
    console.print("Raw JSON string:")
    console.print(json_str)

    console.print("\n[bold]Formatted and colorized JSON using Rich:[/bold]")
    console.print(JSON(json_str))

    console.print("\n[bold cyan]You can also print specific parts of the JSON:[/bold cyan]")
    console.print("Work Experience:")
    console.print(JSON(json.dumps(sample_data["work_experience"], indent=2)))

if __name__ == "__main__":
    main()
