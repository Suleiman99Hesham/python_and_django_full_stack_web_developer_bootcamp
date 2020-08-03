class Book():
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "title: {},\tauthor: {},\tpages: {}".format(self.title,self.author,self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("the book has been deleted.")

b = Book("python", "suleiman", 200)
print(b)
print(len(b))