FROM node:lts-alpine

RUN npm install -g http-server

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

#RUN npm install -g @vue/cli

RUN npm run build

EXPOSE 8080 8000

CMD [ "http-server", "dist"]
