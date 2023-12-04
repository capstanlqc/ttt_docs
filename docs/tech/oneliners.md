# Terminal oneliners

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
pcregrep -Mo --color '(?<=key=")[^"]+?(?=")(?:[\s\S\n]+?<text>)[\s\S]+?(?=</text>)' *.xml | perl -0777 -pe 's/">[\s\n]+<text>/:/gm' | xsel -ib
```




## Resources

[https://linuxcommandlibrary.com/basic/oneliners](https://linuxcommandlibrary.com/basic/oneliners)