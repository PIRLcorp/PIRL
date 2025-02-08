from setuptools import setup, find_packages

setup(
    name='pirl',
    version='0.1.0',
    description='AI-driven platform for accelerating innovation in nutrition, health, and sustainability.',
    author='Your Name',  # Change this to your name or company name
    author_email='your.email@example.com',  # Your email
    packages=find_packages(),  # Automatically finds all packages in the project
    install_requires=[  # List of dependencies you might need in your project
        'numpy',
        'pandas',
        'scikit-learn',
        # Add other libraries as needed
    ],
    classifiers=[  # Optional classifiers for PyPi
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
