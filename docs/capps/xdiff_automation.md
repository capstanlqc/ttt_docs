# xDiff automation: Comparing OMT packages in Ur

This document explains how to automate the generation of diff reports comparing two OMT packages.

## Basic logic

The script sends two packages to xDiff and receives a URL to the diff report in xDiff. The diff report can be consulted directly in xDiff but the script also saves is URL in a HTML file, which redirects to the diff report web page when it is opened in the browser. The execution of the script is scheduled to run every minute.

For every request to xDiff, the script needs to know the paths to the two packages and the path to the folder where the HTML file must be written. Those parameters are fetched from a path template config file, called `paths_for_diff.xlsx`. In order to automate the generation of the xDiff reports, the paths must be added to this file. 

## Path templates config file

### PISA 2022 MS

If you must compare pairs of OMT packages in PISA 2021 Main Survey, you can add the paths to file `PISA_2021` > `MAIN_SURVEY ` > ` _tech > xdiff ` > ` paths_for_diff.xlsx`. 

### Projects other than PISA 2022

If you must compare pairs of OMT packages for another project, proceed as follows:

1. Fetch the `paths_for_diff.xlsx` file from `PISA_2021\MAIN_SURVEY\_tech\xdiff`, and copy it to `{root}` > `_tech` > `xdiff`. 
   - `{root}`  is the root folder of your project, e.g. `U:\PISA_2021\MAIN_SURVEY` for PISA 2021 Main Survey or `U:\IPSOS\EUROBAROMETER_FLASH_2.0\08_FLASH_PROJECTS` for Eurobarometer 2.0 (FLASH).
   - Create folders `_tech` and  `xdiff`  if they don't exist. 
2. In `{root}\_tech\xdiff\paths_for_diff.xlsx` > sheet **paths**: 
   - Delete all paths there. You can simply select rows rows 2 to *n* and delete their content.
   - For every pair of OMT packages you must compare, add your three paths there:
     - A: Path template to input package 1
     - B: Path template to input package 2
     - C: Path template to output HTML file
   - You can put whatever you like in the other columns (D, E, etc.), which are ignored by the script, or leave them empty.
3. In `{root}\_tech\xdiff\paths_for_diff.xlsx` > sheet **config**: 
   - Update the path to the root folder (cell B2). The script assumes this is a Windows path (using backslashes) which starts with `U:\` (or another drive letter), which is how `/media/data/data/company` is mounted in your machine. However, the UNIX path is also fine.
     *Note*: This Windows path will be converted to the UNIX path, e.g. if your root path is `U:\PISA_2021\MAIN_SURVEY`, it'll become `/media/data/data/company/PISA_2021/MAIN_SURVEY` before the script can use it. If you provide the UNIX path, it won't need to be converted. Use whatever you're sure that points to the location you want to use.
   - If needed, update the name template of the OMT package. Any variable part (e.g. language code plus anything else) should be represented with `* `, e.g. `PISA2022MS_CodingGuide_MATNew_*_OMT.omt`.
   - If needed, update the name template of the HTML file (which will contain the URL of the diff report). Use `lll-CCC` as a placeholder for the language code, e.g. `PISA2022MS_CodingGuide_MATNew_lll-CCC_DIFF.html`.
4. Send an email to the [xDiff maintainer](mail:manuel.souto@capstan.be) to request the scheduling of the script for your project. In your email, you must include the full path to your `{root}\_tech\xdiff\paths_for_diff.xlsx` file.

I hope this is useful.
