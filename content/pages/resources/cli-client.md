+++
date = "2017-05-29T00:17:40-05:00"
title = "Command Line Client"
menu = "resources"
weight=10
+++

# Command Line Client

## Download

The ButterflyFX command line client can be downloaded for Windows, Mac, or Linux using the links below.

You can generate your own builds from source by downloading from our code repository. 

<div class="row">
  <div class="col-md-3">
    <div class="promo">
        <a href="https://cdn.butterflyfx.io/downloads/cli/windows/butterflyfx.exe">
            <i class="fa fa-windows"></i>
            <h3>Windows</h3>
        </a>
    </div>
  </div>
  <div class="col-md-3">
    <div class="promo">
        <a href="https://cdn.butterflyfx.io/downloads/cli/mac/butterflyfx">
            <i class="fa fa-apple"></i>
            <h3>Mac</h3>
        </a>
    </div>
  </div>
  <div class="col-md-3">
    <div class="promo">
        <a href="https://cdn.butterflyfx.io/downloads/cli/linux/butterflyfx">
            <i class="fa fa-linux"></i>
            <h3>Linux</h3>
        </a>
    </div>
  </div>
  <div class="col-md-3">
    <div class="promo">
        <a href="https://github.com/butterflyfx" target="new">
            <i class="fa fa-code-fork"></i>
            <h3>Source</h3>
        </a>
    </div>
  </div>
</div>

On Mac and Linux, you'll also need to copy the downloaded file to your path with the right permissions.

    # Replace ~/Downloads with wherever you downloaded the file
    cd ~/Downloads
    cp butterflyfx /usr/local/bin
    chmod +x /usr/local/bin/butterflyfx

## Using the command line client

You can use the command line client to create establish a private tunnel between ButterflyFX and your localhost or other internal resources. 
Once you've downloaded the client, you'll need to [generating an API key](https://www.butterflyfx.io/dash/settings/api) from the website before making any requests.

```bash
butterflyfx --api-key="INSERT-API-KEY-HERE" tunnel localhost:80
```