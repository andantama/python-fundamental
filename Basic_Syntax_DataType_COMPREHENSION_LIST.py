print('\n>> Del Function <<')
book_list = ["Seven Habits", "How to Influence People", "Second Chance", "Donald Duck", "National History"]
del book_list[0]
for i in range(0, len(book_list)):
    print(book_list[i])

print('\n>> DEl Function with Comprehension List <<')
book_list = ["Seven Habits", "How to Influence People", "Second Chance", "Donald Duck", "National History"]
del book_list[:]
for i in range(0, len(book_list)):
    print(book_list[i])

print('\n>> DEl Function with Comprehension List START <<')
book_list = ["Seven Habits", "How to Influence People", "Second Chance", "Donald Duck", "National History"]
del book_list[0:-2] # START:END
for j in range(0, len(book_list)):
    print(book_list[j])

print('\n>> DEl Function with Comprehension List START & STEP <<')
book_list = ["Seven Habits", "How to Influence People", "Second Chance", "Donald Duck", "National History"]
del book_list[0::2] # START:END:STEP
for k in range(0, len(book_list)):
    print(book_list[k])

print('\n>> Creating a New Book List with Comprehension <<')
book_list = ["Seven Habits", "How to Influence People", "Second Chance", "Donald Duck", "National History"]
new_book_list = book_list[:]
for k in range(0, len(book_list)):
    print(book_list[k])

print('\n>> New Book List <<')
del book_list[:]
for k in range(0, len(new_book_list)):
    print(new_book_list[k])

print('\n>> New Book List with Comprehension START STEP <<')
book_list = ["Seven Habits", "How to Influence People", "Second Chance", "Donald Duck", "National History"]
new_book_list = book_list[0::2]
for i in range(0, len(new_book_list)):
    print(new_book_list[i])

print('\n>> New Book List with Comprehension START STEP (Alternative w/o New Variable) <<')
book_list = ["Seven Habits", "How to Influence People", "Second Chance", "Donald Duck", "National History"]
print(book_list[1:-1:2])


