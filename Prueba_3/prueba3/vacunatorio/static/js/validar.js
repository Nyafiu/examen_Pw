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