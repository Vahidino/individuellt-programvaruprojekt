import setuptools

setuptools.setup(
    name = "linter_cleanter",
    version = "0.0.1",
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6",
    scripts = ['main.py', 'config.json', 'corrector.py'],
    setup_requires=['wheel'],
    entry_points = {
        'console_scripts': ['linter_cleanter = main:main']
    }
)