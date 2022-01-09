var socket_dr = new WebSocket('ws://18.221.158.203:8000/ws/datos_recibidos/');

socket_dr.addEventListener('message', function (event) {
    console.log('datos recibidos from server ', event.data);
    var djangoData=JSON.parse(event.data);
    var valor_separado = Object.values(djangoData);
    var valor_separado1 = valor_separado[0][0]
    var valor_separado2 = valor_separado[0][1]
    var valor_separado3 = valor_separado[0][2]
    var valor_separado4 = valor_separado[0][3]
    var valor_separado5 = valor_separado[0][4]

    var valor_entero_CM= parseInt(valor_separado1, 10);
    var valor_entero_CP= parseInt(valor_separado2, 10);


    var valores_pesos_clas = valor_separado3.split(','); 


    var valor_numero_cilindros= valor_entero_CM+valor_entero_CP

    var valor_peso_medido = valores_pesos_clas[0].slice(1);
    var valor_CAC_almacenados = valores_pesos_clas[1]
    var valor_CAL_almacenados = valores_pesos_clas[2].slice(0,-1);


    document.querySelector('#CM').innerText = valor_separado1;
    document.querySelector('#CP').innerText = valor_separado2;
    document.querySelector('#N').innerText = valor_separado4;
    document.querySelector('#MV').innerText = valor_separado5;

    document.querySelector('#NC').innerText = valor_numero_cilindros;

    document.querySelector('#PM').innerText = valor_peso_medido;
    document.querySelector('#CAL').innerText = valor_CAC_almacenados;
    document.querySelector('#CAC').innerText = valor_CAL_almacenados;

});

var socket_i_cel = new WebSocket('ws://18.221.158.203:8000/ws/iniciar_celda/');

function enviarNuevoMensaje_i_cel() {
             // Envia al WebSocket un nuevo mensaje
             socket_i_cel.send(JSON.stringify({
                 'text': 1
             }));
         }

const BOTON_ENVIAR_i_cel = document.querySelector('#start_celda');
BOTON_ENVIAR_i_cel.addEventListener('click', enviarNuevoMensaje_i_cel);


socket_i_cel.addEventListener('message', function (event) {
    console.log('Message5 from server fg ', event.data);
     var djangoData=JSON.parse(event.data);

});


var socket_d_cel = new WebSocket('ws://18.221.158.203:8000/ws/detener_celda/');

function enviarNuevoMensaje_d_cel() {
             // Envia al WebSocket un nuevo mensaje
             socket_d_cel.send(JSON.stringify({
                 'text': 0
             }));
         }

const BOTON_ENVIAR_d_cel = document.querySelector('#stop_celda');
BOTON_ENVIAR_d_cel.addEventListener('click', enviarNuevoMensaje_d_cel);


socket_d_cel.addEventListener('message', function (event) {
    console.log('Message5 from server fg ', event.data);
     var djangoData=JSON.parse(event.data);


});


var socket_a_col = new WebSocket('ws://18.221.158.203:8000/ws/activar_colocacion/');
function enviarNuevoMensaje_a_col() {
             // Envia al WebSocket un nuevo mensaje
             socket_a_col.send(JSON.stringify({
                 'text': 1
             }));
         }

const BOTON_ENVIAR_a_col = document.querySelector('#start_colocacion');
BOTON_ENVIAR_a_col.addEventListener('click', enviarNuevoMensaje_a_col);


socket_a_col.addEventListener('message', function (event) {
    console.log('Message5 from server fg ', event.data);
     var djangoData=JSON.parse(event.data);


});


var socket_d_col = new WebSocket('ws://18.221.158.203:8000/ws/detener_colocacion/');

function enviarNuevoMensaje_d_col() {
             // Envia al WebSocket un nuevo mensaje
             socket_d_col.send(JSON.stringify({
                 'text': 0
             }));
         }

const BOTON_ENVIAR_d_col = document.querySelector('#stop_colocacion');
BOTON_ENVIAR_d_col.addEventListener('click', enviarNuevoMensaje_d_col);


socket_d_col.addEventListener('message', function (event) {
    console.log('Message5 from server fg ', event.data);
     var djangoData=JSON.parse(event.data);


});

/*{% load static %}*/
    /*<script src="{% static 'main.js' %}"></script>*/


var socket_a_t = new WebSocket('ws://18.221.158.203:8000/ws/activar_taladrado/');

function enviarNuevoMensaje_a_t() {
             // Envia al WebSocket un nuevo mensaje
             socket_a_t.send(JSON.stringify({
                 'text': 1
             }));
         }

const BOTON_ENVIAR_a_t = document.querySelector('#activar_taladrado');
BOTON_ENVIAR_a_t.addEventListener('click', enviarNuevoMensaje_a_t);


socket_a_t.addEventListener('message', function (event) {
    console.log('Message5 from server fg ', event.data);
     var djangoData=JSON.parse(event.data);


});



var socket_d_t = new WebSocket('ws://18.221.158.203:8000/ws/desactivar_taladrado/');


function enviarNuevoMensaje_d_t() {
             // Envia al WebSocket un nuevo mensaje
             socket_d_t.send(JSON.stringify({
                 'text': 0
             }));
         }

const BOTON_ENVIAR_d_t = document.querySelector('#desactivar_taladrado');
BOTON_ENVIAR_d_t.addEventListener('click', enviarNuevoMensaje_d_t);


socket_d_t.addEventListener('message', function (event) {
    console.log('Message5 from server fg ', event.data);
     var djangoData=JSON.parse(event.data);


});


var socket_r_c = new WebSocket('ws://18.221.158.203:8000/ws/reiniciar_celda/');
function enviarNuevoMensaje_r_c() {
             // Envia al WebSocket un nuevo mensaje
             socket_r_c.send(JSON.stringify({
                 'text': 1
             }));
         }

const BOTON_ENVIAR_r_c = document.querySelector('#reiniciar_celda');
BOTON_ENVIAR_r_c.addEventListener('click', enviarNuevoMensaje_r_c);


socket_r_c.addEventListener('message', function (event) {
    console.log('Message5 from server fg ', event.data);
     var djangoData=JSON.parse(event.data);


});