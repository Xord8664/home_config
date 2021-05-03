#!/bin/env bash

if [ -f /tmp/chk_updates.pid ] ; then
  echo "pid file already exists"
  exit 1
fi

echo $$ > /tmp/chk_updates.pid

updates="`checkupdates`"
to_grep=("linux" "chromium")
greps=''
total_updates=0

if [[ ! -z "$updates" ]] ; then
  total_updates=`echo "$updates" | wc -l`
fi
  
for i in ${to_grep[@]} ; do
  declare $i=`echo "$updates" | grep $i | wc -l`
  greps="$i:${!i} $greps"
done

echo "${greps}total:$total_updates"
rm -f /tmp/chk_updates.pid

#echo "$updates"
