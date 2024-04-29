# ITS-based SSMC translation workflows
SSMC = single-source multiple-channel

## Internationalization Tag Set (ITS) 

The example below shows how the Internationalization Tag Set (ITS) data categories (using the Locale Filter data category expressed globally) can be used to filter content based on countries' preferences, to allow a unified authoring process and a homogeneous translation workflow regardless of how content is published afterwards.

This sample contains two `localeFilterRule` elements: The first one specifies that the elements `label` with a `channel` attribute set to "pba" apply only to the  locales corresponding to countries that take the paper-based administration (PBA). The second one specifies that the elements `label` with a `channel` attribute set to "cba" apply to all locales corresponding to countries that take the computer-based administration (CBA). 

```xml
<?xml version="1.0" encoding="UTF-8"?>
<instrument xmlns:its="http://www.w3.org/2005/11/its" its:version="2.0">
    <info>
        <its:rules version="2.0">
            <its:localeFilterRule selector="//label[@channel='pba']" localeFilterList="*-KH, *-GT, *-IN, *-PY, *-VN"/>
            <its:localeFilterRule selector="//label[@channel='cba']" localeFilterList="*-KH, *-GT, *-IN, *-PY, *-VN" localeFilterType="exclude"/>
        </its:rules>
        <response>
            <code>Q03HA</code>
            <label channel="cba">Click on the link to fill out the form</label>
            <label channel="pba">Turn the page to fill out the form</label>
        </response>
    </info>
</instrument>
``` 

[More info](https://www.w3.org/TR/its20/#LocaleFilter).