# How to obtain an automated translatability report in OmegaT

## Preconditions

Get the ["TA - Translatability Assessment" script](http://cat.capstan.be/OmegaT/customization/scripts/ta_translatability.groovy) and install it in OmegaT (in the user configuration > `scripts` folder).

## Steps

1. Create an OmegaT project with language pair `en` - `ta` and remove tags in the settings.
2. Add source file(s).
3. Run the `TA - Translatability Assessment` script. It might take a while depending on the volume. Check the status bar to see when the script is done.
4. When the script execution is completed, press **Ctrl+S** to register all translations.
5. Run script "Write Project to Excel" to export source text and notes to Excel.
6. Fetch the report from the `script_output` folder in the project.
