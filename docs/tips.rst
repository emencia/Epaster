.. _intro_tips:
.. _buildout: http://www.buildout.org/
.. _virtualenv: http://www.virtualenv.org/
.. _Foundation 3: http://foundation.zurb.com/old-docs/f3/
.. _Foundation: http://foundation.zurb.com/
.. _Compass: http://compass-style.org/
.. _SCSS: http://sass-lang.com/
.. _rvm: http://rvm.io/
.. _icomoon: http://icomoon.io/
.. _django-assets: http://django-assets.readthedocs.org/en/latest/
.. _webassets: http://webassets.readthedocs.org/en/latest/
.. _yuicompressor: http://yui.github.io/yuicompressor/
 
****************************
Common topics around Epaster
****************************

There are some topics around some things we use in Epaster environnment. 

Note that these topics are based on **emencia_paste_djangocms_3**, but generally they will apply also to **emencia_paste_djangocms_2**.

Compass
=======

`Compass`_ is a **Ruby** tool used to compile `SCSS`_ sources in **CSS**.

By default, a Django project has its `SCSS`_ sources in the ``compass/scss/`` directory. The CSS `Foundation`_ framework is used as the database.

A recent install of Ruby and Compass is required first for this purpose (see `RVM`_ if your system installation is not up to date).

Once installed, you can then compile the sources on demand. Simply go to the ``compass/`` directory and launch this command: ::

    compass compile

When you are working uninterruptedly on the sources, you can simply launch the following command: ::

    compass watch

`Compass`_ will monitor the directory of sources and recompile the modified sources automatically.

