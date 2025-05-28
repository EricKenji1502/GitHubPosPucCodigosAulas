var soap = require('soap');
var url = 'http://www.dneonline.com/calculator.asmx?wsdl';

soap.createClient(url, function (err, client) {
  console.log('Descreve -> ', client.describe().Calculator.CalculatorSoap) 
  client.Subtract({ intA: 2, intB:3}, function(err, result) {
      if(err) return console.log(err);
      console.log("SUBTRAÇÃO: ", result.SubtractResult);
  });
   client.Multiply({ intA: 2, intB:3}, function(err, result) {
      if(err) return console.log(err);
      console.log("MULTIPLICAÇÃO: ", result.MultiplyResult);
  });
  client.Subtract({ intA: 2, intB:3}, function(err, result) {
      if(err) return console.log(err);
      console.log("SUBTRAÇÃO: ", result.SubtractResult);
  });
})