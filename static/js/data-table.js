
function creaObjetoAjax () 
{ 
     var obj;
     if (window.XMLHttpRequest) 
     {
        obj=new XMLHttpRequest();
     }
     else 
     { 
        obj=new ActiveXObject(Microsoft.XMLHTTP);
         
     }
     return obj;
}
function crearTablasHtml(){
    let table = document.getElementById("recomendaciones")
    let tableRow = document.createElement("tr");
    tableRow.setAttribute("class","registro")
    let tableCellId = document.createElement("td");
    let tableCellNombre = document.createElement("td");
    let tableCellAutor = document.createElement("td");
    let tableCellIdioma = document.createElement("td");
    let tableCellPaginas = document.createElement("td");
    tableCellId.setAttribute('class','id-tabla');
    tableCellNombre.setAttribute('class','nombre-tabla');
    tableCellAutor.setAttribute('class','autor-tabla');
    tableCellIdioma.setAttribute('class','idioma-tabla');
    tableCellPaginas.setAttribute('class','paginas-tabla');
    tableRow.append(tableCellId)
    tableRow.append(tableCellNombre)
    tableRow.append(tableCellAutor)
    tableRow.append(tableCellIdioma)
    tableRow.append(tableCellPaginas)
    table.append(tableRow)
}
function rellenandoTablaHtml(resultado,k,index){
    let idLibro = document.getElementsByClassName("id-tabla")[index]
    let nombreLibro = document.getElementsByClassName("nombre-tabla")[index];
    let autorLibro = document.getElementsByClassName("autor-tabla")[index];
    let idiomaLibro = document.getElementsByClassName("idioma-tabla")[index];
    let paginasLibro = document.getElementsByClassName("paginas-tabla")[index];
    textId = document.createTextNode(index);
    textNombre = document.createTextNode(resultado[k].Name);
    textAutor = document.createTextNode(resultado[k].Autor);
    textIdioma = document.createTextNode(resultado[k].Idioma);
    textPaginas = document.createTextNode(resultado[k].Paginas);
    idLibro.appendChild(textId)
    nombreLibro.appendChild(textNombre)
    autorLibro.appendChild(textAutor)
    idiomaLibro.appendChild(textIdioma)
    paginasLibro.appendChild(textPaginas)
}
function limpiezaTabla(){
    let table = document.getElementById('recomendaciones')
    if (table.childElementCount > 0){
        table.innerHTML = ""
    }
}
function ejecucionPeticionAjax(peticio){
    let resultado = JSON.parse(peticio);
    let keys = Object.keys(resultado)
    let longKeys = keys.length
    let index = 0
    for (let index = 0; index < longKeys; index++) {
        crearTablasHtml()
    }
    keys.forEach(function(k){
        rellenandoTablaHtml(resultado,k,index)
        index++
    });
}
function buscar(){
    let peticio = creaObjetoAjax()
    let calificacion = document.getElementById("rating").value
    let libro = document.getElementById("name").value
    let url = "http://localhost:5000/libros/recomendar_pkl?libro="+libro+"&rating="+calificacion
    limpiezaTabla()
    peticio.open("GET",url,true);
    peticio.onreadystatechange = function()
    {
        if(peticio.readyState == 4 && peticio.status == 200)
        {
            ejecucionPeticionAjax(peticio.responseText)
            $('body').removeClass('waiting');
            document.getElementById("loading-animation").hidden = true;
            window.location.href='#portfolio';
        }
    }
    peticio.send();
}
function agregarParametros(){
    let calificacion = document.getElementById("rating").value 
    let libro = document.getElementById("name").value 
    let actualUrl = window.location.href
    let particionUrl = actualUrl.split("?")
    let nuevaUrl = particionUrl[0] + "?libro="+ libro + "&rating="+calificacion
    window.history.pushState({},null,nuevaUrl)
}
function frenarSubmit(event){
    event.preventDefault()
    $('body').addClass('waiting');
    document.getElementById("loading-animation").hidden = false;
    agregarParametros()
    buscar()
    

}

function scrollto(element) {
    // get the element on the page related to the button
    var scrollToId = element.getAttribute("data-scroll");
    var scrollToElement = document.getElementById(scrollToId);
    // make the page scroll down to where you want
    // ...
}