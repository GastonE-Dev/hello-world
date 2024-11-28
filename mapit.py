import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])

else:
    # Get address from clipboard:
    address = pyperclip.paste()

# Open the web browser with Google Maps.
webbrowser.open(f'https://www.google.com/maps/place/{address}')