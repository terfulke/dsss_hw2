from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    install_requires=[random],
    entry_points={"console_scripts": ["math_quiz=math_quiz.math_quiz:main"]},  #main function in math_quiz.py
    description="A math quiz application",
    author="Terezia Fuleova",
    author_email="ter.fueleova@fau.de",
    url="https://github.com/terfulke/dsss_hw2",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)