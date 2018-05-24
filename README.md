# comicScraper
A program that allows you to download a comic to your directory for offline viewing. Using python and a collection of modules (*ie. selenium, beautiful soup 4, etc.*), this program will navigate to the url containing the comic that you would like to read and download the pages to a PDF file for you to read later on.

*Note: this project is not yet complete and is still under development.*
*If you are running this program prior to its completion, expect bugs and unfinished portions.*
*Also, you may need to install all of the modules by yourself before testing it (ie. selenium, beautiful soup 4, etc.)...*
*Check all of the module imports at the beginning and check error messages to learn what installs you need to make.*

### As of now, May 24, 2018, the following are possible:
- opening the website (using selenium) and waiting for it to load
- obtaining user search query, entering it into the search form, and navigating to the results
- parse html (beautiful soup 4) for all comic book titles, and output all results from 
  search to user *at the moment, it only works for multi-result searches*
- let user choose a title from the list created above by entering the number to which it corresponds
- generate the proper url from the title
- open the website again, this time with the url obtained from user choosing title from list

### To do:
- deal with exact input (if user query exactly matches a title and doesn't need to have the list generated)
- deal with no results
- navigating to the actual webpage with all of the comic's pages
- sorting out how to parse webpage for all urls of PNG/jpg files
- setting up wget to fetch the content and a PDF compiler to add all downloaded images to PDF file
