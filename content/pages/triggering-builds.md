+++
date = "2017-04-11T00:00:44-05:00"
draft = false
title = "Builds"
menu = "main" 
weight= 3

+++
# Builds

If all has gone well up to this point, you should be able to see a [list of the fixtures](https://www.butterflyfx.io/dash/fixtures/) you've created. However, the fixtures themselves aren't that interesting until we start creating new builds. 

## Triggering new builds

Once you've updated the styling in your CSS, you can see how these changes impact all the fixtures in a project by triggering a new build. 
 
New builds can be triggered by selecting a project with the New Build button on the [build list page](https://www.butterflyfx.io/dash/builds/), or by issuing the build command using the command line client or API. 


<div class="code-tabs">
  <div class="code-preview">
<img src="/demos/bookmarklet2.gif" />
  </div>


```html
<script type="text/javascript" src="https://www.butterflyfx.io/static/js/client.js"></script>
<script type="text/javascript">
    var API_KEY = "INSERT-API-KEY-HERE";
    var PROJECT_ID = 0;
    var client = new ButterflyFX({project:PROJECT_ID, token:API_KEY});
    var selector = ".my-container";
    var html = document.querySelector(selector.outerHTML);
    client.saveFixture({
      name: "Hello world",
      html: html,
      selector: selector,
      // Assumes a previously create fixture with slug "main-page"
      parent: "main-page"
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
let selector = ".my-container";
let html = document.querySelector("html").outerHTML;
client.saveFixture({
  name: "Hello world",
  html: html,
  selector: selector,
  // Assumes a previously create fixture with slug "main-page"
  parent: "main-page"
});


</code></pre>
</div>
