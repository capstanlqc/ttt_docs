# FLASH: automation diagram ☆

### Scripts:

```
crontab -> launcher.sh
            ├──> flash_init.sh
            │    ├──> flash_prepp_extract.py
            │    ├──> conv_mrt2tmx.py
            │    └──> flash_version.sh (loop)
            │         └──> flash_create_omtprj.py
            ├──> flash_post.sh
            │    ├──> flash_mk_ada_pkgs.py
            │    ├──> flash_mt_omtexp_to_mf.py
            │    ├──> flash_prepp_merge.py
            │    └──> checker.sh
            ├──> xdiff_poster.sh
            └──> update_docs.sh
                 └──> update_docs.py
```

### Docs:


```
flash_prepp_help (original Ur)
└──> docs/
     └──> post to https://capps.capstan.be/doc/ (doc online)
          └──> save to U:\IPSOS\EUROBAROMETER_FLASH_2.0\02_AUTOMATION\Doc
```


## Explanation of each script

| Abbrev | Explanation   |
| --------- | --------- | 
init | initialization
prepp | preparation
extract | extraction
omtprj | OmegaT project
mrt2tmx | conversion of translation found in the MRT into the TMX files
flash_version.sh | Loops through all version folders found and calls `flash_create_omtprj.py`.
post | post-processing (merge etc.)
mk | make
ada | adaptation
pkgs | packages
mt | machine translation
omtexp | Excel export of the OmegaT project
mf | monitoring form
merge | merge

---

