from setuptools import setup, find_packages

setup(
    name='PySubtitle',
    version='0.1.1',
    author='Shadows97',
    author_email='mpoderrick97@gmail.com',
    description='A python library to generate subtitles from a video',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Shadows97/PySubtitle',
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