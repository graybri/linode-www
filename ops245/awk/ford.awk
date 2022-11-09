BEGIN {totalvalue=0}
$1 ~ /ford/ {totalvalue+=$5; print $1, $2, $5}
END {print "The total value of the fords is:", totalvalue}

