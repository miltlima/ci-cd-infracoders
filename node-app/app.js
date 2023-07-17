const express = require('express');
const app = express();
const port = 3001;


const prom = require('prom-client');
const register = prom.register;
const counter = new prom.Counter({
  name: 'color_change_counter_total',
  help: 'Count the color change',
  labelNames: ['statusCode']
}) 

const colors = ['red', 'green', 'blue', 'yellow', 'orange']
app.get('/changeColor', (req, res) => {
    const randomIndex = Math.floor(Math.random() * colors.length);
    const color = colors[randomIndex];
    counter.labels('200').inc();

    res.send(`
    <html>
        <head>
            <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
            <style>
                body {
                    background-color: ${color};
                    font-family: 'Font Name', sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                h1 {
                    font-size: 48px;
                    text-align: center;
                    color: white;
                }
            </style>
        </head>
        <body>
            <h1>Mudar é preciso com Node.js e express</h1>
            
        </body>
    </html>
`);
});

app.get('/metrics', async (req, res) => {
  res.set('Content-Type', register.contentType);
  res.end(await register.metrics());
});

app.listen(port, () => {
    console.log(`Servidor em execução em http://localhost:${port}`);
});