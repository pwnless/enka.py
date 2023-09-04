import setuptools

setuptools.setup(
    name="enka.py",
    version="1.1.5",
    author="pwnless",
    author_email="mystream@riseup.net",
    description="Library for fetching JSON data from site https://enka.network/",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pwnless/enka.py",
    keywords=['enkapy.py', 'enkapy', 'enka.network', 'genshinapi'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
    install_requires=[
        "pydantic",
        "aiohttp",
        "aiocache"
    ],
    python_requires=">=3.6",
    include_package_data=True
)
