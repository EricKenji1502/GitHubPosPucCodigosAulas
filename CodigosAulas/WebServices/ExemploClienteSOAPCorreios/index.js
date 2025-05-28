var soap = require('soap')
var url = 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl'

soap.createClient(url, function (err, client){
       if(err) {
              return console.log(err);
       }
        client.consultaCEP({
           cep: '91520260'
       }, function (err, res) {
        if(err) {
            return console.log(err);
        } else {
            console.log(res)
        }
       })
    }
);