# MemoryLn ☆

MemoryLn is a translation memory and glossary lookup utility. It allows you to find expressions and patterns in segments coming from completed translation projects as well as in term entries glossaries. To run a search, simply enter your search expression(s) and select the appropriate parameters (advanced search options, container, etc.).

## Access

Login is handled by VegaSuite credentials. It's up to the PM who has access -- if a PM wants to give access to someone (linguist or client) who doesn't have it, they must request it. 

## Main purpose 

MemoryLn is particularly useful in projects where linguists or users do not work on a project in a CAT that already includes the TMs and glossaries they need. In those cases, they can find translations in MemoryLn through their browser. 

## Usage

You can use a number of items to restrict results in MemoryLn.

###  Search parameters

| Parameter     | Description | 
|:--------------|:---------------------------|
| Metadata      | You can select a type of metadata and its value to restrict your results. You will obtain only results that are associated to that metadata. |
| Languages     | Please select the combination of the two languages where you want to find your expression. Bear in mind that your search will only be run in a language pair. |
| Search expression(s) | Enter an expression in the source language to see its context in the source language and/or how it was translated in the target language. Enter an expression in the target language to see its context in the target language and/or what was the source expression from which it was translated. Enter a pair of expressions in both the source and the target language to see whether that particular translation exists for that particular source expression, and/or their context in both languages. |
| Container     | You can restrict your results by selecting the container from which they must come. A container is a organization or a project. |
| Content type | You can choose whether you run your search in glossaries, in the translation memories, or in both. |
| Domain | You can choose from which domain you want to have results (cognitive materials, questionnaires, etc.) |

### Search options

| Option        | Description | 
|:--------------|:---------------------------|
| Wildcard | Select this option if you want to use **wildcards** in your search, such as  `?` to match any character and `*` to match any string. |
| Loose words | Select this option if you want to match **words appearing separately** (e.g. `+main +task`) in the text, that is, as independent keywords to be found in different positions in the segment. By default, the search query is used as a **fixed exact phrase**, that is, as a sequence in the exact same order in which you have entered it (e.g. `main task`). |
| Entire words | Select this option if you want your search expression to match **entire words** (e.g. so that `to` matches "to" but not "to" in "towards") or leave it unselected it you want partial matches of longer words to be included in the results (e.g. so that `to` matches both "to" and "to" in "towards"). If you select this option, you will get results that include your search expression where it starts and ends with a space or a punctuation sign. |
| Case sensitive | Select this option if you want your search expression to be **case sensitive**, that is, to run with the same exact case used in the search query e.g. CASE ≠ case ≠ cAsE. By default, case is ignored. |
| Negation | Select this option if you want to find segments that do not contain the search expression, e.g. if you want to find translations in French for "student" that do not contain "élève", you can search for "élève" in the target language and select the negate option. |
| Full segment | If selected, the **entire segment** (from beginning to end) needs to match the search query. By default, partial matches (part of the segment) are included in the results. For example, if you select this option and search for "early childhood", your results will include the segment `Early childhood` but not `Early childhood education`. |
| Regular expression | Select this option if your search pattern is a **regular expression** (regex). Regular expressions are patterns that are interpreted in a special way (not literally) to match different strings of text that have in common the properties described by the regular expression. You need to follow the PCRE syntax. More info about regular expressions [here](http://www.regular-expressions.info/) and here is a [playground](http://leaverou.github.io/regexplained/). |

## Feedback and support

Any feedback would be greatly appreciated, feel free to [contact us](mailto:manuel.souto@capstan.be). Also, should you still have any difficulties or questions, do not hesitate to contact us and we will do our best to help you.

