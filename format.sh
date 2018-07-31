#!/bin/bash

if (($# < 1)); then
	echo "It necessary one argument"
	exit;
fi


if [[ -d "$1" ]]; then
	for filename in $1/*.py; do
		yapf -i $filename && autoflake -i $filename;
	done
elif  [[ -f "$1" ]]; then
	yapf -i "$1" && autoflake -i "$1";
else
	echo "It is not correct input"
	exit 1
fi



