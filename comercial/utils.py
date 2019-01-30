from datetime import datetime
from dateutil import relativedelta


def get_periods_data(start, end):
    """Funcion que retorna un arreglo de meses."""
    date_start = datetime.strptime(start, '%Y-%m-%d')
    date_end = datetime.strptime(end, '%Y-%m-%d')
    r = relativedelta.relativedelta(date_end, date_start)
    months = r.months
    years = r.years

    if years == 0 and months <= 0:
        return 'Error en el rango de fecha'

    if years > 0:
        months += years * 12
    elif years == 0 and months < date_end.month:
        months += 1

    month = date_start.month
    year = date_start.year

    data = []
    for i in range(months):
        data.append({
            'month': month,
            'year': year
        })
        if month < 12:
            month += 1
        else:
            month = 1
            year += 1

    return data


def get_string_month(month):
    """Funcion que retorna el nombre del mes."""
    months = [
        'Enero',
        'Febrero',
        'Marzo',
        'Abril',
        'Mayo',
        'Junio',
        'Julio',
        'Agosto',
        'Septiembre',
        'Octubre',
        'Noviembre',
        'Diciembre',
    ]

    return months[month - 1]
