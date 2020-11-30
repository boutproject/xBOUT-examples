xBOUT examples
==============

A set of self-contained examples showing various features of
[xBOUT](github.com/boutproject/xBOUT).

Getting started
---------------

These examples require xBOUT and Jupyter. You can install these and all their
requirements using conda (after setting up
[anaconda](https://www.anaconda.com/) or
[miniconda](https://docs.conda.io/en/latest/miniconda.html)) by running
```
$ conda install -c conda-forge xbout jupyter
```

If you prefer to use [pip](https://pip.pypa.io/en/stable/) run
```
$ pip install xbout jupyter
```

Once xBOUT and Jupyter are installed, run
```
$ jupyter notebook
```
in the xBOUT-examples directory. A Jupyter session will open in a web browser.
Click on the subdirectory for the example you are interested in, and then click
on the Jupyter notebook (file ending `.ipynb`) to open the example, and follow
the instructions there.

Contributor guidelines
----------------------

In order to make the examples easy to use, we keep them in a single repo and do
not use git-lfs. That means we need to stop the repo from getting too big. We
also want the examples to be self-contained, so people do not need to have
BOUT++ set up and running before they can run these examples.

Some guidelines for making examples:

* Ideally the code and inputs to create datasets should be publically available
  and linked from the example.

* Even if the code is available, the dataset needed for each example should be
  archived on [Zenodo](zenodo.org) so that the example can be run
  independently.

    * Please provide a setup call to download the data from Zenodo if it is not
      present.

* We will use squash-merging of pull requests to minimise the number of data
  objects (e.g. plot output in Jupyter notebooks) present in the history.

    * We should also try to make PRs with significant changes as complete as
      possible before merging so that we minimise the number of PRs that make
      changes to data objects.

    * Small PRs fixing typos, etc., should be fine as long as they do not
      modify data.
