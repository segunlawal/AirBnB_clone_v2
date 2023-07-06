#!/usr/bin/python3
"""This module contains the do_pack function"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Fabric script that generates a .tgz archive from the
    contents of the web_static folder"""
    local("mkdir -p versions")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive = "versions/web_static_{}.tgz".format(timestamp)

    result = local("tar -cvzf {} ./web_static".format(archive))

    if result.return_code == 0:
        return archive
    else:
        return None
