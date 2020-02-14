import setuptools


import os
package_dir = os.path.dirname(os.path.realpath(__file__))
include_dir = os.path.join(package_dir, 'docs')


setuptools.setup(
    name="Huy",
    version="0.4",
    author="Petr Srakovorodnikov",
    author_email="petya.obosralsya@mail.ru",
    description="A package to draw dicks",
    url="https://github.com/Torrentov/Fun_package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    inclode_dirs = [include_sir],
)
