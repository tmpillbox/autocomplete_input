# String Collector with Autocompletion

This Python program allows users to collect a list of strings through a command-line interface with autocompletion support. The program can optionally load autocompletion suggestions from a file and save the collected strings to a file.

## Features

- **Autocompletion**: Offers autocompletion suggestions as the user types, filtered based on the input string.
- **File-Based Autocompletion**: Optionally loads autocompletion suggestions from a file.
- **Save to File**: Collect and save the strings to a file.
- **Interactive Prompt**: Collects strings interactively, and you can type `done` to finish.

## Requirements

- Python 3.x
- The `readline` module (typically included with Unix-like systems. On Windows, you may need to install `pyreadline`).

### Install `pyreadline` on Windows

```bash
pip install pyreadline
```

## Installation

1. Clone or download this repository.
1. Ensure Python3.x is installed on your system.

## Usage
### Basic Usage
To run the program, simply execute the script:
```bash
python autocomplete_input.py
```

This will start the porgram with the default list of autocompletion suggestions. You can type in the prompt and press `Tab` to see autocomplete suggestions.

### Autocompletion with Custom File
To load custom autocompletion suggestions from a file, use the `--file` (or `-f`) option. The file should contain one completion string per line.

Example:
```bash
python autocomplete.py --file completions.txt
```
This will load suggestions from completions.txt

### Save Collected Strings to File
You can optionally save the collected strings to a file by using the `--output` (or `-o`) option. The collected strings will be saved to the specified file.

Example:
```bash
python autocomplete.py --output collected_strings.txt
```
This will save the collected strings to `collected_strings.txt`.

### Combining Both Options
You can combine both `--file` and `--output` options to load completions from a file and save the collected strings to another file:

```bash
python autocomplete.py --file completions.txt --output collected_strings.txt
```

### Command-Line Arguments
* `-f`, `--file`: Path to a file containing possible completions (one per line).
* `-o`, `--output`: Path to a file where collected strings will be saved.
* `-h`, `--help`: Show the help message and exit.

### Example Run
1. Star the program with default completions:
    ```bash
    python autocomplete.py
    ```
2. Start the program with custom completions from a file:
    ```bash
    python autocomplete.py --file completions.txt
    ```
3. Save collected strings to a file:
    ```bash
    python autocomplete.py --output collected_strings.txt
    ```
4. Load completions from a file and save collected strings to another file:
    ```bash
    python autocomplete.py --file completions.txt --output collected_strings.txt
    ```

#### Example `completions.txt`
The `completions.txt` file should contain one completion string per line:
```
apple
banana
grape
kiwi
orange
pear
peach
plum
apricot
avocado
```
