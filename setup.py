from setuptools import setup, find_packages

setup(
    name="Simon", 
    version="0.0.8",
    description="Test GitHub Actions",
    url="https://github.com/SimonDMurray/test-github-actions/",
    author="Simon",
    author_email="sm42@sanger.ac.uk",
    classifiers=[
       "Programming Language :: Python :: 3",
       "Operating System :: OS Independent"
    ],
    packages=find_packages(),
    python_requires=">=3.6",    
    install_requires=[
       "numpy>=1.19.1", 
       "pandas>=1.1.3", 
       "scikit-learn>=0.23.2",
       "scanpy>=1.6.0" 
  ]
)
