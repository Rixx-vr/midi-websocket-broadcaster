import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="midi-websocket-broadcaster",
    version="0.0.1",
    author="Snooper XP",
    author_email="snooperxp@gmail.com",
    description="A server that broadcasts midi packets through a websocket",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SnooperXP/midi-websocket-broadcaster",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Langauge :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)