By default the ``compass/config.rb`` configuration file (the equivalent of `settings.py`` in Django) is used. If needed, you can create another one and specify it to `Compass`_ in its command (for more details, see the documentation).

RVM
---

`rvm`_ is somewhat like what `virtualenv`_ is to Python: a virtual environment. The difference is that it is intended for the parallel installation of a number of different versions of **Ruby** without mixing the gems (the **Ruby** application packages). In our scenario, it allows you to install a recent version of **Ruby** without affecting your system installation.

This is not required, just an usefull cheat to know when developing on a server with an old distribution.

Webfonts
========

Often, we use webfonts to display icons instead of images, because a webfont is more flexible to use (it can take any size without to re-upload it) and more light on file size. It is also more *CSS friendly*.

Commonly we use `icomoon`_ that is a service to pack a selected set of webfonts to a ZIP archive that you can use to easily embed it in your project.

The first thing is to go on `icomoon`_, create a webfont project and select the needed item from fonts. Then you have a webfont project, you have to download it as a ZIP archive and open it when it's done.

When you open the archive, you should something like that : ::

    icomoon/
    ├── demo-files
    │   ├── demo.css
    │   └── demo.js
    ├── demo.html
    ├── fonts
    │   ├── icomoon.eot
    │   ├── icomoon.svg
    │   ├── icomoon.ttf
    │   └── icomoon.woff
    ├── Read Me.txt
    ├── selection.json
    └── style.css

What we need here is the ``fonts`` directory because it contains the font we need to put in our project assets, and the ``style.css`` file that contain the icons class name *map*.

So for a site project named **site_sample** generated from Epaster, first you will copy the fonts directory in ``project/webapp_statics`` into your project, there should allready be a ``fonts`` directory so overwrite it.

Now open the ``style.css`` from the archive, it should look like this :

..  sourcecode:: css
    :linenos:

    @font-face {
            font-family: 'icomoon';
            src:url('fonts/icomoon.eot?n45w4u');
            src:url('fonts/icomoon.eot?#iefixn45w4u') format('embedded-opentype'),
                    url('fonts/icomoon.woff?n45w4u') format('woff'),
                    url('fonts/icomoon.ttf?n45w4u') format('truetype'),
                    url('fonts/icomoon.svg?n45w4u#icomoon') format('svg');
            font-weight: normal;
            font-style: normal;
    }
    [class^="icon-"], [class*=" icon-"] {
            font-family: 'icomoon';
            speak: none;
            font-style: normal;
            font-weight: normal;
            font-variant: normal;
            text-transform: none;
            line-height: 1;

            /* Better Font Rendering =========== */
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
    }
    

    .icon-left:before {
            content: "\e622";
    }
    .icon-right:before {
            content: "\e623";
    }
    .icon-play:before {
            content: "\e62b";
    }

Not that there are two parts, the first with ``@font-face`` and ``[class^="icon-"], [class*=" icon-"]``, and the second part with some icon class names. Don't mind about the first part, we allready define it in our SCSS component, just copy the whole second part with all class names for your icons.

Then you will have to fill the class names used in the SCSS components ``compass/scss/components/_icomoon.scss`` in your project, search for this pattern at the end of the file : ::

    // Icon list
    /*
    * 
    * HERE GOES THE ICONS FROM THE style.css bundled in the icomoon archive
    * 
    */

And put the pasted icon class names after this pattern.

Finally in ``compass/scss/app.scss`` search for the line containing ``@import "components/icomoon";`` and uncomment it, now you can compile your SCSS and the webfont icons will be available from your ``app.css`` file.

Assets management
=================

Why
---

In the past, assets management was painful with some projects, because their includes was often divided in many different templates. This causing issues like to update some library or retrieve effective code that was working on some template by inherit.

Also, this often results in pages loading dozen of asset files and sometime much more. This is a really bad behavior because it slows page loading and add useless performance charge on the web server.

This is why we use an **asset manager** within Epaster: `django-assets`_ which is a subproject of `webassets`_. Firstly read the `webassets`_ documentation to understand how is working its **Bundle** system. Then you can read the `django-assets`_ that is only related about Django usage with the settings, templatetags, etc..

How it works
------------

Asset managers generally perform two tasks :

* Regroup some kind of files together, like regrouping all Javascript files in an unique file;
* Minimize the file weight with removing useless white spaces to have the code on unique line;

Some asset manager implement this with their own file processor, some other like `webassets`_ are just "glue" between the files and another dedicated *compiler* like `yuicompressor`_.

Environments
------------

Asset management is really useful within integration or production environments and so when developing, the manager is generally disabled and the files are never compiled, you can verify this with looking at your page's source code.

make assets
-----------

Epaster pastes have a ``make assets`` command that is useful **on integration and production environment** to deploy update on your assets. In fact **this command is always required in these environments** when you deploy a new update where assets have changed. Also you should never use it on development environment because it can cause you many troubles.

What does this command :

#. Collecting all static files from your project and installed apps to your ``settings.STATIC_ROOT`` directory;
#. Use `django-assets`_ to *compile* all defined bundles using previously collected files;
#. Re-collecting static files again to collect the compiled bundle files;

Static files directories
------------------------

In your ``settings.py`` file you should see :

..  sourcecode:: python
    
    STATIC_ROOT = join(PROJECT_PATH, 'static')

It define the *front* static file directory. But **never put yourself a file in this directory**, it is **reserved** for collected files in **integration and production environment** only.

All static files sources will go in the ``project/webapp_statics`` directory, it is defined in the *assets* mod:

..  sourcecode:: python
    
    ASSETS_ROOT = join(PROJECT_PATH, 'webapp_statics/')
    STATICFILES_DIRS += (ASSETS_ROOT,)

This way we allways have separated directories for the sources and the compiled files. This is required to never commit compiled files and avoid conflict between development and production.

The rule
--------

Never, ever, put CSS stylesheets in your templates, NEVER. You can forget it, this will go in production and forgeted for a long time, this can be painful for other developers that coming after you. So **always add CSS stylesheets by the way of SCSS sources** using `Compass`_.

For Javascript code this is different, sometime we need to generate some code using Django templates for some specific cases. But if you use a same Javascript code in more than one template (using inheriting or so), you must move the code to a Javascript file.

Developers should never have to search in templates to change some CSS or Javascript code that is used in more than one page.

Developing application
======================

Sometimes, you will need to develop some new app package or improve them without to embed them within the project.

You have two choices to do that:

* Use ``develop`` buildout variable to simply add your app to the developped apps, your app have to exists at the root of buildout project;
* Use ``vcs-extend-develop`` buildout variable to define a repository URL to the package sources;

Even they have the same base name *develop*, these two ways are differents:

* The first one simply add a symbolic link to the package in your Python install without to manage it as an installed eggs, it will be accessible as a Python module installed in the Python virtual environment. This method does not require that your app have a repository or have been published on PyPi;
* The second one install the targeted package from a given repository instead of a downloaded package from PyPi, it act like an installed eggs but from which you can edit the source and publish to the repository. And so your app name have to be defined in the buildout's egg variable, buildout will see it in ``vcs-extend-develop`` and will not try to install it from PyPi but from the given repository url;

In all ways, your apps is allways a full package structure that mean this is not a simple Python module, but its package structure containing stuff like ``README`` file and ``setup.py`` at the base of the directory then the Python module containing the code. Trying to use a simple Python module as a develop app will not work.

Which one to use and when
-------------------------

* If you want to **develop a new package**, it's often much faster to create its package directory structure at the root of your buildout project then use it within ``develop``. You would move it to ``vcs-extend-develop`` when you have published it;
* If you want to **develop an allready published package**, you will use ``vcs-extend-develop`` with its repository url, this so you will be able to edit it, commit changes then publish it;

Most of Emencia's apps are allready setted within ``vcs-extend-develop`` in the buildout config for development environment (``development.cfg``) but disabled, just uncomment the needed one.

Take care, an Egg that is installed from a repository url is validated on its version number if defined in the ``versions.cfg``, and so if your develop egg contains a version number less than the one defined in ``versions.cfg``, buildout will try to get the most recent version from PyPi, so allways manage the app version number.