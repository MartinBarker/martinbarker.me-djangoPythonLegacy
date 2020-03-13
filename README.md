# www.martinbarker.me
This repo is the code used for www.martinbarker.me, which includes www.tagger.site and www.discogstagger.site.

The code is hosted with Django 3.0.4, and written in Python 3. The basic structure looks like this:

* martinbarker.me/    = main project folder
  * urls.py = directs & redirects all urls for martinbarker.me
* discogstagger/ = discogstagger.site code
  *  urls.py = directs urls for martinbarker.me/discogstagger
  *  views.py = Python code for discogstagger.site
* tagger/ = tagger.site code
  *  urls.py = directs urls for martinbarker.me/tagger
  *  views.py = Python code for tagger.site
* templates/ = html files for websites
  * discogstagger/discogstagger.html
  * tagger/index.html

To contributre to these files, fork this repo and make a pull request.
