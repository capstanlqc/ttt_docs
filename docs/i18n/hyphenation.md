---
share: true
where: 
---

<!-- <h1>Hyphenation internationalization</h1> -->
# ☆ Hyphenation internationalization

<!-- <h2>Breaking text manually</h2> -->
## Breaking text manually
<p>Ideally, we should produce translations that are independent of the display mode, and therefore render equally well in different kinds of devices and screens, or different sizes of brower or app windows.</p>

<blockquote class="hyph">
Since different browsers and different operating systems might display the text examples below different, this documentation item uses images (taken on Firefox 107.0 64-bit for archlinux) to ensure homogeneous viewing for all audiences. In any case, the original code used is included below (but commented out) so you can fork this article and play with that.
</blockquote>

<!-- <h3>Hard hyphens</h3> -->
### Hard hyphens

<p>
In the text below, the excesive horizontal separation between words in the penultimate line could be unpleasant to the eye.
</p>

<!-- 
<p class="textbox_short text">Bei den älteren Testpersonen war in diesen Regionen eine verminderte Aktivität erkennbar. Dies wurde allerdings durch die Aktivierung anderer Gehirnbereiche kompensiert. Eine dieser Regionen ist der Hippocampus, der als Sitz des Sprachgedächtnisses gilt und beim <span style="color:red">Auswendiglernen</span> aktiv ist.</p>
-->

<!-- <img class="hyph" src="https://imgur.com/llSvcdt.png" /> -->
![](../../_assets/img/llSvcdt.png)

<p>Translators might be tempted (or even instructed) to use a "hard" hyphen character to break the text at the end of the line, and that is likely to seem a good approach to fix layout issues like the one above. In the example below the text looks fine because the hyphen is inserted so as to suit the text box size. </p>

<!-- 
<p class="textbox_short text">Bei den älteren Testpersonen war in diesen Regionen eine verminderte Aktivität erkennbar. Dies wurde allerdings durch die Aktivierung anderer Gehirnbereiche kompensiert. Eine dieser Regionen ist der Hippocampus, der als Sitz des Sprachgedächtnisses gilt und beim <span style="color:red">Auswendig-lernen</span> aktiv ist.</p>
-->

<!-- <img class="hyph" src="https://imgur.com/AMKRyuO.png" /> -->
![](../../_assets/img/AMKRyuO.png)

<p>However, hard hyphens will always be rendered even if they are not needed anymore. That might cause an undesired effect if the size of the text box changes, either because the content must be rendered in another device with a smaller or bigger size screen or simply because the application design turns into a fluid layout, with a dynamic width, to deliver a responsive user experience.</p>

<p>See for example the same text box above with a slightly different size:</p>

<!-- 
<p class="textbox_long text">Bei den älteren Testpersonen war in diesen Regionen eine verminderte Aktivität erkennbar. Dies wurde allerdings durch die Aktivierung anderer Gehirnbereiche kompensiert. Eine dieser Regionen ist der Hippocampus, der als Sitz des Sprachgedächtnisses gilt und beim <span style="color:red">Auswendig-lernen</span> aktiv ist.</p>
-->

<!-- <img class="hyph" src="https://imgur.com/fkeiF42.png" /> -->
![](../../_assets/img/fkeiF42.png)

<p>Hard hyphens should be avoided both in translations and in the source text.</p>

<!-- <h3>Soft hyphens</h3> -->
### Soft hyphens

<p>An invisible, "soft" hyphen is not rendered visibly directly. Instead, it marks a place where the browser should break the word if hyphenation is necessary.</p>

