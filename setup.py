import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mearecipes",
    version="0.0.4",
    author="Rudi Mears",
    author_email="rudi.mears@gmail.com",
    description="A small package to create shopping lists from selected recipes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rm646/mearecipes",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "mearecipes = mearecipes.main:cli",
        ],
    },
    install_requires=[
        "click",
	"astropy",
	"pyyaml",
    ],
    python_requires='>=3.6',
)
