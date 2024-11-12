#!/usr/bin/env python3

import readline
import argparse

# Function to collect strings with autocomplete support
def collect_strings_with_autocomplete(completion_file=None, output_file=None):
    # Default completions list
    default_completions = [
        "apple", "banana", "grape", "kiwi", "orange", "pear", "peach", "plum", "apricot", "avocado"
    ]
    
    # Load completions from the file if provided
    if completion_file:
        try:
            with open(completion_file, 'r') as file:
                completions = [line.strip() for line in file.readlines()]
        except Exception as e:
            print(f"Error reading file: {e}")
            completions = default_completions
    else:
        completions = default_completions

    # Define the completer function for auto-completion
    def completer(text, state):
        options = [s for s in completions if s.startswith(text)]
        if state < len(options):
            return options[state]
        else:
            return None

    # Set up the autocomplete using readline
    readline.set_completer(completer)
    readline.set_completer_delims('')
    readline.parse_and_bind("tab: complete")  # Enable tab completion

    print("Start typing strings (press Enter after each string). Type 'done' to finish.\n")

    # List to hold the collected strings
    collected_strings = []

    # Loop to collect strings from user input
    prefill = ''
    while True:
        def hook():
            readline.insert_text(prefill)
            readline.redisplay()
        if prefill:
            readline.set_pre_input_hook(hook)
        user_input = input('Enter a string: ').strip()
        readline.set_pre_input_hook()
        
        if user_input.lower() == "done":
            break

        if user_input:
            if user_input in completions:
                collected_strings.append(user_input)
            else:
                print(f'ERROR: match not found: {user_input}')
    
    # Output collected strings to console or file
    if output_file:
        try:
            with open(output_file, 'a') as f:
                for s in collected_strings:
                    f.write(s + "\n")
            print(f"\nCollected strings saved to {output_file}")
        except Exception as e:
            print(f"Error writing to file: {e}")
    else:
        print("\nCollected strings:")
        for s in collected_strings:
            print(s)


# Main function with argparse to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description="Collect strings with auto-completion and optional file output.")
    parser.add_argument(
        '-f', '--file', 
        type=str, 
        help="Path to a file containing possible completions (one per line)."
    )
    parser.add_argument(
        '-o', '--output', 
        type=str, 
        help="Path to a file where collected strings will be saved."
    )
    
    args = parser.parse_args()
    
    # Call the function with the necessary arguments
    collect_strings_with_autocomplete(completion_file=args.file, output_file=args.output)


if __name__ == "__main__":
    main()
