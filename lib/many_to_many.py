class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        written_by_author = self.contracts()
        related_books = set(contract.book for contract in written_by_author)
        return list(related_books)
    
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract
    
    def total_royalties(self):
        total = sum(contract.royalties for contract in self.contracts())
        return total


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        book_contracts = self.contracts()
        authors_list = [contract.author for contract in book_contracts]
        return authors_list


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.validate_author(author)
        self.author = author
        self.validate_book(book)
        self.book = book
        self.validate_date(date)
        self.date = date
        self.validate_royalties(royalties)
        self.royalties = royalties
        Contract.all.append(self)

    def validate_author(self, author):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        
    def validate_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        
    def validate_date(self, date):
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        
    def validate_royalties(self, royalties):
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an integer")
        
    @classmethod
    def contracts_by_date(cls, date):
        unsorted_contracts = [contract for contract in cls.all if contract.date == date ]
        sorted_contracts = sorted(unsorted_contracts, key=lambda contract: contract.date)
        return sorted_contracts
        