# LQE backend
Backend application in cApps to store and serve linguistic quality evaluation (LQE) reports

## Introduction 

The purpose of this project is create a new interface in the translation/review environment that allows the reviewer (the language expert responsible for evaluating the quality of the translation) to document their interventions within that environment (the CAT tool). OmegaT is the CAT tool used at the moment for LQE reviews (such as verification tasks).

## LQE plugin for OmegaT 

This new interface is a new dialog in OmegaT that allows the user to document their interventions (issues they find and edits they apply in the translation, or just confirm the translation conforms to expected requirements), entering:

* intervention category and subcategory, 
* comment (based on a template for each subcategory), and
* severity code

These categories and subcategories are determined by the LQE configuration, included in the user configuration files in OmegaT.

### Installation

To have the LQE dialog an OmegaT plugin needs to be installed. It will be installed or updated when the OmegaT customization is updated.

### Authentication

The verifier must make sure their name/ID in OmegaT is either “VER” or something that starts with “VER”. The username for authentication will be a combination of OmegaT user's name/ID and the target language code (e.g. “fr-FR”), joined by an underscore. 

So for example, the verifier of the French (France) version could have OmegaT name/ID `VER`, which will become username `VER_fr-FR` in the report, or the verifier of the Galician version could have name/ID `VER_manuel`, which would become username `VER_gl-ES_manuel` in the report, etc.

The plugin would register the user (with `username` and `password`), and will receive an authentication token, which each request will then include in the HTTP header.

### LQE reports

Apart from including the LQE dialog in the OmegaT interface, the LQE plugin is also responbible for producting a LQE report in several forms.

* As a JSON file
* As an Excel file
* As as a number of HTTP requests to the restful server

The JSON report is created at `lqe/project-lqe.json` when a verifier opens an OmegaT project. 

Even if no issues are registered (in other words, if no interventions are documented), a report will be created for the OmegaT project with an empty list of segments with issues.


#### API

The POST request that initializes the report in the database adds a new row in the "reports" table, and the PUT requests that create or update segments add or update a row in the "segments" table and as many new rows as issues the segment has in the "issues" table. With every segment update request, all existing issues are deleted and saved again.

The report is created with a POST request to URL `{{url}}/lqe/report/<report_uuid>`, containing the following properties in the payload:

| KEY 				| DESCRIPTION |
|:------------------|:---------------------------------|
| report_uuid 		| Hash value that uniquely identifies the report: e.g. `fd928793-eae5-4115-acb5-9bf4c586e91d` |
| tool				| LQE plugin version |
| lqe_config		| The name of the set of categories used in the LQE report. |
| project_name		| The name of the project folder when the LQE report is created. |
| timestamp			| `YYYYMMDD_HHMMSS` |
| source_lang 		| OmegaT or BCP47 language code: e.g. `en-ZZ` |
| target_lang 	 	| OmegaT or BCP47 language code: e.g. `fr-CA` |
| segments			| Array of key-value objects (one object per segment). When initializing the report, it must be empty. |

The report's `report_uuid` property is a hash number that uniquely identifies the report. This property is saved in the `project-lqe.json` persistently and can be used between different user sessions to identify all issues that are saved to the database as part of the same report. This number could be used by another client to get all issues for one report.

Example of report object: 

	{
	  "report_uuid" : "17abf070-329c-4804-81c7-3d4684763955",
	  "tool" : "LQE Plugin 0.4.0",
	  "lqe_config" : "capstan-standard-pisa",
	  "project_name" : "lqe_test_omtprj",
	  "timestamp" : "2020-03-28T12:08:53.833",
	  "source_lang" : "en",
	  "target_lang" : "gl",
	  "segments" : [ ]
	}

Issues will be grouped per segment and a group of issues will be created or updated with a PUT request to url `{{url}}/lqe/report/<report_uuid>/segment/<segment_id>`, including an issues array is a property of the segment.

Each `segment` object will have the following properties:

| KEY 				| DESCRIPTION |
|:------------------|:---------------------------------|
| segment_id 	| Hash value tied to the segment key (source + file + prev + next) |
| report_uuid 	| Foreign key that links the segment to the report. |
| segment_number | One of the correlative integer values that enumerate segments. |
| transunit_id 	| Value of ID attribute of the trans-unit element in an XLIFF file. It must be Null for other file types. |
| filename 		| Name of the file where the segment appears. |
| source_text	| Source text. |
| target_orig	| Original translation before verification. |
| target_edit	| Edited translation that includes changes made by the verifier. |
| translator	| Name/ID of the user who registered the original translation. |
| issues 		| Array of key-value objects (one object per issue). See table below. |

Caveat: In order to have constant segment numbers (which don't change even if the user alters the order of files), the `files_order.txt` file must be deleted on project load (and therefore before the plugin is run).

Each `issue` object will have the following properties:

| KEY 				| DESCRIPTION |
|:------------------|:---------------------------------|
| issue_uuid		| Auto-increment identifier for each issue/intervention. |
| segment_uuid		| Foreign key that links the issue to the segment.  |
| category			| One value from the list of categories for each LQE config. |
| subcategory		| One value from the list of subcategories for each category. |
| comment			| Open-ended text inserted or modified by the user. |
| severity			| One value from the list of severity codes allowed for a certain category. |
| reviewer			| Name/ID of the user who edits the translation during the LQE. |

Example of segment object:

	{
	    "segment_id" : "1276287c",
	    "segment_number" : 1,
	    "transunit_id" : null,
	    "filename" : "source_file.txt",
	    "source_text" : "This is the first sentence.",
	    "target_orig" : "Esta é a primeira frase.",
	    "target_edit" : "Esta é a primeira oración.",
	    "translator" : "souto_translator",
	    "issues" : [ {
	      "issue_uuid" : "c7178fb7-e6f9-44c5-a262-ce6c409571b6",
	      "category" : "Adaptation issue",
	      "subcategory" : "Missed adaptation",
	      "comment" : "“sentence” was not adapted.",
	      "severity" : 1,
	      "reviewer" : "VER_manuel"
	    }, {
	      "issue_uuid" : "798470ac-3aac-4f64-9206-116ee3eb72cc",
	      "category" : "Adaptation issue",
	      "subcategory" : "Wrong adaptation",
	      "comment" : "Wrong adaptation in target “…” + EXPLANATION",
	      "severity" : 5,
	      "reviewer" : "VER"
	    } ]
	}

## Backend deployment

For the time being, the API is deployed as a Heroku app in the following address: https://capps-lqe-backend.herokuapp.com/lqe/. That URL must be included in the OmegaT preferences (Options > Preferences > Plugins > Linguistic Quality), so that the LQE plugin knows where to sent the requests.


## No license

This software doesn’t have a license, which means you have no permission from the creators of the software to use, modify, or share the software for any purpose.
