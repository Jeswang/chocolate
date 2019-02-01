import sys

from setuptools import setup, find_packages, Extension

hv_module = Extension("chocolate.mo.hv",
                      sources=["chocolate/mo/_hv.c", "chocolate/mo/hv.cpp"],
                      optional=True,
                      extra_compile_args = ["-std=c++11", "-stdlib=libc++"])

setup(
    name="chocolate",
    version="0.6",
    packages=find_packages(exclude=['examples', 'tests']),
    test_suite="tests",
    install_requires=["numpy>=1.11", "scipy>=0.18", "scikit-learn>=0.18", "pandas>=0.19", "dataset>=0.8", "filelock>=2.0"],
    author="François-Michel De Rainville, Olivier Gagnon",
    author_email="chocolate@novasyst.com",
    description="Asynchrone hyperparameter optimization",
    license="BSD 3-clauses",
    keywords="AsynchroneHyperparameter Optimizer",
    url="http://github.com/NovaSyst/chocolate",
    ext_modules=[hv_module],
)
