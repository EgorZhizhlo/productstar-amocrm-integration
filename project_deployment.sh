echo "Создание сети nginx"
docker network create nginx_network

echo "Развертка проекта..."
docker compose up --build -d

echo "Сервис запущен!"

# chmod +x project_deployment.sh && ./project_deployment.sh