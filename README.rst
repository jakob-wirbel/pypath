pypath
######


:note: Pypath supports both Python 2.7 and Python 3.5+. In the beginning, pypath has been developed only for Python 2.7. The methods are adjusted to Py3 in arbitrary order, depending on their importance. The vaste majority of the module already has been tested in Py3.

:contributions: denes@ebi.ac.uk
:documentation: http://pypath.omnipathdb.org/
:issues: https://github.com/saezlab/pypath/issues

**pypath** is a Python package built around igraph to work with molecular network representations e.g. protein, miRNA and drug compound interaction networks.

Webservice
==========

One instance of the pypath webservice running on the domain http://omnipathdb.org/, serving the OmniPath data with additional PTMs. It serves data in REST style, by HTTP protocol (browser, wget, curl or anything can make requests). This host is accessible only on the EBI internal network. From outside you can use SSH tunnel of course. The webservice currently recognizes 6 types of queries: ``interactions``, ``ptms``, ``resources``, ``network``, ``about`` and ``info``. 

A request without any parameter, gives some basic numbers about the actual loaded dataset:

    http://omnipathdb.org

The ``about`` tells the version number:

    http://omnipathdb.org/about

The ``network`` prints basic statistics about the whole network:
    
    http://omnipathdb.org/network

The ``resources`` returns the list of all resources with their size:
    
    http://omnipathdb.org/resources

The ``info`` returns a HTML page with comprehensive information about the resources:

    http://omnipathdb.org/info

The ``interactions`` accepts some parameters and returns interactions in tabular format. This example returns all interactions of EGFR (P00533), with sources and references listed:

    http://omnipathdb.org/interactions/P00533/?fields=sources&fields=references

The parameters can be omitted. More UniProts can be given separated by comma, and JSON format is available too (better for import to Python!):

    http://omnipathdb.org/interactions/P00533,O15117,Q96FE5?format=json

Another interface is ``ptms``, to list enzymes, substrates and PTMs. 

    http://omnipathdb.org/ptms/P00533?ptm_type=phosphorylation&fields=sources&fields=references

To list all interactions simply request:

    http://omnipathdb.org/interactions

To list all PTMs similarly:

    http://omnipathdb.org/ptms

Installation
============

Linux
-----

In almost any up-to-date Linux distribution the dependencies of **pypath** are built-in, or provided by the distributors.
You only need to install a couple of things in your package manager (cairo, py(2)cairo, igraph, python(2)-igraph, graphviz, pygraphviz), and after install **pypath** by *pip* (see below).
If any module still missing, you can install them the usual way by *pip* or your package manager.

igraph C library, cairo and pycairo
-----------------------------------

*python(2)-igraph* is a Python interface to use the igraph C library. The C library must be installed.
The same goes for *cairo*, *py(2)cairo* and *graphviz*.

Directly from git
-----------------

.. code:: bash
    
    pip install git+https://github.com/saezlab/pypath.git

With pip
--------

Download the package from /dist, and install with pip:

.. code:: bash
    
    pip install pypath-x.y.z.tar.gz

Build source distribution
-------------------------

Clone the git repo, and run setup.py:

.. code:: bash
    
    python setup.py sdist

Mac OS X
--------

On OS X installation is not straightforward primarily because cairo needs to be compiled from source. We provide 3 scripts here: the **mac-install-source.sh** requires only Python 2.7 and Xcode installed, while the **mac-install-brew.sh** to install everything with HomeBrew, and **mac-install-conda.sh** to install from Anaconda distribution. With these scripts installation of igraph, cairo and graphviz goes smoothly most of the time, and options are available for omitting the 2 latter. To know more see the description in the script header.

Troubleshooting
~~~~~~~~~~~~~~~

* ``no module named ...`` when you try to load a module in Python. Did the installation of the module run without error? Try to run again the specific part from the mac install shell script to see if any error comes up. Is the path where the module has been installed in your ``$PYTHONPATH``? Try ``echo $PYTHONPATH`` to see the current paths. Add your local install directories if those are not there, e.g. ``export PYTHONPATH="/Users/me/local/python2.7/site-packages:$PYTHONPATH"``. If it works afterwards, don't forget to append these export path statements to your ``~/.bash_profile``, so these will be set every time you launch a new shell.

