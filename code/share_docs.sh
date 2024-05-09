#!/usr/bin/env bash

# activate venv
# change directory to the root folder of the project

# share_dir="share-gh-plain-md"
share_dir="share"

for fpath in $(grep -l -R "share: true" docs | grep -P "\.md$")
do
    echo "Will convert file $fpath"
    fname="$(basename -- $fpath .md)"
    output_fpath="$(pwd)/docs/$share_dir/$fname.html"
    python code/md2html.py -i $fpath -o $output_fpath
    echo "HTML file created: $output_fpath"

    echo "Publish the document by adding the following code in the target platform:"
    echo "<iframe src="https://capstanlqc.github.io/ttt_docs/$share_dir/$fname.html" allowfullscreen="true" width="100%" height="100%" frameborder="0"></iframe>"

    echo "---"
done

# todo:
# script: look for files that say share: true (done)
# script: for the md file, find the html endpoint in site
# script: copy that one to the equivalent location under docs/share
# e.g. for docs/tools/omegat/recency.md:
# cp ./site/tools/omegat/recency/index.html docs/share/tools/omegat/recency/index.html
# manually: copy the iframe code to the KS article
# manually: copy the URL of the KS article to the md file for tracking purposes