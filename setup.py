# -*- coding: utf-8 -*-
#from ez_setup import use_setuptools
#use_setuptools()
__revision__ = "$Id$"
import sys
import os
from setuptools import setup, find_packages
import glob

_MAJOR = 0
_MINOR = 1
_MICRO = 2
version = '%d.%d.%d' % (_MAJOR, _MINOR, _MICRO)
release = '%d.%d' % (_MAJOR, _MINOR)

metainfo = {
    'authors': {
    'Türei':('Dénes Türei','denes@ebi.ac.uk'),
    },
    'version': version,
    'license': 'LGPL',
    'download_url': ['http://157.181.231.40/~denes/bioigraph'],
    'url': ['http://157.181.231.40/~denes/bioigraph'],
    'description': 'Work with molecular networks in Python igraph',
    'platforms': ['Linux', 'Unix', 'MacOSX', 'Windows'],
    'keywords': ['graph', 'network', 'protein', 'mRNA', 'DNA', 'signaling',
                 'SignaLink', 'SIGNOR', 'InnateDB', 'IntAct', 'Reactome',
                 'MPPI', 'NCI-PID', 'DIP', 'MatrixDB', 'PANTHER',
                 'PhosphoSite', 'PhosphoPoint', 'DEPOD', 'SPIKE', 'KEGG',
                 'Autophagy', 'ARN', 'NRF2', 'NRF2ome', 'regulation',
                 'phosphorylation', 'kinase', 'phosphatase',
                 'dephosphorylation', 'directed graph'],
    'classifiers': [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: GNU Library or Lesser General Public License (LGPL)',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Scientific/Engineering :: Bio-Informatics',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'Topic :: Scientific/Engineering :: Mathematics']
}

#package_data = [
    #'bioigraph/data/alzpw-ppi.csv', 
    #'bioigraph/data/arn_014.csv', 
    #'bioigraph/data/arn.csv', 
    #'bioigraph/data/arn_lr01.csv', 
    #'bioigraph/data/ca1.csv', 
    #'bioigraph/data/cancer_gene_census.csv', 
    #'bioigraph/data/cell-map-edge-attributes.txt', 
    #'bioigraph/data/dd_refs.csv', 
    #'bioigraph/data/depod-refs.csv', 
    #'bioigraph/data/dip_human_core_processed.csv', 
    #'bioigraph/data/entrez_uniprot.csv', 
    #'bioigraph/data/gdsc.sif', 
    #'bioigraph/data/gold_standard.csv', 
    #'bioigraph/data/gold_standard.xlsx', 
    #'bioigraph/data/innatedb.csv', 
    #'bioigraph/data/intact_filtered.csv', 
    #'bioigraph/data/krishnadev_atg_1.tab', 
    #'bioigraph/data/krishnadev_atg.tab', 
    #'bioigraph/data/krishnadev_vegeredmeny.csv', 
    #'bioigraph/data/kshirsagar_atg_1.tab', 
    #'bioigraph/data/kshirsagar_atg.tab', 
    #'bioigraph/data/kshirsagar_vegeredmeny.csv', 
    #'bioigraph/data/macrophage-strict.csv', 
    #'bioigraph/data/matrixdb_core.csv', 
    #'bioigraph/data/mppi_human_rep.csv', 
    #'bioigraph/data/nci-pid-strict.csv', 
    #'bioigraph/data/netpath_refs.csv', 
    #'bioigraph/data/nrf2ome.csv', 
    #'bioigraph/data/phosphopoint.csv', 
    #'bioigraph/data/phosphosite_human_hc.csv', 
    #'bioigraph/data/phosphosite_human_noref.csv', 
    #'bioigraph/data/salmonella_atg.tar.gz', 
    #'bioigraph/data/sec_ac.txt', 
    #'bioigraph/data/shlecker_atg_1.tab', 
    #'bioigraph/data/shlecker_vegeredmeny.csv', 
    #'bioigraph/data/signor_ppi.tsv', 
    #'bioigraph/data/slk01human.csv', 
    #'bioigraph/data/spike_hc.csv', 
    #'bioigraph/data/swissprot2.csv', 
    #'bioigraph/data/swissprot-gsymbol-name.csv', 
    #'bioigraph/data/trembl2.csv', 
    #'bioigraph/data/uniprot-all-human.tab',
    #'bioigraph/data/intogene_cancerdrivers.tsv'
#]

with open('README.rst') as f:
    readme = f.read()
with open('HISTORY.rst') as f:
    history = f.read()

setup(
    name = 'bioigraph',
    version = version,
    maintainer = metainfo['authors']['Türei'][0],
    maintainer_email = metainfo['authors']['Türei'][1],
    author = metainfo['authors']['Türei'][0],
    author_email = metainfo['authors']['Türei'][1],
    long_description = readme + '\n\n' + history,
    keywords = metainfo['keywords'],
    description = metainfo['description'],
    license = metainfo['license'],
    platforms = metainfo['platforms'],
    url = metainfo['url'],
    download_url = metainfo['download_url'],
    classifiers = metainfo['classifiers'],
    # package installation
    package_dir = {'':'src'},
    packages = list(set(find_packages() + ['bioigraph', 'bioigraph.data'])),
    include_package_data = True,
    install_requires = ['python-igraph','MySQL-python','bioservices', 'pycurl']
)
