# learning how to use enumerate 


books = ["Python", "Git", "Linux"]

# i = 0
# for book in books:
#     print(i, book)
#     i += 1

for index, name in enumerate(books, 1):
    print(f"{index}. {name}")
