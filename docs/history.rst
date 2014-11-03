.. _intro_history:
.. _graphviz: http://www.graphviz.org/

*******
History
*******

Changelog
=========

Version 2.1 - 03/11/2014
------------------------

* Update to ``zc.buildout==2.2.4`` to fix a bug introduced in 2.2.3;
* Update to last ``bootstrap.py`` script;
* Update to ``emencia_paste_djangocms_3==1.1``;

emencia_paste_djangocms_3 version 1.1
.....................................

* Update to ``zc.buildout==2.2.4`` to fix a bug introduced in 2.2.3;
* Update to last ``bootstrap.py`` script;
* Remove Foundation3 sources, CSS and bundles, they are not used anymore;
* Move ckeditor and minimalist CSS to common SCSS sources with Foundation5;
* Update Compass README;
* Correct admin_style Compass config;
* Add 'ar' country to the CSS flags;
* Recompile all CSS in project's webapp_statics;
* Changing ``assets.py`` to use nested bundles, so we can separate app bundles (foundation, royalslider, etc..) from the main bundles where we load the app bundles;
* Main frontend's CSS & JS bundles are now called ``main.css`` and ``main.js`` not anymore ``app.***`` (yes we use the old Foundation3 ones that have been removed);

Version 2.0 - 02/11/2014
------------------------

* Implement new pastes for djangocms 2.x and 3.x
* Update doc to fit to the new structure

Version 1.8.2 - 27/09/2014
--------------------------

* Update docs to get the mods documentation directly from their docstring (in their __init__.py);
* Add eggedpy build part;

Version 1.8.1 - 26/09/2014
--------------------------

* Add Development environnment, close #2;
* Try to fix 'Doc compile fail on rtd', fix #1;

Version 1.8 - 25/09/2014
------------------------

First public release on Github, there has been some changes to split Epaster from its Django project template, the template and its sources now resides in its own package named "emencia-paste-django". Both of them starts from the 1.8 version for history purpose.

Version 1.7 - 24/09/2014
------------------------

* Fix nginx template;
* Moving common apps from 'apps' dir to 'project';
* Some minor changes before going public on Github;
* This is the last version from our internal and private repository before Epaster goes public on Github, previous changelog is keeped here for history although you can't access to these previous versions;

Version 1.6 - 08/02/2014
------------------------

* Update to Foundation 5.3.3;
* Improve documentation by using Sphinx theme Bootstrap with 'yeti' bootswatch theme and add History page;
* Add a structure diagram in introduction (warning this will require to install `graphviz`_ on your system);

Version 1.5 - 07/28/2014
------------------------

* Update to Foundation 5.3.1;
* Update README for last changes and to use the version from ``git describe --tags``;

Version 1.4 - 07/27/2014
------------------------

* Update to last Gestus & Po-projects clients;
* Add emencia-django-staticpages package and 'staticpages' mod to replace 'prototypes' mod;
* Add 'sitemap' mod;
* Fix Gestus config with Jinja2 template syntax;
* Use now a template recipe that use jinja and improve the nginx conf;

