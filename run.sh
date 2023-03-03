#! /bin/bash

EMAIL_FILE="email.txt"
EMAILER="emailsender"

PYTHON="/usr/local/bin/python"

SCRAPERS_DIR="scrapers"
SCRAPERS=("aldi" "pingodoce" "continente" "lidl")

# Check if there is a previous email file
if [ -f "$EMAIL_FILE" ]; 
  then 
    rm $EMAIL_FILE
fi

# Go into the scrapers directory
cd $SCRAPERS_DIR

# Run scrapers
echo "Running scrapers... ⏳"
for SCRAPER in "${SCRAPERS[@]}"; 
  do
    $PYTHON "$SCRAPER.py"
done
echo "Scrapers successfully ran ✅"

# Move email.txt file to the root directory
mv $EMAIL_FILE ../

# Go back to root
cd ..

# Send the email
$PYTHON "$EMAILER.py"



