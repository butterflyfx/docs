from fabric.api import *


def build():
    local("hugo")


def update():
    local("gsutil -m rsync -R public gs://docs.butterflyfx.io")
    local("gsutil -m acl ch -r -u AllUsers:R  gs://docs.butterflyfx.io")
    local("gsutil web set -m index.html -e 404  gs://docs.butterflyfx.io")


def deploy():
    build()
    update()
