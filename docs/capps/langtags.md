# Language tags: basic API ☆

You can fetch the whole list of langtag records as a JSON object. For that, you can send a GET request to the url [https://capps.capstan.be/langtags_json.php](https://capps.capstan.be/langtags_json.php). 

> A future version will provide more endpoints to allow consuming exactly the piece of data needed in a single request.

Each langtag record (a Javascript object or a Python dictionary) is a simple tabular data structure that contains all properties of a specific language variant, e.g. for Valencian:

```
{'BCP47': 'ca-ES-valencia',
 'Country': 'Spain',
 'Language': 'Valencian',
 'Notes': None,
 'OmegaT': 'ca-VL',
 'PIAAC_2letter_region': 'ES',
 'PISA': 'val-ESP',
 'cApStAn': 'val-ESP',
 'created_by': None,
 'id': 265,
 'last_modif_by': None}
```

You might not need the whole list, but for the time being there are no other endpoints that you can use, which means you need to fetch the whole resource first and then filter it and manipulate it on your end for your specific purposes.

See below two demos with examples of some typical operations, such as:
* Get the whole list of cApStAn codes
* Get a whole tag record for a particular language variant
* Get a language tag that corresponds to another tag in a different convention (e.g. from cApStAn to OmegaT)
* Get all language tag records that have a specific language subtag
* Get all region subtags for a specific language subtag

Examples are provided in Node.js and Python, check the appropriate section for the language you'll be using. The two REPL demos below are public so you can simply check or copy the code, or actually run it online. Check the steps in the `readme.md` file.

To run the REPL demos online, you probably need to have a repl.it account and fork the demo first. In any case, you will have to paste the URL above, which is not hardcoded. If you fork the REPL, you may hardcode the URL in the code, but then do not publish the REPL.

## Python

From Python3 applicationS (e.g. Odoo?) or applications that can run Python3 code (e.g. Excel), you can obtain the langtags data with the code below:

```
import requests
url = 'https://capps.capstan.be/langtags_json.php'
response = requests.get(url)
langtags = response.json()
```

The data obtained above will contain a Python dictionary. You can then query and manipulate the data as you need. 

In this [REPL](https://replit.com/@msoutopico/langtagspyclient#readme.md) you cansee a few practical examples of what you can do with the data.

## Node.js

From Node.js applications (or applications that can run Javascript code), e.g. Inky, you can obtain the langtags data with the code below:

```
import fetch from 'sync-fetch'
const url = 'https://capps.capstan.be/langtags_json.php'
const json = fetch(url, {}).json()
const langtags = Object.values(json) // object type
```

The data obtained above will contain a Javascript object. You can also use module `node-fetch` if you prefer to do this asynchronously.

In this [REPL](https://replit.com/@msoutopico/langtagsjsclient#readme.md) you can see a few practical examples of what you can do with the data.

## Other implementations

Other implementations (e.g. curl) are feasible, feel free to experiment on your end. 

Here come just a couple of examples (courtesy of Mr. Mathot -) You can get the whole resource with the following command:
```
curl -X GET https://capps.capstan.be/langtags_json.php | jq
```

Or you can get a specific langtag record with:

```
curl -X GET https://capps.capstan.be/langtags_json.php | jq 'map(select(.cApStAn | contains("fra-BEL")))'
```
