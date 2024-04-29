---
share: true
where: https://odoo.capstan.be/web#id=332&action=871&model=knowsystem.article&view_type=form&cids=1&menu_id=592
---

# Word count analysis -- discrepancies in CAT tools

Word count analysis depend on the definition of "word", which (for the purposes of word count analyses of source texts in Latin alphabet) is considered to be a unit of text between word boundaries (e.g. spacing and punctuation symbols). 

However, different tools will use different parameters to count words, so it's not realistic to expect reports from different tools to be always identical. If you add tags (e.g. `<b>`) or escaped tags (e.g. `&lt;b&gt;`) to the equation, this gets more complex. 

For example:

  * **memoQ** has a simple approach: it simply counts chunks of text between spaces and does not consider escaped tags as unitary tokens.
  * **OmegaT** counts escaped tags as unitary tokens but for example considers the Saxon genitives as independent words.
  * **Rainbow** ignores escaped tags and considers Saxon genitives as a suffix, thus as part of the preceding word.

Therefore, the string `wall’s&lt;br /&gt;` will yield totally different counts in the three tools considered above:

| memoQ                | OmegaT               | Rainbow                   |
|---|---|---| 
| 2 words              | 3 words              | 1 word                    |
| <span style="border:2px solid red;">wall’s&amp;lt;br</span> <span style="border:2px solid purple;">/&amp;gt;</span> |  <span style="border:2px solid red;">wall</span><span style="border:2px solid blue;">’s</span><span style="border:2px solid purple;">&amp;lt;br /&amp;gt;</span> |  <span style="border:2px solid red;">wall’s</span>&amp;lt;br /&amp;gt; | 

Other characters might be differently estimated too. The example above does not mean to be comprehensive. 

