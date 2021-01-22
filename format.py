#   MAIN OUTPUT FILE FOR AMAZON WEBSCRAPER
#   Vanya Kootchin, 01/20/2021
#   
#   Def:
#   Takes a search query and outputs the best results via terminal
#   w/ hyperlinks
#

#PACKAGES
import json
from operator import itemgetter
import re
import sys
from fuzzywuzzy import fuzz
from multsort import multikeysort

#DEBUG
db = 0

#Stylish ness
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Getting user input for query 
userInput = sys.argv[1]

#Opening the File
with open('resources/search_results_output.json') as f:
  json_array = json.load(f)

#PARSE RESULTS
for item in json_array:
    if item == "end":
        del item
        break
    #URL MANIPULATION               - needed for proper hyperlink
    item["url"] = "www.amazon.ca" + item["url"]

    #RATING MANIPULATION            - float
    if item["rating"] == None:
        item["rating"] = "0.0"
    item["rating"] = float(item["rating"][0:3])

    #REVIEWS MANIPULATION           - int
    if item["reviews"] == None:
        item["reviews"] = "0"
    item["reviews"] = item["reviews"].replace(",", "")
    item["reviews"] = int(item["reviews"])

    #PRICE MANIPULATION             - float
    if item["price"] == None:
        item["price"] = "0.00"
    item["price"] =float(re.search(r'\d+\.\d+', item["price"]).group(0))

    #STARBUCK MANIPULATION          - float
    if item["price"] == 0:
        starBuck = -1
    else:
        # This if the formula for determining top possible result
        starBuck = ((4.7* item["rating"]) - (0.25 * item["price"]) + (0.0025 * item["reviews"])) #Rating evaluation
        # 
        #   Could implement a starbuck * (item["flagged"]) evaluation for disregard all missed words, but I think that would lead to very few results
        #
    item["starBuck"] = starBuck
    
    #ACCURACY TO QUERY
    # Need to initialize flagged for every object
    item["flag"] = False
    #Calculate fuzz ratio
    Ratio = fuzz.ratio(item["title"].lower(), userInput.lower())
    item["fuzzRatio"] = Ratio   # this is the accuracy that the title has to the search query

# _ SORTING _

json_array = multikeysort(json_array, ["fuzzRatio", "starBuck"])

# Will use a "flagged" True/False (key/value) pair to determine if the search result
# is close to the word searched

#json_array.sort(key=itemgetter("starBuck"), reverse=True) # sorting based on starBuck ( highest -> lowest )

# _         _

# Formatting the logs file and opening it
file = open("misc/most_recent_lookup.txt", "a")
file.write("\n-------------------------------" + "\n")

#Skip function needed for nice printing output
skip = 1
i = 0
amount = 0
# MAIN
if not db:

    # Need a list to put the duplicate checks in, hopefully range of 25 is sufficient
    dc_list = [""] * 25
    # This is the duplicate checker
    # Can make more efficient
    # Currently O(n^2)
    for item in json_array:
        for i in range(0,25):
            if dc_list[i] == "":
                dc_list[i] = item["title"]
                break
        item["appearances"] = 0
        for i in range(0,25):
            if dc_list[i] == item["title"]:
                item["appearances"] = item["appearances"] + 1
    # Duplicate checker end

    amount = 1

    for item in json_array:
        # Want the top five entries 
        if amount > 5: break
        #Need to check for repeats
        if item["appearances"] < 2 and item["starBuck"] > 1.00:
            #For nice 
            if skip != 1:
                print("-------------------------------\n")
            else:
                skip = 0

            #Main output
            print(bcolors.HEADER,bcolors.BOLD,item["title"][0:95],bcolors.ENDC )
            print(bcolors.OKCYAN," CDN$","{:.2f}".format(item["price"]),bcolors.ENDC )
            print("\n",bcolors.OKBLUE,item["url"],bcolors.ENDC )

            #Log writing
            file.write("Name: " + item["title"] + "\n")
            file.write("Price: " + "{:.2f}".format(item["price"]) + "\n")
            file.write("URL: " + item["url"] + "\n")
            file.write("\n")


            amount = amount + 1
 
# DEBUG

# need to increase the range of the list
if db:

    dc_list = [""] * 25
    print(len(dc_list))

    for item in json_array:
        for i in range(0,25):
            if dc_list[i] == "":
                dc_list[i] = item["title"]
                break
        item["appearances"] = 0
        for i in range(0,25):
            if dc_list[i] == item["title"]:
                item["appearances"] = item["appearances"] + 1


    amount = 0

    for item in json_array:
        if amount >= 50: break
        if amount == 0: print(bcolors.HEADER,bcolors.BOLD,"      === TOP FIVE === ",bcolors.ENDC ) # printing top five
        if amount == 5: print(bcolors.HEADER,bcolors.BOLD,"      === ======== === ",bcolors.ENDC ) # end of top five


        if item["appearances"] < 2 and item["starBuck"] > 1.00:
            print("{:>30}".format(item["title"][0:25]),
             " | " "{:>6.2f}".format(item["price"]), " | ",
              "{:>6.2f}".format(item["starBuck"]), " | ",
               "AMOUNT: ", "{:>6.2f}".format(amount), " | ",
                "Appearances = ",item["appearances"], " | ",
                "fuzz: ", "{:>6.2f}".format(item["fuzzRatio"]))

            amount = amount + 1

#END OF FILE
file.close()
exit()

#End of program execution