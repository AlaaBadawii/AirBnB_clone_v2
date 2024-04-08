from fabric import Connection, task
from fabric.operations import local
from datetime import datetime

c = Connection(
        host="52.91.118.162",
        user="ubuntu",
        connect_kwargs={
            "key_filename": "/home/badawii/.ssh/id_rsa",
        },
)

@task
def do_pack(c):
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")

    with c.local.cwd('~/'):  # Change to the appropriate directory
        local("mkdir -p versions")

        archive_name = "web_static_{}.tgz".format(timestamp)
        archive_path = "versions/{}".format(archive_name)

        result = local("tar -czvf {} web_static".format(archive_path), capture=True)

        if result.succeeded:
            return archive_path
        else:
            return None

