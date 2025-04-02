# Documentation

## Endpoints:  
  METHOD: **POST**  
  URL: **https://egorzhizhlo.ru/ris-integration/create-deal/product/get-order**  
    REQUEST BODY:    
    ```json   
    {  
      "name": string,  
      "phone": string,  
      "email": string,  
      "campaign_id": string,  
      "url": string  
    }  
    ```   
    RESPONSE BODY:   
    ```json   
    {  
      "success": true,  
      "data": {  
        "name": string,  
        "phone": string,  
        "email": string",  
        "campaign_id": string,  
        "url": string  
      }  
    }
    ```  

## Deployment(Необходим Docker и Docker Compouse)
  1. **Клонируем репозиторий к себе на сервер:**
     - git clone https://github.com/EgorZhizhlo/productstar-amocrm-integration.git
  2. **Переходим в директорию проекта:**
     - cd productstar-amocrm-integration
  3. **Корректируем .env файл согласно вашей интеграции в amocrm:**
     - nano .env
    ```
      client_id="ID интеграции"
      client_secret="Секретный ключ"
      subdomain="Ваш логин в amocrm(в url выглядит как https://ваш-логин.amocrm.ru)"
      redirect_url="Ссылка на перенаправление(идентично как в amocrm)"
      twety_min_code="Код авторизации(действителен 20 минут)"
      ris_product_pipeline_id="ID Воронки в которую должны падать заявки"
    ```
  4. **Разворачиваем проект:**
     - chmod +x project_deployment.sh && ./project_deployment.sh
  5. **Смотрим как развернулись сервисы через команду:**
     - docker ps(В списке должны быть 2 сервиса: **nginx** и **amocrm_integrations**

     
