# Textbook inventory
books_inventory = ("Textbook ID", "Textbook Name", "Courses", "Number of Books", "Price Per Book", "Publisher ID")
books1 = ("TEXT-0001", "Basic Anatomy and Physiology", "BIO-100", 400, 94, "PUB-1003")
books2 = ("TEXT-0002", "Chemistry for Biology Students", "BIO-101-102", 400, 105.30, "PUB-1002")
books3 = ('TEXT-0003', 'Anatomy and Physiology', 'BIO-141-142', 330, 159.75, 'PUB-1003')

# Publishers
publisher_inventory = ("Publisher ID", "Publisher Name", "Address", "City", "State", "Zip Code", "Phone Number")
publisher1 = ("PUB-1001", "Science Books Galore", "525 Allen St.", "Trenton", "NJ", 8620, "(609) 555-2554")
publisher2 = ("PUB-1002", "Books for Chemistry Students Ltd.", "142 N. Spring St.", "Los Angeles", "CA", 90012, "(213) 555-8362")
publisher3 = ("PUB-1003", "Carliz Publishers Corp.", "24 King Ave.", "Columbus", "OH", 43201, "(614) 555-3322")

# Tables
books_tbl = [books_inventory, books1, books2, books3]
publisher_tbl = [publisher_inventory, publisher1, publisher2, publisher3]

print("Textbook Name and Price, from the Textbook Inventory: \n")

indx2 = 0
books = []

while indx2 < len(books_tbl):
    books.append(books_tbl[indx2][1])
    books.append(books_tbl[indx2][4])
    indx2 += 1
    print books
    books = []

print("\nPublisher Name and Phone Number, from the Publisher Inventory: \n")

indx3 = 0
pub = []

while indx3 < len(publisher_tbl):
    pub.append(publisher_tbl[indx3][1])
    pub.append(publisher_tbl[indx3][6])
    indx3 += 1
    print pub
    pub = []
