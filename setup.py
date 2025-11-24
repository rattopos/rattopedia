"""MkDocs 플러그인 설치 스크립트"""
from setuptools import setup, find_packages

setup(
    name="mkdocs-auto-index",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'auto_index = mkdocs_plugins.auto_index:AutoIndexPlugin',
        ],
    },
)

