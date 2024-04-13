#!/bin/bash -e

SCRIPTNAME=$0
die() {
	echo "$SCRIPTNAME: $1"
	exit 1
}

TEAM=$1

case $TEAM in
"content")
	FOLDERS="content templates quartz"
	;;
*)
	die "please specify a valid team"
	;;
esac

echo "Running 'git sparse-checkout init --cone'"
git sparse-checkout init --cone

echo "Running 'git sparse-checkout set $FOLDERS'"
git sparse-checkout set $FOLDERS
