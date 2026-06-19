# Get a sentence from the user
sentence = input("Enter a sentence: ")

# Split sentence into words (splits by spaces)
words = sentence.lower().split() # .lower() makes all words lowercase for accurate counting

# Initialize empty dictionary for word counts
word_count = {}

# Count each word
for word in words:
    # .get(word, 0) returns the current count or 0 if not present
    word_count[word] = word_count.get(word, 0) + 1
    
# Display the results
print("\n--- Word Frequency ---")
for word, count in word_count.items():
    print(f"'{word}': {count} times")