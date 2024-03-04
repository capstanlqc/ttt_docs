# How to create T&A notes in OmegaT (second source)

## First time

Steps:

1. Create an OmegaT project with language pair `en` - `ta`, remove tags in the settings
2. Add source file
3. Write T&A notes as the translation whenever appropriate
4. Run script "Write Project to Excel" to export source text and notes to Excel
5. Run script "TA - Create T&A Notes TM" to copy the notes to the second source space (in `/tm/tmx2source`)

## Updates 

If a new version of the source file is submitted:

1. Add it to the previous project (optionally remove the old version).
2. Optional: Ctrl+D and move exported TM to `/tm/auto` to have background color in 100% matches
3. Tweak preferences to insert T&A notes for updated segments (up to a certain limit) -> draft notes
4. Go to next translated segment (Ctrl+Shift+U) to review the original notes (now drafts) in updated segments
5. When all drafts are reviewed, run steps 4 and 5 above if appropriate

## Finally

If the same project needs to be used for a real translation or as a template:

+ Run script "Flush Working TM" to flush the project's internal working TM (remove all translations)
