
//$('#date').datepicker({dateFormat:'dd-mm-yy'});

// FE_INI
//$(document).ready(function() {
//	$("#datepicker").datepicker();
//	});

function llenacaja(){
	var fini = $('#datepicker').val();
	var fini = fini.slice(6,10)+"-"+fini.slice(0, 2)+"-"+fini.slice(3,5);
   	document.getElementById("datepicker").value=fini;
	}


// FE_NAC
//$(document).ready(function() {
//    $("#datepicker2").datepicker();
//    });

function llenacaja2(){
	var fenac = $('#datepicker2').val();
	var fenac = fenac.slice(6,10)+"-"+fenac.slice(0, 2)+"-"+fenac.slice(3, 5);
   	document.getElementById("datepicker2").value=fenac;
	}


jQuery(function($){
	$.datepicker.regional['es'] = {
		closeText: 'Cerrar',
		prevText: '&#x3c;Ant',
		nextText: 'Sig&#x3e;',
		currentText: 'Hoy',
		monthNames: ['Enero','Febrero','Marzo','Abril','Mayo','Junio',
		'Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'],
		monthNamesShort: ['Ene','Feb','Mar','Abr','May','Jun',
		'Jul','Ago','Sep','Oct','Nov','Dic'],
		dayNames: ['Domingo','Lunes','Martes','Mi&eacute;rcoles','Jueves','Viernes','S&aacute;bado'],
		dayNamesShort: ['Dom','Lun','Mar','Mi&eacute;','Juv','Vie','S&aacute;b'],
		dayNamesMin: ['Do','Lu','Ma','Mi','Ju','Vi','S&aacute;'],
		weekHeader: 'Sm',
		dateFormat: 'dd-mm-yy',
		firstDay: 1,
		isRTL: false,
		showMonthAfterYear: false,
		yearSuffix: ''};
	$.datepicker.setDefaults($.datepicker.regional['es']);
});    


function prueba() {
	var x = document.getElementById("rut").value
    alert("!! Entró al MYJS.JS ¡¡"+x);
    document.getElementById("rut").focus();
    document.getElementById("rut").style.border = '2px solid red';
}

function validaemail(email) {
	/*alert("email llegó con :"+email);*/
	if(email=="correo"){ 
    	var x = document.getElementById("correo").value
	} else {
    	var x = document.getElementById("correo_apod").value
	}

    if(x!='') {
        var expr = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        if ( !expr.test(x) ) {
            alert("Error: La dirección de correo " + x + " es incorrecta.");
            document.getElementById("correo").value = "";
        }
    }
}

function validarut() {
	var rut = document.getElementById("rut").value 
	document.getElementById("rut").value=rut.toUpperCase()
	if (rut!='') {
		var rexp = new RegExp(/^([0-9])+\-([kK0-9])+$/);
			if(rut.match(rexp)){
				var RUT = rut.split("-");
				//var elRut = RUT[0].toArray();
				var elRut = RUT[0].split('');
				var factor = 2;
				var suma = 0;
				var dv;
				for(i=(elRut.length-1); i>=0; i--){
					factor = factor > 7 ? 2 : factor;
					suma += parseInt(elRut[i])*parseInt(factor++);
				}
				dv = 11 -(suma % 11);
				if(dv == 11){
					dv = 0;
				}else if (dv == 10){
					dv = "K";
				}
	
				if(dv == RUT[1].toUpperCase()){
          			document.getElementById("rut").style.border = '';
            		document.getElementById("nombre").focus();
            		/* pruebita(); */
      				return true;
				}else{         
         			document.getElementById("rut").style.border = '2px solid red';
            		document.getElementById("rut").focus();		
            		document.getElementById("rut").value = '';			
					alert("El rut es incorrecto por Digito Verificador!!");
					pruebita();
					return false;
				}
			}else{  
			    document.getElementById("rut").style.border = '2px solid red';
            	document.getElementById("rut").focus();	  
            	document.getElementById("rut").value = ''; 
				alert("Formato de RUT incorrecto pot formato digitado!!");
				return false;
			}
		}	
}


funtion pruebita() {
	alert("Derivó a otra fucion desde validarut");
}


