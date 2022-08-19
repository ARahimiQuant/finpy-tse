import setuptools

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name='finpy_tse',                           # should match the package folder
    packages=['finpy_tse'],                     # should match the package folder
    version='1.1.0',                                # important for updates
    license='BSD (3-clause)',                                  # should match your chosen license
    description='A Python Module to Access Tehran Stock Exchange Historical and Real-Time Data',
    long_description=long_description,              # loads your README.md
    long_description_content_type="text/markdown",  # README.md is of type 'markdown'
    author='ALI RAHIMI  AND  RASOOL GHAFOURI AND TAHA SHIRAZI',
    author_email='a.rahimi.aut@gmail.com',
    install_requires=['requests','jdatetime','pandas','numpy','requests','bs4','asyncio','urllib3','aiohttp','unsync','IPython','persiantools','datetime','XlsxWriter','lxml'],                  # list all packages that your package uses
    
)