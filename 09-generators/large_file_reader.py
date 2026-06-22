def read_large_file(file_path):
    """
    Generator that reads a large file line by line without loading it all into memory.
    Yields one line at a time.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                yield line.strip() # Remove trailing newline
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return
    except Exception as e:
        print(f"An error occured: {e}")
        return
    
def count_lines_with_word(file_path, target_word):
    """
    Count how many lines contain a specific word using the generator.
    """
    count = 0
    for line in read_large_file(file_path):
        if target_word.lower() in line.lower(): # Case-insensitive search
            count += 1
        return count
    
def main():
    print("--- Large File Reader with Generator ---")
    filename = input("Enter filename to read: ").strip()
    
    if not filename:
        print("Filename cannot be empty.")
        return
    
    # Test reading first 5 lines
    print(f"\n First 5 lines of '{filename}' : ")
    print("=" * 50)
    line_count = 0
    for line in read_large_file(filename):
        print(line)
        line_count += 1
        if line_count >= 5:
            break
        
    if line_count == 0:
        print("File is empty or could not be read.")
        return
    
    print("=" * 50)
    print(f"First {line_count} lines displayed.")
    
    # Optional: Count occurences of a word
    search_word = input("\n Enter a word to search (or press Enter to skip): ").strip()
    if search_word:
        total_lines = 0
        try:
            # Count total lines (by iterating through generator)
            for _ in read_large_file(filename):
                total_lines += 1
        except:
            total_lines = 0
            
        if total_lines > 0:
            count = count_lines_with_word(filename, search_word)
            print(f"Word '{search_word}' found in {count} out of {total_lines} lines.")
        else:
            print("Unable to count lines.")
        
if __name__ == "__main__":
    main()