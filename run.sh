#! /bin/bash

EMAIL_FILE="email.txt"
EMAILER="emailsender"

SCRAPERS_DIR="scrapers"
SCRAPERS=("aldi" "pingodoce")

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
    python "$SCRAPER.py"
done
echo "Scrapers successfully ran ✅"

# Move email.txt file to the root directory
mv $EMAIL_FILE ../

# Go back to root
cd ..

# Send the email
python "$EMAILER.py"

