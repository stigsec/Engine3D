from setuptools import setup, find_packages

setup(
    name='Engine3D',
    version='0.1',
    packages=find_packages(),
    install_requires=['pygame', 'numpy'],
    description='Very basic 3D rendering engine',
    author='stigs',
    author_email='stigsec',
)
