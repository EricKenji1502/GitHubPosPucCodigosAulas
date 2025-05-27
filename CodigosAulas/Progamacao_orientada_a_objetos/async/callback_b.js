const fs = require('fs')

fs.readFile(
    'texto.txt', 
    (err, buf) => {
        if(err)
            console.log("houve um erro")
        else
            console.log(buf.toString())
    })