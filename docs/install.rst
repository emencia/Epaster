.. _intro_install:
.. _buildout: http://www.buildout.org/
.. _pip: http://www.pip-installer.org/
.. _virtualenv: http://www.virtualenv.org/
.. _graphviz: http://www.graphviz.org/
 
*******
Install
*******

This install procedure is designed for a virtual Python environment. The Epaster tool will not be installed in your system’s Python environment to avoid conflicts or the crashing of Python modules in your system.

It is possible to install Epaster in your system’s Python environment but you will need to skip the virtualenv stage, which may create a risk.

Requirements
============

The Python virtualenv module is required and must be installed on your system. We recommend you install it directly from pip to ensure you install a more recent version that the one in your system package.

A few devel libraries are required to correctly compile some modules within your buildout project :

* Python
* libpq (for **psycopg2**)
* python (for **psycopg2**)
* libjpeg (for **Pillow**)
* zlib (for **Pillow**)
* libfreetype (for **Pillow**)

Note that **psycopg2** is only required if you plan to use a PostgreSQL database instead of the default **sqlite3** database.

If you plan to build the documentation (in ``docs`` directory) you will have to install `graphviz`_ before on your system.

Procedure
=========

When the required elements are installed, you will need to retrieve **Epaster** from its `Github repository <https://github.com/emencia/Epaster>`_, install it and activate it: ::

    git clone git@github.com:emencia/Epaster.git
    make install
    source bin/activate

This will downloads all dependencies and install them in the virtual environment. If an error occurs, the buildout process will stop and print out the problem. You can correct it and relaunch the buildout process that will continue from the previous job.

If the behavior seems uncertain, you can clean all the files installed and the directory using the dedicated Makefile feature: ::

    make clean

When the buildout process is successfully completed, **Epaster** is ready and you can use it to create new projects.

Additionaly if you have to make some development on Epaster (and/or edit its documentation and rebuild it) or its Paste templates, you will have to install its development environment, after the basic install just do: ::

    buildout -c development.cfg

Global config
=============

You can set a global config where the default option will be used with Buildout. A common method is to create this global config with these lines: ::

    [buildout]
    download-cache = /home/django/.buildout-cache

The path defined in ``download-cache`` will be used to store downloaded packages. This is a cache to avoid re-downloading these packages every time you launch buildout. Note that you have to create this path beforehand or an error will occur in the buildout.
