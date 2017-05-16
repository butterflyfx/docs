+++
date = "2017-04-11T00:00:44-05:00"
draft = false
title = "Introduction"
menu = "main"
identifier = "introduction"
weight= 1

+++

# Introduction

ButterflyFX is designed to provide a data driven alternative to screenshots based on code instead of pixels. 

This guide provides a visual overview of each concept in the "Example" tab with additional code examples in the "HTML" and "Javascript" tabs.

**All code based examples require [generating an API key](https://www.butterflyfx.io/dash/settings/api) from the website** before making any requests.

## Getting Started

The easiest way to get started is to drag and drop the <a href='
javascript:(function()%7Bfunction callback()%7Bvar bfx %3D new ButterFlyFX()%3Bbfx.showFixtureDialog()%7Dvar s%3Ddocument.createElement(&#34;script&#34;)%3Bs.src%3D&#34;https%3A%2F%2Fwww.butterflyfx.io%2Fstatic%2Fjs%2Fclient.js&#34;%3Bif(s.addEventListener)%7Bs.addEventListener(&#34;load&#34;%2Ccallback%2Cfalse)%7Delse if(s.readyState)%7Bs.onreadystatechange%3Dcallback%7Ddocument.body.appendChild(s)%3B%7D)()
' title="Take a Buttershot"> ButterflyFX Bookmarklet</a> link into your bookmarks toolbar.

<div class="code-tabs">
  <div class="code-preview">

  </div>


```html
    <script type="text/javascript" src="https://www.butterflyfx.io/static/js/client.js"></script>
```

  
  <pre class="line-numbers">
<code class="language-javascript">
// npm install butterflyfx-client
let butterflyfx = require('butterflyfx-client');
console.log("Hello world")
</code></pre>
</div>


Alternatively, you can copy and paste the following code into the URL section of a new bookmark in your toolbar to enable to the bookmarklet.


<input type="text" style="width: 70%" onclick="this.focus(); this.select()" value='
javascript:(function()%7Bfunction callback()%7Bvar bfx %3D new ButterFlyFX()%3Bbfx.showFixtureDialog()%7Dvar s%3Ddocument.createElement(&#34;script&#34;)%3Bs.src%3D&#34;https%3A%2F%2Fwww.butterflyfx.io%2Fstatic%2Fjs%2Fclient.js&#34;%3Bif(s.addEventListener)%7Bs.addEventListener(&#34;load&#34;%2Ccallback%2Cfalse)%7Delse if(s.readyState)%7Bs.onreadystatechange%3Dcallback%7Ddocument.body.appendChild(s)%3B%7D)()
' />