BEGIN {fordtotalvalue=0; chevytotalvalue=0}
$1 ~ /ford/ {fordtotalvalue+=$5; print $1, $2, $5}
$1 ~ /chevy/ {chevytotalvalue+=$5; print $1, $2, $5}
END {print "The total value of the fords is:", fordtotalvalue;
    print "The total value of the chevys is:", chevytotalvalue}

