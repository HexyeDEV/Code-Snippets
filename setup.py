import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Code-Snippets",
    version="0.0.1",
    author="Hexye",
    author_email="dragonsale22@gmail.com",
    description="An api wrapper to return random code snippets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HexyeDEV/Code-Snippeys",
    project_urls={
        "Bug Tracker": "https://github.com/HexyeDEV/Code-Snippets/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
