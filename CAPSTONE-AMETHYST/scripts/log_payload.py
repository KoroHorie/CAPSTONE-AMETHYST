from mitmproxy import http

LOG_FILE = "/home/mitmproxy/.mitmproxy/requests.log"

def request(flow: http.HTTPFlow) -> None:
    method = flow.request.method
    url = flow.request.pretty_url
    body = flow.request.get_text()
    with open(LOG_FILE, "a") as f:
        f.write(f"{method} {url} | BODY: {body.strip()}\n")
