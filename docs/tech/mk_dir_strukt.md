---
tags:
  - Audience꞉User
---

# AUTOMATION: CREATE FOLDER STRUCTURE

Script name: `mk_dir_skrukt.sh`

## Description

This automation can be used to create folder structures in the project folder, including one subfolder per version (language variant). The name of each version subfolder will be the locale of the version (e.g. `ron-ROU` for Romanian, etc.).

## Preparation

Required input from the PM:
* Zip file, whose name must be (or end in) `lll-CCC.zip` containing the contents of the version subfolder that need to be replicated,
* A text file, whose name must be (or end in) `lll-CCC.txt`, containing a list of locales (as cApStAn language codes) for which the version subfolder must be created, one locale per file.

Those two files must be included under a `_tech` subfolder, which must sit in the path where the version subfolders must be generated.

**IMPORTANT**: The zip file should include the contents of the version subfolder, not the version subfolder itself. The best way to create the `lll-CCC.zip` file is to simply go into the model `lll-CCC` folder, select all subfolders and zip them, and then rename the zip file created as `lll-CCC.zip`. Do not zip the `lll-CCC/` folder itself.

<!-- In other words, when unzipping the `lll-CCC.zip` package, that should create a `lll-CCC` folder containing all the language task sub-subfolders, rather than a `lll-CCC` folder containing a `lll-CCC` folder containing all the subfolders. -->

### Examples

An example of `lll-CCC.zip` file would be:


	Archive:  lll-CCC.zip
	  Length      Date    Time    Name
	---------  ---------- -----   ----
	        0  2020-02-07 16:55   00_source/
	        0  2020-02-07 16:55   01_translator_1/
	        0  2020-02-07 16:55   02_translator_2/
	        0  2020-02-07 16:55   03a_to_reconciler/
	        0  2020-10-19 14:50   03b_from_reconciler/
	        0  2020-02-07 16:56   04a_to_proofreader/
	        0  2020-10-19 14:51   05a_from_proofreader/
	        0  2020-10-19 14:51   06_delivered/
	---------                     -------
	        0                     8 files

An example of `lll-CCC.txt` file would be:

	bul-BGR
	ces-CZE
	deu-DEU
	ell-GRC
	esp-ESP
	est-EST
	fra-FRA
	hun-HUN
	ita-ITA
	pol-POL
	slo-SVK
	ron-ROU
	rus-EST

## Request

To accomplish this automation, the PM must do the following:

1. Define the path to the folder where the version subfolders are to be generated, e.g. `U:\IPSOS\ETUI\01_PILOT_FIELD`.
2. Create the `_tech` subfolder in the path above, e.g. `U:\IPSOS\ETUI\01_PILOT_FIELD\_tech`.
3. Create the two `lll-CCC` files above and put them in the `_tech` subfolder.
4. Send an email to `manuel.souto@capstan.be` to request the automation, providing the path above.

## Questions

To be addressed to Manuel or Adrien. Danina could probably help as well with the preparation steps above, as she has followed them for a few projects in 2020/2021.
