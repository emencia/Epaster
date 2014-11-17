.. _intro_emencia_paste_djangocms_2:
.. _buildout: http://www.buildout.org/
.. _virtualenv: http://www.virtualenv.org/
.. _pip: http://www.pip-installer.org
.. _Foundation 3: http://foundation.zurb.com/old-docs/f3/
.. _Foundation: http://foundation.zurb.com/
.. _Foundation Orbit: http://foundation.zurb.com/orbit.php
.. _modular-scale: https://github.com/scottkellum/modular-scale
.. _Compass: http://compass-style.org/
.. _SCSS: http://sass-lang.com/
.. _rvm: http://rvm.io/
.. _Django: https://www.djangoproject.com/
.. _django-admin-tools: https://bitbucket.org/izi/django-admin-tools/
.. _Django CMS: https://www.django-cms.org/
.. _django-assets: http://elsdoerfer.name/docs/django-assets/
.. _django-debug-toolbar: https://github.com/django-debug-toolbar/django-debug-toolbar/
.. _Django Blog Zinnia: https://github.com/Fantomas42/django-blog-zinnia
.. _Django CKEditor: https://github.com/divio/djangocms-text-ckeditor/
.. _Django Filebrowser: https://github.com/wardi/django-filebrowser-no-grappelli
.. _django-google-tools: https://pypi.python.org/pypi/django-google-tools
.. _Django Porticus: https://github.com/emencia/porticus
.. _Django PDB: https://github.com/tomchristie/django-pdb
.. _Django flatpages app: https://docs.djangoproject.com/en/1.5/ref/contrib/flatpages/
.. _Django sites app: https://docs.djangoproject.com/en/1.5/ref/contrib/sites/
.. _Django reCaptcha: https://github.com/praekelt/django-recaptcha
.. _Django registration: https://django-registration.readthedocs.org/en/latest/
.. _CKEditor: http://ckeditor.com/
.. _emencia-cms-snippet: https://github.com/emencia/emencia-cms-snippet
.. _Service reCaptcha: http://www.google.com/recaptcha
.. _Django Codemirror: https://github.com/sveetch/djangocodemirror
.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
.. _crispy-forms-foundation: https://github.com/sveetch/crispy-forms-foundation
.. _emencia-django-slideshows: https://github.com/emencia/emencia-django-slideshows
.. _emencia-django-staticpages: https://github.com/emencia/emencia-django-staticpages
.. _emencia-django-socialaggregator: https://github.com/emencia/emencia-django-socialaggregator
.. _django-urls-map: https://github.com/sveetch/django-urls-map
.. _Sitemap framework: https://docs.djangoproject.com/en/1.5/ref/contrib/sitemaps/

*******************
DjangoCMS 2.x paste
*******************

DjangoCMS projects are created with the many components that are available for use. These components are called **mods** and these mods are already installed and ready to use, but they are not all enabled. You can enable or disable them, as needed.

It is always preferable to use the mods system to install new apps. You should never install a new app with `pip`_. If you plan to integrate it into the project, always use the `buildout`_ system. Just open and edit the ``buildout.cfg`` file to add the new egg to be installed. For more details, read the `buildout`_ documentation.

**This paste is not really maintained anymore, you should prefer to see for the DjangoCMS 3.x version instead.**

Links
=====

* Download his `PyPi package <https://pypi.python.org/pypi/emencia_paste_djangocms_2>`_;
* Clone it on his `Github repository <https://github.com/emencia/emencia_paste_djangocms_2>`_;

Paste
=====

This paste will appear with the name ``djangocms-2`` in the paster templates list (with the ``paster create --list-templates`` command).

To use this paste to create a new project you will do something like : ::

    paster create -t djangocms-2 myproject

Django
======

django-instance
---------------

This is the command installed to replace the ``manage.py`` script in Django. ``django-instance`` is aware of the installed eggs.

Paste template version
----------------------

In your projects, you can find from which Paste template they have been builded in the 'project/__init__.py' file where you should find the used package name and its version.

