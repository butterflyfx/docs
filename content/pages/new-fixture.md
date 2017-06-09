+++
date = "2017-04-11T00:00:44-05:00"
draft = false
title = "Creating Fixtures"
menu = "main"
weight= 2

+++
# Creating a new fixture

A fixture is made up of three basic components: A unique identifier (slug), the html associated with a particular element or page, and a project which this fixture belongs to. From there, CSS is derived from stylesheets defined or loaded from the html.

## Selecting a page element

When you click the bookmarklet link, a UI will appear that allows you to select the page you'd like to use for the fixture.

You can also create a fixture based on a specific element on the page by holding down the `CTRL` key and clicking on its area. 
The next screen will allow you to choose a unique query selector if it was not detected automatically.

Fixtures based on a specific element require an existing fixture that includes the element as its parent.


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
