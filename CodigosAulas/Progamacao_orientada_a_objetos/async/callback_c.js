const fs = require('fs')

fs.readFile(
    'texto.txt', 
    (err, buf) => {
        if(err)
            throw err
        else
            console.log(buf.toString())
    })