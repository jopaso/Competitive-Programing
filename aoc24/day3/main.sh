#!/bin/bash


function remove_dont(){
	file=$1
	algo=$(cat $file | tr -d "\n" | sed -E "s/don't\(\)/ABORT/g" | sed -E "s/do\(\)/START\r\n/g" | sed -E "s/ABORT.*?START//g")
	echo $algo
}


valid_text=$(remove_dont $1)
#echo $valid_text

muls=$(echo ${valid_text} | grep -Eo 'mul\([0-9]{1,3},[0-9]{1,3}\)')

suma=0

for num in $muls; do
	vals=$(echo $num | sed -E 's/mul\(([0-9]{1,3}),([0-9]{1,3})\)/\1 \2/')
	#echo $vals

	num1=$(echo "$vals" | cut -d' ' -f1)
    	num2=$(echo "$vals" | cut -d' ' -f2)

	#echo "Suma: ${num1} + ${num2} "
	suma=$(($suma + $((${num1} * ${num2}))))
done

echo -e "Suma total: $suma"
