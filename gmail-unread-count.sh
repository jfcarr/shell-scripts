#!/bin/bash
 
LASTGMAIL="$(curl -u johndoe:mypassword --silent 'https://mail.google.com/mail/feed/atom' | tr -d '\n' | awk -F '<entry>' '{for (i=2; i<=NF; i++) {print $i}}' | sed -n 's/<title>\(.*\)<\/title.*name>\(.*\)<\/name>.*/\2 - \1/p' | wc -l)"
 
if [ $LASTGMAIL -ne 0 ]
then
	echo "$LASTGMAIL : johndoe@gmail.com"
fi
