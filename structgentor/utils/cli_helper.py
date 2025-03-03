def cli_help():
    """Displays help information for Structgentor."""
    help_text = """
    Structgentor - Project Structure Generator

    Usage:
      structgentor init [project_name]   Initialize a new project structure.
      structgentor freeze                Save the current directory structure to layout.txt.
      structgentor help                   Show this help message.

    Options:
      project_name  (Optional) Specify a project folder name. If not provided, it initializes in the current directory.
    
    Example:
      structgentor init my_project       # Creates 'my_project' with the structure
      structgentor freeze                # Saves the current folder structure
      structgentor help                  # Shows this help menu
    """
    print(help_text.strip())
