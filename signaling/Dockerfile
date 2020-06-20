FROM node:latest

EXPOSE 9000
COPY . .
COPY app.js app.js
RUN npm install

CMD ['node','app.js']