#!/bin/bash

if (($# < 1)); then
	echo "It necessary one argument"
	exit;
fi

for filename in $1/*.py; do
	yapf -i $filename && autoflake -i $filename;
done
