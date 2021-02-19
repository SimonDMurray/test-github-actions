from setuptools import setup, find_packages

setup(
    name="Simon", 
    version="0.0.38",
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
       "numpy>=1.19.2,<2",
       "pandas>=1.2.2",
       "python>=3.6",
       "scikit-learn>=0.23.2",
       "scanpy>=1.7.0",
       "six>=1.15.0",
       "setuptools>=52.0.0",
       "joblib>=1.0.0",
       "mkl-service>=2.3.0",
       "h5py >=3.1.0",
       "seaborn",
       "scipy",
       "python-dateutil >=2.8.1",
       "openssl >=1.0.1",
  ]
)
