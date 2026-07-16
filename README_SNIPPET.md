### Retries & pagination

```python
from whoisfreaks.helpers import with_retries, paginate
result = with_retries(lambda: api.whois_live(domain_name="whoisfreaks.com", api_key=KEY))
for rec in paginate(lambda p: api.dns_historical(domain_name="x.com", type="all", page=p, api_key=KEY),
                    items_field="historical_dns_records"):
    print(rec)
```
