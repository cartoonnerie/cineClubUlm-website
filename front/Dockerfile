FROM node:latest

WORKDIR /front

COPY package*.json ./

RUN ls

RUN npm install

EXPOSE 3000

CMD [ "npm", "run", "dev" ]
