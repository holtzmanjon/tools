from setuptools import setup

setup(
    name='holtz-tools',
    version='0.1.0',    
    description='Python utility tools',
    url='https://github.com/holtzmanjon/tools',
    author='Jon Holtzman',
    author_email='holtz@nmsu.edu',
    license='BSD 2-clause',
    packages=['tools'],
    package_dir={"": "python/ptools"},
    install_requires=[
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)

