from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Python functions for geocoding addresses using the Radar API'
LONG_DESCRIPTION = 'This package allows users to use the radar module to forward (reverse and ip to be added later on) geocode a list of addresses using the Radar API, extract all the values, and store them in a dataframe.'

# Setting up
setup(
    name="radar_geocoder",
    version=VERSION,
    author="Adventist Virtual",
    author_email="<devsupport@adventistvirtual.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'radar-python'],
    keywords=['python', 'geocoding', 'pandas', 'radar', 'radar-python'],
    classifiers=[
        "Development Status :: Production",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)