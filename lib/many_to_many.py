#Define a class method named contracts_by_date that takes a date parameter.
# Initialize an empty list named contracts_on_date.
#Iterate through each contract in the all contracts list.
# If the contract's date matches the input date, add it to the contracts_on_date list.
# Sort the contracts_on_date list based on the contract's date attribute.
# Return the sorted contracts_on_date list

class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]


class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author class")
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an integer")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        contracts_on_date = [contract for contract in cls.all if contract.date == date]
        return sorted(contracts_on_date, key=lambda x: x.date)


