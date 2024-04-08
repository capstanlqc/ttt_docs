# How to update the issues tracker

1. Add the new ticket(s) to the `OmegaT_issues.xlsx` file, save when done
2. Save as `OmegaT_issues_nopw.xlsx` (no password), making sure columns G,H,I are removed and that the file is not password-locked
3. Within folder `capstanlqc/ttt_docs/docs/tools/tickets` (where the reports and the script sit), run `python tickets_xls2md.py` to update the markdown document
4. Commit changes

<!-- todo: transfer this to capps/docs for a cleaner single page -->