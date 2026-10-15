# WhoisFreaks Python SDK: WHOIS API Client for Python

[![PyPI version](https://img.shields.io/pypi/v/whoisfreaks.svg)](https://pypi.org/project/whoisfreaks/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![API status](https://img.shields.io/badge/API%20status-live-brightgreen.svg)](https://status.whois.whoisfreaks.com/)

The official Python client for the [WhoisFreaks WHOIS API](https://whoisfreaks.com/products/whois-api). Look up live WHOIS records for any domain across 1,529+ TLDs, pull WHOIS history back to 1986, search registrants with reverse WHOIS and run bulk WHOIS lookups from Python code.

The same package covers the [DNS lookup API](https://whoisfreaks.com/products/dns-checker-api), [domain availability API](https://whoisfreaks.com/products/domain-availability-api), [typosquatting API](https://whoisfreaks.com/products/domain-typosquats-api), [SSL certificate API](https://whoisfreaks.com/products/ssl-certificate-api), IP geolocation and IP reputation.

A live WHOIS lookup returns structured JSON like this (trimmed):

```json
{
  "status": true,
  "domain_name": "whoisfreaks.com",
  "domain_registered": "yes",
  "create_date": "2019-03-19",
  "update_date": "2026-02-17",
  "expiry_date": "2027-03-19",
  "domain_registrar": {
    "iana_id": "1068",
    "registrar_name": "NAMECHEAP INC",
    "normalized_name": "namecheap, inc.",
    "website_url": "http://www.namecheap.com"
  },
  "registrant_contact": {
    "city": "Lewes",
    "state": "Delaware",
    "zip_code": "19958",
    "country_name": "United States",
    "country_code": "US"
  },
  "name_servers": ["albert.ns.cloudflare.com", "sue.ns.cloudflare.com"],
  "domain_status": ["clienttransferprohibited"]
}
```

## Contents

- [Installation](#installation)
- [Get an API key](#get-an-api-key)
- [WHOIS lookup](#whois-lookup)
- [Normalized registrar, address and date fields](#normalized-registrar-address-and-date-fields)
- [Bulk WHOIS lookup](#bulk-whois-lookup)
- [WHOIS history](#whois-history)
- [Reverse WHOIS](#reverse-whois)
- [DNS lookup](#dns-lookup)
- [Domain availability check](#domain-availability-check)
- [Typosquatting detection](#typosquatting-detection)
- [Error handling](#error-handling)
- [All endpoints](#all-endpoints)
- [Requirements](#requirements)
- [Support](#support)

## Installation

```sh
pip install whoisfreaks
```

## Get an API key

Create a free account at [billing.whoisfreaks.com/signup](https://billing.whoisfreaks.com/signup). New accounts get 500 free credits with no credit card, usable across the live WHOIS, WHOIS history and reverse WHOIS APIs.

Keep the key out of source control. The examples read it from an environment variable:

```sh
export WHOISFREAKS_API_KEY="your_api_key"
```

Every example below assumes this setup:

```python
import os
import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]
```

## WHOIS lookup

Each request queries WHOIS servers and RDAP live, so you get the current record rather than a cached copy. One lookup costs 1 credit.

```python
with whoisfreaks.ApiClient(config) as client:
    record = whoisfreaks.WHOISApi(client).whois_live("whoisfreaks.com")

    print(record.create_date, record.expiry_date)  # 2019-03-19 2027-03-19
    print(record.domain_registrar.registrar_name)  # NAMECHEAP INC
    print(record.name_servers)
```

## Normalized registrar, address and date fields

Registries and registrars write the same facts in different formats. The API returns normalized fields so records from different TLDs line up without your own parsing code.

| What you get | Field | Example |
|---|---|---|
| One registrar name, however the registry spells it | `domain_registrar.normalized_name` | `namecheap, inc.` for both "NAMECHEAP INC" and "NameCheap, Inc" |
| A parsed and geocoded contact address | `registrant_contact.street`, `city`, `state`, `zip_code`, `country_name`, `country_code` | `Lewes`, `Delaware`, `19958`, `United States`, `US` |
| One date format | `create_date`, `update_date`, `expiry_date` | `2019-03-19` |

```python
registrant = record.registrant_contact

print(record.domain_registrar.normalized_name)  # namecheap, inc.
print(registrant.city, registrant.state)        # Lewes Delaware
print(registrant.country_code)                  # US
```

Use these fields to group a domain portfolio by registrar, filter registrants by country code or sort domains by expiry date across every TLD.

## Bulk WHOIS lookup

Look up to 100 domains in one call.

```python
with whoisfreaks.ApiClient(config) as client:
    request = whoisfreaks.BulkWhoisRequest(domain_names=["example.com", "whoisfreaks.com", "github.com"])
    result = whoisfreaks.WHOISApi(client).bulk_whois(request)
```

For larger jobs, the [Bulk WHOIS API](https://whoisfreaks.com/products/bulk-whois-api) accepts file uploads of up to 3M domains.

## WHOIS history

Get every recorded ownership change for a domain in one request. A new record is stored only when the WHOIS data changed, and history goes back to 1986.

```python
with whoisfreaks.ApiClient(config) as client:
    history = whoisfreaks.WHOISApi(client).whois_history("whoisfreaks.com")
```

## Reverse WHOIS

Find every domain registered with a keyword, such as a company name or registrant email, across 4.5B+ WHOIS records.

```python
with whoisfreaks.ApiClient(config) as client:
    matches = whoisfreaks.WHOISApi(client).whois_reverse("whoisfreaks", page=1)
```

## DNS lookup

Pull live DNS records for a domain. Pass `all` or a comma-separated list of record types: `A`, `AAAA`, `MX`, `NS`, `TXT`, `SOA`, `SPF`, `CNAME`.

```python
with whoisfreaks.ApiClient(config) as client:
    records = whoisfreaks.DNSApi(client).dns_live("A,MX,TXT", domain_name="whoisfreaks.com")
```

The same class also covers bulk DNS, historical DNS and reverse DNS lookups.

## Domain availability check

Check whether a domain is registered and, with suggestions turned on, get up to 100 available alternatives on other TLDs.

```python
with whoisfreaks.ApiClient(config) as client:
    result = whoisfreaks.DomainAvailabilityApi(client).domain_availability_v2(
        "whoisfreaks.io", sug=True, count=5
    )
```

## Typosquatting detection

Find registered domains that look like typo variants of a brand name. Search by a brand `keyword`, or by a wildcard `pattern` such as `whois*` (up to 3 asterisks). Results come 100 domains per page with registration date, expiry date and drop status, across 1,529+ TLDs.

```python
with whoisfreaks.ApiClient(config) as client:
    typos = whoisfreaks.TyposquattingApi(client).typosquatting(keyword="whoisfreaks")
```

To get the next page, pass the `nextPageToken` value from the response as `page_token`, along with the same keyword or pattern.

## Error handling

Failed requests raise `ApiException` with the HTTP status code and response body.

```python
from whoisfreaks.rest import ApiException

with whoisfreaks.ApiClient(config) as client:
    try:
        record = whoisfreaks.WHOISApi(client).whois_live("whoisfreaks.com")
    except ApiException as e:
        print(e.status, e.body)
```

Live API uptime and incident history are on the [status page](https://status.whois.whoisfreaks.com/).

## All endpoints

All URIs are relative to `https://api.whoisfreaks.com`. Each method links to its parameters and response model.

### WHOIS

| Class | Method | HTTP request | Description |
|---|---|---|---|
| WHOISApi | [bulk_whois](docs/WHOISApi.md#bulk_whois) | POST /v2.0/bulkwhois/live | Bulk WHOIS Lookup |
| WHOISApi | [whois_history](docs/WHOISApi.md#whois_history) | GET /v2.0/whois/history | Historical WHOIS records for a domain |
| WHOISApi | [whois_live](docs/WHOISApi.md#whois_live) | GET /v2.0/whois/live | Live WHOIS Lookup |
| WHOISApi | [whois_reverse](docs/WHOISApi.md#whois_reverse) | GET /v2.0/whois/reverse | Reverse WHOIS lookup by keyword |
| ASNWHOISApi | [asn_whois](docs/ASNWHOISApi.md#asn_whois) | GET /v2.0/asn-whois | ASN WHOIS Lookup |
| IPWHOISApi | [ip_whois](docs/IPWHOISApi.md#ip_whois) | GET /v1.0/ip-whois | IP WHOIS Lookup |

### DNS, SSL and subdomains

| Class | Method | HTTP request | Description |
|---|---|---|---|
| DNSApi | [dns_bulk](docs/DNSApi.md#dns_bulk) | POST /v2.0/dns/bulk/live | Bulk DNS Lookup |
| DNSApi | [dns_historical](docs/DNSApi.md#dns_historical) | GET /v2.0/dns/historical | Historical DNS Lookup |
| DNSApi | [dns_live](docs/DNSApi.md#dns_live) | GET /v2.0/dns/live | Live DNS Lookup |
| DNSApi | [dns_reverse](docs/DNSApi.md#dns_reverse) | GET /v2.1/dns/reverse | Reverse DNS Lookup |
| SSLApi | [ssl_lookup](docs/SSLApi.md#ssl_lookup) | GET /v1.0/ssl/live | SSL Certificate Lookup |
| SubdomainsApi | [subdomains](docs/SubdomainsApi.md#subdomains) | GET /v1.0/subdomains | Subdomains Lookup |

### Domain availability, typosquatting and reputation

| Class | Method | HTTP request | Description |
|---|---|---|---|
| DomainAvailabilityApi | [bulk_domain_availability_v2](docs/DomainAvailabilityApi.md#bulk_domain_availability_v2) | POST /v2.0/domain/availability | Bulk Domain Availability Check |
| DomainAvailabilityApi | [domain_availability_v2](docs/DomainAvailabilityApi.md#domain_availability_v2) | GET /v2.0/domain/availability | Domain Availability Check with Suggestions |
| TyposquattingApi | [typosquatting](docs/TyposquattingApi.md#typosquatting) | GET /v3.0/domain/typos | Typosquatting Lookup |
| DomainReputationApi | [domain_reputation](docs/DomainReputationApi.md#domain_reputation) | GET /v1/domain/security | Domain Reputation Lookup |

### IP geolocation and reputation

| Class | Method | HTTP request | Description |
|---|---|---|---|
| GeolocationApi | [bulk_geolocation](docs/GeolocationApi.md#bulk_geolocation) | POST /v1.0/geolocation | Bulk IP Geolocation |
| GeolocationApi | [geolocation](docs/GeolocationApi.md#geolocation) | GET /v1.0/geolocation | IP Geolocation Lookup |
| IPReputationApi | [bulk_ip_reputation](docs/IPReputationApi.md#bulk_ip_reputation) | POST /v1.0/security | Bulk IP Reputation |
| IPReputationApi | [ip_reputation](docs/IPReputationApi.md#ip_reputation) | GET /v1.0/security | IP Reputation Lookup |

### Account

| Class | Method | HTTP request | Description |
|---|---|---|---|
| AccountApi | [account_usage](docs/AccountApi.md#account_usage) | GET /v1.0/whoisapi/usage | Account Usage |
| AccountApi | [database_file_status](docs/AccountApi.md#database_file_status) | GET /v3.4/status | Database File Status (Public) |
| AccountApi | [rotate_api_key](docs/AccountApi.md#rotate_api_key) | GET /v1.0/api-key/rotate | Rotate API Key |

### Database downloads

WHOIS, DNS, subdomain, IP, newly registered, expiring and dropped domain databases, plus the phishing, malware and spam threat feeds, are available through the `Databases*` classes. See the [full method list](docs/) for every download and status endpoint.

## Requirements

Python 3.8 or later.

## Support

- WHOIS API documentation: [whoisfreaks.com/documentation/whois-api](https://whoisfreaks.com/documentation/whois-api)
- All API documentation: [whoisfreaks.com/documentation](https://whoisfreaks.com/documentation)
- Product page: [WhoisFreaks WHOIS API](https://whoisfreaks.com/products/whois-api)
- API status: [status.whois.whoisfreaks.com](https://status.whois.whoisfreaks.com/)
- Email: support@whoisfreaks.com
- Quick start: [WHOIS API examples](https://github.com/WhoisFreaks/whois-api)
- Other languages: [Python](https://github.com/WhoisFreaks/whoisfreaks-python), [JavaScript](https://github.com/WhoisFreaks/whoisfreaks-javascript), [TypeScript](https://github.com/WhoisFreaks/whoisfreaks-typescript), [Java](https://github.com/WhoisFreaks/whoisfreaks-java), [Go](https://github.com/WhoisFreaks/whoisfreaks-go), [C#](https://github.com/WhoisFreaks/whoisfreaks-csharp), [Ruby](https://github.com/WhoisFreaks/whoisfreaks-ruby), [PHP](https://github.com/WhoisFreaks/whoisfreaks-php), [Swift](https://github.com/WhoisFreaks/whoisfreaks-swift), [Kotlin](https://github.com/WhoisFreaks/whoisfreaks-kotlin)

## License

MIT. See [LICENSE](LICENSE).
