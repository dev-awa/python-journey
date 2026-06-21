import os

def safe_file_reader(filename):
    """Read a file safely with comprehensive error handling."""
    try:
        # Check if file exists
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File '{filename}' not found in the current directory.")
        
        # Try to open and read the file
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Check if file is empty
        if not content.strip():
            print("Warning: File is empty.")
            return None
        
        return content
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
    except PermissionError:
        print(f"Error: Permision denied. You don't have access to '{filename}'.")
        return None
    except UnicodeDecodeError:
        print(f"Error: Unable to decode '{filename}'. The file might be binary or use an unsupported encoding.")
        return None
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        return None
    
def main():
    print("--- Safe File Reader ---")
    filename = input("Enter filename to read: ").strip()
    
    # Validate filename (not empty)
    if not filename:
        print("Error: Filename cannot be empty.")
        return
    
    content = safe_file_reader(filename)
    
    if content is not None:
        print("\n File Content: ")
        print("=" * 50)
        print(content)
        print("=" * 50)
        print(f"File read successfully! Total characters: {len(content)}")
    
    print("Program finished.")
    
if __name__ == "__main__":
    main()