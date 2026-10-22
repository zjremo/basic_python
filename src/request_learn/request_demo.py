import json
import logging
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def main():
    logger.debug("hello, this is a requests demo!")
    testPost()

def testGet():
    """结果在result.json中"""
    base_url = "https://github.com/search"
    params = {
        "q": "dotenv",
        "type": "repositories"
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36 Edg/155.0.0.0",
        "Accept": "application/json"
    }

    # read Cookie from Cookie file
    with open('Cookie', "r", encoding="utf-8") as f:
        cookie_text = f.read()
        headers["Cookie"] = cookie_text

    # logger.debug(headers)
    r = requests.get(
        url=base_url,
        params=params,
        headers=headers,
        timeout=(20, 10)
    )

    resp = r.json()
    logger.debug(resp)

    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(resp, f, ensure_ascii=False, indent=2)

def testPost():
    payload = {"name": "张三", "tags": ["a", "b"]}
    try:
        r = requests.post("https://httpbin.org/post", json=payload, timeout=10)
        r.raise_for_status()
        logger.debug(r.json()["json"])
    except requests.HTTPError as e:
        logger.error(f"HTTP Error: {e}")
    except requests.Timeout as e:
        logger.error(f"Timeout Error: {e}")
    except requests.ConnectionError as e:
        logger.error(f"Connection Error: {e}")
    except requests.RequestException as e:
        logger.error(f"Request Error: {e}")
    finally:
        logger.debug("Request completed")

if __name__ == "__main__":
    main()