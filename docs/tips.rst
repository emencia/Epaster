.. _intro_tips:
.. _buildout: http://www.buildout.org/
.. _icomoon: http://icomoon.io/
 
**************************
Common tips around Epaster
**************************

There are some topics around some things we use in Epaster environnment.

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

