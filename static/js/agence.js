// Archivo con las funciones Javascript

$('select').formSelect();
$('.datepicker').datepicker({
  'defaultDate': new Date(2007, 0, 1),
  'setDefaultDate': true,
  'minDate': new Date(2003, 0, 1),
  'maxDate': new Date(2007, 11, 31),
  'format': 'yyyy-mm-dd'
})

$(document).on('click', 'a.btn', function(event) {
  event.preventDefault()
  let id = this.id
  let url = this.dataset.url
  let date_start = $('#date_start').val()
  let date_end = $('#date_end').val()
  if (date_start === date_end) {
    alert('El Rango de Fechas son iguales, favor corregir e intentar nuevamente.')
  } else {
    $('#form_relatorio').attr('action', url).submit()
  }
});
