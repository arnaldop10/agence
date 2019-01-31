// Archivo con las funciones Javascript

let dataStorage = window.localStorage

$('select').formSelect();
$('.datepicker').datepicker({
  'defaultDate': new Date(2007, 0, 1),
  'setDefaultDate': true,
  'minDate': new Date(2003, 0, 1),
  'maxDate': new Date(2007, 11, 31),
  'format': 'yyyy-mm-dd'
})

$(".dropdown-trigger").dropdown()
$('.sidenav').sidenav()

$(document).on('click', 'a.btn', function(event) {
  event.preventDefault()
  let url = this.dataset.url
  let date_start = $('#date_start').val()
  let date_end = $('#date_end').val()
  let consultants = $('#consultants').val()
  
  dataStorage.setItem('start', date_start)
  dataStorage.setItem('end', date_end)
  dataStorage.setItem('consultants', consultants)
  
  if (date_start === date_end) {
    alert('El Rango de Fechas son iguales, favor corregir e intentar nuevamente.')
  } else {
    if (consultants.length === 0) {
      alert('Debe seleccionar al menos un (1) consultor.')
    } else {
      $('#form_relatorio').attr('action', url).submit()
    }
  }
})

$(function() {
  if (window.location.pathname === '/relatorio/') {
    if (dataStorage) {
      $('#date_start').val(dataStorage.getItem('start'))
      $('#date_end').val(dataStorage.getItem('end'))
      let consultants = dataStorage.getItem('consultants')
      $.each(consultants.split(","), function(i,e){
        $("#consultants option[value='" + e + "']").prop("selected", true);
      })
      $('#consultants').formSelect()
    }
  }
})
