from flask import Flask, request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='web_app_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(ip_address)s - %(message)s')

@app.route('/')
def index():
    # Log incoming request details
    log_request(request)
    return 'Hello, World!'

def log_request(req):
    # Log request details with separate lines, timestamps, and from IP address
    log_info = f"{get_request_info(req)}\n"
    log_info += f"{get_user_info(req)}\n"
    log_info += f"{get_security_info(req)}\n"
    logging.info(log_info, extra={'ip_address': req.remote_addr})

def get_request_info(req):
    # Log request details
    return f"Request: {req.method} {req.url}\nHeaders: {req.headers}\nParameters: {req.args}\nData: {req.data}"

def get_user_info(req):
    # Log user-related information
    return f"User-Agent: {req.headers.get('User-Agent')}\nReferrer: {req.headers.get('Referer')}\nCookies: {req.cookies}"

def get_security_info(req):
    # Log security-related information
    return f"Response Status Code: {req.status_code}\nRequest Duration: {req.elapsed.total_seconds():.3f}s\nClient IP Geolocation: {get_geolocation(req.remote_addr)}"

def get_geolocation(ip_address):
    # Use a geolocation service to determine the approximate location of the IP address
    # Replace this with a proper geolocation implementation
    return "Geolocation information"

if __name__ == '__main__':
    app.run(debug=True)
