from datetime import datetime
from dateutil import relativedelta
from .models import CaoUsuario, PermissaoSistema


def get_periods_data(start, end):
    """Funcion que retorna un arreglo de meses."""
    date_start = datetime.strptime(start, '%Y-%m-%d')
    date_end = datetime.strptime(end, '%Y-%m-%d')
    r = relativedelta.relativedelta(date_end, date_start)
    month_start = date_start.month
    year_start = date_start.year
    months = r.months
    years = r.years
    days = r.days

    if years == 0:
        if months == 0:
            if days >= 1:
                months = 1
            else:
                return 'Error en el rango de fecha'
        elif months < 0:
            return 'Error: La fecha inicial debe ser menor a la fecha final'
        else:
            if months < date_end.month:
                months += 1
    else:
        months += (years * 12) + 1

    data = []
    for i in range(months):
        data.append({
            'month': month_start,
            'year': year_start
        })
        if month_start < 12:
            month_start += 1
        else:
            month_start = 1
            year_start += 1

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


def get_consultants_list():
    """Funcion que retorna la lista de consultores."""
    consultants = []
    permisos = PermissaoSistema.objects.filter(
        co_sistema=1, in_ativo='S', co_tipo_usuario__in=[0, 1, 2]
    )
    usuarios = CaoUsuario.objects.filter(co_usuario__in=permisos)
    for usuario in usuarios:
        consultants.append({
            'co_usuario': usuario.co_usuario,
            'no_usuario': (
                usuario.no_usuario).encode("latin-1").decode("utf-8")
        })

    return consultants
