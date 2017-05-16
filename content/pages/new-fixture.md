+++
date = "2017-04-11T00:00:44-05:00"
draft = false
title = "Creating Fixtures"
menu = "main"
weight= 2

+++
# Creating a new fixture

A fixture is made up of three basic components: A unique identifier (slug), the html associated with a particular element or page, and a project which this fixture belongs to. From there, CSS is derived from stylesheets defined or loaded from the html.

If a fixture contains references to relative paths, then it'll need to specify `origin` and `path` properties in its revision. This can also be derived by setting the `base_url` property of a fixture's project.


## Selecting a page element

> Include the snippet in your code below to get started

```javascript
// npm install butterflyfx-client
let butterflyfx = require('butterflyfx-client');
```

```html

<script type="text/javascript" src="https://www.butterflyfx.io/static/js/client.js"></script>

```
When you click the bookmarklet link, a UI will appear that allows you to select the element you'd like to use for the fixture.

You can skip this screen and select the entire area by clicking the secondary (right) mouse button instead of the primary button.

Before you can select a child element, you will need to create at least one base fixture to use with its query selector


