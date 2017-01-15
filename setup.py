from distutils.core import setup

setup(
    name='Apollo',
    version='0.1',
    packages=['Apollo'],
    url='https://github.com/PugliaSOS/Apollo',
    license='Apache',
    author='paolo',
    author_email='paolodellaquila1999@gmail.com',
    description='command line tool to get weather condition',

     classifiers=[
        'Development Status :: 5 - Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: Apache License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='sample weather condition tool development',

    install_requires=['pyowm','colorama'],
)
