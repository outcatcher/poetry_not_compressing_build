# -*- coding=utf-8 -*-
"""Setup script for chappi server"""
from setuptools import setup

setup(
    name="poetry_build_not_compressed",
    version="0.1.1",
    packages=["with_setup_py"],
    package_dir={"with_setup_py": "src/poetry_build_not_compressed"},
    package_data={
        "with_setup_py": ["static/*"]
    },
    license="MIT",
    description="Web API for chemodan library remote execution",
    install_requires=[]
)
