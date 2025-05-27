import {UmaClasse} from "../../desestruturacao/umaclasse.mjs"

let umObjetoDeClasse = new UmaClasse("um valor")
let json = JSON.stringify(umObjetoDeClasse);
console.log(json);