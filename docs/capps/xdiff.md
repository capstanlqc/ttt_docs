# xDiff ☆

This documentation describes how to use xDiff to obtain diff reports that show the difference between two versions of a text. A number of different file formats (or collections of files) can be submitted to xDiff, either through the web inteface or as a background process from the server `Ur`.

## 1. Web interface 

If you visit [xDiff](https://capps.capstan.be/xdiff_cg.php), you will see a series of tabs which will display sections for defining or viewing:

* the settings
* the upload type
* all existing reports

### 1.1. Settings

To modify the settings, click on the Settings tab (the first tab). You can modify the following settings:

#### Display

You can choose whether you want to see rows or segments that have changed, or the ones that haven't changed, or both. 

<!--- #### 1.1.2. Diff granularity 
You can choose whether you want to see the differences highlighted as full words or as individual characters. To change this, click on the **Clean up** button in the report page.
--->

### 1.2. Upload types

You can upload different formats. To upload each format, click on the tab for the file format that you want to upload.

The expected input consists of text pairs (typically two versions/stages of the same translation), i.e. two versions of the same text, which can be two columns in a spreadsheet, two XLIFF files, two batches of XLIFF files or two OmegaT project packages. 

#### Excel file

If you want to compare two columns in a spreadsheet containing, say, a translation and an edited/verified version of that translation, select the number of the worksheet you want to analyze, and the column letters that correspond to the source text, the original translation and the modified translation. Then, simply press **Compare files**.

#### Two XLIFF files

If you want to compare two XLIFF files, you can upload the two files separately. Simply upload the two files, first the original and then the modified file, and press **Compare files**.

#### A batch of parallel XLIFF files

If you want to submit a set of XLIFF files and their corresponding modified versions, you can upload just one zip file containing all the files, which must be organized as follows. The zip file must contain: 

* A folder containing the original files
* A folder containing the modified files
* An Excel spreadsheet indicating the correspondences between the files from the two folders

To prepare the zip file, proceed as follows: 

1. Create two folders and name them as you wish, e.g. Old and New, Original and Modified, Translation and Verification, etc.
2. Put the original files in the first folder, and the modified files in the second folder.
3. Create an Excel file and name it `correspondences.xlsx`. In this file, in the first row of the first worksheet, add the names of the folders: the first folder in the first cell (A1), and the second folder in the second cell (A2). The first two cells of the spreadsheet must contain the names of the two folders. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
If the base name of the modified files is the **same** as the original files plus some addition (e.g. `PISA_srp-SRB_SCI_S514_eng_FT2018_TRANSLATED.xlf` vs `PISA_srp-SRB_SCI_S514_eng_FT2018_VERIFIED.xlf`), you don't need to do anything else (see an [example](https://capps.capstan.be/Files/correspondences.xlsx)). 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
If the base name of the two files is **not** the same, then you need to fill in the two columns with the names of the files. For example:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![](https://capps.capstan.be/Images/correspondences_filled.png)

4. Zip the two folders and the correspondences file together, and name it as you wish.
5. Simply upload the zip file.

#### Two OMT packages

If you want to compare two OmegaT packages, simply drag and drop the two packages individually and press **Compare files**.

### 1.3. List of existing reports

The Reports tab lists the latest 100 reports for containers and target languages that the user credentials give access to.

## 2. Background service 

A different approach has been implemented to obtain diff reports to show differences between two OmegaT project packages for the translation of the PISA 2021 FT coding guides. This approach does not require uploading the two packages on the webpage, but instead the submission is done automatically behind the scenes provided that some conditions are met. 

### 2.1. Functionality

A running service watches a pre-defined set of folder pairs in the server. Folders are watched in pairs because two packages must be submitted to xDiff. Whenever an OMT package appears in a watched folder (because the PM drops it there or downloads it there), the service will check whether its paired folder contains an OMT package and, if found, both packages will be submitted to xDiff. 

If the process is successful, xDiff will process the request, compare the two packages, store the diff report in a database and respond with the URL to a page where that xDiff report can be consulted. The running service in Ur will write a log file and create a HTML document that will open the report in the browser. To see the report, simply double click the HTML file to open it in a browser.

If the process is not successful, xDiff will respond with an error message, which should be written in the log. No xDiff reportr will be created in that case. 

Both the log and the HTML report will be written in the second folder (next to the second package). 

### 2.2. How to use it

To run xDiff in the background, follow these steps: 

* Make sure the first package is in the first folder
* Drag and drop the second package to the second folder
* Wait for a few seconds
* Double click the HTML report to open it or send/upload it to be used by third parties

![jcoyYX7G4L](https://user-images.githubusercontent.com/3659409/79289439-8306ab00-7ec9-11ea-93aa-a79d6fa9ff5c.gif)
<!--- https://im.ezgif.com/tmp/ezgif-1-90ae1696978b.gif) --->
<!-- https://ezgif.com/resize -->


### 2.3. Watched folder definition

The folder pairs that must be watched are defined in the file `U:\PISA_2021\FIELD_TRIAL\_Tech\cg_xdiff\200129_Steps_for_Difference_Reports.xlsx`, which has the following structure: 

| Steps where the diff report is needed | Path template to package 1 | Path template to package 2 | Notes |
|:--------------------------------------|:---------------------------|:---------------------------|:------|
| Verification review  | U:\PISA\FT\XXX_xxx\ 4_CG\01_from_country |  U:\PISA\FT\XXX_xxx\ 4_CG\03_from_verifier | Diff between reconciled and verified version (for PM) |
| Referee review  |  U:\PISA\FT\XXX_xxx\ 4_CG\01_from_country |  U:\PISA\FT\XXX_xxx\ 4_CG\04_reviewed_delivered | Diff between  reconciled and reviewed version (for Referee) |
| etc. | | | |

The service replaces `XXX_xxx` in each of these path templates with every actual language code and that way it builds the list of all the folders that need to be watched for each version. Whenever an OMT package appears in the second folder, it will fetch for the twin OMT package in the first folder and will submit both packages to xDiff.

### 2.4. Constraints and disclaimer

The process will not succeeed in the following cases:

* If the first folder contains no OMT package.
* If the first folder contains more than one OMT package.

If any of these contrainsts is not convenient, it can be discussed. 

## 3. Results

You can access reports in three ways:

1. After your submission has been processed by uploading the files through the webpage, the page will display a one-row table for the diff report that has been generated based on the analysis of your upload. Use this to access the diff report you have just generated.
2. Double-clicking the HTML file that appears in the second folder besides the second pair OMT package when using the background service in `Ur`.
3. Regardless of the submission mode, the **Reports** tab will display the whole list of diff reports available to you, where you can access any previously generated report. 

In either case, in the row for each report, you have some information about the report, as well as some buttons: 

* Press the eye button to open the report page in a new tab
* Press the copy button to copy the URL to that report to your clipboard 
* Press the save button to save the report as a file that you can archive
<!--- * Click the delete button to delete that report --->

## 4. The xDiff report page

Each diff report is displayed in its own page. This page can be opened by clicking on the eye button in the list of reports or by pasting the URL in the address bar of your browser. 

In the report page you can: 

* Check administrative information about the report 
* Check the diff report itself
* Filter results
* Clean up results

### 4.1. Administrative information

Click the Admin info tab to display the administrative information of the diff report, which includes: 

| Row   				     | Description |
|:-------------------|:------------|
| report_id          |	The identification number of the report. |
| report_name	       | The name of the report, with the date and time, the language version, the name of the batch and the file extension. |
| batch_name         | 	The name of the batch. |
| container	         | e.g: PISA |
| timestamp_readable | The date and the time of creation in readable format |
| timestamp          | 	Date and time, less readable format |
| file_list	         | The list of files in the batch |
| total_files	       | Number of files to compare |
| source_lang	       | The source language |
| target_lang	       | The language of the translation |
| created_by	       | The name of the person who uploaded the package  | 

### 4.2. The diff report

The xDiff report consists of a table with one row per segment where differences have been found, including the following details: 

| Column 				       | Description |
|:---------------------|:---------------------------------|
| #	                   | The number of the segment |
| File name          	 | The name of the file that is compared |
| Segment ID (XLIFF)   | Only for XLIFF files |
| Source text          | The original text |
| Original translation | The original/old translation  |
| Edited translation   | The modified/new translation where you can see all track changes highlighted |

The "original translation" refers to the one extracted from package 1 or file 1 or column 1 in the Excel. The "edited translation" refers to the one extracted from package 2 or file 2 or column 2 in the Excel.

### 4.3. Filtering results

Use the search box to filter the results displayed. You can search for words included in the source text or the translation, filename, segment number or ID, etc. 

You can also make a combined search, if you wish to see changes only in a certain file format, e.g.: XLIFF

### 4.4. Cleaning up results

Click the **Clean-up** button to make track changes more readable. If a word contains more than 4 edits (deletions or addition or replacements), the edits will be joined as one single change of several characters.

Any feedback would be greatly appreciated. Feel free to [contact us](mailto:manuel.souto@capstan.be).
