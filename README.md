# IPA Fetcher

A command-line tool to fetch IPA files from Apple Configurator.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/drewg233/ipafetch.git
cd ipafetch
```

2. Install the package:
```bash
pip install -e .
```

## Usage

Basic usage:
```bash
ipafetch
```

This will use the default location (`~/Desktop/IPAs`) to store the IPA files.

### Command-line Options

- `-o, --output`: Specify a custom directory to store IPA files
```bash
ipafetch -o ~/Downloads/IPAs
# or
ipafetch --output ~/Downloads/IPAs
```

The tool will:
1. Check if Apple Configurator is installed
2. Open Apple Configurator if it's installed
3. Create the specified IPA directory (or use default: ~/Desktop/IPAs)
4. Monitor for new IPA files and copy them automatically

## Requirements

- Python 3.6 or higher
- Apple Configurator (from Mac App Store)

## How it works

1. The tool monitors the Apple Configurator's temporary directory
2. When you use Apple Configurator to install an app, it temporarily stores the IPA file
3. The tool detects new IPA files and copies them to your specified directory
4. You can stop the tool at any time by pressing Ctrl+C 