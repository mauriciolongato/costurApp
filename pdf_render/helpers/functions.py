import pathlib
import os


def path2url(path):
    """Return file:// URL from a filename."""
    path = os.path.abspath(path)
    return pathlib.Path(path).as_uri()


if __name__ == '__main__':
    print(path2url('static/29.png'))