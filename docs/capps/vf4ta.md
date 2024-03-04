# VF4TA ☆

## How to run Veryfire for TA 

Submit your input file to [the latest version of Veryfire](https://capps.capstan.be/veryfire_DEV.php). The file you submit must meet certain requirements: 

* It must be an Excel file. 
* The source text must be in the first column of the first worksheet, starting after the third row. 
* The file name must contain the word `_translability_`. 

You can use the following [test file](https://capps.capstan.be/Files/FAMA_usa-ENG_translatability_TestFile_TA.xlsx) to test Veryfire for TA, or as a template where to paste your source text. 

## How Veryfire for TA works 

Veryfire for TA is triggered when files for TA are submitted: Veryfire looks for the word `_translability_` in the input file: if it's found, TA rules rather than QA checks are applied. So all existing rules are applied, regardless of the project. 

Some checks are generic: `FindSemanticCorrespondence`, `Semiidenticalness`, etc. Other checks are rule-based, and rules can be based on previous corrections or on style guides (see for example a [ruleset based on CIPFA's English style guide](https://capps.capstan.be/Rules/RuleSet_Translatability_FAMA_usa-ENG_20160530.csv)). 

## How to provide content for creating rules

Veryfire reads rules that must have a certain structure:

| Col. |       Title      |                                                Description                                               |
|:----|:----------------|:--------------------------------------------------------------------------------------------------------|
| A    | Active           | active if empty, inactive if "#"                                                                         |
| B    | Expression       | the pattern you want to match                                                                            |
| C    | Category         | the category that VF4TA must choose                                                                      |
| D    | CheckType        | Translatability (always)                                                                                 |
| F-J  | Options          | they can be confusing for you and the PMs, so we can go into them later (not so important right now)     |
| K    | Comments         | The comment you want the reader of the TA report to see (explaining why the expression has been flagged) |
| L    | Suggestion       | Alternative wording suggested                                                                            |
| M    | OrigProj | the project where these expressions should be found if one day we select rules by project.               |
| N    | DevNotes         | I write here my notes about the creation of the rule, if any, and you can also leave there notes for me  |

The user or the PM should provide an almost ready file, where literal matches need no intervention from my side, whereas patters to be more generic (e.g. "Which (one/two…)?") will be refined so that the match works. You could use this [template](https://capps.capstan.be/Files/RuleSet_Translatability_PROJ_usa-ENG_template.xlsx).

To streamline the process, please observe the following recommendations.

#### Structure of the ruleset

* Line breaks should be avoided within cells. 
* No merged cells please – that makes it difficult to work with spreadsheets or CSV files (e.g. to import to the database). 
* About rows in the file that classify the rest of the rows (and have a Roman number in column A): please remove them, or include that info at the end of the file in an extra column. 

#### Separate data items clearly

* No metalinguistic information in the cell that contains the pattern (e.g. POS: `value(verb)`, `access(verb)`) or anywhere else (except perhaps column `N/DevNotes`).

#### Special characters / conventions

* You will have to specify what special characters mean (or we can agree on some conventions). For example, in `[This] includes [followed by an enumeration]`, what do the square brackets mean? 

#### Patterns

* In the cases where the expression is meant to match a pattern, it would help me have the different examples that the expression is meant to match. Ideally, we should import the translations into ML, where I can run searches and get a good idea of what needs to be matched and what needs not. 

#### Placeholders 

* If the expression is meant to match several options, you should indicate so. For example, I assume `take someone or something at face value` is not a literal match, but instead it should match "take someone at face value" or "take something at face value" or even "take ... at face value". If that's the case, you should provide an expression like `take (someone/something/*) at face value`. You shouldn't leave that to my discernment, because I might overlook it. 
* If there are more than one term that should be matched by the same expression, include them in the same cell, not in different columns (and you can use the VF glossary wildcard syntax to separate them, e.g. `accountable;accountability`, or `accountab*`, depending how specify you want to be, or leave me the choice: `accountable/accountability`). In some cases, you might want to have different rows, e.g. for "actual" and for "actualise". 


## Results 

You can see the results in the HTML report or, if you are using Veryfire as a 3rd or 4th linguist, you should then use the merged report. 

* * * 

Any feedback would be greatly appreciated. Feel free to [contact us](mailto:manuel.souto@capstan.be).
