from distutils.core import setup

setup(
    name='ClassicUPS',
    version='0.2.3',
    author='Jay Goel',
    author_email='jay@classicspecs.com',
    url='http://github.com/classicspecs/ClassicUPS/',
    packages=['ClassicUPS'],
    description='Usable UPS Integration in Python',
    long_description=open('README.rst').read(),
    keywords=['UPS'],
    install_requires=[
        'dict2xml==1.6',
        'xmltodict==0.4.2',
        'requests>=2.5.1'
    ],
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta'
    ]
)

# To update pypi: `python setup.py register sdist bdist_wininst upload`
