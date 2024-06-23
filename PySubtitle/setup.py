from setuptools import setup, find_packages

setup(
    name='nom_de_votre_bibliotheque',
    version='0.1.0',
    author='Votre Nom',
    author_email='votre.email@example.com',
    description='Une description de votre bibliothèque',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/votre_username/nom_de_votre_bibliotheque',
    packages=find_packages(),
    install_requires=[
        'ffmpeg-python',
        'pydub',
        'SpeechRecognition',
        'webvtt-py'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)