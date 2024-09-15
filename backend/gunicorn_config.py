import multiprocessing

# Bind to address and port
bind = "0.0.0.0:8000"

# Number of worker processes
workers = multiprocessing.cpu_count() * 2 + 1

# Worker class (sync, eventlet, gevent, etc.)
worker_class = "gunicorn.workers.ggevent.GeventWorker"

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Timeout (in seconds)
timeout = 30

# Max request size (in bytes)
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

# Daemonize (run in the background)
daemon = False

# Reload on code changes
reload = True

# Application to be served
# Note: If you want to specify the app module here, use the form "myapp:app"
# app = "myapp:app"
