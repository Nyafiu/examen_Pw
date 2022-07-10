function validar()
{
   var nombre_aux = document.formulario.txt_nombre.value;
   var paterno_aux = document.formulario.txt_appaterno,value;
   var materno_aux = document.formulario.txt_apmaterno.value;
   var rut_aux = document.formulario.txt_rut.value;
   var edad_aux = document.formulario.txt_edad.value;
   var nombre_vacuna_aux = document.formulario.txt_vacuna_nombre.value;

    if(nombre_aux.length<=2){
        alert("el nombre debe tener mas de 2 caracteres...");
        document.formulario.txt_nombre.focus();
        return false;
    }

    if(paterno_aux.length<=2){
        alert("el apellido debe tener mas de 2 caracteres...");
        document.formulario.txt_appaterno.focus();
        return false;
    }

    if(materno_aux.length<=2){
        alert("el apellido debe tener mas de 2 caracteres...");
        document.formulario.txt_apmaterno.focus();
        return false;
    }

    if (rut_aux.charAt(8) != "-"){
        alert("Debe ingresar el rut con guión");
        document.formulario.txt_rut.focus();
        return false;
    }

    if(edad_aux<18){
        alert("Debe ser mayor de edad para continuar");
        document.formulario.txt_edad.focus();
        return false;
    }

    if(nombre_vacuna_aux.length<=2){
        alert("el nombre de la vacuna debe tener mas de 2 caracteres...");
        document.formulario.txt_vacuna_nombre.focus();
        return false;
    }

    document.formulario.action = "/ingresar_informacion/"
    document.formulario.submit() = true
    alert("Ingreso correcto");
}

function validar_vacuna(){

    var vacuna_nombre = document.formu.txt_nombre_vacuna.value;
    var fabricacion = document.formu.txt_fabricacion.value;
    var tipo_vacuna = document.formu.txt_tipo_vacuna.value;
    var lote = document.formu.txt_lote.value;
    var administracion = document.formu.txt_administracion.value;

    if(vacuna_nombre.length<=2){
        alert("el nombre de la vacuna debe tener mas de 2 caracteres...");
        document.formu.txt_nombre_vacuna.focus();
        return false;
    }
    if(fabricacion.length<=2){
        alert("la fabricacion debe tener mas de 2 caracteres...");
        document.formu.txt_fabricacion.focus();
        return false;
    }
    if(tipo_vacuna.length<=2){
        alert("el tipo de vacuna debe tener mas de 2 caracteres...");
        document.formu.txt_tipo_vacuna.focus();
        return false;
    }
    if(lote.length<=2){
        alert("el lote debe tener mas de 2 caracteres...");
        document.formu.txt_lote.focus();
        return false;
    }
    if(administracion.length<=2){
        alert("La administracion debe tener mas de 2 caracteres...");
        document.formu.txt_administracion.focus();
        return false;
    }
    document.formu.action = "/vacuna_ingresada/"
    document.formu.submit() = true
    alert("Ingreso correcto");
    
}