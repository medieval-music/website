Institute of Mediaeval Music Website
===================================

This is the website.


Development
-----------

If you want to work on the website.

1. Make sure you've cloned the "theme" submodule. If not, or if you're not sure, run this:
`git submodule init && git submodule update`
2. Prepare for installing the Python dependencies. You'll need to use Python 3 (probably at least
   3.6, but who really knows?) and you'll also need a C++ compiler, and possibly other related
   packages, in order to compile `libsass`. With Fedora 29, I needed to install `python3-devel`,
   `redhat-rpm-config`, and `gcc-c++`.
3. Install the Python dependencies by creating a virtualenv, then running `pip install` with the
   `requirements.txt` file in this directory. Best not to put the virtualenv in the repository.
4. Use the `Makefile` to build the website. Run `make` to see the available commands.
