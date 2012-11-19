from setuptools import setup, find_packages
from setuptools.command.test import test


class TestCommand(test):
    def run(self):
        from tests.runtests import runtests
        runtests()


setup(
    name='implace',
    version='0.0.1',
    description='Image placebo.',
    long_description=open('README.rst').read(),
    author='Mikko Hellsing',
    author_email='mikko@aino.se',
    license='BSD',
    url='https://github.com/aino/implace',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=[ 'PIL>=1.1.7' ],
    zip_safe=False,
    cmdclass={"test": TestCommand},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

