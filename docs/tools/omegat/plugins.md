# OMT Package Plugin

## Latest version

https://github.com/briacp/plugin-omt-package/releases

## How to create an OMT package on the command line

You can now create an OMT package without opening OmegaT.

On a Linux terminal (in Windows): 

``` bash
java -cp /mnt/c/Program\ Files/OmegaT/OmegaT.jar:/mnt/c/Users/<USER>/AppData/Roaming/OmegaT/plugins/plugin-omt-package-<version>.jar net.briac.omegat.plugin.omt.ManageOMTPackage <XXX_OmtPrj> <XXX_OmtPrj>.omt
```

Update the user config path accordingly (i.e. replacing `<USER>` with your actual username). 

On Windows CMD (notice the different classpath separator `;`, not `:`): 

```
java -cp "C:\Program Files\OmegaT\OmegaT.jar;C:\Users\<USER>\AppData\Roaming\OmegaT\plugins\plugin-omt-package-<version>.jar" net.briac.omegat.plugin.omt.ManageOMTPackage <XXX_OmtPrj> <XXX_OmtPrj>.omt
```

This allows you to batch process a number of projects:

```
for proj in `ls -d *_OmtPrj`; do java -cp /mnt/c/Program\ Files/OmegaT/OmegaT.jar:/mnt/c/Users/<USER>/AppData/Roaming/OmegaT/plugins/plugin-omt-package-<version>.jar net.briac.omegat.plugin.omt.ManageOMTPackage $proj $proj.omt; done
```

<!--- for proj in `ls -d *_OmtPrj`; do java -cp /mnt/c/Program\ Files/OmegaT/OmegaT.jar:/mnt/c/Users/souto/AppData/Roaming/OmegaT/plugins/plugin-omt-package-1.1.0.jar net.briac.omegat.plugin.omt.ManageOMTPackage $proj _Packages/$proj.omt; done -->

## Options

Note: the plugin can be configured by means of file `<config_dir>/omt-package-config.properties`. Example below:

``` java 
#
# OmegaT Plugin - OMT Package Manager
#
#    omt-package-config.properties
#

# List of regex pattern (separated by ";") of files to exclude when
# generating an OMT package. (default: "\\.(zip|bak|omt)$")
exclude-pattern=\.(zip|bak|omt|DOCX?|docx?)$;pseudoxlat;\.(utf8|tmx)\.2019;/?~

# The "\\" is needed because JAva needs the "\" to be escaped.
# The "/?" is to exclude files begining with ? (the /? is to make sure we catch the beginning of the filename)

# If set to true, the folder containing the exported OMT will be
# displayed. (default: false)
open-directory-after-export=true
# If set to true, the translated documents will be created before
# creating the package. (default: false)
generate-target-files=false
# If set to true, a dialog asking the user if they want to delete the
# imported OMT package will appear at the end of the importation.
# (default: false)
prompt-remove-omt-after-import=true

# If this property is set, the script located in the OmegaT scripts
# folder will be executed. The OMT package file is available in the
# binding "omtPackageFile". The console output is done in OmegaT
# logfile, not in the scripting window.
#post-package-script=processOmtPackage.groovy
```

## Help

Run line: 

```
java -cp /mnt/c/Program\ Files/OmegaT/OmegaT.jar:/mnt/c/Users/<USER>/AppData/Roaming/OmegaT/plugins/plugin-omt-package-<version>.jar net.briac.omegat.plugin.omt.ManageOMTPackage --help
```

to get the following message: 

```
usage: ManageOMTPackage [options] omegat-project-directory [omt-package-file]
 -c,--config <property-file>   use given file for configuration (default: /home/<USER>/.omegat/omt-package-config.properties)
 -h,--help                     print this message
 -q,--quiet                    be extra quiet
 -v,--verbose                  be extra verbose
```
