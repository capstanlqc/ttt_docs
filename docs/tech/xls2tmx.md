---
share: true
where: 
---

# Convert Excel to TMX
<!--- [task 20.3000] -->

## Summary: 

* Input: a spreadsheet containing source text in one column and at least one more column with the translation. 
* Expected output: a TMX file for each language pair

## Approaches

We have different ways to conduct this task: 

### Bilingual input

If the spreadsheet contains one language pair, then it's okay to do in [TMX Editor](https://capstanlqc.github.io/ttt_docs/tools/aux/tmx-editor/):

- Go to **File** > **Convert Excel file to TMX**

### Multilingual input

If the spreadsheet contains many language pairs, then it's more efficient to use [this script](https://github.com/capstanlqc/convert-multilingual-xlsx2tmx)

In this case, attention must be paid to the configuration (either `config.json` or the first worksheet, called `config`, in the spreadsheet -- example provided [here](https://github.com/capstanlqc/convert-multilingual-xlsx2tmx/blob/master/data/multilingual_tmwb_template.xlsx).

