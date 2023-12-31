import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='toolbox',
    version='0.0.1',
    author='Mahender',
    author_email='mahender@hotmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/rajingithub/toolbox',
    license='MIT',
    packages=['toolbox'],
    install_requires=['requests'],
)
