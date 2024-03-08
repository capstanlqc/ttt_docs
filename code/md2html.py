#!/usr/bin/env python3

import os, sys
import markdown
from rich import print
import re
import argparse

# initialize arg parser with a description
text = "Convert Markdown document to HTML"
parser = argparse.ArgumentParser(description=text)
parser.add_argument("-V", "--version", help="show program version", action="store_true")
parser.add_argument("-i", "--input", help="path to input markdown file')")
parser.add_argument("-o", "--output", help="path to output html file')")

args = parser.parse_args()
version_text = "md2html 1.0"
if args.version:
    print(version_text)
    sys.exit()

if args.input and args.output:
    input_fpath = args.input.strip()
    output_fpath = args.output.strip()
else:
    print("One or both of the two required arguments is missing. Run this script with `--help` for details.")
    sys.exit()

def markdown_to_html_with_preserved_html(markdown_text):
    md = markdown.Markdown(extensions=['markdown.extensions.tables'])
    return md.convert(markdown_text)

def cleanup(md):
    return re.sub("(?s)^---[\s\S]+?---\n", "", md)

def add_html_barebones(html):
    return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Document</title>
        <link rel="stylesheet" href="github-markdown.css">
        <style>
            .markdown-body {{
                box-sizing: border-box;
                min-width: 200px;
                max-width: 980px;
                margin: 0 auto;
                padding: 45px;
            }}
        
            @media (max-width: 767px) {{
                .markdown-body {{
                    padding: 15px;
                }}
            }}
        </style>
    </head>
    <body class="markdown-body">
    {html}
    </body>
    </html>
    """

with open(input_fpath, 'r') as f:
    md = f.read()

# html = markdown.markdown(cleanup(md))
html = markdown_to_html_with_preserved_html(cleanup(md))
final_html = add_html_barebones(html)

with open(output_fpath, 'w') as f:
    f.write(final_html)