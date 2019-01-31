import json
from django.shortcuts import render
from .models import (
    CaoUsuario, PermissaoSistema, CaoOs, CaoFatura, CaoSalario)
# from django.http import HttpResponse
from .utils import get_periods_data, get_string_month


def index(request):
    """Vista principal para el index."""
    permisos = PermissaoSistema.objects.filter(
        co_sistema=1, in_ativo='S', co_tipo_usuario__in=[0, 1, 2]
    )
    usuarios = CaoUsuario.objects.filter(co_usuario__in=permisos)
    return render(request, 'con_desempenho.html', {'usuarios': usuarios})


def relatorio_detail_view(request):
    """Vista para el boton relatorio."""
    if request.method == 'POST':
        data = request.POST
        date_start = data.get('date_start')
        date_end = data.get('date_end')
        consultores = data.getlist('consultants')
        dates = get_periods_data(date_start, date_end)
        ganancias = []

        for consultor in consultores:
            usuario = CaoUsuario.objects.get(co_usuario=consultor)
            os = CaoOs.objects.filter(co_usuario=consultor)
            try:
                salario = CaoSalario.objects.get(co_usuario=consultor)
                costo_fijo = salario.brut_salario
            except CaoSalario.DoesNotExist:
                costo_fijo = 0

            periodos = []
            total_ganancias = 0
            total_costo = 0
            total_comision = 0
            total_lucro = 0

            for date in dates:
                comision = 0
                ganancias_netas = 0
                lucro = 0

                facturas = CaoFatura.objects.filter(
                    co_os__in=os,
                    data_emissao__month=date['month'],
                    data_emissao__year=date['year'])

                for factura in facturas:
                    impuesto = factura.valor * (factura.total_imp_inc / 100)
                    valor_neto = factura.valor - impuesto
                    ganancias_netas += valor_neto
                    comision += valor_neto * (factura.comissao_cn / 100)

                lucro = ganancias_netas - (costo_fijo + comision)

                total_ganancias += ganancias_netas
                total_costo += costo_fijo
                total_comision += comision
                total_lucro += lucro

                periodos.append({
                    'nombre': get_string_month(
                        date['month']) + ' ' + str(date['year']),
                    'ganancia_liquida': round(ganancias_netas, 2),
                    'costo_fijo': round(costo_fijo, 2),
                    'comision': round(comision, 2),
                    'lucro': round(lucro, 2)
                })

            ganancias.append({
                'consultor': usuario.no_usuario,
                'periodos': periodos,
                'totales': {
                    'total_ganancias': round(total_ganancias, 2),
                    'total_costo': round(total_costo, 2),
                    'total_comision': round(total_comision, 2),
                    'total_lucro': round(total_lucro, 2)
                }
            })

    permisos = PermissaoSistema.objects.filter(
        co_sistema=1, in_ativo='S', co_tipo_usuario__in=[0, 1, 2]
    )
    usuarios = CaoUsuario.objects.filter(co_usuario__in=permisos)

    return render(
        request,
        'con_desem_consultor_rel.html',
        {'ganancias': ganancias, 'usuarios': usuarios}
    )


def grafico_view(request):
    """Vista para el boton grafico."""
    if request.method == 'POST':
        data = request.POST
        date_start = data.get('date_start')
        date_end = data.get('date_end')
        consultores = data.getlist('consultants')
        dates = get_periods_data(date_start, date_end)
        series = []
        periodos = []
        costos = []
        num_consultores = len(consultores)
        costo_fijo = 0

        for consultor in consultores:
            usuario = CaoUsuario.objects.get(co_usuario=consultor)
            os = CaoOs.objects.filter(co_usuario=consultor)
            salario = CaoSalario.objects.get(co_usuario=consultor)
            costo_fijo += salario.brut_salario
            ganancias = []
            ganancias_netas = 0

            for date in dates:

                facturas = CaoFatura.objects.filter(
                    co_os__in=os,
                    data_emissao__month=date['month'],
                    data_emissao__year=date['year'])

                for factura in facturas:
                    impuesto = factura.valor * (factura.total_imp_inc / 100)
                    valor_neto = factura.valor - impuesto
                    ganancias_netas += round(valor_neto, 2)

                ganancias.append(ganancias_netas)
                periodos.append(get_string_month(
                    date['month']) + ' ' + str(date['year']))

            series.append({
                'name': usuario.no_usuario,
                'data': ganancias,
            })

        costos = [costo_fijo / num_consultores] * len(dates)
        series.append({
            'type': 'spline',
            'name': 'Costo Fijo Promedio',
            'data': costos,
            'marker': {
                'lineWidth': 2,
                'lineColor': 'blue',
                'fillColor': 'white'
            }
        })

        chart = {
            'chart': {
                'type': 'column'
            },
            'title': {
                'text': 'Desempeño Gráfico de Consultores'
            },
            'xAxis': {
                'categories': periodos
            },
            'series': series
        }

        dump = json.dumps(chart)

    return render(request, 'con_desem_consultor_graf.html', {'chart': dump})


def pizza_view(request):
    """Vista para el boton grafico pizza."""
    if request.method == 'POST':
        data = request.POST
        date_start = data.get('date_start')
        date_end = data.get('date_end')
        consultores = data.getlist('consultants')
        dates = get_periods_data(date_start, date_end)
        series = []

        for consultor in consultores:
            usuario = CaoUsuario.objects.get(co_usuario=consultor)
            os = CaoOs.objects.filter(co_usuario=consultor)
            ganancias_netas = 0
            for date in dates:
                facturas = CaoFatura.objects.filter(
                    co_os__in=os,
                    data_emissao__month=date['month'],
                    data_emissao__year=date['year'])

                for factura in facturas:
                    impuesto = factura.valor * (factura.total_imp_inc / 100)
                    valor_neto = factura.valor - impuesto
                    ganancias_netas += round(valor_neto, 2)

            series.append({
                'name': usuario.no_usuario,
                'y': ganancias_netas,
            })

        chart = {
            'chart': {
                'plotBackgroundColor': None,
                'plotBorderWidth': None,
                'plotShadow': False,
                'type': 'pie'
            },
            'title': {
                'text': 'Ganancias Liquidas por Consultor'
            },
            'tooltip': {
                'pointFormat': '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            'plotOptions': {
                'pie': {
                    'allowPointSelect': True,
                    'cursor': 'pointer',
                    'dataLabels': {
                        'enabled': True,
                        'format': '<b>{point.name}</b>:\
                                    {point.percentage:.1f} %',
                        'style': {
                            'color': 'black'
                        }
                    }
                }
            },
            'series': [{
                'name': 'Consultores',
                'colorByPoint': True,
                'data': series
            }]
        }

        dump = json.dumps(chart)

    return render(
        request, 'con_desem_consultor_pizza.html', {'chart_pizza': dump})
