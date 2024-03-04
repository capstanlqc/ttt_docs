# FLASH: Workflow automation ☆

This document outlines the steps that the PM must take to automate the translation of the Flash surveys, as well as what is the outcome of every step.

<!-- This document can be read as a web page on [https://capps.capstan.be/doc/flash_automation.php](https://capps.capstan.be/doc/flash_automation.php). -->

> To make changes in this document, edit [/docs/flash_automation.md](https://github.com/capstanlqc/flash_prepp_help/blob/main/docs/flash_automation.md)
<!--  and then copy to https://capps.capstan.be/doc/flash_automation.php and /README.md (not vice versa) -->

### Changes history

| Date  | Person  | Summary |
|---------|---------|-------|
| 2021.03.29 | Manuel | Creation of first version of the document |
| 2021.04.27 | Manuel | Added TM management, ADA config, updated triggered actions, general review |
| 2021.10.08 | Manuel | Updated `_tech/processed.txt`'s name to `_tech/post.complete`. |
| 2022.05.23 | Manuel | Review. |
| 2023.10.15 | Manuel | Updates in language codes and logic to flag unaltered matches |
| 2024.02.13 | Manuel | Updated to Python 3.10. |

### Recommended tools:

- [**7-zip**](https://www.7-zip.org/) for zipping, unzipping and opening packages (without unpacking)
- [Total Commander](https://www.ghisler.com/) for transferring files from one folder to another (especially from server to local and vice versa)
- Notepad (or any other text editor such as [Sublime Text](https://www.sublimetext.com/) or [Atom](https://atom.io/)) to edit text files. DO NOT use Microsoft Word or Wordpad and the like instead of a text editor to edit text files.
- [Typora](https://typora.io/) for reading or editing markdown files.


## 0. General

### Some notions and conventions

Here is a short list of common terms used in this document:

| **Term**  | Explanation                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Project** | The container or generic project name (i.e. Eurobarometer) to which each translation workflow belongs. |
| **Survey** | Each actual translation request (e.g. `FLASH-001`, etc.)       |
| **OmegaT project** | The folder containing all the OmegaT files, folders and project settings. Note: this is not a package, it's a folder. |
| **OmegaT package** | An OmegaT project that has been packed with extension `.omt`. Aka the OMT file. |
| **Reference**   | Any materials that the client might have sent containing translations that we should use as reference. |
| **Language assets** | Any TMs, glossaries, etc. that we prepare to include in the OmegaT project or in MemoryLn.                               |
| **Version** | A language variant for which a whole language task is executed |

Reminder: Every info item in file names must be separated with underscore (\_). Hyphens or dashes (-) are reserved for separating parts in a compound item (e.g. `FLASH-001` or `fra-FRA`). Do not use underscores (\_) inside items.

### Project folders

The project's root folder is located at `.../data/company/IPSOS/EUROBAROMETER_FLASH_2.0` (or `U:/IPSOS/EUROBAROMETER_FLASH_2.0`, if that's how the share is mounted in your machine).

The project's root folder contains the following subfolders:

| Folder | Purpose                |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `_tech` | Tech team stuff (warning: beware of the dog!) |
| `00_ADMIN` | Budgets, bid information, SOW, etc. |
| `01_SOURCE_MRT` | Location of the source files handed off by the client. |
| `02_AUTOMATION` | Any files used by the autoamation that either TT or PM need to keep up to date. |
| `03_INTERNAL` | Internal resources for REF |
| `04_REF` | Any resources the client has provided as a reference or/and that could be converted into language assets.  |
| `05_MEETINGS` | Meeting minutes |
| `06_EHR` | Resources related to Linguists |
| `07_PROJECT_MANAGEMENT` | PM stuff  |
| `08_FLASH_PROJECTS` | All the workflow folders. |
| `09_ASSETS` | Any language assets (TMs, glossaries, etc.) used or produced in the project. |
| `Z_outdated` | Anything that won't be needed unless this statement is proved wrong... |

For the sake of shortness, this document uses relative paths inside the project's root folder.


## 1. Pre-processing

Pre-processing and post-processing refer to any automation that takes place in the server before and after the language tasks.

There is a translation workflow for every **survey** the client wants to translate. To initiate the workflow, the PM must put a new **initiation bundle** in the folder `/02_AUTOMATION/Initiation/` of the project. The name of the initiation bundle will be also the name of the survey folder under `/08_FLASH_PROJECTS` (e.g. if the initiation bundle is called `FLASH-005.zip`, the folder `/08_FLASH_PROJECTS/FLASH-005` will be created).

The name of the initiation bundle (and survey folder) is expected to be something like, say, "FLASH-420" (it should contain the word "FLASH" in upper case followed by a three-digit number and an optional letter at the end).

### Configuration

The configuration file (or config file for short) is available at `/02_AUTOMATION/Config/config.ods` and it contains certain more or less constant pieces of data that the automation needs to know about the project, the survey, the monitoring form, the source file or the deliverable, to either find or generate certain files in a certain location with a certain name.

The PM (in consultation with TT) is responsible for keeping this config file up to date if there are any changes throughout the project. If there are no such changes, the config file does not need to be modified.


### Initiation bundle

The initiation bundle must contain folders `00_source`, `10_deliverables` and then one folder for each language task (e.g. `01_TRA`, `02_ADA`, etc.).

The `00_source` must contain the source MRT file (one `.xlsm` file only is expected), where all rows out of scope for translation have been hidden. The target MRT file will be generated in the folder `10_deliverables` and updated with every version that is processed.

In other words:

```
├── 00_source
├── 01_TASK
├── 02_TASK
├── 03_TASK (etc.)
└── 10_deliverables
```

Each language task folder (e.g. `01_TRA`, `02_ADA`, etc.) must contain one file `lll-CCC.txt` containing the list of languages (one cApStAn language code per line) to which that language task applies and one file `lll-CCC.zip` containing the version folder structure to be replicated for each version.

In particular for the adaptation task, a third file must be included under the `02_ADA` folder, called `ada_lang_mapping.ods`, containing the correspondences between base and borrowing versions.

####  Examples

An example of `lll-CCC.zip` file would be:

```
Archive:  lll-CCC.zip
Name
----
01_To_Translator
02_From_Translator
03_From_Verifier
04_Verif_Review
05_Machine_Translation
-------
5 files
```

An example of the contents of the `lll-CCC.txt` file would be:

```
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
```


An example of the contents of the `ada_lang_mapping.ods` file would be (base version code on the left, borrowing version code on the right):

| 01_TRA  | 02_ADA  |
|---------|---------|
| deu-DEU | deu-AUT |
| nld-NLD | nld-BEL |
| fra-FRA | fra-BEL |
| swe-SWE | swe-FIN |
| rus-EST | rus-LVA |
| fra-FRA | fra-LUX |
| deu-DEU | deu-LUX |
| ell-GRC | ell-CYP |
| eng-ZZZ | eng-IRL |
| eng-ZZZ | eng-MLT |


In the example below, showing the contents to be zipped inside a fictitious initiation bundle, `01_TRA` and `02_ADA` are the task folders for the translation+verification and for adaptation tasks, respectively:

```
├── 00_source
│   ├── [source_MRT_file].xlsm
├── 01_TRA
│   ├── lll-CCC.txt
│   └── lll-CCC.zip
├── 02_ADA
│   ├── ada_lang_mapping.ods
│   ├── lll-CCC.txt
│   └── lll-CCC.zip
└── 10_deliverables
```

A template can be found under `/02_AUTOMATION/Initiation/Templates/FLASH-XXX-Template.zip`. It may be used as the basis for the initiation bundle for a new survey translation workflow (after updating the various details to the characteristics of the new survey (e.g. the list of languages for each task, the source MRT file, the bundle's name, etc.), which must be put it in the folder `/02_AUTOMATION/Initiation/` of the project.

The PM is responsible for preparing the survey's initiation bundle, e.g. updating the list of languages for the translation of every survey, etc. *Tips*: Use a text editor (e.g. Notepad, Notepad++, Sublime Text, etc.) to edit the list of languages. The tool 7zip is recommended to pack the `lll-CCC.zip` files and the contents of the initiation bundle.

> **IMPORTANT**: The `lll-CCC.zip` file should include the contents of the version subfolder, not the version subfolder itself. The best way to create the `lll-CCC.zip` file is to simply go into the model `lll-CCC` folder, select all subfolders and zip them, and then rename the zip file created as `lll-CCC.zip` if necessary. Do not zip the `lll-CCC/` folder itself. The same applies to the initiation bundle itself.


#### @PM - Steps to prepare the initiation bundle

In a nutshell:

1. Copy the new MRT for translation and the initiation bundle template to a local folder in your machine.

  > - The initiation bundle template can be fetched from `/EUROBAROMETER_FLASH_2.0/02_AUTOMATION/Initiation/Templates/FLASH-XXX-Template.zip`. 

  > - A previously used initiation bundle may be used as a template instead.

2. Open the new MRT in Excel and filter out rows that are not for translation. Only rows to be extracted for translation should be visible. Save and close.
  > - In the column that indicates whether translation is needed, there should be only digits (0, 1 or 2).

3. Unzip the initiation bundle template (or simply open it in 7-zip, if you prefer).

3. Put the new MRT file inside the `00_source` folder of the initiation bundle.

4. Update the list of languages under each language task folder.
  > - Use a text editor to edit the `lll-CCC.txt`.
  > - You may use the [**Locale checker**](https://capps.capstan.be/locale_checker.php) app in cApps to make sure the language codes are correct.

5. Under the `ADA` task folder, make sure the file that maps the correspondences between base versions and their corresponding borrowing versions (e.g. `ada_lang_mapping.ods`) is complete and up to date.

5. Zip the contents of the initiation bundle (or just close it if you had simply opened it in 7-zip in step 3).
  > - If you zip them, make sure you select the folders and pack them as a new zip file. Please DO NOT zip the main initiation bundle folder, but its contents!

6. Rename the initiation bundle as the new survey name, e.g. `FLASH-005` (see above about character restrictions for this name).

7. Copy the new initiation bundle you have created to the `/02_AUTOMATION/Initiation/` folder in the project in the server.

That's it. The process will start, the workflow will be created and, after a couple of minutes, the packages should be ready for dispatch.

You can watch a hands-on demo of the above steps (or this whole section) in the video below:

<iframe title="vimeo-player" src="https://player.vimeo.com/video/530800278" width="640" height="360" frameborder="0" allowfullscreen></iframe>

----

### Actions triggered

When the initiation bundle is put in the folder `/02_AUTOMATION/Initiation/`,  several things happen within a few minutes: all version folders are created and the OmegaT project packages are created inside them.

More in detail:

Firstly, the survey folder structure is generated:

- The initiation bundle is uncompressed in `/08_FLASH_PROJECTS` thereby creating the survey workflow folder.
  - It is also archived under `/02_AUTOMATION/Initiation/_done` (in case it needs to be reused).
- Inside each task folder under the survey folder, one version folder will be generated for each version in the list of languages (i.e. `lll-CCC.txt`) including the contents of the version project template (i.e. `lll-CCC.zip`).
  - The list of languages and the version folder template are archived (for further reference, if needed) under the `_tech` folder inside the task folder.
- Any translations found in the source MRT file will be extracted and saved in TMs under `09_ASSETS/01_Incoming/FLASH_MRT_TM`.

Secondly, the OmegaT project packages are generated for each version under the `/08_FLASH_PROJECTS/[survey]/[task]/[version]/01_To_Translator` folder, including:

- The right project settings (including segmentation rules, filter settings, etc.)
- The source file in HTML format, with perhaps a shortened name (a copy remains under `/08_FLASH_PROJECTS/[survey]/00_source` for reference).
- Any glossaries, if available under `09_ASSETS/01_Incoming/*_glossary`.
- Any TMs, if available under `09_ASSETS/01_Incoming/*_TM`.

Thirdly, for the `eng-ZZZ` version, OmegaT will run in the background to translate the project with the source text.

####  Examples

For example, for a fictitious "FLASH-005" survey with a file for translation called `S21007984_x0_multi.xlsm`, the following contents will be created under `/08_FLASH_PROJECTS/FLASH-005` when the initiation bundle `FLASH-005.zip` appears in `/02_AUTOMATION/Initiation/`:

```
├── 00_source
│   ├── Eurobarometer_FLASH-005_xxx-XXX_OMT.omt
│   ├── S21007984.html
│   └── S21007984_x0_multi.xlsm
├── 01_TRA
│   ├── _tech (...)
│   ├── bul-BGR
│   │   ├── 01_To_Translator
│   │   │   └── Eurobarometer_FLASH-005_bul-BGR_OMT.omt
│   │   ├── 02_From_Translator
│   │   ├── 03_From_Verifier
│   │   ├── 04_Verif_Review
│   │   └── 05_Machine_Translation
│   ├── fra-FRA
│   │   ├── 01_To_Translator
│   │   │   └── Eurobarometer_FLASH-005_fra-FRA_OMT.omt
│   │   ├── (... etc. same for other versions)
├── 02_ADA
│   └── _tech (...)
└── 10_deliverables
    └── S21007984_x0_multi.xlsm
```


The OMT packages generated under the `01_To_Translator` folder are named according to the pattern specified in the configuration file. They should not be renamed. Likewise, the expected name of the monitoring form is specified in the config file.

## 2. Diff reports

Diff reports showing verifier's interventions will be automatically generated when both the project package handed back by the translator and the project package handed back by the verifier are available.

The process will permanently watch for the project package under the `03_From_Verifier` folder. When it appears there, if the package from the translator is found under `02_From_Translator`, both packages are sent to [xDiff](https://capps.capstan.be/xdiff.php) and a diff report is generated.

The process will watch the paths specified in file `/02_AUTOMATION/Diff/flash_steps_for_xdiff.xlsx`.

<!-- The URL of the new xDiff report will be emailed to `flash-eb@capstan.be` (or the addresses specified in file `../data/company/cApStAn_Tech/20_Automation/Scripts/xdiff_ps/email/receivers_pm.txt`) and a HTML file that will open the xDiff report will be written under the `03_From_Verifier` folder. -->

More information available [here](https://capps.capstan.be/doc/xdiff.php), under section **2. Background service**.

#### @PM - Steps to generate the xDiff reports

At the kickoff of the project (once-off), confirm that paths specified in the `flash_steps_for_xdiff.xlsx` are correct.

Then, to generate each report, the PM doesn't really need to do anything special other than:

- Make sure that project packages haven't been renamed
- Put the package from translation under `02_From_Translator`
- Put the package from verification under `03_From_Verifier`
- Wait a few seconds

If for any reasons the xDiff report is not generated, please check with TT or drag the packages manually to [xDiff](https://capps.capstan.be/xdiff.php).

## 3. Post-processing

When the files have been handed back by the linguists, some post-processing takes place.

#### @PM - Steps to post-process the packages

When the verification review is complete, the PM must simply copy the OMT package and the monitoring form to the `05_Machine_Translation` folder.

If for any reasons the files need to be post-procssed again, the PM can delete the `_tech` folder (or any specific file inside it) to let the post-processing step run again.

### Actions triggered per version

When both the finalized OMT package *and* the monitoring form (as an `.xlsm` file) are copied to the `05_Machine_Translation` folder for a specific version (i.e. under path `/08_FLASH_PROJECTS/[survey]/[task]/[version]/05_Machine_Translation`), that version is post-processed, which means that several things happen inside that folder within a few minutes:

#### *Version wise*:

- Before anything else, OmegaT is run on the project behind the scenes to generate the target HTML file with the translation and export the project as a bilingual Excel.
- Last, a `_tech` folder is generated in the `05_Machine_Translation`, containing these files:
  - `omt.complete`, which indicates that the target files have been produced,
  - `mt.complete`, which indicates that the translation has been back-translated,
  - `post.complete`, which indicates that this version has been processed and the MRT populated with it.

Those files stop the corresponding automation steps from running again on a version that has already been post-processed. 

> *Tip:* If for any reason any of the post-processing steps needs to be repeated for one version, simply delete the corresponding `*.complete` file (or just the whole `_tech` folder).

#### *Monitoring form-wise*:
  - The target-language column in the Excel export is machine translated to English (by the engine defined in the config file), to be used as the back-translation.
  - The target-language column from the Excel export and its back-translation are added to the monitoring form, in the two columns specified in the config file.
  - A zip file called `[survey]_TAVF_all.zip` under `10_deliverables` is updated with the monitoring form (TAVF file) for this version.

  > *Warning*: If the MT engine does not cover that language, the back-translation will be empty.

#### *Target file-wise*:
- The target (HTML) file is converted back to Excel (kind of monolingual MRT, with the same structure as the source-language column in the original MRT). Both files (HTML and Excel) contain one same target version of the survey. Both are:
    -  archived for reference under the `05_Machine_Translation/_done` folder
    -  added to a `done` folder inside the OMT package.
- The column in the target  MRT file (under `10_deliverables`) corresponding to the version being post-processed is updated with the translation.

For example:

```
10_deliverables:
├── FLASH-005_TAVF_all.zip     (<---- containing all monitoring forms)
└── S21007984_x0_multi.xlsm    (<---- containing all target versions, one per column)
```

When all versions have been post-processed, all columns in the target MRT are populated and all the monitoring forms are included in final TAVF bundle.

#### *TM-wise*:

- The master TM (`-level2` flavour) from each OmegaT project is added to `09_ASSETS/02_Outgoing/[survey]_TM.zip`.
- The master TM (`-omegat` flavour) from each OmegaT project is added to `09_ASSETS/01_Incoming/FLASH_OMT_TM`.



### Formatting in the MRT

Updating the target MRT file with all the translations removes the formatting from all worksheets. It's possible to re-apply the same formatting on each worksheet by opening the source MRT and the target MRT, and copying the formatting from the former and pasting it in the target (for the several worksheets in the file). If this becomes a nuisance, we could look again into a possible solution.

### Validation and updates

Before delivery, the validation macro must be run in the target MRT file. If the macro highlights any required changes in a translation to make it pass the validation, the changes should not be entered directly in the target MRT file. Instead, the translation in the OmegaT project under `05_Machine_Translation` should be updated, and then the `_tech/post.complete` deleted so that that version is post-processed again.


## 4. Language asset management

The project has a `09_ASSETS` folder, that contains language assets used or produced in the project. Folder `09_ASSETS/01_Incoming` contains TMs and glossaries what will be added to each new OmegaT project package, and folder `09_ASSETS/02_Outgoing` contains the archived TMs containing all the translations we’re producing, for the purpose of, say, sharing them with the client, adding them to MemoryLn, etc.

### Incoming assets

The `09_ASSETS/01_Incoming`  folder has several subfolders. On the one hand, there’s one for each batch of TMs or glossaries we prepare out of separate resources or reference materials that the client sends. That’s the case of folders like `COFOE_glossary` or `FL419_TM`.

On the other hand, there are two more folders:

- `FLASH_MRT_TM`: This hosts TMs with the translations that each source MRT file we receive contains for a specific survey, which are extracted when the translation workflow for that survey is initiated. When the OmegaT project packages are compiled for each version, if this folder contains a TM for that version, it is included in the package.

* `FLASH_OMT_TM`: This contains the master TMs (exported from each OmegaT project) from all previous surveys, which will be also added to OMT packages for new surveys. For example, right now (after having handled two surveys) there are only TMs for FLASH-001 and FLASH-002, which will be added for OMT packages for FLASH-003. Master TMs from the OMT packages for FLASH-003 will be added to this folder when a version reaches step `05_Machine_Translation` (see above), which will thereby be available for FLASH-004. And so on and so forth.

### Outgoing assets

The main purpose of the `02_Outgoing` folder and the zip files inside is to store the master TMs from all surveys in this project in case they need to be shared with other tools (MemoryLn, a CAT tool, etc.), other parties, etc. (e.g. to include as deliverable to the client). There is one zip per survey containing all the TMs for all the languages for that survey.

### Checks

Delete issues files.

## TODO

* Check that eng* versions are not sent to MT (instead the translation itself should be used as "pseudo-backtranslation")
* Update xDiff docs
* Check for completion in folders `02_From_Translator` and `03_From_Verifier` -> completion.txt/pending.txt
* Check contents of initialization bundle -> warning.txt
* Check whether any version is missing in the TAVF bundle under 10_deliverables -> completion.txt/pending.txt
* Check whether a file in a folder has an unexpected name -> warning.txt
* Check name of init bundle -> warning.txt
* Prevent formatting loss when updating the target MRT file (not sure it's possible)
* Create merged TMs with newer-first/older-last order for OT5
* Get wordcount stats for all versions
* Use pyenv or similar to use a python installation other than the system's default version