function validarut2() {
	var rut = document.getElementById("rut_apod").value 
	document.getElementById("rut_apod").value=rut.toUpperCase()
	if (rut!='') {
		var rexp = new RegExp(/^([0-9])+\-([kK0-9])+$/);
			if(rut.match(rexp)){
				var RUT = rut.split("-");
				//var elRut = RUT[0].toArray();
				var elRut = RUT[0].split('');
				var factor = 2;
				var suma = 0;
				var dv;
				for(i=(elRut.length-1); i>=0; i--){
					factor = factor > 7 ? 2 : factor;
					suma += parseInt(elRut[i])*parseInt(factor++);
				}
				dv = 11 -(suma % 11);
				if(dv == 11){
					dv = 0;
				}else if (dv == 10){
					dv = "K";
				}
	
				if(dv == RUT[1].toUpperCase()){
          			document.getElementById("rut_apod").style.border = '';
            		document.getElementById("nombre").focus();
					return true;
				}else{         
         			document.getElementById("rut_apod").style.border = '2px solid red';
            		document.getElementById("rut_apod").focus();		
            		document.getElementById("rut_apod").value = '';			
					alert("El rut es incorrecto por Digito Verificador!!");
					return false;
				}
			}else{  
			    document.getElementById("rut_apod").style.border = '2px solid red';
            	document.getElementById("rut_apod").focus();	  
            	document.getElementById("rut_apod").value = ''; 
				alert("Formato de RUT incorrecto por formato digitado!!");
				return false;
			}
		}	
}



function habilitadeshabilita(campo) {
	var estadoActual = document.getElementById(campo);
	if(estadoActual.disabled)   {
		estadoActual.disabled= false;
	} else {
		estadoActual.disabled= true;
    }
}


// obtiene el focus
function txt_onfocus(txt) {
    txt.style.backgroundColor = " ";
}

// pierde el focus
function txt_onchange(txt)
{
    txt.style.backgroundColor = " ";   
}


function upperCase() {
	var x=document.getElementById("rut").value
	document.getElementById("rut").value=x.toUpperCase()
}

function valida_fono() {
	var fon = document.getElementById("fono_cuid").value;
    if(fon!='') {
		if( (!/^([0-9])*$/.test(fon)) ) {
			alert("El formato del numero telefonico introducido es incorrecto.");
			document.getElementById("fono_cuid").style.border = '2px solid red';
			document.getElementById("fono_cuid").focus();
		}else{
			document.getElementById("fono_cuid").style.border = '';	
		}
	}
}

/*
<!-- Modal Structure -->
<div id="modal1" class="modal">
    <div class="modal-content">
        <h3>estas apunto de eliminar {{identificador.clave}}</h3> 
    </div>
    <div class="modal-footer">
        <a href="#!" class=" modal-action modal-close waves-effect waves-green btn-flat">Cancelar</a>
        <button onclick="eliminarIdentificador('{{ identificador.id }}')" class="modal-action modal-close waves-effect waves-green btn-flat">Eliminar</a>
    </div>
</div>
*/


/*
function confirmar_borrado(nombre,id) {
   if(confirm('¿Estas seguro de borrar a :'+nombre+' ?')) {
 
    	var request = $.ajax({
    	    type: "POST",
    	    url: "{% url 'eliminar_identificador' id %}",
    	    data: {
    	        "csrfmiddlewaretoken": "{{ csrf_token }}",
    	        "id": id                    
    	    },
    		});
   			request.done(function(response) {
   		});

 	}
}

*/

function mayuscula(e) {
	e.value = e.value.toUpperCase();
}


function limpia() {
	document.getElementById("busca").value = " ";
}


function Ocultar() {
	if(document.getElementById('div1_id').style.display == 'none') {
 		 document.getElementById('div0_id').style.display = 'block'; 
 		 document.getElementById('div1_id').style.display = 'block'; 
 		 document.getElementById('div2_id').style.display = 'block';
 		 document.getElementById('div3_id').style.display = 'block'; 
		document.getElementById('div7_id').style.display = 'block'; 
		document.getElementById('div8_id').style.display = 'block'; 
		document.getElementById('div9_id').style.display = 'block'; 
		document.getElementById('div10_id').style.display = 'block'; 
		document.getElementById('div11_id').style.display = 'block'; 
		document.getElementById('div12_id').style.display = 'block'; 

 	} else {
 		document.getElementById('div0_id').style.display = 'none';
 		document.getElementById('div1_id').style.display = 'none';
 		document.getElementById('div2_id').style.display = 'none';
 		document.getElementById('div3_id').style.display = 'none';
 		document.getElementById('div7_id').style.display = 'none';
 		document.getElementById('div8_id').style.display = 'none';
 		document.getElementById('div9_id').style.display = 'none';
 		document.getElementById('div10_id').style.display = 'none';
 		document.getElementById('div11_id').style.display = 'none';
 		document.getElementById('div12_id').style.display = 'none'; 		
 	}
}


$('#displayNone').click(function(e) {
   if( $('#hide-me').is(":visible") ) {
    $('#hide-me').css('display', 'none'); 
  } else {
    $('#hide-me').css('display', 'block');
  }
});

