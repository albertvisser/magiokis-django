Files in this directory

manage.py
    Django utility functions
readme.rst
    what this is about
files.rst
    this file
.ignore
    stuff for dvcs to ignore

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
    wsgi server

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
    copy of script to read songtekst
    TODO: compare with original, if duplicate remove and fix import
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
Denk.css
    css for denk app - TODO: move to static/
base_site.html
    customizing for denk app
detail.html
    detail screen
favicon.ico
    site icon - TODO: move to static/, check if used
index.html
    start page for denk app - TODO: replace with start.html (in building response)
input_args.html
    ? TODO: check if used, if not remove
select_args.html
    separate page to enter arguments for selection
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

Vertel.css
    stylesheet - TODO mode to static/
base_site.html
    customization
detail.html
    show story details
detail_ro.html
    edit story details
favicon.ico
    site icon - TODO: move to static/
login_form.html
    login as "narrator"
select.html
    select (from) story collection
start.html
    select action
vertellers.html
    show "narrator"s

static/ (not tracked)
.......
admin
    symlink to style stuff for the admin site
