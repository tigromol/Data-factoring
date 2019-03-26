FROM node:9.10

RUN npm install react-scripts@2.1.5 -g --silent

RUN npx create-react-app app
COPY package.json /app/package.json
RUN npm install --silent --save-dev

WORKDIR /app

EXPOSE 3000
EXPOSE 35729

VOLUME [ "/app/src" ]

CMD ["npm", "start"]