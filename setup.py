# -*- coding=utf-8 -*-
"""Setup script for chappi server"""
from setuptools import setup

setup(
    name="poetry_build_not_compressed",
    version="0.1.1",
    packages=["poetry_build_not_compressed"],
    package_dir={"poetry_build_not_compressed": "src/poetry_build_not_compressed"},
    package_data={
        "poetry_build_not_compressed": ["static/*"]
    },
    license="MIT",
    description="Web API for chemodan library remote execution",
    install_requires=[]
)
