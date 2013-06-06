from setuptools import setup, find_packages

setup(
    name="tdaemon",
    version="0.1.3",
    maintainer="John Paulett",
    maintainer_email="john@7oars.com",
    description="Test Daemon",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    url="http://github.com/brunobord/tdaemon",
    license="MIT",
    platforms=['POSIX', 'Windows'],
    keywords=['test', 'testing', 'noestests', 'django', 'py.test'],
    packages=find_packages(),
    data_files=[('', ['LICENSE'])],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
    ],
    entry_points={
        'console_scripts': [
            'tdaemon = tdaemon:main',
        ],
    },
    py_modules=['tdaemon'],
    include_package_data=True,
)
