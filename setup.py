import setuptools

setuptools.setup(
    name="Huy",
    version="1.2",
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
    package_data={'': ['huy.py']},
    include_package_data=True,
)
