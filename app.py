import streamlit as st

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.borrow():
                    return True, f"You have borrowed '{title}'"
                else:
                    return False, f"'{title}' is already borrowed."
        return False, f"'{title}' not found in the library."

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return True, f"You have returned '{title}'"
        return False, f"'{title}' not found in the library."

    def get_all_books(self):
        return self.books

    def get_available_books(self):
        return [book for book in self.books if not book.is_borrowed]

    def get_borrowed_books(self):
        return [book for book in self.books if book.is_borrowed]

# Initialize library in session state
def init_library():
    if 'library' not in st.session_state:
        st.session_state.library = Library()
        # Add some sample books
        st.session_state.library.add_book(Book("1984", "George Orwell"))
        st.session_state.library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
        st.session_state.library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))

# Main Streamlit App
def main():
    st.set_page_config(page_title="📚 Library Management System", page_icon="📖")
    
    # Initialize library
    init_library()
    library = st.session_state.library
    
    # Header
    st.title("📚 Library Management System")
    st.markdown("---")
    
    # Sidebar for actions
    st.sidebar.header("📋 Menu")
    action = st.sidebar.radio(
        "Choose an action:",
        ["View Books", "Add Book", "Borrow Book", "Return Book", "Statistics"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info("Crafted with ❤️ by Maliha Mehejabin")
    
    if action == "View Books":
        st.header("📖 All Books")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("✅ Available Books")
            available = library.get_available_books()
            if available:
                for book in available:
                    st.success(f"📕 **{book.title}**\n\n✍️ *{book.author}*")
            else:
                st.warning("No books available.")
                
        with col2:
            st.subheader("📌 Borrowed Books")
            borrowed = library.get_borrowed_books()
            if borrowed:
                for book in borrowed:
                    st.error(f"📕 **{book.title}**\n\n✍️ *{book.author}*\n\n🔴 Currently borrowed")
            else:
                st.success("No books currently borrowed.")
    
    elif action == "Add Book":
        st.header("➕ Add New Book")
        
        with st.form("add_book_form"):
            title = st.text_input("Book Title", placeholder="Enter book title...")
            author = st.text_input("Author Name", placeholder="Enter author name...")
            submitted = st.form_submit_button("📚 Add Book")
            
            if submitted:
                if title and author:
                    new_book = Book(title, author)
                    library.add_book(new_book)
                    st.success(f"✅ Successfully added '{title}' by {author}!")
                    
                    # Show updated book list
                    st.info("📚 Updated Book List:")
                    for book in library.get_all_books():
                        status = "🔴 Borrowed" if book.is_borrowed else "✅ Available"
                        st.write(f"- {book.title} by {book.author} ({status})")
                else:
                    st.error("❌ Please fill in both fields!")
    
    elif action == "Borrow Book":
        st.header("📤 Borrow a Book")
        
        available_books = library.get_available_books()
        if available_books:
            book_titles = [book.title for book in available_books]
            selected_book = st.selectbox("Select a book to borrow:", book_titles)
            
            if st.button("📤 Borrow Book"):
                success, message = library.borrow_book(selected_book)
                if success:
                    st.success(f"✅ {message}")
                    st.balloons()
                else:
                    st.error(f"❌ {message}")
        else:
            st.warning("⚠️ No books available to borrow!")
    
    elif action == "Return Book":
        st.header("📥 Return a Book")
        
        borrowed_books = library.get_borrowed_books()
        if borrowed_books:
            book_titles = [book.title for book in borrowed_books]
            selected_book = st.selectbox("Select a book to return:", book_titles)
            
            if st.button("📥 Return Book"):
                success, message = library.return_book(selected_book)
                if success:
                    st.success(f"✅ {message}")
                else:
                    st.error(f"❌ {message}")
        else:
            st.success("🎉 No books are currently borrowed!")
    
    elif action == "Statistics":
        st.header("📊 Library Statistics")
        
        total = len(library.get_all_books())
        available = len(library.get_available_books())
        borrowed = len(library.get_borrowed_books())
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📚 Total Books", total)
        with col2:
            st.metric("✅ Available", available)
        with col3:
            st.metric("📌 Borrowed", borrowed, delta=-borrowed)
        
        # Progress bar
        if total > 0:
            availability = (available / total) * 100
            st.subheader("📈 Availability Rate")
            st.progress(availability / 100)
            st.caption(f"{availability:.1f}% of books are available")
            
        # List all books with status
        st.subheader("📋 Complete Book List")
        for book in library.get_all_books():
            status = "🔴 Borrowed" if book.is_borrowed else "✅ Available"
            st.text(f"{book.title} by {book.author} - {status}")

if __name__ == "__main__":
    main()