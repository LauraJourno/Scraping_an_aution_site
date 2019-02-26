# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("https://www.sdlauctions.co.uk/property-list/")
#print the HTML variable containing the webpage
#print(html)

# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
root.cssselect("li p a")
#
#Change "div[align='left']" to a different CSS selector to grab something else. 
#Looking on the site, I'm going to scrape through a series of tags to drill down information. I've asked it to find all a under p under li.
#In the inspector, this is seen like this: 
#<li>
# <p>
#   <a> 
#This will essentially scrape all data that match this pattern. 
#Then if I wanted to look only at the Birmingham datasets, I would need to filter this further.
print(root)


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
