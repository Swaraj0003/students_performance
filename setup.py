from setuptools import setup, find_packages

setup(
    name="Students performance",
    version="1.0.0",
    author="Swaraj",
    author_email="swarajkayaniyil@gmail.com",
    description="A sample Python project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Swaraj0003/students_performance",
    packages=find_packages(),
    install_requires=[
        "pandas",  
        "numpy",
        "matplotlib",
        "seaborn",
        "flask",
        "scikit-learn"
    ]
)
