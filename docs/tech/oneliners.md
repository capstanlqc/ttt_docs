# Terminal oneliners

## Bash pipelines

> Shared in KS [here](https://odoo.capstan.be/web#id=422&action=871&model=knowsystem.article&view_type=form&cids=1&menu_id=592).

### Check completion of project

Gives you the number of remaining segments in an OmegaT project, if it’s not 0 that means that not all segments are translated. It’s not advisable to match literally the word “Remaining:” in that line because when the user has changed the UI language, this word might be localized.
```bash
head -6 project_stats.txt | tail -1 | sed -E 's/[[:space:]]+/#/g' | cut -d# -f2
```

### Avoid concurrent OmegaT execution 
This loop can be used to delay the execution of a new OmegaT.jar while there's already one running:
```bash
while [[ $(expr $(ps aux | grep OmegaT.jar | wc -l)) -gt 1 ]]; do sleep 1; done
```

### Perl replace

Replaces in text file.
```bash
perl -pi -e 's/foo/bar/g' file
```

### Watch for event

Watches folder for events:
```bash
inotifywait -r -m . [-e create] [-e delete] [-e etc]
```

### Update zip bundle

Updates a zip with files from a number of directories:
```bash
here="$(pwd)"; for d in $(find $here -name dir_name*); do cd $d; \
zip -ur /media/data/data/company/path/to/zipfile.zip file*; done; cd $here
```

### Count elements

Gets the number of translation units in PISA TMs for French:
```bash
/var/www/capps/TM_by_container$ for f in $(find . -name "*PISA*fra-FRA*.tmx"); \
do grep '</tu>' $f; done | wc -l
```

Gets the number fo translation units in TMs that are not PISA for French:
```bash
/var/www/capps/TM_by_container$ for f in $(find . -name "*fra-FRA*.tmx"); \
do if [[ "$f" == *"PISA"* ]]; then :; else grep '</tu>' $f; fi; done | wc -l
```

### Send request to xDiff

Posts two OMT packages to xDiff to produce a diff report:
```bash
curl -L -X POST 'https://capps.capstan.be/xdiff_cg_api.php' \
-H 'Content-Type: application/x-www-form-urlencoded' \
-F 'omt_pkg_1=@"file1.omt"' \
-F 'omt_pkg_2=@"file2.omt"' \
-F '{"token": "202020", "app": "xdiff", "rows": "different"}'
```

### Set file access control lists

Removes the extended permissions from the Windows domain:
```bash
setfacl -bR /your/file
```

### Finding stuff

Finds subfolders which are not empty

```bash
find /path/to/dir ! -empty -maxdepth 1 -type d
```

### List files in project package

Lists external TMs added to a series of OMT packages:
```bash
for o in $(ls *.omt); do echo "#" $o; unzip -l $o | grep '\.tmx' | \
tr -s ' ' | cut -d ' ' -f5; echo "---------------------------"; done
``` 

### Copy and transforms 

Reads what is in your clipboard, modifies it, and puts it back in your clipboard (can be put in a function in ~/.bashrc), after doing some replacements:
```bash
xsel -o -b | sed -r 's#\\+#/#g' | sed 's#192.168.67.50#media/data#' | \
sed 's#U:#/media/data/data/company#' | xsel -i -b
```

### From and to server

Downloads files from Ur:
```bash
scp user@192.168.67.50:dir_or_ln_in_home/foo/bar/files*.ext .
```
Source: [here](https://unix.stackexchange.com/questions/106480/how-to-copy-files-from-one-machine-to-another-using-ssh/106482#106482)

Uploads files to Ur:
```bash
scp file(s) user@192.168.67.50:dir_or_ln_in_home/foo/bar
```

### Replaces in text files

Removes line breaks in markdown files, only in the middle of sentences but not anywhere else:
```bash
perl -i -00pe 's/^(?!```)(.+[a-z),])\p{Zs}*[\r\n](?=[a-z{])/$1 /gm' *
```

### Matches in files

Find files that contain a certain pattern:
```bash
grep -rnw '/path/to/somewhere/' -e 'pattern'
```

### Move files to their batch folder

The following loop gets the batch (key) including each file in the YAML config and copies the file from `new-keys/03_lint` to the batch folder that corresponds under `RELEASE_A`:

```bash
for f in $(cat pisa25_files.yaml | shyaml get-value releaseA | sed 's/^- //' | \
cut -d':' -f1); do b=$(grep -Poh "(?<=${f}: ).+" pisa25_files.yaml) && echo $b \
&& find new-keys/03_lint -name $f && cp new-keys/03_lint/$f RELEASE_A/$b; done
```
!!! note
    File and folder names can be probably simplified.


### Edit subnodes in XHTML files

The following command finds HTML files that do not (`-L`) contain `<meta charset="utf-8"/>` and adds that node to them at the bottom of the head section:

```bash
find $work_path -name "*.html" -type f -exec grep -L '<meta charset="utf-8"/>' \
{} \; -exec xmlstarlet ed --inplace --subnode "/html/head" --type elem -n meta \
-i /html/head/meta -t attr -n charset -v "utf-8" {} \;
```

### Extract key and text

Given a number of XML files containing labels such as:

```xml
<label key="item1_93cba07454f06a4a960172bbd6e2a435_25">
<text>Yes</text>
</label>
```

The following oneliner extracts filename, key and text:

```bash
pcregrep -Mo --color \
'(?<=key=")[^"]+?(?=")(?:[\s\S\n]+?<text>)[\s\S]+?(?=</text>)' *.xml | \
perl -0777 -pe 's/">[\s\n]+<text>/:/gm' | xsel -ib
```

### Adds node in HTML/XML

Adds `<meta charset="utf-8"/>` when missing in HTML files:
```bash
find $work_path -name "diffte*t.html" -type f \
-exec grep -L '<meta charset="utf-8"/>' {} \; \
-exec xmlstarlet ed --inplace --subnode "/html/head" --type elem -n meta \
-i /html/head/meta -t attr -n charset -v "utf-8" {} \;
```

### Git / restore TMs

Steps to restore translations deleted in the previous commit:

```bash
git checkout [previous-commit-before-the-commit-that-deleted-translations]
cp omegat/project_save.tmx ../03d9f5e.tmx # where 03d9f5e is the commit hash
git checkout main
mkdir tm/auto/restored
mv ../03d9f5e.tmx tm/auto/restored 
git pull && git add . && git commit -m "Restored translations from day Nov 3, accidentally removed" && git push 
```

## Resources

[https://linuxcommandlibrary.com/basic/oneliners](https://linuxcommandlibrary.com/basic/oneliners)