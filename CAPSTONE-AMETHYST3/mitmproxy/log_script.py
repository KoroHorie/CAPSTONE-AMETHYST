import os

log_name = os.getenv("LOG_NAME", "requests") + "-requests.log"
log_path = f"/logs/{log_name}"

def request(flow):
    req = flow.request
    body = req.get_text().replace('\n', '\\n') if req.method in ["POST", "PUT", "PATCH"] else ""
    log_entry = f"{req.method} {req.pretty_url} Headers: {dict(req.headers)} Body: {body}"
    with open(log_path, "a") as log:
        log.write(log_entry + "\n")
