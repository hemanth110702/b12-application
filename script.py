import json
import hmac
import hashlib
import requests
from datetime import datetime, timezone

timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

print("Checkpoint-1")

payload = {
  "action_run_link": "https://github.com/hemanth110702/b12-application/actions/runs/22021144971",
  "email": "mamidihemanthkumar2002@gmail.com",
  "name": "Mamidi Hemanth Kumar",
  "repository_link": "https://github.com/hemanth110702",
  "resume_link": "https://drive.google.com/file/d/1Tsqlmvfz7yoMrCoEG7BisPzvJjTLYEtq/view?usp=sharing",
  "timestamp": timestamp,
}

print("Checkpoint-2")

body = json.dumps(payload, separators=(",", ":"), sort_keys=True)

print("Checkpoint-3")

secret = b"hello-there-from-b12"
signature = hmac.new(secret, body.encode("utf-8"), hashlib.sha256).hexdigest()
header_signature = f"sha256={signature}"

print("Checkpoint-4")

response = requests.post(
  "https://b12.io/apply/submission",
  data=body,
  headers={
    "Content-Type": "application/json",
    "X-Signature-256": header_signature
  }
)

print("Checkpoint-5")

print("STATUS:", response.status_code)
print("RESPONSE:", response.text)