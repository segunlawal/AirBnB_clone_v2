#!/usr/bin/python3
"""This module contains the do_deploy function"""
import os
from fabric.api import run, env, cd, put
from datetime import datetime
env.hosts = ['52.91.128.8', '100.24.240.21']
env.user = "ubuntu"


def do_deploy(archive_path):
    """Fabric script that distributes to web servers"""
    if not os.path.exists("archive_path"):
        return False

    else:
        try:
            filename = '/data/web_static/releases/{}'.format(
                    archive_path.strip(".tgz"))
            archive = archive_path.lstrip('versions/')
            run('mkdir -p {}'.format(filename))
            put('{}'.format(archive_path), "/tmp/")
            run('tar -xzf /tmp/{} -C {}'.format(archive, filename))
            run('mv {}/web_static/* {}'.format(filename, filename))
            run('rm -rf {}/web_static/'.format(filename))
            run('rm /tmp/{}'.format(archive))
            run('rm /data/web_static/current')
            run('ln -sf {} /data/web_static/current'.format(filename))
            return True
        except Exception:
            return False