<p>HTML provides the <code style="color:blue">&amp;shy;</code> named entity to insert a soft hyphen, however for translatability reasons it's always better to use plain Unicode text, i.e. in this case it's invisible character U+00AD (not used here because it's an invisible character). If for any reason it's not possible to use the Unicode character, hexadecimal entityes are always preferable than named entities, e.g. <code style="color:blue">&amp;#x00AD;</code> in this case.</p>

<p>See the result in the same text as above in text boxes of identical size. Here the soft hyphen causes hyphenation because the line wraps at that point:</p>

<!-- 
<p class="textbox_short manual text">Bei den älteren Testpersonen war in diesen Regionen eine verminderte Aktivität erkennbar. Dies wurde allerdings durch die Aktivierung anderer Gehirnbereiche kompensiert. Eine dieser Regionen ist der Hippocampus, der als Sitz des Sprachgedächtnisses gilt und beim <span style="color:red">Auswendig&#x00AD;lernen</span> aktiv ist.</p>
-->

<!-- <img class="hyph" src="https://imgur.com/wnyCk9l.png" /> -->
![](../../_assets/img/wnyCk9l.png)

<p>On the other hand, here hyphenation is unnecessary and therefore no hyphen is produced:</p>

<!-- 
<p class="textbox_long manual text">Bei den älteren Testpersonen war in diesen Regionen eine verminderte Aktivität erkennbar. Dies wurde allerdings durch die Aktivierung anderer Gehirnbereiche kompensiert. Eine dieser Regionen ist der Hippocampus, der als Sitz des Sprachgedächtnisses gilt und beim <span style="color:red">Auswendig&#x00AD;lernen</span> aktiv ist.</p>
-->

<!-- <img src="https://imgur.com/1ps2zKW.png" /> -->
![](../../_assets/img/1ps2zKW.png)

<p>
Authors and translators may use soft hyphens when that seems the only way to cause hyphenation in a preview (and this is always preferable to using hard hyphens). The authoring tool or the translation tool, respectively, should provide a practical means to insert that special character. However, internationalized products can be designed in a way that may make this manual approach unnecessary. 
</p>

<!-- <h2>Breaking text automatically</h2> -->
## Breaking text automatically

<p>Whereas soft hyphens can be useful as seen above, that method has a clear limitation: it requires knowing in advance where exactly the text might need to be hyphenated, however it's not always possible to foresee where words might need to hyphenate in all different potential layouts and displays. Automatic hyphenation might be more convenient for that reason.</p>

<!-- <h3>Hyphenating with styles</h3> -->
### Hyphenating with styles

<p>CSS provides properties that specify how words should be hyphenated when text wraps across multiple lines. Styling may be used to prevent hyphenation entirely, use hyphenation in manually-specified points within the text, or let the browser automatically insert hyphens where appropriate. Let's look at the third option.</p>

<!-- <h4>Automatic hyphenation by the browser</h4> -->
#### Automatic hyphenation by the browser

<p>Letting the browser hyphenate automatically allows authors and translators to focus on the text and not be distracted by layout issues. If the language expert confirms that results are correct, this approach may be prioritized.</p>

<p>See what automatic hyphenation yields in the two text box sizes considered (differences highlighted in red):</p>

<!-- 
<p lang="de" class="textbox_short auto text">Bei den älteren Testpersonen war in diesen Regionen <span style="color:red">eine</span> verminderte Aktivität erkennbar. Dies wurde <span style="color:red">allerdings</span> durch die Aktivierung anderer Gehirnbereiche <span style="color:red">kompensiert</span>. Eine dieser Regionen ist der Hippocampus, der als Sitz des Sprachgedächtnisses gilt und beim <span style="color:red">Auswendiglernen</span> aktiv ist.</p>
-->

<!-- <img class="hyph" src="https://imgur.com/vvByuHW.png" /> -->
![](../../_assets/img/vvByuHW.png)

<p>And:</p>

<!-- 
<p lang="de" class="textbox_long auto text">Bei den älteren Testpersonen war in diesen Regionen <span style="color:red">eine</span> verminderte Aktivität erkennbar. Dies wurde <span style="color:red">allerdings</span> durch die Aktivierung anderer Gehirnbereiche <span style="color:red">kompensiert</span>. Eine dieser Regionen ist der Hippocampus, der als Sitz des Sprachgedächtnisses gilt und beim <span style="color:red">Auswendiglernen</span> aktiv ist.</p>
-->

<!-- <img class="hyph" src="https://imgur.com/2DbrmWD.png" /> -->
![](../../_assets/img/2DbrmWD.png)

<p>The drowback of the automated approach is that it depends on the browswer having a hyphenation dictionary available for that language, which might not be the case for lesser used languages. Some research might be necessary to know for which language versions this is the case.</p>

<p>For language versions for which the browser does not have a hyphenation dictionary (if any!), a good compromise could be to use manual hyphenation based on the review for particular layouts. The person responsible for fixing layout issues (including hyphenation-related ones) may insert the soft hyphens based on the results of previewing the text in the most likely display modes. However, the same thing would need to be done again whenever new displays are foreseen.</p>

<!-- <h4>Hyphenation requires engineering</h4> -->
#### Hyphenation requires engineering

<p>In any of the two hyphenation approaches above (both through manual insertion of soft hyphens or based on the browser hyphenation dictionary), the localization engineer must interact with web designers in order to optimize CSS styling in the display application. In the automatically hyphenated language versions, the language tag (e.g. <code>lang="de"</code>) must be correct so that the browser knows settings must be applied.</p>

## References 

[Code](https://jsfiddle.net/msoutopico/0djnp6ck/1/)