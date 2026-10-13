
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, quote
import html

PAGE = """<!doctype html>
<html lang="uz">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta charset="utf-8">
<title>DaromadAI</title>
<style>
body{font-family:Arial;background:#101827;color:white;
max-width:650px;margin:35px auto;padding:18px}
main{background:#1e293b;padding:22px;border-radius:18px}
h1{color:#67e8f9}
input,textarea,button{box-sizing:border-box;width:100%;
padding:13px;margin:8px 0;border-radius:9px;font-size:16px}
textarea,input{background:#0f172a;color:white;border:1px solid #475569}
button{background:#06b6d4;color:#001018;border:0;font-weight:bold}
small{color:#cbd5e1}
</style></head>
<body><main>
<h1>🤖 DaromadAI</h1>
<p>Shaxsiy daromad loyihalari yordamchisi</p>
<form method="get">
<label>Qiziqishingiz yoki g‘oyangiz:</label>
<textarea name="idea" rows="4" placeholder="Masalan: qishloqda 500 ming so‘m bilan biznes boshlash"></textarea>
<label>Mavjud budjet (so‘m):</label>
<input name="budget" type="number" min="0" placeholder="500000">
<button type="submit">Reja tuzish</button>
</form>
<p><small>Bu boshlang‘ich namuna. Hozircha haqiqiy AI ulanmagan.</small></p>
</main></body></html>"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(PAGE.encode("utf-8"))

HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
