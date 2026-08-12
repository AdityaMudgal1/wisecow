import re
import sys
from collections import Counter
from pathlib import Path


LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<time>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<path>\S+) \S+" (?P<status>\d{3})'
)


def analyze_log(file_path):
    path = Path(file_path)

    if not path.is_file():
        print(f"Error: Log file not found: {file_path}")
        return 1

    status_codes = Counter()
    requested_pages = Counter()
    client_ips = Counter()
    total_requests = 0

    with path.open("r", encoding="utf-8", errors="ignore") as log_file:
        for line in log_file:
            match = LOG_PATTERN.search(line)

            if not match:
                continue

            total_requests += 1
            status = match.group("status")
            page = match.group("path")
            ip = match.group("ip")

            status_codes[status] += 1
            requested_pages[page] += 1
            client_ips[ip] += 1

    print("\nWisecow Log Analysis Report")
    print("=" * 30)
    print(f"Log file: {path}")
    print(f"Total requests: {total_requests}")

    print("\nHTTP Status Summary:")
    for status, count in status_codes.most_common():
        print(f"  {status}: {count}")

    print(f"\n404 errors: {status_codes.get('404', 0)}")

    print("\nMost Requested Pages:")
    for page, count in requested_pages.most_common(5):
        print(f"  {page}: {count}")

    print("\nTop Client IPs:")
    for ip, count in client_ips.most_common(5):
        print(f"  {ip}: {count}")

    return 0


if __name__ == "__main__":
    log_file = sys.argv[1] if len(sys.argv) > 1 else "sample_access.log"
    raise SystemExit(analyze_log(log_file))