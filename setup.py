import setuptools

setuptools.setup(
    name = "linter_cleanter",
    version = "0.0.1",
    packages = setuptools.find_packages() + ["config"],
    classifiers=[ # classifiers är en lista med information om paketet
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6", # kräver python 3.6 eller högre
    scripts = ['main.py', 'corrector.py'], # skript som ska installeras
    setup_requires=['wheel'], # kräver wheel
    entry_points = { # entry points är vilka kommandon som ska köras
        'console_scripts': ['linter_cleanter = main:main']
    }
)
# setuptool är en modul som används för att skapa paket och distribuera dem.

# kommand:
# Bygga paketet: python3 setup.py bdist_wheel
# Installera paketet: pip3 install dist/linter_cleanter-0.0.1-py3-none-any.whl