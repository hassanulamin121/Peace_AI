# Ek bohot chota aur fast Nginx web server
FROM nginx:alpine

# Nginx ke default public folder mein apna sara frontend code (index.html, bg.png) copy kar do
COPY . /usr/share/nginx/html

# Port 80 open kar rahe hain taake browser se access ho sake
EXPOSE 80

# Nginx ko background mein run karne ki command
CMD ["nginx", "-g", "daemon off;"]