# Web Application
The following part explains the implementation of the search engine. The aim is to allow fast and efficient search of terms in the whole range of speeches of the Parliament.

The web application supports:

1. A search bar for searching terms in the speeches.
2. A results page based on the query provided by the user, which displays the top-100 results along with basic information (speaker, date, party, etc.) for each result.
3. A detail page to display full speeches after user selection from within the results page (2).
4. Static display page for the results of important keywords.
5. **Dynamic** page for displaying the results of the top-k speaker pairs with the highest similarity.
6. Page **dynamic** display of the LSI results.
7. Static display page of the Named-Entity Recognition results.

The front-end implementation is located in the web-app folder. Specifically, the templates folder contains the .html files for displaying the appropriate pages. At the same time, the static folder contains .css files for styling the above html files as well as some basic JavaScript functions that implement some system behaviors. Finally, the folder also contains the necessary images used in the application.

The single JavaScript file contains two functions that implement:

1. Submitting a keywords search using enter rather than clicking on the search icon.
2. The correct routing for submitting the search by clicking on the search icon.

The static/images folder contains images for our application's logo, Aristotle University, and the search icon (magnifying glass). The application logo is custom-made by us.

The main component of the search engine implementation is the app.py script. The implementation of the web application has been done using the Flask library. In app.py main "serves" our application to the address localhost:5000. At the same time there are functions that implement the routing of the application and allow it to work properly.

Specifically:

1. **homepage**: the home page of the application. It contains a search bar for searching terms and a dropdown menu for viewing the results of the remaining queries of the task.
2. **query_results**: the results page after the user has searched for some keywords. The function calls the backend's perform_query and returns a list of search results. It then passes the list to the html file for display. If the keywords provided by the user are all stopwords or do not exist in the speeches then an appropriate error page is displayed, prompting the user to modify their query.
3. **show_speech**: the full show page of a particular speech. The function accepts a speech ID in its URL. The function calls the backend's fetch_speech and returns the speech data. It then passes the speech to the html file for display.
4. **keywords**: this page displays the results of the 2nd query. Specifically, it reads the generated (from the 2nd query) JSON file and statically displays it in the html file.
5. **similarities**: This page displays the results of the 3rd question. The page displays by default the first 5 pairs. If the user specifies a particular k from within a form then it calls fetch_top_k with the given k and returns the results of the function back to the html file for display.
6. **lsi**: This page displays the results of the 4th query. By default the page reads from memory the file with the results of 100 topics and displays them. If the user specifies a certain number of subjects through a form then it reads the appropriate file again and returns it to the html file for display.
7. **ner:** The page displays the results of the 6th query. It reads the result file from memory and returns it to the html file for display.