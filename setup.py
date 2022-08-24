from setuptools import find_packages, setup

setup(
    name="pkg-installer", 
    version="1.0.1", 
    author="SML", 
    author_email="seungminlee92@kakao.com", 
    description="git modules installer",
    license="SEUNGMINLEE", 
    packages=find_packages(), 
    data_files=[], 
    install_requires=[
        "importlib_metadata"
    ]
)
