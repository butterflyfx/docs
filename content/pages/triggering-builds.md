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
<img src="/demos/trigger-build-doc.gif" />
  </div>
  
  <pre class="line-numbers">
<code class="language-javascript">
// npm install butterflyfx-client
const API_KEY = "INSERT-API-KEY-HERE";
const PROJECT_ID = 0;
const ButterflyFX = require('butterflyfx-client');
let client = new ButterflyFX({project:PROJECT_ID, token:API_KEY});
client.build();


</code></pre>
</div>
