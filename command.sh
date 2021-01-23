#!/bin/bash

function amazon()   {
    # Nice formatting
    clear
    cwd=$(pwd)
    printf '\e[8;40;150t'

    #activate Virtual Environment
    source "$AMWSDirectory/python-code/AmazonWSMA-venv/Scripts/activate" # differ for mac
    echo "AmazonWSMA-venv activate"
    cd "$AMWSDirectory/python-code"
    
    #Executing the python code
    python url_gen.py "$1 $2 $3 $4 $5 $6 $7 $8 $9" # differ for mac
    python searchresults.py # differ for mac
    echo -e "\e[1;31m===================================================================AMAZON_RESULTS===================================================================\e[0m"
    python -W ignore format.py "$1 $2 $3 $4 $5 $6 $7 $8 $9" # differ for mac
    echo -e "\e[1;31m====================================================================================================================================================\e[0m"
    
    #Clean up 
    cd "$cwd"
    deactivate AmazonWSMA-venv
    pause
    clear
    printf '\e[8;34;100t'
    rl

} # amazon()

#Helpful for visuals
function pause(){
 read -s -n 1 -p "Press any key to continue . . ."
 echo ""
} # pause ()