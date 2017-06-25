+++
date = "2017-04-11T00:00:44-05:00"
draft = false
title = "Style Reports"
menu = "main" 
weight= 4

+++
# Style Reports

Style reports allow you to compare changes in a fixture between each build. You should be able to see all the style reports for each build by clicking on its title from the build list and then clicking on the thumbnail or title of a given fixture. 

## Comparing Differences

Assuming there have been any changes in the CSS since the when the fixture was taken, you can either visualize these changes from the “Render” tab or see a JSON text representation from the “Style Diff” tab. 
 
You can highlight which elements were affected by these changes by clicking the “Highlight Changes” button. You can also see the differences between what was expected and what was actually rendered by clicking the respective buttons nearby. 


<div class="code-tabs">
  <div class="code-preview">
<img src="https://www.butterflyfx.io/assets/images/highlight-diff-thumb.gif" />
  </div>
  
</div>

### Approving changes

 If the changes to a fixture are all intentional, you can click the "New Baseline" button to use this style as the comparison for all future builds.

