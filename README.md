# devops-etna
## Lancement de l'api et des micro services
- Prérequis
  - docker installé ainsi que docker-compose

- Lancement des dockers
  - cd docker
  - chmod +x scripts/run_service.sh
  - docker-compose up -d

- Doc api accessible sur localhost:5000/apidocs
- RabbitMQ sur localhost:15672

- Arret
  - cd docker
  - docker-compose down
