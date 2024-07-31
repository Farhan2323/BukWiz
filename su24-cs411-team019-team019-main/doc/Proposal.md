# Project Proposal

## Title 

BukWiz

## Summary

BukWiz is a digital library that aims to make it easier to find and access books. The core functionality of our application is a search system that allows users to find books, a recommendation system, and a checkout system that allows users to reserve books in the library or join a reservation waitlist if the books are already loaned out. These features provide a fine-grained search method and a list of recommendations, allowing for users to quickly find books of interest. The integrated checkout system allows for fast and easy access to books. Other features include BukWiz posts and BukWiz trivia. These features allow users to discuss their thoughts with other patrons and provide a fun competition, both of which encourage interest in the library and strengthen the library’s community.

## Description

We plan to build BukWiz, an online library with a web application interface where users can search for and borrow books. As part of this project, we will create a website, small backend, and database. Our website and backend will be hosted from the same server and, depending on ease, the database will be on the same server or be part of a managed service.

BukWiz will tackle a few modern issues: With the plethora of books available, people struggle to find books that actually interest them. BukWiz will address this problem through its own book recommendation system. Additionally, BukWiz’s borrowing system will increase the accessibility of books and allow people to read books they could not have read otherwise. Lastly, BukWiz’s convenience will push users to read more books, hopefully combating the significant decline in reading overall.

## Creative Component

One interesting feature of BukWiz is the ability for users to freely post their opinions and thoughts about books they have read. In a way that is somewhat like Twitter, other users can then see recent posts and discover books they have never heard of and learn more about books that are popular right now. We plan to implement this feature by storing posts written by users and displaying recent posts to all users.

Another cool feature that we plan to include in BukWiz is the trivia component. This feature will allow users to guess books based on some features about them and rank users based on their ability to guess correctly. This feature will allow users to explore books they may like in a fun way. We plan to implement this feature by selecting portions of book information and displaying that to users, allowing them to pick from a selection of real books as their guess. We will keep track of user scores and increment their score when they make a correct guess.

## Usefulness 

BukWiz will be useful because it connects readers to books they are interested in and lets them freely share their opinion about books. From our app, users can search for books, post opinions about books, play a book-related trivia game, request to borrow books, and find books similar to other books. Through these features, BukWiz will encourage people to read more.

There are many library websites (i.e., the campus library) that offer some similar features. In particular, the ability to search for books and request to borrow books. However, BukWiz will offer a unique platform to share posts about books. Additionally, there will be an integrated trivia game that will encourage people to discover new books in a fun way. While somewhat similar features do exist in other websites like Twitter (posts), these websites are not book-focused at all and are not part of an easy to use book borrowing system.

## Realness

The [dataset](https://zenodo.org/records/4265096) we will use comes from the GoodReads Best Books Ever list. It contains 52,478 records covering 25 fields, and it is stored in a CSV format. The columns are bookId, title, series, author, rating, description, language, isbn, genres, characters, bookFormat, edition, pages, publisher, publishDate, firstPublishDate, awards, numRatings, ratingsByStars, likePercent, setting, coverImg, bbeScore, bbeVotes, and price.

The variables will be used to uniquely identify and comprehensively describe each of the books. Many of the variables, such as genres, rating, author, etc., will be used in the search functionality and recommendation system. Some of these will also be used for the trivia section. Since this dataset covers a large amount of information, we feel like we do not need a second data source. Instead, other systems of our application will require us to use many different tables.

## Functionality 

BukWiz offers a plethora of features. From the home page, users will be able to search for books by name or genre and access individual book pages. From the posts page, users will explore the other users’ thoughts on specific books and find out more about them. Users will also be able to create posts here. From the trivia page, users can read simple information about a book and guess the book’s name from a selection, earning points. Users with high points will be seen on the page. From an individual book page, users can see information about the book, including ratings and similar books, and request to borrow the book. From the login page, users can log in to their accounts.

### UI Mockup

![Home Page](/img/HomePage.jpg)
![Book Page](/img/BookPage.jpg)
![Login Page](/img/LoginPage.jpg)
![Create Account Page](/img/CreateAccountPage.jpg)
![Blog Page](/img/BlogPage.jpg)
![Trivia Page](/img/TriviaPage.jpg)

### Work Distribution

Anuj will primarily be working closely with the databases and creating a simple backend API in Flask to facilitate pulling necessary information for webpage functionality. Akul and Farhan will primarily be working closely on the webpages, using JavaScript to send API requests and manipulate responses to display dynamic content. Akul will mostly be working on the login page and the trivia page. Farhan will mostly be working on the home page, posts page, and the individual book page.
