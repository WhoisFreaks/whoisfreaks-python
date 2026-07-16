"""Hand-maintained ergonomic helpers layered onto the generated whoisfreaks SDK.

Provides retry-with-backoff and a pagination iterator that work with the
generated api classes. Kept in an overlay so `make generate-python` never
overwrites it.
"""
from __future__ import annotations
import time
from typing import Callable, Iterator, Any

def with_retries(fn: Callable[[], Any], *, retries: int = 3, backoff: float = 0.5,
                 retry_on=(429, 500, 502, 503, 504)):
    """Call *fn*, retrying on transient HTTP status codes with exponential backoff."""
    last = None
    for attempt in range(retries + 1):
        try:
            return fn()
        except Exception as exc:  # generated ApiException carries .status
            status = getattr(exc, "status", None)
            last = exc
            if status in retry_on and attempt < retries:
                time.sleep(backoff * (2 ** attempt))
                continue
            raise
    raise last  # pragma: no cover

def paginate(fetch_page: Callable[[int], Any], *, page_field: str = "total_pages",
             items_field: str) -> Iterator[Any]:
    """Iterate all items across paginated endpoints (historical/reverse WHOIS, DNS…).

    *fetch_page(page)* must return a response object exposing *page_field* and
    *items_field*.
    """
    page = 1
    while True:
        resp = fetch_page(page)
        for item in getattr(resp, items_field, []) or []:
            yield item
        total = getattr(resp, page_field, page) or page
        if page >= total:
            return
        page += 1
