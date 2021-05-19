cat $1 | egrep "^[0-9]" | egrep -v "PUNCT|SYM|NUM" | cut -f 3 | sort | uniq -ci | sort -rn 