Note that previously (before the Epaster version 1.8), this file was containing the Epaster version, not the Paste template one, since the package didn't exists yet.

How the Mods work
-----------------

The advantage of centralizing app configurations in their mods is the project's ``settings.py`` and ``urls.py`` are gathered together in its configuration (cache, smtp, paths, BDD access, etc.). Furthermore, it is easier to enable or disable the apps.

To create a new mods, create a directory in ``$PROJECT/mods_avalaible/`` that contains at least one empty ``__init__.py`` and a ``settings.py`` to build the app in the project and potentially its settings. The `settings.py`` and ``urls.py`` files in this directory will be executed automatically by the project (the system loads them after the project ones so that a mods can overwrite the project's initial settings and urls). N.B. With Django's ``runserver`` command, a change to these files does not reload the project instance; you need to relaunch it yourself manually.

To enable a new mods, you need to create its symbolic link (**a relative path**) in ``$PROJECT/mods_enabled``. To disable it, simply delete the symbolic link.

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

Foundation
----------

This project embeds `Foundation`_ 5 sources installed from the `Foundation`_ app so you can update it from the sources if needed (and if you have installed the Foundation cli, see its documentation for more details). If you update it, you need to synchronize the updated sources in the project's static files using a command in the Makefile: ::

    make syncf5
    
**You only have to do this when you want to synchronize the project's Foundation sources from the latest Foundation release. Commonly this is reserved for Epaster developers.**

This will update the Javascript sources in the static files, but make sure that it cleans the directory first. Never put your files in the ``project/webapp_statics/js/foundation5`` directory or they will be deleted. Be aware that the sources update will give you some file prefixed with a dot like ``.gitignore``, you must rename all of them like this ``+dot+gitignore``, yep the dot character have to be renamed to ``+dot+``, else it will cause troubles with GIT and Epaster. There is a python script named ``fix_dotted_filename.py`` in the source directory, use it to automatically apply this renaming.

For the `Foundation`_ SCSS sources, no action is required; they are imported directly into the compass config.

The project also embeds `Foundation 3`_ sources (they are used for some components in Django administration) but you don't have to worry about them.

RVM
---

`rvm`_ is somewhat like what `virtualenv`_ is to Python: a virtual environment. The difference is that it is intended for the parallel installation of a number of different versions of **Ruby** without mixing the gems (the **Ruby** application packages). In our scenario, it allows you to install a recent version of **Ruby** without affecting your system installation.

This is not required, just an usefull cheat to know when developing on a server with an old distribution.

Installation and initial use
============================

Once your project has been created with this epaster template, you need to install it to use it. The process is simple. Do it in your project directory: ::

    make install

When it's finished, active the virtual environment: ::

    source bin/active

You can then use the project on the development server: ::

    django-instance runserver 0.0.0.0:8001

You will then be able to access it at the following url (where ``127.0.0.1`` will be the server's IP address if you work on a remote machine) : ``http://127.0.0.1:8001/``

The first action required is the creation of a CMS page for the home page and you must fill in the site name and its domain under ``Administration > Sites > Sites > Add site``.


Available mods
==============

accounts
--------

Enable `Django registration`_ and everything you need to allow users to request registration and to connect/disconnect. The views and forms are added so this part can be used. 

It includes:

* A view for the login and one for the logout;
* All the views for the registration request (request, confirmation, etc.);
* A view to ask for the reinitialization of a password.

In the ``skeleton.html`` template, a partial HTML code is commented. Uncomment it to display the *logout* button when the user is connected.

The registration process consists in sending an email (to be configured in the settings) with the registration request to an administrator responsible for accepting them (or not). Once validated, an email is sent to the user to confirm his registration by way of a link. Once this step has been completed, the user can connect.

admin_tools
-----------

Enable `django-admin-tools`_ to enhance the administration interface. This enables three widgets to customize certain elements. `filebrowser`_ is used, so if your project has not enabled it, you need to remove the occurrences of these widgets.

assets
------

Enable `django-assets`_ to combine and minify your *assets* (CSS, JS). The minification library used, *yuicompressor*, requires the installation of Java (the OpenJDK installed by default on most Linux systems is sufficient).

In general, this component is required. If you do not intend to use it, you will need to modify the project's default templates to remove all of its occurrences.

ckeditor
--------

Enable the customization of the `CKEditor`_ editor. It is enabled by default and used by `Django CKEditor`_ in the `cms`_ mod, and also in `zinnia`_.

Use "djangocms_text_ckeditor", a djangocms plugin to use CKEditor (4.x) instead of the default one

This mod contains some tricks to enable "django-filebrowser" usage with "image" plugin from CKEditor.

And some contained patches/fixes :

* the codemirror plugin that is not included in djangocms-text-ckeditor;
* Some missed images for the "showblocks" plugin;
* A system to use the "template" plugin (see views.EditorTemplatesListView for more usage details);
* Some patch/overwrites to have content preview and editor more near to Foundation;

cms
---

`Django CMS`_ allows for the creation and management of the content pages that constitute your site's tree structure. By default, this component enables the use of `filebrowser`_, `Django CKEditor`_ and `emencia-cms-snippet`_ (a clone of the snippets' plugin with a few improvements).

By default it is configured to use only one language. See its ``urls.py`` to find out how to enable the management of multiple languages.

codemirror
----------

Enable `Django Codemirror`_ to apply the editor with syntax highlighting in your forms (or other content).

It is used by the snippet's CMS plugin.

contact_form
------------

A simple contact form that is more of a standard template than a full-blown application. You can modify it according to your requirements in its ``apps/contact_form/`` directory. Its HTML rendering is managed by `crispy_forms`_ based on a customized layout.

By default, it uses the `recaptcha`_ mods.

crispy_forms
------------

Enable the use of `django-crispy-forms`_ and `crispy-forms-foundation`_. **crispy_forms** is used to manage the HTML rendering of the forms in a finer and easier fashion than with the simple Django form API. **crispy-forms-foundation** is a supplement to implement the rendering with the structure (tags, styles, etc.) used in `Foundation`_.

debug_toolbar
-------------

Add `django-debug-toolbar`_ to your project to insert a tab on all of your project's HTML pages, which will allow you to track the information on each page, such as the template generation path, the  query arguments received, the number of SQL queries submitted, etc.

This component can only be used in a development or integration environment and is always disabled during production.

Note that its use extends the response time of your pages and can provokes some mysterious bugs (like with syncdb or zinnia) so for the time being, this mods is disabled. So enable it locally for your needs, but never commit its enabled mod and remember to disable it when you have a strange bug.

emencia_utils
-------------

Group together some common and various utilities from ``project.utils``.

filebrowser
-----------

Add `Django Filebrowser`_ to your project so you can use a centralized interface to manage the uploaded files to be used with other components (`cms`_, `zinnia`_, etc.).

The version used is a special version called *no grappelli* that can be used outside of the *django-grapelli* environment.

flatpages
---------

Enable the use of `Django flatpages app`_ in your project. Once it has been enabled, go to the ``urls.py`` in this mod to configure the *map* of the urls to be used.

google_tools
------------

Add `django-google-tools`_ to your project to manage the tags for *Google Analytics* and *Google Site Verification* from the site administration location.

pdb
---

Add `Django PDB`_ to your project for more precise debugging with breakpoints. 

N.B. Neither ``django_pdb`` nor ``pdb`` are installed by the buildout. You must install 
them manually, for example with `pip`_, in your development environment so you do not 
disrupt the installation of projects being integrated or in production. You must also 
add the required breakpoints yourself.

See the the django-pdb Readme for more usage details.

.. note::
        django-pdb should be put at the end of settings.INSTALLED_APPS :
        
        "Make sure to put django_pdb after any conflicting apps in INSTALLED_APPS so 
        that they have priority."
        
        So with the automatic loading system for the mods, you should enable it with a 
        name like "zpdb", to assure that it is loaded at the end of the loading loop.

porticus
--------

.. _DjangoCMS plugin for Porticus: https://github.com/emencia/cmsplugin-porticus

Add `Django Porticus`_ to your project to manage file galleries.

There is a `DjangoCMS plugin for Porticus`_, it is not enabled by default, you will have to uncomment it in the mod settings.

recaptcha
---------

Enable the `Django reCaptcha`_ module to integrate a field of the *captcha* type via the `Service reCaptcha`_. This integration uses a special template and CSS to make it *responsive*.

If you do in fact use this module, go to its mods setting file (or that of your environment) to fill in the public key and the private key to be used to transmit the data required.

By default, these keys are filled in with a *fake* value and the captcha's form field therefore sends back a silent error (a message is inserted into the form without creating a Python *Exception*).

site_metas
----------

Enable a module in ``settings.TEMPLATE_CONTEXT_PROCESSORS`` to show a few variables linked to `Django sites app`_ in the context of the project views template.

Common context available variables are:

* ``SITE.name``: Current *Site* entry name;
* ``SITE.domain``: Current *Site* entry domain;
* ``SITE.web_url``: The Current *Site* entry domain prefixed with the http protocol like ``http://mydomain.com``. If HTTPS is enabled 'https' will be used instead of 'http';

Some projects can change this to add some other variables, you can see for them in ``project.utils.context_processors.get_site_metas``.

sitemap
-------

This mod use the Django's `Sitemap framework`_ to publish the ``sitemap.xml`` for various apps. The default config contains ressources for DjangoCMS, Zinnia, staticpages, contact form and Porticus but only ressource for DjangoCMS is enabled.

Uncomment ressources or add new app ressources for your needs (see the Django documentation for more details).

slideshows
----------

Enable the `emencia-django-slideshows`_ app to manage slide animations (slider, carousel, etc.). This was initially provided for `Foundation Orbit` and *Royal Slider*, but can be used with other libraries if needed.

socialaggregator
----------------

Enable the `emencia-django-socialaggregator`_ app to manage social contents.

This app require some API key settings to be filled to work correctly.

staticpages
-----------

This mod uses `emencia-django-staticpages`_ to use static pages with a direct to template process, it replace the deprecated mod *prototype*.

urlsmap
-------

`django-urls-map`_ is a tiny Django app to embed a simple management command that will display the url map of your project.

zinnia
------

`Django Blog Zinnia`_ allows for the management of a blog in your project. It is perfectly integrated into the `cms`_ component but can also be used independently.

At the time of installation, an automatic patch (that can be viewed in the ``patches/`` directory) is applied to it to implement the use of `ckeditor`_, which is enabled by default in its settings.



Changelogs
==========

Version 1.9.6 - 2014/11/17
--------------------------

* Mount 500 and 404 page view in urls.py when debug mode is activated;

Version 1.9.5 - 2014/11/07
--------------------------

* Update to ``zc.buildout==2.2.5``;
* Update to ``buildout.recipe.uwsgi==0.0.24``;
* Update to ``collective.recipe.cmd==0.9``;
* Update to ``collective.recipe.template==1.11``;
* Update to ``djangorecipe==1.10``;
* Update to ``porticus==0.8.1``;
* Add package ``cmsplugin-porticus==0.1.2`` in buildout config;
* Remove dependancy for ``zc.buildout`` and ``zc.recipe.egg``;

Version 1.9.4 - 2014/11/02
--------------------------

Update mods doc

Version 1.9.3 - 2014/11/01
--------------------------

Fix some app versions in version.cfg

Version 1.9.2 - 2014/09/31
--------------------------

Following repository renaming (*emencia-paste-djangocms-2* to *emencia_paste_djangocms_2*) for a workaround with 'gp.vcsdevelop'

Version 1.9.1 - 2014/09/31
--------------------------

Fix paste template and setup

Version 1.9 - 2014/09/31
------------------------

Renaming repository to *emencia-paste-djangocms-2* to follow Epaster new structure.

Version 1.8.2 - 2014/09/27
--------------------------

Add mods documentations taken from Epaster documentation.

Version 1.8 - 2014/09/26
------------------------

First release as *emencia_paste_django* started from ``Epaster==1.8``

