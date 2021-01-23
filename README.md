# Amazon Web Scraper
A bash command line program that searches Amazon and displays the top five results based on a formula for best result and similarity to search query.

### [Download for Windows](https://github.com/18vmck/AmazonWebScraper/raw/main/AmazonWebScraper(Windows).zip)
### [Download for Mac OS](https://github.com/18vmck/AmazonWebScraper/raw/main/AmazonWebScraper(Mac).zip)


This is to be used with a standard bash terminal, either GitBash on Windows or Terminal on mac
    - The code is executed using a personalized bash function 'amazon'
## Installation:
In the uncompressed zip folder (put it where you want installing to be), the INSTALL.sh script is run using the following bash commands:
                
                bash@AmazonWebScraper(OS):
                   
                    chmod u+x INSTALL.sh   
                    ./INSTALL.sh
                  
This will add the directory as a variable and the *.command.sh* source file to your .bashrc script, this can be found in the *AmazonWebScraper(OS)/python-code/resources* directory

**If it doesn't work immediately, restart bash shell, needs to resource .bashrc**

Program depends on:
    - Having bash
        - Currently existing .bashrc file / .bash_profile file that sources .bashrc
    - Having Python 3.8 upwards
 


## Sample Output:
![alt text](https://github.com/18vmck//AmazonWebScraper-MoreAccurate/blob/main/SampleOutput.jpg?raw=true)
