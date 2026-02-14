import json
import hmac
import hashlib
import requests
from datetime import datetime, timezone

payload = {
  "action_run_link": "https://github.com/hemanth110702/b12-application/actions/runs/22021144971",
  "email": "mamidihemanthkumar2002@gmail.com",
  "name": "Mamidi Hemanth Kumar",
  "repository_link": "https://github.com/hemanth110702",
  "resume_link": "https://drive.google.com/file/d/1Tsqlmvfz7yoMrCoEG7BisPzvJjTLYEtq/view?usp=sharing",
  "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00","Z"),
}

body = json.dumps(payload, separators=(",", ":"), sort_keys=True)

secret = b"hello-there-from-b12"
signature = hmac.new(secret, body.encode("utf-8"), hashlib.sha256).hexdigest()
header_signature = f"sha256={signature}"

response = requests.post(
  "https://b12.io/apply/submission",
  data=body,
  headers={
    "Content-Type": "application/json",
    "X-Signature-256": header_signature
  }
)

print(response.text)