book Inventory Management System

Objective:

Develop a RESTful API for managing a book inventory using any programming language and an MVC framework. 
The API will handle operations related to books, suppliers, and stock levels.

Requirements:

1. API Functionality:
● Create book: Add a new book with details such as name, supplier, price, and stock quantity.
● Update book: Modify existing book details.
● Delete book: Remove a book from the inventory.
● List books: Retrieve a list of all books with the option to filter by supplier orprice range.
● View book Details: Retrieve detailed information of a single book by ID.
● Adjust Stock: Increment or decrement the stock level for a given book.

2. Data Model:
● book: Should have at least the following fields:● ID (unique identifier)● Name● Supplier ID (foreign key)● Price● Stock Quantity● Images (List of images of any dimension) (Maximum 10) (Optional)
● Supplier: Should have at least the following fields:● ID (unique identifier)● Name● Contact Information

3. Technology Stack:
● Programming Language: Any (e.g., Python, Java, Ruby, JavaScript)
● Framework: Any MVC framework (e.g., Django, Spring Boot, Ruby on Rails,Express.js)
● Database: Any relational database (e.g., PostgreSQL, MySQL, SQLite)
● ORM: Compatible with the chosen stack (e.g., Django ORM, Hibernate,ActiveRecord)
● Docker and Docker compose for running your application and database

4. REST API Standards:
● Adhere to RESTful design principles.
● Utilize appropriate HTTP methods, URLs, and status codes.
● Implement content negotiation and robust error handling.

5. Documentation:
● Provide a README file with:
● Setup and installation instructions.
● An overview of the API endpoints and their usage.

Evaluation Criteria:
● Functionality: All API endpoints must function as intended.
● Code Quality: Code should be clean, well-organized, and maintainable.
● Database Design: Effective database schema with proper relationships and indexing.
● Error Handling: Comprehensive and consistent error responses.
● Documentation: Documentation should be clear, detailed, and easy to follow.

Submission:Candidate should submit following:

1. A GitHub repository link that includes all source code, database schema, and anyadditional documentation required.
2. A Postman collection or similar tool for testing the API endpoints.
3. Docker Compose file for running the application on a local machine.
4. Readme file for running the application.



APIs:

create : POST / list : GET => books/
update: PUT / get : GET/ delete : DELETE => books/<int:pk> 
adjustStock : POST ==> books/<int:pk>/stock Body{stock: int}

Data models:

Supplier: id (pk), name, contact
Books: id (pk) , name, s_id (fk), price, stock_quanity, images (optional)