from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="allreverso",
      version="1.2.7",
      description="A simple package to handle allreverso.net services (translation, voice, dictionary etc.).",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="PetitPotiron",
      packages=["allreverso"],
      install_requires=["requests", "bs4", "lxml"],
      license="Apache 2.0",
      classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Topic :: Internet :: WWW/HTTP",
            "Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking",
            "Environment :: Console",
            "Environment :: Web Environment",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
      ],
      project_urls={
            'Homepage': 'https://github.com/PetitPotiron/allreverso',
      }
      )
