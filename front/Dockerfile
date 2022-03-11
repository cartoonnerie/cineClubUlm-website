FROM node:latest

WORKDIR /front

COPY package*.json ./

RUN yarn install

EXPOSE 3000

CMD [ "yarn", "dev" ]
