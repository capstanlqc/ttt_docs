# FLIP+ -- Translation aspects

## 1. Assumed tasks:

### Lot 1

1. Submission (or creation) of items in national languages
2. Harmonization of items in the IMS Question and Test Interoperability specification (QTI) format

### Lot 2

3. Machine translation into English of existing items
4. Human translation of existing items into other national languages (from English or from the original language)

## 2. Requirements for Lot 1

+ To integrate translation solutions, the "platform" ideally runs in a server (preferably running Linux) where other applications and services can be run on schedule.
+ Languages should be correctly identified in the preamble[^1] of QTI (XML) files and/or in file names using  BCP-47 language tags[^2].
+ XLIFF[^3] is optional. If XLIFF is used, the XLIFF round-trip should be handled using open-source libraries and filters such as Okapi Rainbow[^4] or OpenXLIFF[^5], *not* hand-writing XLIFF or creating it with home-made routines. cApStAn can provide insight in good practices for the use of these tools.

## 3. Technical aspects 

cApStAn can provide support with regard to translation tools and preparation of translation kits for language tasks.

### 3.1. Translation formats 

QTI is an ideal format for translation and can [most probably] be imported and translated directly in the translation tool without the need to use XLIFF. The input to translation projects would be a monolingual QTI file in the source language and the output would be the equivalent QTI file in the target language (also monolingual). 

XLIFF[^3] has some advantages but also entails further complexity and know-how. If deemed more convenient to use XLIFF, it's possible to convert QTI files to and from XLIFF. The referred open-source libraries and filters should be used to create XLIFF files.  

Other monolingual (or bilingual) formats are also possible, such as JSON, either preparing them as XLIFF or translating them directly without intermediary formats.

### 3.2. Translation tools

If XLIFF files are to be created, localization engineering tools (such as Okapi Rainbow[^4] or OpenXLIFF[^5]) must be used. cApStAn can provide insight in good practices for the use of these tools.

cApStAn proposes OmegaT[^6] as the translation editor. OmegaT is a multiplatform computer assisted translation (CAT) tool with fuzzy matching, translation memory, keyword search, glossaries, and translation leveraging into updated projects. cApStAn can provide support and customization[^7] to optimize its usage.

OmegaT's is free software and open source. Its code is freely available online[^8], which would allow Java developers in OAT to create their own build (installer) with modified functionality to fit their own purposes if needed. 

### 3.3. Language tasks and MT

Machine translation can be implemented in different ways:

+ integrated in the server (or perhaps the platform)
+ called up by translators in the translation tool on demand

For the first option, cApStAn can provide recommendations for implementation and sample code[^9] that could be used to translate batches of text in order to provide translation kits with translations ready for review or post-editing. MT vendors provide libraries in the most common programming languages[^10]. 

A paid subscription to the MT provider is generally required, but if data privacy is not an issue and translation volumes are low (max. 500,000 characters/month), perhaps a DeepL API Free subscription (for Developers) would be sufficient. 

Raw machine translation should be not be used for final publication, instead it should be post-edited. Linguist working on post-editing tasks need to have received (or be provided) specific training for that.

### 3.4. Translation kits

Translation projects could be offline (transferred as zipped packages) or online (handled as Git repositories[^11]). cApStAn can provide OmegaT project templates, in either case[^12]. If translation projects are online, Github can be used to automate them[^13]. 

Online team projects can be permanent containers (one repository per language pair) where files are added as they become ready for translation and removed as their translation is completed, no need to create a project every time a file must be translated. If there's a variety of different domains or subject fields and it's convenient not to mix them in the same container, a repository can be created for each language pair and domain combo.

Permanent containers would greatly simplify TM management and file management in general and would remove the need of workflows on demand, but it of course depends on how translation is to be done. If it's not a problem for a translator to see other files or folders in the project that other translators are busy with, it could work. It they need separate containers for each translation job, then a workflow on demand  seems better. 

### 3.5. Preview

How preview is implemented depends in fact on the implementation of translation kits, but there are a few options, e.g. 

1. Copying or creating symlinks of the target files to the place in the server where they are expected to generate the preview
2. Posting translations directly from OmegaT to an API endpoint: the request includes the translations and the response with the URL that must be opened in the browser in the local machine.
3. Other options might be feasible too.

## 4. Support to translators

OAT+ cApStAn may provide training and support to countries wishing to have translation kits prepared for them. 
Training would be contingent on the specific implementation so it only makes sense to elaborate materials once the full structure is in place. 

## References

[^1]: For language identification in the preamble of XML files, see [https://www.w3.org/TR/REC-xml/#sec-lang-tag](https://www.w3.org/TR/REC-xml/#sec-lang-tag)
[^2]: See "related links" section in [https://www.w3.org/International/articles/language-tags/](https://www.w3.org/International/articles/language-tags/)
[^3]: See [https://github.com/capstanlqc/i18n_guide/blob/main/xliff-prepp-best-practices.md](https://github.com/capstanlqc/i18n_guide/blob/main/xliff-prepp-best-practices.md)
[^4]: See [https://okapiframework.org/wiki/index.php/Rainbow](https://okapiframework.org/wiki/index.php/Rainbow)
[^5]: See [https://github.com/rmraya/OpenXLIFF](https://github.com/rmraya/OpenXLIFF)
[^6]: OmegaT's official site: [https://omegat.org/](https://omegat.org/)
[^7]: Instructions for customizing OmegaT: [https://github.com/capstanlqc/omegat_customization](https://github.com/capstanlqc/omegat_customization)
[^8]: OmegaT's code is publiclly available at [https://github.com/omegat-org/](https://github.com/omegat-org/)
[^9]: See this piece of code for batch translating text with DeepL (API Pro authentication key for developers required): [https://gist.github.com/msoutopico/d3420e68c4ce746351b80bfe0165ea1c . Full documentation available here: https://www.deepl.com/docs-api.](https://gist.github.com/msoutopico/d3420e68c4ce746351b80bfe0165ea1c . Full documentation available here: https://www.deepl.com/docs-api.)
[^10]: See the full official documentation for integrating DeepL in Python applications: [https://github.com/DeepLcom/deepl-python](https://github.com/DeepLcom/deepl-python)
[^11]: See [https://omegat.sourceforge.io/manual-standard/en/howtos.html#howto.useteamproject](https://omegat.sourceforge.io/manual-standard/en/howtos.html#howto.useteamproject)
[^12]: Project package templates available at [https://github.com/capstanlqc/omegat_package_templates for XLIFF and Word. @TODO: One more template will be added for QTI.](https://github.com/capstanlqc/omegat_package_templates for XLIFF and Word. @TODO: One more template will be added for QTI.)
[^13]: See [https://capps.capstan.be/doc/team_projects.php](https://capps.capstan.be/doc/team_projects.php)