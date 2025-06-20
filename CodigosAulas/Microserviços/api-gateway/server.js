// api-gateway/server.js
const express = require('express');
const Consul = require('consul');
const axios = require('axios');

const app = express();
const PORT = 3000; // Porta principal da nossa aplicação

const consul = new Consul();

app.get('/produtos', async (req, res) => {
    console.log('Requisição recebida no API Gateway para /produtos...');
    const serviceName = 'servico-produtos';

    try {
        // 1. Pergunta ao Consul por instâncias saudáveis do serviço de produtos
        const services = await consul.health.service({
            service: serviceName,
            passing: true // Apenas serviços que estão passando no health check
        });

        if (services.length === 0) {
            console.error(`Nenhuma instância saudável de '${serviceName}' encontrada.`);
            return res.status(503).send('Serviço indisponível no momento.');
        }

        // 2. Pega a primeira instância saudável encontrada
        const serviceInstance = services[0].Service;
        const serviceUrl = `http://${serviceInstance.Address}:${serviceInstance.Port}/produtos`;

        console.log(`Redirecionando requisição para: ${serviceUrl}`);

        // 3. Faz a requisição para o serviço de produtos
        const response = await axios.get(serviceUrl);

        // 4. Retorna a resposta do serviço de produtos para o cliente final
        res.json(response.data);

    } catch (error) {
        console.error('Erro ao buscar serviço no Consul ou ao fazer a requisição:', error.message);
        res.status(500).send('Erro interno no servidor.');
    }
});

app.listen(PORT, () => {
    console.log(`API Gateway rodando na porta ${PORT}`);
});