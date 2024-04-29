# YSC -- project setup 

- Responsible TT: Valentina
- Backup TT: Manuel (or Kos, in Manuel's absence)

## Summary of the project setup

- All team projects are hosted in github repositories under organization [https://github.com/capstanlqc-ysc](https://github.com/capstanlqc-ysc). 
- They pull settings and assets from [https://github.com/capstanlqc-ysc/ysc_settings](https://github.com/capstanlqc-ysc/ysc_settings) and [https://github.com/capstanlqc-ysc/ysc_assets](https://github.com/capstanlqc-ysc/ysc_assets) 
- They pull source files from the DevBridge's repository [https://dev.azure.com/YSCConsulting/Pheme/_git/Pheme%20Inbox](https://dev.azure.com/YSCConsulting/Pheme/_git/Pheme%20Inbox)
- The project settings include segmentation rules and filter parameters.

## Project requirements include: 

- extracting label's keys (resnames) as text unit IDs

## Potential TT actions

### 1. Update filter parameters to capture new node's keys

- DevBridge is expected to notify of any changes in source files in the Inbox repo. Whenever there are updates in source files, we must verify that the updates haven't affected the key extraction. 
- That check can be done exporting any of the projects as Excel and looking for keys that are pure segment IDs rather than resnames. 
- To fix any found issues, new xpaths must be added to the XML filter parameters to capture the key in the added/updated element nestings.

For example, the [ResX filter parameters](https://github.com/capstanlqc-ysc/ysc_settings/blob/master/okf_xml%40ysc.fprm) include an extraction rule that matches the key (i.e. `name` attribute) of items in unordered lists (i.e. `<ul>` element).
```xml
 <its:translateRule itsx:idValue="../../../@name" selector="//data/value/ul/li" translate="yes" itsx:whiteSpaces="default"/>
``` 
If the files are updated and ordered lists (i.e. `<ol>` element) are added, a new extraction rule must be added to the ResX filter parameters accordingly to match the new content: 
```xml
 <its:translateRule itsx:idValue="../../../@name" selector="//data/value/ol/li" translate="yes" itsx:whiteSpaces="default"/>
```
In the above examples, the `selector` matches the text node that must be translated and the `idValue` matches the key to identify that node. There must be one `translateRule` (extraction rule) for each text node that must be extracted for translation, including children of other extracted nodes.

The filter includes some working examples, if more rules are needed it's just a matter of finding what nodes are not matched in the new files and then reuse any of the working examples in the filter parameters and change it to match the new case.

### 2. Create mirror projects for gender adaptation

For some files three versions will be produced to address the target audience in three different ways: in a gender-neutral way, as a female respondent and as a male respondent. There will be: 

- one translation project, to produce the gender-neutral **base** version (which already exists)
- two adaptation projects, to produce the female and male versions, adapting the base version (to be created)

The two projects for the gender-oriented adaptation will include only specific files, not the whole set of source files, and will pull the base version dynamically through a repository mapping.

What to do:

1. For every locale, create the two repositories, which could be called:

  - ysc_LOCALE_fem_omt
  - ysc_LOCALE_mas_omt

	For example, for the female-target pt-PT project, if you use gh-cli, you would use the command `gh repo create capstanlqc-ysc/ysc_pt-PT_fem_omt --private --clone --team translators`. 

2. Make sure the "translators" team has write permissions to the projects you create. 

3. In each of the repos, create the OmegaT project and copy all the settings of the base version.

4. In order to pull just one file (or specific files) for the adaptation, modify the repository mapping that pulls the whole **Pheme%20Inbox** repo containing the source files to pull just the file(s) you want.

	In order words, remove the base mapping to the whole inbox repo and add the mapping for the file(s) you want: 

    ```
                <repository type="git" url="https://dev.azure.com/YSCConsulting/Pheme/_git/Pheme%20Inbox">
                    <mapping local="source/IdentityService/IdentityServerResources.en.resx" repository="IdentityService/IdentityServerResources.en.resx" />
                </repository>
    ```

5. Add the repository mapping to get the base version, which we want to be dynamic from the working TM of the base project: 

    ```
            <repository type="git" url="https://github.com/capstanlqc-ysc/ysc_&LOCALE;_omt.git">
                <mapping local="tm/auto/base/&LOCALE;.tmx" repository="omegat/project_save.tmx" />
            </repository>
    ```

That's it. 

The steps above are recorded in this video: https://player.vimeo.com/video/874375423 (password: Y$C)

##### References

- [https://capps.capstan.be/doc/team_projects.php](https://capps.capstan.be/doc/team_projects.php)

### 3. Reuse es-ES version as base for adaptation into es-MX

The starting point is two projects for two Spanish versions:

- ysc_es-MX_omt (adapting/borrowing)
- ysc_es-ES_omt (base/borrowed)

One third of the es-MX version has been produced (through adaptation of a es-ES base version). Now we want to do the same for the other two thirds, and we want the Mexican adaptor to focus only on on those two thirds (because the rest should be already good as it is). 

Follow these steps: 

1. Once the es-ES translation is finalized, export the master TM of that project (`Ctrl+D` produces three master TMs, the one which ends with  `-omegat.tmx` is the one we need. Rename the TM as `es-ES.tmx`.
2. In this TMX file, replace whatever values the attributes `tuv/@changeid` and `tuv/@creationid` with `base_es-ES`.
2. Put that TM in the `tm/auto/base/`folder of the es-MX project.
3. Instruct the es-MX adaptor to filter by author `base_es-ES` and adapt the visible segments.