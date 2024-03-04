<body>

<h1>Wrapping text with CSS</h1>

<h2>General consideration</h2>

<p>The most important principle is that content and presentation should be independent independent. Linguists (translators, verifiers, etc.) should focus on the text and not be asked to deal with layout and typesetting, which is the job of the publishers (DTP, CSS engineers, etc.). Following that principle helps avoid situations where text is over-fitted to a specific context/medium while at the same time compromising its chances of it being reused in other contexts/media.</p>

<p>Of course, that excludes semantic formatting that applies to specific inline elements (e.g. bold, italics, etc.). </p>

<p>In a nutshell, asking linguists to insert line breaks, hyphens, extra spacing, etc. to fake a certain visual effect (wrapping, indentation, etc.) in the layout is a bad idea. Instead, in a web publication as is our case, styles (CSS) should be used for that, and often that requires language-specific CSS rules. Let me know if you or your CSS crew need more details about this.</p>

<h2>In action</h2>

<p>Let's see what the same text looks like both forcing wrapping manually (by explicitly inserting line breaks in the text and letting the browser take care of wrapping automatically (with CSS styles), in different widths.</p>

<h3>Context 1 -- Width: 25em</h3>

<p>The text below looks the same when line breaks are inserted manually or when the text is wrapped automatcially through styling rules.</p>

<h4>With line breaks:</h4>

<div class="width30"> Since the 1970s, scientists have been <br/> worried about the amount of Dioxin, a <br/> toxin in fish caught in Baltic Sea.</div>

<br/>

<div class="width30"> 1970年代以来、科学者たちはバルト海で捕獲された魚<br/>に含まれる毒素であるダイオキシンの量を懸念してき<br/>た。</div>

<h4>With styles:</h4>

<div class="width30 test"> Since the 1970s, scientists have been worried about the amount of Dioxin, a toxin in fish caught in Baltic Sea.</div>

<br/>

<div class="width30"> 1970年代以来、科学者たちはバルト海で捕獲された魚に含まれる毒素であるダイオキシンの量を懸念してきた。</div>

<h3>Context 2 -- Width: 18em</h3>

<p>The same text as above is rendered correctly when the text is wrapped automatcially through styling rules but it scales badly where line breaks were inserted manually.</p>

<h4>With line breaks (in the same position as above):</h4>

<div class="width18"> Since the 1970s, scientists have been <br/> worried about the amount of Dioxin, a <br/> toxin in fish caught in Baltic Sea.</div>

<br/>

<div class="width18"> 1970年代以来、科学者たちはバルト海で捕獲された魚<br/>に含まれる毒素であるダイオキシンの量を懸念してき<br/>た。</div>

<h4>With styles:</h4>

<div class="width18 test"> Since the 1970s, scientists have been worried about the amount of Dioxin, a toxin in fish caught in Baltic Sea.</div>

<br/>

<div class="width18 test"> 1970年代以来、科学者たちはバルト海で捕獲された魚に含まれる毒素であるダイオキシンの量を懸念してきた。</div>

</body>

<!-- another way:
https://www.html5canvastutorials.com/tutorials/html5-canvas-wrap-text-tutorial/
-->

## References

<a href="https://jsfiddle.net/msoutopico/08btgs5j/3/">Code</a>