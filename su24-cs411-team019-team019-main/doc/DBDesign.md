# Database Design

## Diagram 

![Database Design Diagram](/img/DBDesignDiagram.png)

## Attributes
Attributes are not null and not unique unless mentioned otherwise.
- Book
    - bookId: the unique book ID
    - title: the book title of the book
        - may be used in the trivia
    - series: name of book series
        - may be used in trivia
    - author: the book author
        - may be used in trivia
        - may be the same for multiple books
    - rating: the book rating
    - description: the book description
        - may be used in trivia
    - language: the book language
    - isbn: the unique International Standard Book Number of the book
    - genres: the categories of the book
        - may be used in trivia
    - characters: the primary characters featured in the book
        - may be used in trivia
    - bookFormat: the format (physical or digital) in which the book is available
    - edition: the edition of the book
    - pages: the total number of pages in the book 
    - publisher: the publisher of the book.
    - publishDate: the date the specific edition of the book was published
    - firstPublishDate: the date the book was first published
    - awards: the book's awards
        - may be used in trivia
    - numRatings: the total number of ratings of the book
    - ratingsByStars: the distribution of ratings of the book
    - likedPercent: the percentage of readers who liked the book
    - setting: the setting of the book
    - coverImg: the cover image of the book 
        - will be used in book page
    - bbeScore: the Book Binge Experience score of the book
    - bbeVotes: the number ratings contributing to the BBE score of the book
    - price: the cost of purchasing the book
        - may be used in a purhasing system
- Stock
    - bookId: the same bookId used in Book
    - quantity (Stock): the available copies of the book
- User
    - username: the unique identifier of the user
    - password: the password of the user
    - score: the user's trivia score
- Transaction
    - bookId: the book involved in the transaction
    - username: the user involved in the transaction
    - transactionDate: the date and time when the transaction occurred
    - quantity (Transaction): the number of copies of the book involved in the transaction
    - type: the type of transaction
- Reservation
    - bookId: the book involved in the reservation
    - username: the user involved in the reservation
    - reservationDate: the date and time when the reservation was placed
    - quantity (Reservation): the number of copies of the book involved in the reservation
- Post
    - postId: the unique identifier of the post
    - bookId: the potentially null book related to the post
    - username: the user that created the post
    - postDate: the date and time when the post was created
    - post: the content of the post


## Entities and Relationships

The entities in our model are Book, Post, Transaction, Reservation, Stock, and User. As a library, it makes sense to have a book entity to contain all general book information and to be referenced by other entities. Furthermore, it is logical to have a user entity since we need users to be able to login, make posts, and borrow/return books. Since we intend for users to be able to make book-related posts, we include a post entity to store all posts. Since users can make multiple posts, there is a one-to-many relationship between the user entity and the post entity. A transaction entity is also essential since we need to be able to store all transactions that occur in our library. Since every transaction is done by a single user and books can be transacted by multiple people, there is a one-to-many relationship between the book entity and the transaction entity. For the same reason, there is a one-to-many relationship between the user entity and the transaction entity. In addition, to a transaction entity, there is a reservation entity that has user reservation records. We choose to separate the transaction entity from the reservation entity (which has a similar purpose, except for reserving) since we intend for it to act as a separate system. On top of that, we want the reservation entity to be less binding for our library system and allow for the removal of a reservation without any problems. The reservation entity has the same relationships as the transaction entity. We have also chosen to create a stock entity in order to capture the current library stock of every book. This exists as a separate entity from the book entity since the book entity is meant to encapsulate general information about a book, irrespective of our library. As a result, there is a one-to-one relationship between the book entity and the stock entity.

## Normalization and Schema

<ins>Functional Dependencies</ins>
*  bookId -> bookId, title, series, author, rating, description, language, isbn, genres, characters, bookFormat, edition, pages, publisher, publishDate, firstPublishDate, awards, numRatings, ratingsByStars, likedPercent, setting, coverImg, bbeScore, bbeVotes, price, quantity (Stock)
* username -> username, password, score
* bookId, username, date -> bookId, username, date, quantity (Transaction), type, quantity (Reservation)
* postId -> postId, bookId, username, date, post

<ins>Key</ins>
* {user, date, postId}

<ins>Schema</ins>
* Book(bookId, title, series, author, rating, description, language, isbn, genres, characters, bookFormat, edition, pages, publisher, publishDate, firstPublishDate, awards, numRatings, ratingsByStars, likedPercent, setting, coverImg, bbeScore, bbeVotes, price)
* Stock(bookId, quantity)
* User(username, password, score)
* Transaction(bookId, username, date, quantity, type)
* Reservation(bookId, user, date, quantity)
* Post(postId, bookId, user, date, post)


The above schema is in BCNF: for each relation given above, all applicable functional dependencies have the left hand side as a superkey of the relation. For Book, only the first functional dependency is applicable. The first dependency has bookId on the left hand side, and bookId is a key for the Book relation. So, Book is in BCNF. For Stock, only the first functional dependency is applicable. The first dependency has bookId on the left hand side, and bookId is a key for the Stock relation. So, Stock is in BCNF. For User, only the second functional dependency is applicable. The second dependency has username on the left hand side, and username is a key for the User relation. So, User is in BCNF. For Transaction, only the third functional dependency is applicable. The third dependency has bookId, username, and date on the left hand side, and those three form a key for the Transaction relation. So, Transaction is in BCNF. For Reservation, only the third functional dependency is applicable. The third dependency has bookId, username, and date on the left hand side, and those three form a key for the Reservation relation. So, Reservation is in BCNF. For Post, only the fourth functional dependency is applicable. The fourth dependency has postId on the left hand side, and postId is a key for the Post relation. So, Post is in BCNF. Since all relations are in BCNF, the schema is in BCNF.

## Logical Design

<ins>Schema</ins>
* Book(bookId:INT UNSIGNED PK, title:VARCHAR(256), series:VARCHAR(256), author:VARCHAR(256), rating:REAL UNSIGNED, description:TEXT, language:VARCHAR(256), isbn:BIGINT UNSIGNED, genres:VARCHAR(256), characters:TEXT, bookFormat:VARCHAR(256), edition:VARCHAR(256), pages:INT UNSIGNED, publisher:VARCHAR(256), publishDate:DATE, firstPublishDate:DATE, awards:TEXT, numRatings:INT UNSIGNED, ratingsByStars:VARCHAR(256), likedPercent:REAL, setting:TEXT, coverImg:VARCHAR(256), bbeScore:INT, bbeVotes:INT, price:REAL UNSIGNED)
* Stock(bookId:INT UNSIGNED PK FK to Book.bookId, quantity:INT UNSIGNED)
* User(username:VARCHAR(32) PK, password:VARCHAR(32), score:INT)
* Transaction(bookId:INT UNSIGNED PK FK to Book.bookId, username:VARCHAR(32) PK FK to User.username, transactionDate:DATE PK, quantity:INT UNSIGNED, type:VARCHAR(32))
* Reservation(bookId:INT UNSIGNED PK FK to Book.bookId, username:VARCHAR(32) PK FK to User.username, reservationDate:DATE PK, quantity:INT UNSIGNED)
* Post(postId:INT PK, user:VARCHAR(32) FK to User.username, postDate:DATE, post:TEXT)
