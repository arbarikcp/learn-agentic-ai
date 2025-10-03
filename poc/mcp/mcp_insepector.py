import requests, sseclient, json

SSE_URL = "http://localhost:8000/sse"

# 1️⃣  open the SSE stream
resp    = requests.get(SSE_URL, stream=True, headers={"Accept": "text/event-stream"})
client  = sseclient.SSEClient(resp)

# 2️⃣  first event = endpoint to POST to
endpoint_evt = next(client.events())          # blocks until the server sends the line
post_url     = f"http://localhost:8000{endpoint_evt.data}"
print("POST to:", post_url)

# 3️⃣  handshake then list tools
init_msg = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {"client": {"name": "demo", "version": "0.1"}}
}
requests.post(post_url, json=init_msg)

list_msg = {"jsonrpc": "2.0", "id": 2, "method": "tools/list"}
requests.post(post_url, json=list_msg)

# 4️⃣  read responses (they arrive on the SSE stream)
for evt in client.events():
    print("🔻", evt.data)
