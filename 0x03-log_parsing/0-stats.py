#!/usr/bin/python3
import sys
import signal
import re

def print_stats(total_size, status_codes):
    """Print the statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Handle CTRL+C signal."""
    print_stats(total_file_size, status_codes)
    sys.exit(0)

# Initialize variables
total_file_size = 0
line_count = 0
status_codes = {
    200: 0, 301: 0, 400: 0, 401: 0,
    403: 0, 404: 0, 405: 0, 500: 0
}

# Regular expression pattern for line validation
pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'

# Set up signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            # Remove trailing whitespace
            line = line.strip()
            
            # Check if line matches the expected format
            match = re.match(pattern, line)
            if not match:
                continue
            
            # Extract status code and file size
            status_code = int(match.group(1))
            file_size = int(match.group(2))
            
            # Update metrics
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_file_size += file_size
            line_count += 1
            
            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_file_size, status_codes)
                
        except (ValueError, IndexError):
            continue
            
except KeyboardInterrupt:
    print_stats(total_file_size, status_codes)
    sys.exit(0)
