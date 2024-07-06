
mkdir -p .postgresql

Invoke-WebRequest -Uri https://cockroachlabs.cloud/clusters/d08078a8-1e28-4cb6-886f-5ccd2a4b5616/cert -OutFile .postgresql/root.crt


gunicorn ashurawebblog.wsgi:application