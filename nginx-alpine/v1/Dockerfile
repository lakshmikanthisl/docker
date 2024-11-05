# Use the official Alpine image as the base
FROM alpine:latest

# Install Nginx
RUN apk update 

RUN apk add --no-cache nginx

# Copy a basic Nginx configuration (optional step if you have a custom config)
COPY nginx.conf /etc/nginx/nginx.conf

# Copy custom index.html file to /usr/share/nginx/html
COPY static /usr/share/nginx/html


# Expose port 80 to access Nginx
EXPOSE 80

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]

