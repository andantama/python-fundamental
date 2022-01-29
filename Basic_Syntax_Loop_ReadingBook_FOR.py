"""
LOOP Program 'Book Reading' using FOR
"""

book_count = 10
print('Mom said, "Go read your books."')

book_read = 0
print(f"Books have been read {book_read}")

for book_read in range(1, book_count + 1):
    print(f"Book number {book_read} has been read.")

print(f"Total books have been read are {book_read} books.")
