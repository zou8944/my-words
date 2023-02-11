#!/usr/bin/env bash

function iterateDir() {
  for year in $(ls -t ./posts); do
    yearDir=./posts/$year
    if [ -d $yearDir ]; then
      echo "## $year"
      echo
      iteratePost $yearDir
      echo
    fi
  done
}

function iteratePost() {
  yearDir=$1
  for post in $(ls -t $yearDir); do
    if [ -d $yearDir ]; then
      title=${post%.*}
      echo "- [$title]($yearDir/$post)"
    fi
  done
}

oldIFS=$IFS
IFS=$'\n'
iterateDir
IFS=$oldIFS