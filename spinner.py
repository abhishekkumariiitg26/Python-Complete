import time
import sys

spinner = ["|", "/", "-", "\\"]
for _ in range(20):  # Run the animation for a short duration
    for symbol in spinner:
        sys.stdout.write(f"\rLoading... {symbol}")  # Overwrite line with `\r`
        sys.stdout.flush()  # Ensure immediate output
        time.sleep(0.1)  # Small delay for animation

print("\rDone!       ")  # Clear the spinner with final message
