# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html=scraperwiki.scrape("https://www.sdlauctions.co.uk/property-list/")
#print the HTML variable containing the webpage
#print(html)

# # Find something on the page using css selectors
root=lxml.html.fromstring(html)
root.cssselect("li p a")
#
#Change "div[align='left']" to a different CSS selector to grab something else. 
#Looking on the site, I'm going to scrape through a series of tags to drill down information. 
#I've asked it to find all a under p under li.
#In the inspector, this is seen like this: 
#<li>
# <p>
#   <a> 
#This will essentially scrape all data that match this pattern. 
#Then if I wanted to look only at the Birmingham datasets, I would need to filter this further.
#So this root.cssselect runs fine, but we haven't asked it to store teh data or print it. So now we need to do this.
#First, let's store those matches.
matchedlinks=root.cssselect("li p a")
#So now we've stored it, we want to print it.
#print(matchedlinks)
#So now this has run successfully, it doesn't make much sense. Now we are going to convert it to something more readable.

#Loop through the items in matchedlinks, calling each one li
for li in matchedlinks:
  #Store the text contents of li in a new variable listtext
  listtext = li.text_content()
  #print that
  print(listtext)
  
 #Now we need to save our scraper by creating a dictionary.
#create a dictionary called record
record = {}
#Loop through the items in matchedlinks, calling each one li
for li in matchedlinks[0:300]:
  #Store the text contents of li in a new variable listtext
  listtext = li.text_content()
  #print that
  print(listtext)
  #store it in the 'record' dictionary under the key 'address'
  record['address'] = listtext
  #save the record to the datastore with 'address' as the unique key
  scraperwiki.sqlite.save(['address'],record)

print(li.text_content().encode('utf-8'))
#The ['address'] bit in record['address'] = listtext creates a key in that empty dictionary (think of it as a column header). Whatever listtext is, is then stored against that key (think of it as being put in that column).
#The function .text_content() converts that confusing code <Element a at 0x7fd8d69ed310> into something more readable and useful: the text contents of the tag that was grabbed.

# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
