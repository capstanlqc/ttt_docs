---
share: true
where: https://odoo.capstan.be/web#action=871&cids=1&id=617&menu_id=592&model=knowsystem.article&view_type=form
tags:
  - Audience꞉Tech
---

# Segmenting with SRX

This is a short guide about segmentation using the SRX standard in OpenXLIFF. 

## Default ruleset

I think a simple example can be useful, so consider the following scenario. The following JSON file needs to be prepared for translation (converted to XLIFF):

```json
{
    "paragraph": "This is one sentence. This is another sentence!! Mrs. 
    are a married person. The U.S.A. is a great country, e.g. not like 
    the US. The Dept. Of Finance has the blessing of Rev. Johnson. Let's 
    go climb Mnt. Everest."
}
```

You may create an XLIFF file with the OpenXLIFF library:

```bash
bash ~/Apps/maxprograms/OpenXLIFF/convert.sh -file file.json -srcLang en \
-tgtLang el -type JSON -embed -xliff file.xlf -2.0
```

The OpenXLIFF library uses segmentation by default (using the built-in [default ruleset](https://github.com/rmraya/OpenXLIFF/blob/master/srx/default.srx)), and produces the following segments: 

    ✅ This is one sentence.
    ✅ This is another sentence!!
    ✅ Mrs. are a married person.
    ✅ The U.S.A. is a great country, e.g. not like the US.
    ❌ The Dept.
    ❌ Of Finance has the blessing of Rev. Johnson.
    ❌ Let's go climb Mnt.
    ❌ Everest.

<!-- 
```xml
<segment id="0-0">
  <source>This is one sentence.</source>
</segment>
<segment id="0-1">
  <source> This is another sentence!!</source>
</segment>
<segment id="0-2">
  <source> Mrs. are a married person.</source>
</segment>
<segment id="0-3">
  <source> The U.S.A. is a great country, e.g. not like the US.</source>
</segment>
<segment id="0-4">
  <source> The Dept.</source>
</segment>
<segment id="0-5">
  <source> Of Finance has the blessing of Rev. Johnson.</source>
</segment>
<segment id="0-6">
  <source> Let's go climb Mnt.</source>
</segment>
<segment id="0-7">
  <source> Everest.</source>
</segment>
```

```xml
<segment id="0-0">
  <source>This is one sentence.</source>
</segment>
<segment id="0-1">
  <source> This is another sentence!!</source>
</segment>
<segment id="0-2">
  <source> Mrs. are a married person.</source>
</segment>
<segment id="0-3">
  <source> The U.S.A. is a great country, e.g. not like the US.</source>
</segment>
<segment id="0-4">
  <source> The Dept. Of Finance has the blessing of Rev. Johnson.</source>
</segment>
<segment id="0-5">
  <source> Let's go climb Mnt. Everest.</source>
</segment>
```

-->

You can see that the default segmentation rules correctly recognize "Mrs.", "U.S.A.", "e.g." and "Rev." as abbreviations and did not start a new segment after those. 

However, it fails to recognize "Dept." and "Mnt.", hence splitting the last two sentences in two parts. This kind of segmentation defect may be more or less common depending on the content, but it's a common practice to fix them.

## Customizing rules

To amend the problem above, one can use a custom SRX. I have made a copy of the custom.srx included in the OpenXLIFF library, and added a couple of rules that prevent breaking at those two points:

```xml
<rule break="no">
	<beforebreak>Dept\.</beforebreak>
	<afterbreak>\sOf</afterbreak>
</rule>
<rule break="no">
	<beforebreak>Mnt\.</beforebreak>
	<afterbreak>\s(Everest|Kilimanjaro)</afterbreak>
</rule>
```

I can now use the `-srx` argument to point to my segmentation rules: 
  
```bash
bash ~/Apps/maxprograms/OpenXLIFF/convert.sh -file file.json -srcLang en \ 
-tgtLang el -type JSON -embed -xliff file.xlf -2.0 -srx custom.srx
```

The result is correct now: 

    ✅ This is one sentence.
    ✅ This is another sentence!!
    ✅ Mrs. are a married person.
    ✅ The U.S.A. is a great country, e.g. not like the US.
    ✅ The Dept. Of Finance has the blessing of Rev. Johnson.
    ✅ Let's go climb Mnt. Everest.

This kind of rule customization is a common operation in the preparation of translation projects, regardless of the preparation tool used (SRX is a standard that all modern translation tools should understand).

## Update SRX rules

One can edit the SRX file directly as XML (assuming good knowledge of the SRX standard) or by other means, but there are off-the-shelf editors for that, e.g. https://www.maxprograms.com/products/srxeditor.html).

## References

Some more info:
https://en.wikipedia.org/wiki/Segmentation_Rules_eXchange

OpenXLIFF's default ruleset:
https://github.com/rmraya/OpenXLIFF/blob/master/srx/default.srx
