from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="task3_comp_metrics",
    scripts=['task3_comp_metrics.py'],
    packages=find_packages(),
    install_requires=['psutil'],
    version="1.0",
    author="Michael",
    author_email="michael@example.com",
    description="System Metrics Snapshot Utility",
)
