// servico-produtos/server.js
const express = require('express');
const Consul = require('consul');

const app = express();
const PORT = 3001; // Porta única para este serviço

// Conecta ao agente Consul local (que está rodando em localhost:8500)
const consul = new Consul();

const serviceName = 'servico-produtos';
const serviceId = `produtos-${PORT}`;

// 1. Definição do serviço para registro no Consul
const serviceDefinition = {
    name: serviceName,
    id: serviceId,
    address: 'localhost',
    port: PORT,
    check: {
        http: `http://localhost:${PORT}/health`,
        interval: '10s',
        timeout: '5s'
    }
};

// 2. Rota de health check
app.get('/health', (req, res) => {
    res.status(200).send('OK');
});

// 3. Rota principal que retorna os produtos
app.get('/produtos', (req, res) => {
    const produtos = [
        { id: 1, nome: 'Notebook Gamer', preco: 7500.00 },
        { id: 2, nome: 'Mouse sem fio', preco: 150.00 },
        { id: 3, nome: 'Teclado Mecânico', preco: 450.00 }
    ];
    console.log('Requisição recebida em servico-produtos. Enviando lista...');
    res.json(produtos);
});

// 4. Inicia o servidor e registra no Consul
app.listen(PORT, () => {
    console.log(`Serviço de produtos rodando na porta ${PORT}`);

    consul.agent.service.register(serviceDefinition, (err) => {
        if (err) {
            console.error('Falha ao registrar serviço no Consul', err);
            throw err;
        }
        console.log(`Serviço '${serviceName}' registrado no Consul com sucesso.`);
    });
});

// 5. Desregistra o serviço ao encerrar (Ctrl+C)
process.on('SIGINT', () => {
    console.log(`Desregistrando o serviço '${serviceName}'...`);
    consul.agent.service.deregister(serviceId, (err) => {
        if (err) console.error('Falha ao desregistrar serviço.', err);
        else console.log('Serviço desregistrado com sucesso.');
        process.exit();
    });
});