* ``pkgconfig`` not found. Check if the ``$PKG_CONFIG_PATH`` variable is set correctly, and pointing on a directory where pkgconfig really can be found.

* Error while trying to install py(2)cairo by pip. py(2)cairo could not be installed by pip, but only by waf. Please set the ``$PKG_CONFIG_PATH`` before. See **mac-install-source.sh** on how to install with waf.

* Error at pygraphviz build: ``graphviz/cgraph.h file not found``. This is because the directory of graphviz detected wrong by pkgconfig. See **mac-install-source.sh** how to set include dirs and library dirs by ``--global-option`` parameters.

* Can not install bioservices, because installation of jurko-suds fails. Ok, this fails because pip is not able to install the recent version of setuptools, because a very old version present in the system path. The development version of jurko-suds does not require setuptools, so you can install it directly from git as it is done in **mac-install-source.sh**.

* In **Anaconda**, *pypath* can be imported, but the modules and classes are missing. Apparently Anaconda has some built-in stuff called *pypath*. This has nothing to do with this module. Please be aware that Anaconda installs a completely separated Python distribution, and does not detect modules in the main Python installation. You need to install all modules within Anaconda's directory. **mac-install-conda.sh** does exactly this. If you still experience issues, please contact us.

Microsoft Windows
-----------------

Not many people have used *pypath* on Microsoft computers so far. Please share your experiences and contact us if you encounter any issue. We appreciate your feedback, and it is very important for us to provide better support for Microsoft computers.

With Anaconda
~~~~~~~~~~~~~

The same workflow like you see in ``mac-install-conda.sh`` should work for Anaconda on Windows. The only problem you certainly will encounter is that not all the channels have packages for all platforms. If certain channel provides no package for Windows, or for your Python version, you just need to find an other one. For this, do a search:

.. code:: bash
    
    anaconda search -t conda <package name>

For example, if you search for *pycairo*, you will find out that *vgauther* provides it for osx-64, but only for Python 3.4, while *richlewis* provides also for Python 3.5. And for win-64 platform, there is the channel of *KristanAmstrong*. Go along all the commands in ``mac-install-conda.sh``, and modify the channel if necessary, until all packages install successfully.

With other Python distributions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here the basic principles are the same as everywhere: first try to install all external dependencies, after *pip* install should work. On Windows certain packages can not be installed by compiled from source by *pip*, instead the easiest to install them precompiled. These are in our case *fisher, lxml, numpy (mkl version), pycairo, igraph, pygraphviz, scipy and statsmodels*. The precompiled packages are available here: http://www.lfd.uci.edu/~gohlke/pythonlibs/. We tested the setup with Python 3.4.3 and Python 2.7.11. The former should just work fine, while with the latter we have issues to be resolved.

Known issues
~~~~~~~~~~~~

* *"No module fabric available."* -- or *pysftp* missing: this is not important, only certain data download methods rely on these modules, but likely you won't call those at all.
* Progress indicator floods terminal: sorry about that, will be fixed soon.
* Encoding related exceptions in Python2: these might occur at some points in the module, please send the traceback if you encounter one, and we will fix as soon as possible.

*Special thanks to Jorge Ferreira for testing pypath on Windows!*

Release History
===============

Main improvements in the past releases:

0.1.0:
------
* First release of pypath, for initial testing.

0.2.0:
-----
* Lots of small improvements in almost every module
* Networks can be read from local files, remote files, lists or provided by any function
* Almost all redistributed data have been removed, every source downloaded from the original provider.

0.3.0:
------
* First version whith partial Python 3 support.

0.4.0:
------
* **pyreact** module with **BioPaxReader** and **PyReact** classes added
* Process description databases, BioPax and PathwayCommons SIF conversion rules are supported
* Format definitions for 6 process description databases included.

0.5.0:
------
* Many classes have been added to the **plot** module
* All figures and tables in the manuscript can be generated automatically
* This is supported by a new module, **analysis**, which implements a generic workflow in its **Workflow** class.

