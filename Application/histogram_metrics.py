import http.server
import time
from prometheus_client import start_http_server, Histogram #usualy used when want to calculate latency time of your request
from prometheus_client import Gauge

REQUEST_LATENCY_TIME = Histogram('latency_request_time', 'Response latency in seconds')
REQUEST_IN_PROGRESS = Gauge('reuests_inprogress', "Number of Live Request on Application")


class HandleRequests(http.server.BaseHTTPRequestHandler):
    @REQUEST_LATENCY_TIME.time()
    @REQUEST_IN_PROGRESS.track_inprogress()
    def do_GET(self):
        # startTime = time.time()
        self.send_response(200)

        time.sleep(3)

        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First python Application</title></head><body style='color: #333; margin-top: 30px;'><center><h2>Welcome to our first Python application.</center></h2></body></html>", "utf-8"))
        self.wfile.close
        # endTime = time.time() - startTime
        # REQUEST_LATENCY_TIME.observe(endTime)

if __name__ == "__main__":
    start_http_server(5001)
    server = http.server.HTTPServer(('209.38.226.129', 5000), HandleRequests)
    server.serve_forever()