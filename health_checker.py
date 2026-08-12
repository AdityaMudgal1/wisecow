import sys
import time
import urllib.request
import urllib.error

url = sys.argv[1] if len(sys.argv) > 1 else "https://wisecow.local/"

try:
    start = time.perf_counter()

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Wisecow-Health-Checker/1.0"}
    )

    with urllib.request.urlopen(request, timeout=10) as response:
        elapsed = (time.perf_counter() - start) * 1000
        status = response.status

        if 200 <= status < 400:
            print("Application Health Check")
            print("-------------------------")
            print(f"URL: {url}")
            print(f"HTTP Status: {status}")
            print(f"Response Time: {elapsed:.2f} ms")
            print("Status: UP")
            sys.exit(0)
        else:
            print(f"HTTP Status: {status}")
            print("Status: DOWN")
            sys.exit(1)

except urllib.error.HTTPError as error:
    print("Application Health Check")
    print("-------------------------")
    print(f"URL: {url}")
    print(f"HTTP Status: {error.code}")
    print("Status: DOWN")
    sys.exit(1)

except Exception as error:
    print("Application Health Check")
    print("-------------------------")
    print(f"URL: {url}")
    print(f"Error: {error}")
    print("Status: DOWN")
    sys.exit(1)