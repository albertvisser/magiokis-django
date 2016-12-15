Files in this directory
=======================

files.rst
    this file
.hgignore
    stuff for dvcs to ignore
manage.py
    Django utility functions
readme.rst
    what this is about

magiokis/
.........
files for the entire project (all the apps)

__init__.py
    (empty) package indicator
magiokis.db (not tracked)
    project database (SQLite)
settings_no_secret_key.py
    project settings
urls.py
    root urlconf
views.py
    processing code
wsgi.py
    wsgi server program


magiokis/denk/
..............
application code for the denk app

__init__.py
    (empty) (sub)package indicator
admin.py
    register models on admin site
models.py
    data definitions
urls.py
    urlconfs for denk app
views.py
    processing code


magiokis/songs/
...............
application code for the songs app

__init__.py
    (empty) (sub)package indicator
admin.py
    register models on admin site
copyover.py
    script (intended to be) used in conversion from old site
getsongtekst.py
    songtekst functions used in views.py
models.py
    data definitions
urls.py
    urlconfs for songs app
views.py
    processing code


magiokis/songs/templatetags/
............................
__init__.py
    (empty) (sub)package indicator
extratags.py
    custom tag definition(s)


magiokis/templates/
...................
html templates

base.html
    base include for all pages
base_site.html
    customizing for all pages - TODO: check if this is so
index.html
    root landing page


magiokis/templates/denk/
........................
base_site.html
    customizing for denk app
detail.html
    detail screen
input_args.html
    separate page for entering input (add trefwoord or enter search text)
select_args.html
    separate page to enter arguments for selection (select trefwoord)
select_list.html
    page to show selection
start.html
    select action page


magiokis/templates/songs/
.........................
pages for the songs app

base_site.html
    customizing
index.html
    select action page
opname.html
    details of sound recording
opnlist.html
    show selection of sound recordings
registratie.html
    details of notation registration
reglist.html
    show selection of notation registrations
regtype.html
    details on type(s) of notation registration
series.html
    show defined collection of songs
showreg.html
    show notation sheets (pictures with possible pagination)
song.html
    show details of song
songlist.html
    show selection of songs
tabel.html
    show entries in code table
wijzig.html
    edit song details
wijzigsongtekst.html
    edit song lyrics


magiokis/templates/vertel/
..........................
pages for the vertel app

base_site.html
    customization
detail.html
    show story details
login_form.html (not used)
    login as "narrator"
select.html
    select (from) story collection
start.html
    select action
vertellers.html (not used)
    show "narrator"s


magiokis/vertel/
................
application code for the vertel app

__init__.py
    (empty) (sub)package indicator
models.py
    data definitions
urls.py
    urlconfs for vertel app
views.py
    processing code
zetom.py
    script for data conversion (not sure if used)
    TODO: remove


static/ (not tracked)
.......
admin
    symlink to style stuff for the admin site
