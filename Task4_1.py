# Lesson 4: Clean Code
# 1. Building a Modular Online Bookstore System

class Book:
    def __init__(self, title, author, price, stock):
        self.__title = title
        self.__author = author
        self.__price = price
        self.__stock = stock

    # Getters and Setters for title
    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    # Getters and Setters for author
    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    # Getters and Setters for price
    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("Price must be a non-negative value.")

    # Getters and Setters for stock
    def get_stock(self):
        return self.__stock

    def set_stock(self, stock):
        if stock >= 0:
            self.__stock = stock
        else:
            print("Stock must be a non-negative value.")

    # Method to check availability
    def is_available(self):
        return self.__stock > 0

    # Method to display book information
    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")
        print(f"Available: {'Yes' if self.is_available() else 'No'}")

# Additional functions related to book management
def restock_book(book, additional_stock):
    if additional_stock > 0:
        book.set_stock(book.get_stock() + additional_stock)
        print(f"Restocked {book.get_title()} by {additional_stock} units.")
    else:
        print("Additional stock must be a positive number.")

def apply_discount(book, discount_percentage):
    if 0 <= discount_percentage <= 100:
        new_price = book.get_price() * (1 - discount_percentage / 100)
        book.set_price(new_price)
        print(f"Applied {discount_percentage}% discount on {book.get_title()}. New price is ${book.get_price():.2f}")
    else:
        print("Discount percentage must be between 0 and 100.")

# Example usage
if __name__ == "__main__":
    my_book = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99, 5)
    my_book.display_info()

    restock_book(my_book, 10)
    apply_discount(my_book, 20)
    my_book.display_info()
