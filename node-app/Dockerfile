# Use a base image Node.js
FROM node:14-alpine

# Defina um diretório de trabalho para a aplicação
WORKDIR /app

# Copie o package.json e o package-lock.json para o diretório de trabalho
COPY package*.json ./

# Instale as dependências do projeto
RUN npm install

# Copie os arquivos do aplicativo para o diretório de trabalho
COPY . .

# Defina um usuário não-root para executar o aplicativo
RUN addgroup -g 1001 appuser && \
    adduser -D -u 1001 -G appuser appuser
USER appuser

# Exponha a porta em que o aplicativo está ouvindo
EXPOSE 3000

# Inicie o aplicativo Node.js
CMD [ "node", "app.js" ]