import time
import statistics
import requests

URLS = {
    "standard": "https://read-google-sheets-481696182127.northamerica-northeast2.run.app/?sheet_id=1zO6N2c2nKAW6DHJbZHqcJPZBhC3OYvWG0So7wAzbGoE&tab_name=Sheet1",
    "fast_api": "https://sheets-api-481696182127.northamerica-northeast2.run.app?sheet_id=1zO6N2c2nKAW6DHJbZHqcJPZBhC3OYvWG0So7wAzbGoE&tab_name=Sheet1",
}
RUNS = 10

def main():
    print('main')
    results = {name: [] for name in URLS}

    # Interleave the calls so network conditions affect both equally
    for i in range(RUNS):
        for name, url in URLS.items():
            start = time.perf_counter()
            r = requests.get(url, timeout=60)
            elapsed = time.perf_counter() - start
            results[name].append(elapsed)
            print(f"run {i+1:2d} {name:9s} {elapsed:.3f}s  status={r.status_code}  bytes={len(r.content)}")

    print("\nSummary (seconds)")
    for name, times in results.items():
        print(f"{name:9s} mean={statistics.mean(times):.3f}  median={statistics.median(times):.3f}  "
              f"min={min(times):.3f}  max={max(times):.3f}  first={times[0]:.3f}")


if __name__ == "__main__":
    main()
