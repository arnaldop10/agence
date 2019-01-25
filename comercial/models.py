"""This is an auto-generated Django model module."""
from django.db import models
"""You'll have to do the following manually to clean this up:
  * Rearrange models' order
  * Make sure each model has one field with primary_key=True
  * Make sure each ForeignKey has `on_delete` set to the desired behavior.
  * Remove `managed = False` lines if you wish to allow Django to create,
  * modify, and delete the table
Feel free to rename the models, but don't rename db_table values or field
names.
"""


class CaoAcompanhamentoSistema(models.Model):
    co_acompanhamento = models.IntegerField(primary_key=True)
    email = models.TextField(blank=True, null=True)
    senha = models.TextField(blank=True, null=True)
    co_sistema = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    status = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_acompanhamento_sistema'


class CaoAgendamento(models.Model):
    co_agendamento = models.IntegerField(primary_key=True)
    dt_hr_inicio = models.DateTimeField(blank=True, null=True)
    dt_hr_fim = models.DateTimeField(blank=True, null=True)
    co_status_agendamento = models.BigIntegerField()
    co_diary_report_consultor = models.BigIntegerField()
    co_complemento = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cao_agendamento'


class CaoArquiteturaOs(models.Model):
    co_arquitetura = models.BigIntegerField(primary_key=True)
    ds_arquitetura = models.TextField()

    class Meta:
        managed = False
        db_table = 'cao_arquitetura_os'


