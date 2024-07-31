# Project Proposal

## Please list out changes in the directions of your project if the final project is different from your original proposal (based on your stage 1 proposal submission).

The overall direction of our project is the same, with one major caveat. In the end, we chose to put less focus on providing a simple book recommendation system and made sure to implement the other features of our project like the trivia and book search. However, we do provide the user with information about the books they read and provide a book search system that can help them find similar books. We think that this change does not stray too far from one of our major goals for the project: to increase the accessibility of books and encourage people to read.

## Discuss what you think your application achieved or failed to achieve regarding its usefulness.

We believe that our application is able to achieve our goals of making books more accessible and encouraging people to read. We think that the trivia and posts pages are an important part of this. Unfortunately, the lack of a direct book recommendation system is certainly something that makes our project less useful than we initially intended. However, our stronger book search system hopefully helps offset this to a degree.

## Discuss if you changed the schema or source of the data for your application.

Throughout this project, we only made 2 changes to our schema: We needed to change certain column data types to ensure our dataset was able to fit in our tables. We also chose to rename our original Transaction table to Transactions to avoid any keyword confusion. Other than that, our schema and source has had no changes.

## Discuss what you change to your ER diagram and/or your table implementations. What are some differences between the original design and the final design? Why? What do you think is a more suitable design? 

While we did make some minor changes to our first ER diagram, it was only to correct for a few inaccuracies. Since making those changes during the previous stage, our design and implementation has not changed.

## Discuss what functionalities you added or removed. Why?

The main functionalities that we included are to search for books using various attributes, to reserve/return/checkout books, to read/write posts, to login, and to play trivia. The only original feature we did not include was a quick and direct book recommendation system. We decided not to include this feature for the sake of time and to help us reach our minimum viable product by focusing on other features. In addition to our original functionalities, we introduced a user page to allow users to get some information about the books they tend to read. This feature should help users find books that interest them through our book search.

## Explain how you think your advanced database programs complement your application.

The advanced queries used by our program help our application in a few ways. Mainly, it allows us to make advanced search queries for our users, hopefully providing a good search experience. In addition, it helps us provide users with information about authors and genres that seem to interest them. Lastly, it helps us make sure that users with reservations are given the reserved book once someone returns the book.

## Each team member should describe one technical challenge that the team encountered.  This should be sufficiently detailed such that another future team could use this as helpful advice if they were to start a similar project or where to maintain your project. 

- (Farhan) One technical challenge that I faced during development was figuring out how to properly connect the API endpoints to the web pages that I had worked on. To help with this challenge I used online documentation by W3School to better understand how API endpoints work and how to implement it into the code.
- (Akul) One issue we encountered was the requests being processed too slowly. In our trivia section, we needed to get four random books for each question. We first were using fetch without waiting, which caused issues as we tried to access data from a promise that had not yet been fulfilled. In order to resolve this, we had to await each request, but this caused an excessively long wait time to get trivia questions. We resolved this by rewriting our endpoint to take a number of random books rather than just returning one.
- (Anuj) The main technical challenges I faced were trying to connect to the database, figuring out peculiarities of MySQL, and debugging. It ended up being more difficult to connect to the database and send queries than I thought it would be. I ended up creating an API using Flask and PyMySQL. I definitely had to spend some time going through docs to understand these libraries and resolve some strange issues between these two libraries (ensure no threads and only 1 process). Another challenge I faced was finding online resources for different SQL queries that did not work for MySQL by default (COMMIT is default and should not be used as such.) Lastly, debugging problems ended up being pretty difficult as I had to debug server-side.

## Are there other things that changed comparing the final application with the original proposal?

Compared to our original proposal, the final application has only a few minor changes with respect to the UI. Our UI mockup does not accurately reflect our current interface. For instance, our mockup suggests an account creation feature that does not exist and does not include a user page that does exist.

## Describe future work that you think, other than the interface, that the application can improve on.

Other than some interface improvements, our application could definitely use a system to keep track of reservations and loaned out books. For a real library, this kind of system is essential. Another important thing that could be added is a direct book recommendation system as we originally intended to include. One last thing that could be improved is our book search feature to allow even more complex queries.

## Describe the final division of labor and how well you managed teamwork.

Farhan created the user, book, and home page using HTML and CSS. Then used JS to connect to API endpoints to pull information from the database. Akul created the trivia, login, post, and search pages using HTML and CSS, and also connected the pages to the API. Akul also debugged and helped resolve problems across our stack. Anuj made the API, created the SQL queries, and managed the servers. Overall, we managed teamwork fairly well.
