#Needed for cmd line args
import sys

#INIT
base_url = "https://www.amazon.ca/s?k="
input = sys.argv
search=input[1]

#LOGS
prefile = open("misc/most_recent_lookup.txt", "w")
prefile.write("Query = " + search.upper())
prefile.close()

#Cleaning String - Amazon needs special query
search = search.replace(" ","+")
search = search.replace("++","")
                                 # Ex., oven mitts => oven+mitts
                                 # Needed for proper search Query in HTTPS

#Setting up the URLs
file = open("resources/search_results_urls.txt", "w")
for i in range(1, 6):
    #Writting the new urls to be used
    file.write(base_url + search + "&page=" + str(i)+"\n")
    # For the purposes of this bot
    # we will only parse 5 pages, also keeps
    # amazon from flagging this IP as bot
file.close()
exit()