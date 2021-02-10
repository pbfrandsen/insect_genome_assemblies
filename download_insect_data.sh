for i in `cat insect_orders.txt`; do ./datasets summary genome taxon $i > $i.json; done
