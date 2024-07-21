from rich.tree import Tree
from rich.console import Console
from rich import print

def create_file_tree():
    tree = Tree("📁 Project Root")
    
    src = tree.add("📁 src")
    src.add("📄 main.py")
    src.add("📄 utils.py")
    
    tests = tree.add("📁 tests")
    tests.add("📄 test_main.py")
    tests.add("📄 test_utils.py")
    
    docs = tree.add("📁 docs")
    docs.add("📄 README.md")
    docs.add("📄 CONTRIBUTING.md")
    
    assets = tree.add("📁 assets")
    images = assets.add("📁 images")
    images.add("🖼️ logo.png")
    images.add("🖼️ banner.jpg")
    
    return tree

if __name__ == "__main__":
    console = Console()
    file_tree = create_file_tree()
    console.print(file_tree)
    print("\n[bold green]This is an example of Rich's tree functionality![/bold green]")
