import time
import requests
import concurrent.futures


def check_wiki_page_exist(wiki_page_url, timeout=10):
    response = requests.get(url=wiki_page_url, timeout=timeout)
    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
    elif response.status_code == 404:
        page_status = "does not exist"
    return wiki_page_url + " - " + page_status


wiki_page_urls = [
    "https://en.wikipedia.org/wiki/Shark",
    "https://en.wikipedia.org/wiki/Ocean",
    "https://en.wikipedia.org/wiki/Island",
    "https://en.wikipedia.org/wiki/this_page_does_not_exist",
]


def wiki_test1():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for url in wiki_page_urls:
            futures.append(executor.submit(check_wiki_page_exist, wiki_page_url=url))
        for future in concurrent.futures.as_completed(futures):
            print(future.result())


def wiki_test2():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for url in wiki_page_urls:
            futures.append(
                executor.submit(check_wiki_page_exist, wiki_page_url=url, timeout=0.0005)
            )
        for future in concurrent.futures.as_completed(futures):
            try:
                print(future.result())
            except requests.ConnectTimeout:
                print("ConnectTimeout.")


def run_without_thread():
    page_urls = ["https://en.wikipedia.org/wiki/" + str(i) for i in range(20)]
    print("Running without threads:")
    without_threads_start = time.time()
    for url in page_urls:
        print(check_wiki_page_exist(wiki_page_url=url))
    print("Without threads time:", time.time() - without_threads_start)


def run_with_thread():
    page_urls = ["https://en.wikipedia.org/wiki/" + str(i) for i in range(20)]
    print("Running threaded:")
    threaded_start = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for url in page_urls:
            futures.append(executor.submit(check_wiki_page_exist, wiki_page_url=url))
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
    print("Threaded time:", time.time() - threaded_start)


if __name__ == "__main__":
    # run_without_thread()
    run_with_thread()
