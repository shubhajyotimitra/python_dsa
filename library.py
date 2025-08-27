# Node for Linked List
class BookNode:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available
        self.next = None  # pointer to next book


# Linked List for storing books
class LibraryLinkedList:
    def __init__(self):
        self.head = None
        self.book_map = {}  # HashMap for fast search by ID

    # Add new book
    def add_book(self, book_id, title, author):
        new_book = BookNode(book_id, title, author)
        
        # Add to linked list (at beginning for simplicity)
        new_book.next = self.head
        self.head = new_book

        # Add to HashMap
        self.book_map[book_id] = new_book
        print(f"✅ Book '{title}' added successfully!")

    # Display all books
    def display_books(self):
        if not self.head:
            print("📭 No books available in library.")
            return
        
        print("\n📚 Library Collection:")
        temp = self.head
        while temp:
            status = "Available" if temp.available else "Issued"
            print(f"ID: {temp.book_id}, Title: {temp.title}, Author: {temp.author}, Status: {status}")
            temp = temp.next

    # Search book by ID
    def search_book(self, book_id):
        if book_id in self.book_map:
            book = self.book_map[book_id]
            status = "Available" if book.available else "Issued"
            print(f"🔎 Found -> ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Status: {status}")
        else:
            print("❌ Book not found.")

    # Delete book
    def delete_book(self, book_id):
        if book_id not in self.book_map:
            print("❌ Book not found.")
            return

        # Remove from Linked List
        temp = self.head
        prev = None
        while temp:
            if temp.book_id == book_id:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                break
            prev = temp
            temp = temp.next

        # Remove from HashMap
        del self.book_map[book_id]
        print(f"🗑️ Book ID {book_id} deleted successfully!")

    # Borrow / Return Book
    def update_availability(self, book_id, available):
        if book_id in self.book_map:
            self.book_map[book_id].available = available
            if available:
                print(f"✅ Book ID {book_id} has been returned.")
            else:
                print(f"📕 Book ID {book_id} has been issued.")
        else:
            print("❌ Book not found.")


# =============================
# 📌 Example Run
# =============================
if __name__ == "__main__":
    library = LibraryLinkedList()

    # Add books
    library.add_book(101, "Python Programming", "John Doe")
    library.add_book(102, "Data Structures", "Alice Smith")
    library.add_book(103, "Algorithms Unlocked", "Thomas Cormen")

    # Display books
    library.display_books()

    # Search book
    library.search_book(102)

    # Issue a book
    library.update_availability(102, False)

    # Return a book
    library.update_availability(102, True)

    # Delete a book
    library.delete_book(103)

    # Display again
    library.display_books()
