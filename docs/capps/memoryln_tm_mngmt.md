# MemoryLn -- TM management ☆

<!-- published at
https://odoo.capstan.be/web#id=197&action=871&model=knowsystem.article&view_type=form&menu_id=592 -->

Putting content in MemoryLn serves two purposes: one is that linguists or any stakeholder can look up translations and terminology, another one is to gradually build a corpus that we can use for other tasks in the long run, such as doing language research or NLP tasks (e.g. MT training), etc. 

> If our data is scattered we might be wasting potential for data-powered tasks, and that's the reason why archiving the final TMs of each project should be one of the mandatory steps in the PM's checklist, without which the project cannot be considered closed.

This guide describes the life cycle of translation memories (TM), from their creation up to how they can be used, using MemoryLn both as repository and lookup tool.

### Roles and responsibilities 

Several roles are involved in TM management: 

| Role | Person | Responsibility  |
|:---|:---|:---|
| Project manager | (per-project) | owner of the project and its language assets, and therefore responsible for managing them appropriately, with the support of the tech team (TT). |
| Container manager | Laura#?/Valentina | responsible for creating glossaries and TMs upon PM's request or upon their own initiative whenever appropriate. The PM is encourage to as a member of the TT to play this role but might designate someone else if they feel confident. |
| Language asset manager | ? /Valentina? | responsible for creating containers in cApps' [**Containers Manager**](https://capps.capstan.be/containers_edit.php) whenever appropriate and adding details (description, tages, etc.) |
| Language code manager | Steve/Manuel | responsible for creating and maintaining [language codes](http://capps.capstan.be/langtags.php) |

### Summary

The next steps must be followed:

1. Check that the container exists in the [**Containers Manager**](https://capps.capstan.be/containers_edit.php) and check with the container manager if you can't find it there.
2. Check that the language version exists in the [**Language code finder**](https://capps.capstan.be/langtags.php) and check with the language codes manager if you can't find it there.
3. Ask the language asset manager of the project (preferably, a TT member) to create the TMX files.
3. Put TMX files in the container folder in Ur.



## Creating TMs

TMs can be created in different ways, depending on the starting point: 
- OmegaT: press **Ctrl+D** from the project in question (or `console-translate` the project)
- memoQ or Trados: use the relevant export options
- Excel/CSV: use [TMX Editor](https://www.maxprograms.com/products/tmxeditor.html) or the [`conv_xls2tmx.py`](https://github.com/msoutopico/cli_automation/tree/master/conv_multilingual_wb_to_tmxs) script
- alignment: use [LF Aligner](https://sourceforge.net/projects/aligner/), [Paralela](https://paralela.logrusglobal.com/home) or any other CAT tool's alignment module.

If you must convert one spreadsheet (for one language pair) to one TMX file, [TMX Editor](https://www.maxprograms.com/products/tmxeditor.html) is a very useful tool. If you have a multilingual spreadsheet, however, the [`conv_xls2tmx.py`](https://github.com/msoutopico/cli_automation/tree/master/conv_multilingual_wb_to_tmxs) script, however, is going to be more efficient (all TMX files are generated in one go if the spreadsheet has the expected format).

>  It goes without saying that the TMX file must be well-formed and valid according to XML syntax and type definition.

The activity of creating TMs to be uploaded to MemoryLn must observe some constraints: 
+ TMX filename patterns
+ Language tags

### TMX filename

The file name of the TMX file is meaningful, in the sense that information is obtained from it and the file is handled diferently depending on its name. Elements can be many (e.g. organization/client, container, project or project  cycle, unit identifier, unit name, target language code, source language, etc.) depending on each particular case, of which only two are mandatory:

+ the name of the **container**, e.g. `PISA` (not the project cycle, e.g. `PISA2018`, though)
+ the **target language code** as per [cApStAn’s convention](http://capps.capstan.be/langtags.php).

> Before you can use an XML language tag or a language code, an entry for that language version needs to exist in the [Language code finder](http://capps.capstan.be/langtags.php). If you can find your language version there, please ask the language code manager to create it. 

The source language could optionally be indicated if deemed necessary (e.g. if different from English). Only the language tag is necessary.

The different elements in the file name must always be separated by **underscore**. For example: `PISA_eng-USA_MAT_M033-AViewRoom_eng_MS2015.tmx`.

#### Other language code conventions

Other organizations or tools normally have different language codes. If you produce TMX files that inherit a filename with language codes in other conventions, the language code must be converted to [cApStAn’s convention](http://capps.capstan.be/langtags.php).

> For TMX files converted from PISA XLIFF files, or for PISA files in general, many language codes match cApStAn's  convention, but some differ, so **those must be converted**. For example, files with  `cym-QUK` in their name need to be renamed to use `cym-GBR` instead. 

### Internal language tags

The TMX file's internal language code must follow [our convention for OmegaT projects](http://capps.capstan.be/langtags.php). For example, for Dubai's Arabic, use `ar-DU`, rather than `ar-AE-dubai` (BCP-47) or `ara-UAE` (cApStAn/PISA).<!-- to be updated when migrating to BCP-47 -->

For the target language, the full language tag must be used. However, for the source language only the language subtag is needed, since MemoryLn ignores anything else after the language subtag (there’s only `en` and `fr` in the list above) -- although the full language tag (e.g. `en-US`, `en-GB`, `en-ZZ`) should work just fine too.

<!-- You may edit a TMX file in any text editor (such as Atom, Sublime, etc.) or an XML editor. You can open all the TMX you need to edit, then open the Search  functionality, search for the current code and if needed type the  corrected code and then click on select “Search and replace in all open documents”. You may also used a command line utility (e.g. `perl -pi -e 's/xx/yy/g' file.tmx`) or ask someone in the tech team to do that for you. -->

#### Language tag checklist

To minimize the number of issues that need to be fixed later, please remember the following guidelines with regards to language codes when you create TMX files:

1. The expected order is language subtag, then region subtag: `fr-BE`is okay, but `be-FR` or `BE-fr` are not. <!-- to be updated when migrating to BCP-47 -->
2. The character that separates the two or more subtags in a language tag is a hyphen: `fr-BE` is OK, but `fr_BE` is not.
3. Please use the same case as you see in the [Language code finder](http://capps.capstan.be/langtags.php): language subtag in lower case, region subtag in upper case, etc.
4. Indicate the source-language code in the `srclang` attribute of the `header` node of the TMX file.
5. The value of the `header/@srclang` attribute must match the value of the `@lang`  attribute of the source-language `tuv/seg` nodes.
<!-- srclang = en (with or without a region subtag, US, GB, ZZ, ) same as the tu lang? -->

> For MemoryLn, case (point 3 above) doesn't actually really matter, since to avoid mismatches due to different case all language codes are lower-cased before running searches. However other applications might rely on case to match language codes, and it's also better to be visually consistent with the language code used in the filename (especially considering we used to have the opposite order, i.e. `CCC-lll`).

## Adding TMs to MemoryLn

The PM has full access to how TMX files and can decide how TMs are organized.

### Location in the server

Once they are created, TMX files must be put in their corresponding **container** folder in Ur. The path to the container folder in Ur would be `/media/data/data/company/R&D/05_LangAssets/01_TMs/MemoryLn/[CONTAINER]` (which is probably accessible as `U:\R&D\05_LangAssets\01_TMs/MemoryLn\[CONTAINER]` on your Windows machine).

> Before you can put TMX file in its container folder in Ur, the container must have been created in the [**Containers Manager**](https://capps.capstan.be/containers_edit.php). If you can't find your container there, please check with the container manager.

## TM maintenance 

Attention points for the language asset manager:

### Penalties 

It is possible to apply a penalty to a TM, which will reduce the matching score in MemoryLn as in OmegaT. Reducing the matching score in MemoryLn means that results from that TM will appear below results that have a higher score. The penalty in MemoryLn is applied to the TMX file, not the match.

This can be useful when TMs for a new cycle are released and should be given priority over older TMs for previous cycles, or it can be useful to distinguish between high-quality TMs and those that are less reliable for whatever reason -- the way to give priority to new assets is to penalize old assets. 

The procedure to apply penalties is [the same as in OmegaT](https://omegat.sourceforge.io/manual-latest/en/project.folder.html). For TMs in folders with a name `penalty-xxx` (`xxx` being a number between 0 and 100), matches will be degraded according to the name of the folder: a 100% match residing in a folder called, say, `penalty-30` will be lowered to a 70% match. 

### Sanity checks

When TMX files are added to the container folder, the [overhaul_langtags_in_tmx.sh](https://gist.github.com/msoutopico/7cdb6b0397f4a8d51eabb93890102ea1) script will run on them to detect any possible problems in the constraints described above. 

If any issues are found, they will be reported in a issues file with the date of that day (e.g. `issues_2021-09-22.txt`), and a monthly issues file is compiled with all issues found that month and in previous months that haven't been solved yet.

The actions required are
- check for any issues file for that day or that month
- read each line in the issues file and see what is wrong
- fix every issue (or ask TT to do it, if you are not 100% sure)
- delete the issues file of that day
- verify one hour or one day later that the issue is not flagged again

### Metadata clean up 

To avoid making TMX files unnecessarily heavier, empty properties can be removed. <!-- , e.g. `      <prop type="domain"/>`.-->For example:
```
<prop type="client"/>
<prop type="domain"/>
<prop type="project"/>
<prop type="subject"/>
```
You might also want to remove some non-empty properties if they are irrelevant: 

```
<prop type="corrected">no</prop>
<prop type="aligned">no</prop>
<prop type="x-document">en.json</prop>
<prop type="x-context">examSessionModal.okButton</prop>
```

The same applies to proprietary metadata (added by some commercial CAT tool) that both MemoryLn and OmegaT ignore, such as namespaced tags, e.g. `<mq:foo>`.








<!-- .gitignore : *.tmx ? -->



<!-- PISA25:
create one TMX per file.
- take files out of the project 
- for each file, put it in the project
- rename the project as the file
- run console-translate
- fetch leve1 tm
-->


<!-- containers/scopes: 
- type: project, client, domain
-->