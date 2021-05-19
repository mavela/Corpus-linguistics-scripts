cat $1 | cut -f 2 | perl -pe 's/ /\n/g' |  sort | uniq -ci | sort -rn
