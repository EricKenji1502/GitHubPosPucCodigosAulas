const { MongoClient, ServerApiVersion } = require('mongodb');

const url = "mongodb+srv://ericktdias:yogoma9zoz@cluster0.pdhggsa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";

// Crie um MongoClient com um objeto MongoClientOptions para definir a versão da Stable API
const client = new MongoClient(url, {
    serverApi: {
        version: ServerApiVersion.v1,
        strict: true,
        deprecationErrors: true,
    }
});

async function run() {
    try {
        await client.connect();

        await client.db("admin").command({ ping: 1 });
        console.log("Pingou sua implantação. Você se conectou com sucesso ao MongoDB!");

        // A partir daqui, você pode adicionar suas operações de banco de dados

        // Acessa o banco de dados e a coleção
        const database = client.db("meuBancoDeDados");
        const colecao = database.collection("minhaColecao");

        // Encontra um documento específico
        const documentoEncontrado = await colecao.findOne({ nome: "Produto A" });
        console.log("Documento encontrado:", documentoEncontrado);

        // Encontra todos os documentos
        const todosDocumentos = await colecao.find({}).toArray();
        console.log("Todos os documentos:", todosDocumentos);

        // Atualiza um documento
        const filtro = { nome: "Produto A" };
        const atualizacao = { $set: { preco: 24.99 } };
        const resultadoUpdate = await colecao.updateOne(filtro, atualizacao);
        console.log(`${resultadoUpdate.modifiedCount} documento(s) foi/foram atualizado(s)`);

        // Deleta um documento
        const filtroDelete = { nome: "Produto A" };
        const resultadoDelete = await colecao.deleteOne(filtroDelete);
        console.log(`${resultadoDelete.deletedCount} documento(s) foi/foram deletado(s)`);

        // Cria um novo documento
        const novoDocumento = { nome: "Produto A", preco: 19.99, quantidade: 100 };
        const resultado = await colecao.insertOne(novoDocumento);
        console.log(`Um documento foi inserido com o _id: ${resultado.insertedId}`);

    } finally {
        // Garante que o cliente fechará quando você terminar/errar
        await client.close();
    }
}
run().catch(console.dir);