class CaoAtividade(models.Model):
    co_atividade = models.AutoField(primary_key=True)
    ds_atividade = models.TextField()
    co_tipo_usuario = models.DecimalField(
        max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'cao_atividade'


class CaoAtividadeConsultor(models.Model):
    co_atividade = models.IntegerField(primary_key=True)
    ds_atividade = models.TextField()
    ativo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_atividade_consultor'


class CaoAtividadeReport(models.Model):
    id = models.IntegerField(primary_key=True)
    co_cliente = models.BigIntegerField()
    inicio = models.TextField(blank=True, null=True)
    fim = models.TextField(blank=True, null=True)
    lembrete = models.TextField(blank=True, null=True)
    co_atividade = models.BigIntegerField()
    co_os = models.BigIntegerField()
    assunto = models.TextField(blank=True, null=True)
    conteudo = models.TextField(blank=True, null=True)
    status = models.TextField()
    tempo = models.TextField(blank=True, null=True)
    co_usuario = models.TextField()
    data_ativ = models.DateTimeField(blank=True, null=True)
    retorno = models.TextField()
    co_fase = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_atividade_report'


class CaoAtividadeTeste(models.Model):
    co_atividade = models.AutoField(primary_key=True)
    ds_atividade = models.TextField()
    co_tipo_usuario = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cao_atividade_teste'


class CaoAviso(models.Model):
    co_aviso = models.IntegerField(primary_key=True)
    ds_aviso = models.TextField()

    class Meta:
        managed = False
        db_table = 'cao_aviso'


class CaoBancoDeHoras(models.Model):
    id = models.IntegerField(primary_key=True)
    co_usuario = models.TextField()
    data_cadastro = models.DateField()
    segundos = models.BigIntegerField()
    tipo = models.TextField()

    class Meta:
        managed = False
        db_table = 'cao_banco_de_horas'


class CaoBancoHoras(models.Model):
    co_banc_horas = models.IntegerField(primary_key=True)
    co_usuario = models.TextField()
    periodo = models.TextField()
    min_mes = models.BigIntegerField()
    min_ferias = models.BigIntegerField()
    min_pago = models.BigIntegerField()
    min_total = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cao_banco_horas'


class CaoBoleto(models.Model):
    co_boleto = models.IntegerField(primary_key=True)
    co_cliente = models.BigIntegerField()
    co_sistema = models.BigIntegerField()
    co_os = models.BigIntegerField()
    valor = models.TextField()
    vencimento = models.TextField()
    status = models.BigIntegerField()
    boleto = models.TextField(blank=True, null=True)
    linha_dig = models.TextField(blank=True, null=True)
    parcela = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_boleto'


class CaoBonus(models.Model):
    bon_categoria = models.IntegerField(primary_key=True)
    bon_inicio = models.IntegerField()
    bon_fim = models.IntegerField()
    bon_valor_sem = models.FloatField(blank=True, null=True)
    bon_valor_fimsem = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_bonus'
        unique_together = (('bon_categoria', 'bon_inicio', 'bon_fim'),)


class CaoBonusStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    co_usuario = models.TextField()
    data_solic = models.DateField()
    mes = models.TextField()
    valor = models.TextField()
    is_solic = models.TextField(blank=True, null=True)
    is_pg = models.TextField(blank=True, null=True)
    is_horas = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_bonus_status'


class CaoCategoriasOmbudsman(models.Model):
    idcategoria = models.AutoField(primary_key=True)
    descricao = models.TextField()

    class Meta:
        managed = False
        db_table = 'cao_categorias_ombudsman'


class CaoCidade(models.Model):
    co_cidade = models.IntegerField(primary_key=True)
    no_cidade = models.TextField()
    co_uf = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cao_cidade'


class CaoCliente(models.Model):
    co_cliente = models.IntegerField(primary_key=True)
    no_razao = models.TextField(blank=True, null=True)
    no_fantasia = models.TextField(blank=True, null=True)
    no_contato = models.TextField(blank=True, null=True)
    nu_telefone = models.TextField(blank=True, null=True)
    nu_ramal = models.TextField(blank=True, null=True)
    nu_cnpj = models.TextField(blank=True, null=True)
    ds_endereco = models.TextField(blank=True, null=True)
    nu_numero = models.IntegerField(blank=True, null=True)
    ds_complemento = models.TextField(blank=True, null=True)
    no_bairro = models.TextField()
    nu_cep = models.TextField(blank=True, null=True)
    no_pais = models.TextField(blank=True, null=True)
    co_ramo = models.BigIntegerField(blank=True, null=True)
    co_cidade = models.BigIntegerField()
    co_status = models.BigIntegerField(blank=True, null=True)
    ds_site = models.TextField(blank=True, null=True)
    ds_email = models.TextField(blank=True, null=True)
    ds_cargo_contato = models.TextField(blank=True, null=True)
    tp_cliente = models.CharField(max_length=2, blank=True, null=True)
    ds_referencia = models.TextField(blank=True, null=True)
    co_complemento_status = models.BigIntegerField(blank=True, null=True)
    nu_fax = models.TextField(blank=True, null=True)
    ddd2 = models.TextField(blank=True, null=True)
    telefone2 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_cliente'


class CaoClienteContato(models.Model):
    co_cliente = models.BigIntegerField(primary_key=True)
    dt_contato = models.DateField(blank=True, null=True)
    fg_agendado = models.IntegerField(blank=True, null=True)
    hr_ini = models.TimeField(blank=True, null=True)
    hr_end = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_cliente_contato'


class CaoComissao(models.Model):
    co_comissao = models.IntegerField(primary_key=True)
    co_fatura = models.BigIntegerField(unique=True)
    dt_efetuado = models.DateField()

    class Meta:
        managed = False
        db_table = 'cao_comissao'


class CaoComplemento(models.Model):
    co_complemento = models.IntegerField(primary_key=True)
    ds_complemento = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_complemento'


class CaoConhecimentoUsuario(models.Model):
    co_usuario = models.TextField(primary_key=True)
    co_conhecimento = models.IntegerField()
    nv_conhecimento = models.IntegerField(blank=True, null=True)
    is_certificado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_conhecimento_usuario'
        unique_together = (('co_usuario', 'co_conhecimento'),)


class CaoConhecimentos(models.Model):
    idconhecimento = models.IntegerField(primary_key=True)
    assunto = models.TextField()
    conhecimento = models.TextField()
    url = models.TextField()
    tags = models.TextField()
    usuario = models.TextField()
    datahora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_conhecimentos'


class CaoConhecimentosFontes(models.Model):
    idfonte = models.IntegerField(primary_key=True)
    idconhecimento = models.ForeignKey(
        CaoConhecimentos, models.DO_NOTHING, db_column='idconhecimento')
    datahora = models.DateTimeField(blank=True, null=True)
    arquivo = models.TextField()
    caminho = models.TextField()

    class Meta:
        managed = False
        db_table = 'cao_conhecimentos_fontes'


class CaoCusto(models.Model):
    co_custo = models.IntegerField(primary_key=True)
    co_tipo_custo = models.SmallIntegerField()
    descricao = models.TextField()
    co_escritorio = models.SmallIntegerField()
    dt_compra = models.DateField(blank=True, null=True)
    dt_pagamento = models.DateField(blank=True, null=True)
    co_boleto = models.TextField(blank=True, null=True)
    valor = models.FloatField()
    parcela = models.TextField(blank=True, null=True)
    pag = models.BooleanField(blank=True, null=True)
    co_custo_high = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'cao_custo'


class CaoDiaryReport(models.Model):
    co_diary_report = models.IntegerField(primary_key=True)
    hr_gasta = models.TimeField(blank=True, null=True)
    co_atividade = models.IntegerField()
    ds_assunto = models.TextField()
    co_movimento = models.DecimalField(max_digits=65535, decimal_places=65535)
    nu_os = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    co_sistema = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_diary_report'


class CaoDiaryReportConsultor(models.Model):
    co_diary_report_consultor = models.AutoField(primary_key=True)
    co_movimento = models.IntegerField()
    co_atividade = models.IntegerField()
    ds_empresa = models.TextField()
    ds_assunto = models.TextField()
    dt_agendamento = models.DateTimeField(blank=True, null=True)
    dt_agendamento_fim = models.DateTimeField(blank=True, null=True)
    vl_fechamento = models.FloatField()
    co_cliente = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_diary_report_consultor'


class CaoDocumentacaoCasosUso(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.TextField()
    co_sistema = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cao_documentacao_casos_uso'


class CaoDocumentacaoOutros(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.TextField()
    co_sistema = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cao_documentacao_outros'


class CaoDocumentacaoSistema(models.Model):
    id = models.IntegerField(primary_key=True)
    co_sistema = models.BigIntegerField()
    descricao = models.TextField(blank=True, null=True)
    pasta = models.TextField()
    sub_grupo = models.BigIntegerField(blank=True, null=True)
    co_usuario = models.TextField()
    dt_doc = models.DateTimeField(blank=True, null=True)
    arquivo = models.TextField()

    class Meta:
        managed = False
        db_table = 'cao_documentacao_sistema'


class CaoDrAtivComp(models.Model):
    id_ativ_comp = models.IntegerField(primary_key=True)
    co_usuario = models.TextField()
    data = models.DateField()
    assunto = models.TextField()
    tempo_gasto = models.TimeField()

    class Meta:
        managed = False
        db_table = 'cao_dr_ativ_comp'


class CaoEscalaRanking(models.Model):
    idescala = models.AutoField(primary_key=True)
    qtd_visual = models.SmallIntegerField()
    pontuacao = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cao_escala_ranking'


class CaoEscritorio(models.Model):
    co_escritorio = models.AutoField(primary_key=True)
    local = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'cao_escritorio'


class CaoFatura(models.Model):
    co_fatura = models.AutoField(primary_key=True)
    co_cliente = models.IntegerField()
    co_sistema = models.IntegerField()
    co_os = models.IntegerField()
    num_nf = models.BigIntegerField()
    total = models.FloatField()
    valor = models.FloatField()
    data_emissao = models.DateField()
    corpo_nf = models.TextField()
    comissao_cn = models.FloatField()
    total_imp_inc = models.FloatField()

    class Meta:
        managed = False
        db_table = 'cao_fatura'


class CaoFaturaPag(models.Model):
    id_fatura_pag = models.IntegerField(primary_key=True)
    co_fatura = models.BigIntegerField(unique=True)
    dt_efetuado = models.DateField()
    valor_pago = models.FloatField()

    class Meta:
        managed = False
        db_table = 'cao_fatura_pag'


class CaoFeriados(models.Model):
    dia = models.SmallIntegerField(blank=True, null=True)
    mes = models.SmallIntegerField(blank=True, null=True)
    ano = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_feriados'


class CaoFormacaoIdiomaUsuario(models.Model):
    co_usuario = models.TextField(primary_key=True)
    co_idioma = models.IntegerField()
    nv_leitura = models.IntegerField(blank=True, null=True)
    nv_escrita = models.IntegerField(blank=True, null=True)
    nv_fala = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_formacao_idioma_usuario'
        unique_together = (('co_usuario', 'co_idioma'),)


class CaoFormacaoUsuario(models.Model):
    co_usuario = models.TextField(primary_key=True)
    tp_curso = models.TextField()
    ds_curso = models.TextField(blank=True, null=True)
    ds_instituicao = models.TextField(blank=True, null=True)
    dt_conclusao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_formacao_usuario'
        unique_together = (('co_usuario', 'tp_curso'),)


class CaoHelpAutor(models.Model):
    co_autor = models.AutoField(primary_key=True)
    no_autor = models.TextField()
    co_filial = models.IntegerField()
    nu_ddd1 = models.TextField(blank=True, null=True)
    nu_tel1 = models.TextField(blank=True, null=True)
    nu_ramal1 = models.TextField(blank=True, null=True)
    nu_ddd2 = models.TextField(blank=True, null=True)
    nu_tel2 = models.TextField(blank=True, null=True)
    nu_ramal2 = models.TextField(blank=True, null=True)
    ds_email = models.TextField(blank=True, null=True)
    ds_funcao = models.TextField()

    class Meta:
        managed = False
        db_table = 'cao_help_autor'


class CaoHelpChamado(models.Model):
    co_chamado = models.IntegerField(primary_key=True)
    ds_chamado = models.TextField()
    ds_solucao = models.TextField(blank=True, null=True)
    co_status = models.SmallIntegerField()
    co_motivo = models.IntegerField()
    co_tela = models.IntegerField()
    co_autor = models.IntegerField()
    co_filial = models.IntegerField()
    co_sistema = models.DecimalField(max_digits=65535, decimal_places=65535)
    dt_chamado = models.DateField()
    dt_solucao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_help_chamado'


class CaoHelpFilial(models.Model):
    co_filial = models.AutoField(primary_key=True)
    no_filial = models.TextField()
    co_cliente = models.BigIntegerField()
    estado = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'cao_help_filial'


class CaoHelpMotivoChamado(models.Model):
    co_motivo = models.AutoField(primary_key=True)
    ds_motivo = models.TextField()

    class Meta:
        managed = False
        db_table = 'cao_help_motivo_chamado'


class CaoHelpStatusChamado(models.Model):
    co_status = models.AutoField(primary_key=True)
    ds_status = models.TextField()

    class Meta:
        managed = False
        db_table = 'cao_help_status_chamado'


class CaoHelpTelaChamado(models.Model):
    co_tela = models.AutoField(primary_key=True)
    co_cliente = models.BigIntegerField()
    co_sistema = models.BigIntegerField()
    ds_tela = models.TextField()

    class Meta:
        managed = False
        db_table = 'cao_help_tela_chamado'


class CaoHistOcorrenciasOs(models.Model):
    idocorrencia = models.IntegerField(primary_key=True)
    co_os = models.IntegerField(blank=True, null=True)
    co_usuario = models.TextField(blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    tipo = models.TextField()  # This field type is a guess.
    descricao = models.TextField()
    responsavel = models.TextField()
    data_fechamento = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_hist_ocorrencias_os'


class CaoHorarioAlmoco(models.Model):
    co_usuario = models.TextField()
    almoco_saida_hora = models.TextField()
    almoco_volta_hora = models.TextField()

    class Meta:
        managed = False
        db_table = 'cao_horario_almoco'


class CaoLogChamado(models.Model):
    id = models.IntegerField(primary_key=True)
    co_chamado = models.BigIntegerField()
    dt_chamado = models.DateTimeField(blank=True, null=True)
    co_usuario = models.TextField()
    co_daily = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cao_log_chamado'


class CaoMenu(models.Model):
    co_menu = models.AutoField(primary_key=True)
    ds_menu = models.TextField()
    ds_pagina = models.TextField()
    ds_imagem = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_menu'


class CaoMenuContador(models.Model):
    co_usuario = models.TextField(primary_key=True)
    co_menu = models.SmallIntegerField()
    nu_pontos = models.SmallIntegerField()
    in_processado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cao_menu_contador'
        unique_together = (('co_usuario', 'co_menu'),)


class CaoMovimento(models.Model):
    co_movimento = models.IntegerField(primary_key=True)
    co_usuario = models.TextField()
    dt_entrada = models.DateTimeField(blank=True, null=True)
    dt_saida_almoco = models.DateTimeField(blank=True, null=True)
    dt_volta_almoco = models.DateTimeField(blank=True, null=True)
    dt_saida = models.DateTimeField(blank=True, null=True)
    is_encerrado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cao_movimento'


class CaoMovimentoJustificativa(models.Model):
    co_movimento_justificativa = models.IntegerField(primary_key=True)
    co_movimento = models.DecimalField(max_digits=65535, decimal_places=65535)
    nu_os = models.DecimalField(max_digits=65535, decimal_places=65535)
    ds_justificativa = models.TextField()

    class Meta:
        managed = False
        db_table = 'cao_movimento_justificativa'


class CaoMovimentoOs(models.Model):
    co_movimento_os = models.AutoField(primary_key=True)
    nu_os = models.IntegerField()
    co_sistema = models.DecimalField(max_digits=65535, decimal_places=65535)
    co_tipo_movimento = models.BigIntegerField(blank=True, null=True)
    nu_valor = models.BigIntegerField(blank=True, null=True)
    ds_valor = models.TextField(blank=True, null=True)
    usuario_obs = models.TextField(blank=True, null=True)
    dt_ini = models.DateTimeField(blank=True, null=True)
    dt_fim = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_movimento_os'


class CaoNoticia(models.Model):
    co_noticia = models.IntegerField(primary_key=True)
    assunto = models.TextField()
    descricao = models.TextField()
    foto = models.TextField()
    co_usuario = models.TextField()
    dt_noticia = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_noticia'


class CaoObsCliente(models.Model):
    co_obs = models.IntegerField(primary_key=True)
    descricao = models.TextField()
    co_cliente = models.BigIntegerField()
    co_usuario = models.TextField(blank=True, null=True)
    dt_obs = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_obs_cliente'


class CaoObsSistema(models.Model):
    co_obs = models.IntegerField(primary_key=True)
    descricao = models.TextField(blank=True, null=True)
    co_sistema = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    co_usuario = models.TextField(blank=True, null=True)
    dt_obs = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_obs_sistema'


class CaoOmbudsman(models.Model):
    id = models.IntegerField(primary_key=True)
    idtipo = models.ForeignKey(
        'CaoTipoOmbudsman', models.DO_NOTHING, db_column='idtipo')
    idcategoria = models.ForeignKey(
        CaoCategoriasOmbudsman, models.DO_NOTHING, db_column='idcategoria')
    data = models.DateTimeField(blank=True, null=True)
    comentario = models.TextField()
    co_escritorio = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cao_ombudsman'


class CaoOs(models.Model):
    co_os = models.AutoField(primary_key=True)
    nu_os = models.IntegerField(blank=True, null=True)
    co_sistema = models.IntegerField(blank=True, null=True)
    co_usuario = models.TextField(blank=True, null=True)
    co_arquitetura = models.IntegerField(blank=True, null=True)
    ds_os = models.TextField(blank=True, null=True)
    ds_caracteristica = models.TextField(blank=True, null=True)
    ds_requisito = models.TextField(blank=True, null=True)
    dt_inicio = models.DateField(blank=True, null=True)
    dt_fim = models.DateField(blank=True, null=True)
    co_status = models.IntegerField(blank=True, null=True)
    diretoria_sol = models.TextField(blank=True, null=True)
    dt_sol = models.DateField(blank=True, null=True)
    nu_tel_sol = models.TextField(blank=True, null=True)
    ddd_tel_sol = models.TextField(blank=True, null=True)
    nu_tel_sol2 = models.TextField(blank=True, null=True)
    ddd_tel_sol2 = models.TextField(blank=True, null=True)
    usuario_sol = models.TextField(blank=True, null=True)
    dt_imp = models.DateField(blank=True, null=True)
    dt_garantia = models.DateField(blank=True, null=True)
    co_email = models.BigIntegerField(blank=True, null=True)
    co_os_prospect_rel = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_os'


class CaoOsAnalista(models.Model):
    co_analista = models.AutoField(primary_key=True)
    co_os = models.IntegerField(blank=True, null=True)
    co_usuario = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_os_analista'


class CaoOsChamado(models.Model):
    co_chamado = models.IntegerField(primary_key=True)
    co_sistema = models.BigIntegerField()
    co_os = models.BigIntegerField()
    ds_chamado = models.TextField()
    co_tipo = models.BigIntegerField()
    co_prioridade = models.BigIntegerField()
    co_item = models.BigIntegerField()
    descricao = models.TextField()
    ds_solucao = models.TextField()
    tempo = models.TextField()
    dt_chamado = models.DateTimeField(blank=True, null=True)
    status = models.BigIntegerField()
    co_usuario = models.TextField()
    co_analista = models.TextField()
    email = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_os_chamado'


class CaoOsDailyReport(models.Model):
    co_daily = models.AutoField(primary_key=True)
    co_os = models.IntegerField(blank=True, null=True)
    co_fase = models.IntegerField(blank=True, null=True)
    co_usuario = models.TextField(blank=True, null=True)
    ds_assunto = models.TextField(blank=True, null=True)
    tempo_gasto = models.TimeField(blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    co_status_atual = models.IntegerField(blank=True, null=True)
    co_chamado = models.BigIntegerField(blank=True, null=True)
    co_atividade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_os_daily_report'


class CaoOsEmail(models.Model):
    co_email = models.AutoField(primary_key=True)
    co_os = models.IntegerField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    senha = models.TextField(blank=True, null=True)
    nome = models.TextField()
    co_cliente = models.BigIntegerField()
    ativo = models.BigIntegerField()
    ddd = models.TextField(blank=True, null=True)
    tel = models.TextField(blank=True, null=True)
    cargo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_os_email'


class CaoOsFase(models.Model):
    co_fase = models.AutoField(primary_key=True)
    descricao = models.TextField(blank=True, null=True)
    descricao_ingl = models.TextField()
    ordem = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_os_fase'


class CaoOsItemMenu(models.Model):
    co_item = models.IntegerField(primary_key=True)
    ds_item = models.TextField()
    co_sistema = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cao_os_item_menu'


class CaoOsObs(models.Model):
    co_obs = models.AutoField(primary_key=True)
    co_os = models.IntegerField(blank=True, null=True)
    co_usuario = models.TextField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    dt_obs = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_os_obs'


class CaoOsObsChamado(models.Model):
    co_obs = models.AutoField(primary_key=True)
    co_chamado = models.IntegerField(blank=True, null=True)
    co_usuario = models.TextField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    dt_obs = models.DateTimeField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    arquivo_obs = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_os_obs_chamado'


class CaoOsPrazo(models.Model):
    co_prazo = models.AutoField(primary_key=True)
    co_os = models.IntegerField(blank=True, null=True)
    co_fase = models.IntegerField(blank=True, null=True)
    total_analista = models.IntegerField(blank=True, null=True)
    total_hora = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_os_prazo'


class CaoOsStatus(models.Model):
    co_status_atual = models.IntegerField(primary_key=True)
    ds_status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cao_os_status'


class CaoPagamento(models.Model):
    co_pagamento = models.IntegerField(primary_key=True)
    co_usuario = models.TextField()
    tp_pagamento = models.CharField(max_length=2)
    dt_pagamento = models.DateField()
    vl_pagamento = models.FloatField()
    dt_referencia_pagamento = models.DateField()

    class Meta:
        managed = False
        db_table = 'cao_pagamento'


class CaoParticipacaoFuncionario(models.Model):
    co_part_funcionario = models.IntegerField(primary_key=True)
    pc_participacao = models.FloatField()
    co_usuario = models.TextField()
    co_escritorio = models.SmallIntegerField()
    dt_referencia = models.DateField()

    class Meta:
        managed = False
        db_table = 'cao_participacao_funcionario'


class CaoPermissao(models.Model):
    co_usuario = models.TextField()
    permissao_intervalo = models.TextField()  # This field type is a guess.
    permissao_hora_extra = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'cao_permissao'


class CaoPermissaoHoraExtra(models.Model):
    id_permissao = models.IntegerField(primary_key=True)
    co_movimento = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'cao_permissao_hora_extra'


class CaoPontosConhecimento(models.Model):
    idpontos = models.IntegerField(primary_key=True)
    pontuacao = models.ForeignKey(
        CaoEscalaRanking, models.DO_NOTHING, db_column='pontuacao')
    co_coordenador = models.TextField()
    idconhecimento = models.ForeignKey(
        CaoConhecimentos, models.DO_NOTHING, db_column='idconhecimento')

    class Meta:
        managed = False
        db_table = 'cao_pontos_conhecimento'


class CaoRamo(models.Model):
    co_ramo = models.IntegerField(primary_key=True)
    ds_ramo = models.TextField()

    class Meta:
        managed = False
        db_table = 'cao_ramo'


class CaoRelEmailOs(models.Model):
    id = models.IntegerField(primary_key=True)
    co_email = models.BigIntegerField()
    co_os = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cao_rel_email_os'


class CaoSalario(models.Model):
    co_usuario = models.TextField(primary_key=True)
    dt_alteracao = models.DateField()
    brut_salario = models.FloatField()
    liq_salario = models.FloatField()

    class Meta:
        managed = False
        db_table = 'cao_salario'
        unique_together = (('co_usuario', 'dt_alteracao'),)


class CaoSalarioPag(models.Model):
    id_pagamento = models.IntegerField()
    co_usuario = models.ForeignKey(
        'CaoUsuario', models.DO_NOTHING, db_column='co_usuario')
    dt_efetuado = models.DateField()
    status = models.TextField()  # This field type is a guess.
    observacao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_salario_pag'
        unique_together = (('co_usuario', 'dt_efetuado'),)


class CaoServico(models.Model):
    co_servico = models.AutoField(primary_key=True)
    ds_servico = models.TextField()

    class Meta:
        managed = False
        db_table = 'cao_servico'


class CaoSistema(models.Model):
    co_sistema = models.AutoField(primary_key=True)
    co_cliente = models.IntegerField(blank=True, null=True)
    co_usuario = models.TextField(blank=True, null=True)
    co_arquitetura = models.IntegerField(blank=True, null=True)
    no_sistema = models.TextField(blank=True, null=True)
    ds_sistema_resumo = models.TextField(blank=True, null=True)
    ds_caracteristica = models.TextField(blank=True, null=True)
    ds_requisito = models.TextField(blank=True, null=True)
    no_diretoria_solic = models.TextField(blank=True, null=True)
    ddd_telefone_solic = models.TextField(blank=True, null=True)
    nu_telefone_solic = models.TextField(blank=True, null=True)
    no_usuario_solic = models.TextField(blank=True, null=True)
    dt_solicitacao = models.DateField(blank=True, null=True)
    dt_entrega = models.DateField(blank=True, null=True)
    co_email = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_sistema'


class CaoSistemaObs(models.Model):
    co_obs = models.IntegerField(primary_key=True)
    descricao = models.TextField(blank=True, null=True)
    co_sistema = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    co_usuario = models.TextField(blank=True, null=True)
    dt_obs = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_sistema_obs'


class CaoStatusAgendamento(models.Model):
    co_status_agendamento = models.IntegerField(primary_key=True)
    ds_status_agendamento = models.TextField()

    class Meta:
        managed = False
        db_table = 'cao_status_agendamento'


class CaoStatusCliente(models.Model):
    co_status = models.IntegerField(primary_key=True)
    ds_status = models.TextField()

    class Meta:
        managed = False
        db_table = 'cao_status_cliente'


class CaoStatusClienteComplemento(models.Model):
    co_complemento_status = models.IntegerField(primary_key=True)
    ds_status = models.TextField(blank=True, null=True)
    co_status = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_status_cliente_complemento'


class CaoStatusOs(models.Model):
    co_status_atual = models.IntegerField(primary_key=True)
    ds_status = models.TextField()

    class Meta:
        managed = False
        db_table = 'cao_status_os'


class CaoTempImport(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descricao = models.TextField()

    class Meta:
        managed = False
        db_table = 'cao_temp_import'


class CaoTipoConhecimentoUsuario(models.Model):
    co_conhecimento = models.AutoField(primary_key=True)
    ds_conhecimento = models.TextField(blank=True, null=True)
    co_sistema = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cao_tipo_conhecimento_usuario'


class CaoTipoCusto(models.Model):
    co_tipo_custo = models.AutoField(primary_key=True)
    descricao = models.TextField()

    class Meta:
        managed = False
        db_table = 'cao_tipo_custo'


class CaoTipoIdiomaUsuario(models.Model):
    co_idioma = models.AutoField(primary_key=True)
    ds_idioma = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_tipo_idioma_usuario'


class CaoTipoOmbudsman(models.Model):
    idtipo = models.AutoField(primary_key=True)
    descricao = models.TextField()

    class Meta:
        managed = False
        db_table = 'cao_tipo_ombudsman'


class CaoTipoSistemaUsuario(models.Model):
    co_sistema = models.AutoField(primary_key=True)
    ds_sistema = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_tipo_sistema_usuario'


class CaoUf(models.Model):
    co_uf = models.IntegerField(primary_key=True)
    ds_uf = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'cao_uf'


class CaoUsuario(models.Model):
    co_usuario = models.TextField(primary_key=True)
    no_usuario = models.TextField()
    ds_senha = models.TextField()
    co_usuario_autorizacao = models.TextField(blank=True, null=True)
    nu_matricula = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    dt_admissao_empresa = models.DateField(blank=True, null=True)
    dt_desligamento = models.DateField(blank=True, null=True)
    dt_inclusao = models.DateTimeField(blank=True, null=True)
    dt_expiracao = models.DateField(blank=True, null=True)
    nu_cpf = models.TextField(blank=True, null=True)
    nu_rg = models.TextField(blank=True, null=True)
    no_orgao_emissor = models.TextField(blank=True, null=True)
    uf_orgao_emissor = models.TextField(blank=True, null=True)
    ds_endereco = models.TextField(blank=True, null=True)
    no_email = models.TextField(blank=True, null=True)
    no_email_pessoal = models.TextField(blank=True, null=True)
    nu_telefone = models.TextField(blank=True, null=True)
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    url_foto = models.TextField(blank=True, null=True)
    instant_messenger = models.TextField(blank=True, null=True)
    icq = models.BigIntegerField(blank=True, null=True)
    msn = models.TextField(blank=True, null=True)
    yms = models.TextField(blank=True, null=True)
    ds_comp_end = models.TextField(blank=True, null=True)
    ds_bairro = models.TextField(blank=True, null=True)
    nu_cep = models.TextField(blank=True, null=True)
    no_cidade = models.TextField(blank=True, null=True)
    uf_cidade = models.TextField(blank=True, null=True)
    dt_expedicao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_usuario'


class CaoUsuarioDtDisp(models.Model):
    co_dt_disp = models.AutoField(primary_key=True)
    co_usuario = models.TextField(blank=True, null=True)
    dt_disp = models.DateField()
    dt_alt = models.DateField()

    class Meta:
        managed = False
        db_table = 'cao_usuario_dt_disp'


class CaoValorDescanso(models.Model):
    id = models.IntegerField(primary_key=True)
    co_usuario = models.TextField()
    segundos = models.TextField()
    mes_referencia = models.TextField()

    class Meta:
        managed = False
        db_table = 'cao_valor_descanso'


class PermissaoSistema(models.Model):
    co_usuario = models.TextField(primary_key=True)
    co_tipo_usuario = models.DecimalField(
        max_digits=65535, decimal_places=65535)
    co_sistema = models.DecimalField(max_digits=65535, decimal_places=65535)
    in_ativo = models.CharField(max_length=1)
    co_usuario_atualizacao = models.TextField(blank=True, null=True)
    dt_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissao_sistema'
        unique_together = (('co_usuario', 'co_tipo_usuario', 'co_sistema'),)


class TipoUsuario(models.Model):
    co_tipo_usuario = models.DecimalField(
        primary_key=True, max_digits=65535, decimal_places=65535)
    ds_tipo_usuario = models.TextField()
    co_sistema = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'
        unique_together = (('co_tipo_usuario', 'co_sistema'),)
