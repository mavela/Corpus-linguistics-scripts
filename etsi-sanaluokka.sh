cat $1 |
    egrep $2 |
    cut -f 3 |
    sort | uniq -ci | sort -rn

