"""
LOOP Program Book Reading and Comprehendin using WHILE
"""

book_count = 10
print('Mom asked, "Go read and comprehend all books you have."')

total_read = 0

total_comprehended = 0
print(f"Total books have been read and comprehended {total_comprehended}.")

while total_read < book_count * 2:
    total_read = total_read + 1
    if total_comprehended == 9:
        print(f"Book number {total_comprehended + 1} wasn't comprehended yet.")
    else:
        total_comprehended = total_comprehended + 1
        print(f"Book number {total_comprehended} has been read and comprehended.")

print(f"Total books have been read and comprehended {total_comprehended}.")
if total_comprehended == book_count:
    print('"Mom, I have already read and comprehend all books content."')
else:
    print(f'"Mom, I can not comprehend all the books. I just comprehend with the {total_comprehended} books."')