Upcoming:
---------
* New, more flexible network reader class
* Full support for multi-species molecular interaction networks (e.g. pathogene-host)
* Better support for not protein only molecular interaction networks (metabolites, drug compounds, RNA)
* ChEMBL webservice interface, interface for PubChem and eventually for DrugBank
* Silent mode: a way to suppress messages and progress bars

Features
========

The primary aim of **pypath** is to build up networks from multiple sources on one igraph object. **pypath** handles ambiguous ID conversion, reads custom edge and node attributes from text files and **MySQL**.

Submodules perform various features, e.g. graph visualization, working with drug compound data, searching drug targets and compounds in **ChEMBL**. 

ID conversion
-------------

The ID conversion module ``mapping`` can be used independently. It has the feature to translate secondary UniProt IDs to primaries, and Trembl IDs to SwissProt, using primary Gene Symbols to find the connections. This module automatically loads and stores the necessary conversion tables. Many tables are predefined, such as all the IDs in **UniProt mapping service,** while users are able to load any table from **file** or **MySQL,** using the classes provided in the module ``input_formats``.

Pathways
--------

**pypath** includes data and predefined format descriptions for more than 25  high quality, literature curated databases. The inut formats are defined in the ``data_formats`` module. For some resources data downloaded on the fly, where it is not possible, data is redistributed with the module. Descriptions and comprehensive information about the resources is available in the ``descriptions`` module. 

Structural features
-------------------

One of the modules called ``intera`` provides many classes for representing structures and mechanisms behind protein interactions. These are ``Residue`` (optionally mutated), ``Motif``, ``Ptm``, ``Domain``, ``DomainMotif``, ``DomainDomain`` and ``Interface``. All these classes have ``__eq__()`` methods to test equality between instances, and also ``__contains__()`` methods to look up easily if a residue is within a short motif or protein domain, or is the target residue of a PTM.

Sequences
---------

The module ``seq`` contains a simple class for quick lookup any residue or segment in **UniProt** protein sequences while being aware of isoforms.

Tissue expression
-----------------

For 3 protein expression databases there are functions and modules for downloading and combining the expression data with the network. These are the Human Protein Atlas, the ProteomicsDB and GIANT. The ``giant`` and ``proteomicsdb`` modules can be used also as stand alone Python clients for these resources.

Functional annotations
----------------------

**GSEA** and **Gene Ontology** are two approaches for annotating genes and gene products, and enrichment analysis technics aims to use these annotations to highlight the biological functions a given set of genes is related to. Here the ``enrich`` module gives abstract classes to calculate enrichment statistics, while the ``go`` and the ``gsea`` modules give access to GO and GSEA data, and make it easy to count enrichment statistics for sets of genes.

Drug compounds
--------------

**UniChem** submodule provides an interface to effectively query the UniChem service, use connectivity search with custom settings, and translate SMILEs to ChEMBL IDs with ChEMBL web service.

**ChEMBL** submodule queries directly your own ChEMBL MySQL instance, has the features to search targets and compounds from custom assay types and relationship types, to get activity values, binding domains, and action types. You need to download the ChEMBL MySQL dump, and load into your own server.

Technical
---------

**MySQL** submodule helps to manage MySQL connections and track queries. It is able to run queries parallely to optimize CPU and memory usage on the server, handling queues, and serve the result by server side or client side storage. The ``chembl`` and potentially the ``mapping`` modules rely on this ``mysql`` module.

The most important function in module ``dataio`` is a very flexible **download manager** built around ``curl``. The function ``dataio.curl()`` accepts numerous arguments, tries to deal in a smart way with local **cache,** authentication, redirects, uncompression, character encodings, FTP and HTTP transactions, and many other stuff. Cache can grow to several GBs, and takes place in ``./cache`` by default. Please be aware of this, and use for example symlinks in case of using multiple working directories.

A simple **webservice** comes with this module: the ``server`` module based on ``twisted.web.server`` opens a custom port and serves plain text tables over HTTP with REST style querying.
