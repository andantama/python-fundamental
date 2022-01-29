book_list = ["Seven Habits", "How to Influence People", "First thing First", "Donald Duck"]
print(">> Show the variable of book_list <<")
print(book_list)

print("\n>> Compile the book_list with FOR IN <<")
for book in book_list:
    print(book)

print("\n>> Show book_list on certain index <<")
print(book_list[0])
print(book_list[3])

print("\n>> Compile the book_list with FOR IN RANGE <<")
for j in range(0, len(book_list)):
    print(book_list[j])

print("\n>> Add 1 New Book <<")
book_list.append("National History")
for j in range(0, len(book_list)):
    print(book_list[j])

print("\n>> Clear The Book List <<")
book_list.clear()

print("\n>> Change Book 2 <<")
book_list = ["Seven Habits", "How to Influence People", "First thing First", "Donald Duck"]
book_list.append("National History")
book_list[2] = "Second Chance"
for k in range(0, len(book_list)):
    print(book_list[k])

print('\n>> Take Out Book No.2 <<')
books = book_list.pop(1)
for k in range(0, len(book_list)):
    print(book_list[k])

print('\n>> List of Taken Books <<')
print(books)

print('\n>> pop function 01 <<')
book_list.pop()
for k in range(0, len(book_list)):
    print(book_list[k])

print('\n>> pop function 02 <<')
book_list.pop(-3)
for k in range(0, len(book_list)):
    print(book_list[k])
