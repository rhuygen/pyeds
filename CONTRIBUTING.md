
Release HOWTO
=============

To make a release, 

  1) Update release date/version in:
    * setup.py
    * doc/conf.py
    * NEWS.txt 
  2) Run 'python3 setup.py sdist'
  3) Test the generated source distribution in dist/
  4) Upload to PyPI: 'python3 setup.py sdist upload'
  5) Increase version (for next release) in:
    * setup.py
    * doc/conf.py
    * NEWS.txt 