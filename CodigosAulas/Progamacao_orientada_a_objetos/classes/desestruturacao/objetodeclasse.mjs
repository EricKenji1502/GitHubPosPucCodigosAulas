import {UmaClasse} from "./umaclasse.mjs"

let umaClasse = new UmaClasse("Primeiro atributo")

let {capturaPrimeiroAtributo: umAtributo, outroAtributo} = umaClasse;

console.log("um Atributo: " + umAtributo)
console.log("Outro Atributo: " + outroAtributo)