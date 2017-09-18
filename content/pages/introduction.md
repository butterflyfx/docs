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

If don't plan on testing against your localhost or any other internal URLs, then you can skip this section. Otherwise, you'll need to download the [command line client](/pages/resources/cli-client) for your platform or use the `tunnel()` method from the javascript client within your test or task runner. 

<div class="code-tabs">

<pre class="line-numbers">

<code class="language-bash">
butterflyfx --api-key="INSERT-API-KEY-HERE" tunnel
</code>
</pre>

<pre class="line-numbers">

<code class="language-javascript">
// npm install butterflyfx-client
const API_KEY = "INSERT-API-KEY-HERE";
const PROJECT_ID = 0;
const ButterflyFX = require('butterflyfx-client');
let client = new ButterflyFX({project:PROJECT_ID, token:API_KEY});
// Only works when run from a node based task runner.
// e.g karma.conf.js, gulpfile.js, ember-cli-build.js, etc
client.tunnel("localhost:8000");
</code>

</pre>


</div>

### Create a fixture using the UI or the API

The easiest way to get started is to drag and drop the <a href='
javascript:(function()%7Bfunction callback()%7Bvar bfx %3D new ButterflyFX()%3Bbfx.showFixtureDialog()%7Dvar s%3Ddocument.createElement(&#34;script&#34;)%3Bs.src%3D&#34;https%3A%2F%2Fwww.butterflyfx.io%2Fstatic%2Fjs%2Fclient.js&#34;%3Bif(s.addEventListener)%7Bs.addEventListener(&#34;load&#34;%2Ccallback%2Cfalse)%7Delse if(s.readyState)%7Bs.onreadystatechange%3Dcallback%7Ddocument.body.appendChild(s)%3B%7D)()
' title="Take a Buttershot"> ButterflyFX Bookmarklet</a> link into your bookmarks toolbar.


<div class="code-tabs">
  <div class="code-preview">
<img src="/demos/bookmarklet1.gif" />
<hr />
<img src="/demos/bookmarklet2.gif" />
  </div>


```html
<script type="text/javascript" src="https://www.butterflyfx.io/static/js/client.js"></script>
<script type="text/javascript">
    var API_KEY = "INSERT-API-KEY-HERE";
    var PROJECT_ID = 0;
    var client = new ButterflyFX({project:PROJECT_ID, token:API_KEY});
    client.saveFixture({
      name: "Hello world",
    });
</script>
    
```

  
  <pre class="line-numbers">
<code class="language-javascript">
// npm install butterflyfx-client
const API_KEY = "INSERT-API-KEY-HERE";
const PROJECT_ID = 0;
const ButterflyFX = require('butterflyfx-client');
let client = new ButterflyFX({project:PROJECT_ID, token:API_KEY});
// An ordinary html string can be used here instead of document.querySelector 
let html = document.querySelector("html").outerHTML;
client.saveFixture({
  name: "Hello world",
  html: html
});


</code></pre>
</div>


Alternatively, you can copy and paste the following code into the URL section of a new bookmark in your toolbar to enable to the bookmarklet.


<input type="text" style="width: 70%" onclick="this.focus(); this.select()" value='
javascript:(function()%7Bfunction callback()%7Bvar bfx %3D new ButterflyFX()%3Bbfx.showFixtureDialog()%7Dvar s%3Ddocument.createElement(&#34;script&#34;)%3Bs.src%3D&#34;https%3A%2F%2Fwww.butterflyfx.io%2Fstatic%2Fjs%2Fclient.js&#34;%3Bif(s.addEventListener)%7Bs.addEventListener(&#34;load&#34;%2Ccallback%2Cfalse)%7Delse if(s.readyState)%7Bs.onreadystatechange%3Dcallback%7Ddocument.body.appendChild(s)%3B%7D)()
' />