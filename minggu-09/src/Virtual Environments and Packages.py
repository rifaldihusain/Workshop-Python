# Virtual Environments and Packages

1. python -m venv tutorial-env

2. tutorial-env\Scripts\activate.bat

3. (tutorial-env) $ python
	Python 3.5.1 (default, May  6 2016, 10:59:36)
	...
	>>> import sys
	>>> sys.path
	['', '/usr/local/lib/python35.zip', ...,
	'~/envs/tutorial-env/lib/python3.5/site-packages']
	>>>

4. https://bootstrap.pypa.io/get-pip.py

5. python get-pip.py

6. (tutorial-env) $ pip search astronomy
	skyfield               - Elegant astronomy for Python
	gary                   - Galactic astronomy and gravitational dynamics.
	novas                  - The United States Naval Observatory NOVAS astronomy library
	astroobs               - Provides astronomy ephemeris to plan telescope observations
	PyAstronomy            - A collection of astronomy related tools for Python.
	...

7. (tutorial-env) $ pip install novas
	Collecting novas
	Downloading novas-3.1.1.3.tar.gz (136kB)
	Installing collected packages: novas
	Running setup.py install for novas
	Successfully installed novas-3.1.1.3

8. (tutorial-env) $ pip install requests==2.6.0
	Collecting requests==2.6.0
	Using cached requests-2.6.0-py2.py3-none-any.whl
	Installing collected packages: requests
	Successfully installed requests-2.6.0

9. (tutorial-env) $ pip install --upgrade requests
	Collecting requests
	Installing collected packages: requests
	Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
    Successfully uninstalled requests-2.6.0
	Successfully installed requests-2.7.0
	
10. (tutorial-env) $ pip show requests
	---
	Metadata-Version: 2.0
	Name: requests
	Version: 2.7.0
	Summary: Python HTTP for Humans.
	Home-page: http://python-requests.org
	Author: Kenneth Reitz
	Author-email: me@kennethreitz.com
	License: Apache 2.0
	ocation: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
	Requires:

11. (tutorial-env) $ pip list
	novas (3.1.1.3)
	numpy (1.9.2)
	pip (7.0.3)
	requests (2.7.0)
	setuptools (16.0)
	
12. (tutorial-env) $ pip freeze > requirements.txt
	(tutorial-env) $ cat requirements.txt
	novas==3.1.1.3
	numpy==1.9.2
	requests==2.7.0
	
13. (tutorial-env) $ pip install -r requirements.txt
	Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
	...
	Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
	...
	Collecting requests==2.7.0 (from -r requirements.txt (line 3))
	...
	Installing collected packages: novas, numpy, requests
	Running setup.py install for novas
	Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0