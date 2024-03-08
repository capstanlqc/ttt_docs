#!/usr/bin/env bash

# activate venv
# change directory to the root folder of the project

for fpath in $(grep -l -R "share: true" docs | grep -P "\.md$")
do
    echo "Will convert file $fpath"
    fname="$(basename -- $fpath .md)"
    output_fpath="$(pwd)/docs/share/$fname.html"
    python code/md2html.py -i $fpath -o $output_fpath
    echo "HTML file created: $output_fpath"
done