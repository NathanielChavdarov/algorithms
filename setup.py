import setuptools

VERSION = "0.0.1"

setuptools.setup(
    name="Algorithms",
    version=VERSION,
    author="Nathaniel Chavdarov",
    author_email="49632679+NathanielChavdarov@users.noreply.github.com",
    description="Some algorithms, for learning purposes",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/nathanielchavdarov/algorithms",
    packages=setuptools.find_packages(),
    package_data={"algorithms": ["py.typed"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[],
    setup_requires=["wheel"],
    zip_safe=False,
)
