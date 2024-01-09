# YouTube video downloader

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

A DIY way of downloading YouTube videos, using the [pytube](https://github.com/pytube/pytube) library.

## Getting Started <a name = "getting_started"></a>

Clone this repository into your machine:

```
git clone https://github.com/Toorreess/yt-video-downloader
```

### Prerequisites

- Python 3.11.0
- pip 23.3.2

### Installing

If you want use a virtual environment to install the libraries only for this project, first create it and activate it:

```
python -m venv venv

# Windows
.\venv\Scripts\activate

# Unix systems
source venv/bin/activate
```

Then, install the requirements:

```
pip install -r requirements.txt
```

## Usage <a name = "usage"></a>

To define the path where you want the videos to be downloaded, you must complete the output path in the config.yml file. For example:

```
output_path: "/home/Toorreess/Videos"
```

Then, you run the main.py in terminal and follow the instructions.
