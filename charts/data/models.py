# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BrasilApiBaseMundo(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    cases = models.BigIntegerField(blank=True, null=True)
    confirmed = models.BigIntegerField(blank=True, null=True)
    deaths = models.BigIntegerField(blank=True, null=True)
    recovered = models.FloatField(blank=True, null=True)
    updated_at = models.TextField(blank=True, null=True)
    insert_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Brasil_api_base_mundo'


class BrasilApiBaseNacional(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    uid = models.BigIntegerField(blank=True, null=True)
    uf = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    cases = models.BigIntegerField(blank=True, null=True)
    deaths = models.BigIntegerField(blank=True, null=True)
    suspects = models.BigIntegerField(blank=True, null=True)
    refuses = models.BigIntegerField(blank=True, null=True)
    broadcast = models.FloatField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    datetime = models.TextField(blank=True, null=True)
    insert_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Brasil_api_base_nacional'


class BrasilIoBaseCartorio(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    epidemiological_week_2019 = models.BigIntegerField(blank=True, null=True)
    epidemiological_week_2020 = models.BigIntegerField(blank=True, null=True)
    deaths_indeterminate_2019 = models.IntegerField(blank=True, null=True)
    deaths_respiratory_failure_2019 = models.IntegerField(blank=True, null=True)
    deaths_others_2019 = models.IntegerField(blank=True, null=True)
    deaths_pneumonia_2019 = models.IntegerField(blank=True, null=True)
    deaths_septicemia_2019 = models.IntegerField(blank=True, null=True)
    deaths_sars_2019 = models.IntegerField(blank=True, null=True)
    deaths_covid19 = models.IntegerField(blank=True, null=True)
    deaths_indeterminate_2020 = models.IntegerField(blank=True, null=True)
    deaths_respiratory_failure_2020 = models.IntegerField(blank=True, null=True)
    deaths_others_2020 = models.IntegerField(blank=True, null=True)
    deaths_pneumonia_2020 = models.IntegerField(blank=True, null=True)
    deaths_septicemia_2020 = models.IntegerField(blank=True, null=True)
    deaths_sars_2020 = models.IntegerField(blank=True, null=True)
    deaths_total_2019 = models.BigIntegerField(blank=True, null=True)
    deaths_total_2020 = models.BigIntegerField(blank=True, null=True)
    new_deaths_indeterminate_2019 = models.IntegerField(blank=True, null=True)
    new_deaths_respiratory_failure_2019 = models.IntegerField(blank=True, null=True)
    new_deaths_others_2019 = models.IntegerField(blank=True, null=True)
    new_deaths_pneumonia_2019 = models.IntegerField(blank=True, null=True)
    new_deaths_septicemia_2019 = models.IntegerField(blank=True, null=True)
    new_deaths_sars_2019 = models.IntegerField(blank=True, null=True)
    new_deaths_covid19 = models.IntegerField(blank=True, null=True)
    new_deaths_indeterminate_2020 = models.IntegerField(blank=True, null=True)
    new_deaths_respiratory_failure_2020 = models.IntegerField(blank=True, null=True)
    new_deaths_others_2020 = models.IntegerField(blank=True, null=True)
    new_deaths_pneumonia_2020 = models.IntegerField(blank=True, null=True)
    new_deaths_septicemia_2020 = models.IntegerField(blank=True, null=True)
    new_deaths_sars_2020 = models.IntegerField(blank=True, null=True)
    new_deaths_total_2019 = models.BigIntegerField(blank=True, null=True)
    new_deaths_total_2020 = models.BigIntegerField(blank=True, null=True)
    insert_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Brasil_io_base_cartorio'


class BrasilIoBaseNacional(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    city_ibge_code = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    epidemiological_week = models.BigIntegerField(blank=True, null=True)
    estimated_population = models.FloatField(blank=True, null=True)
    estimated_population_2019 = models.IntegerField(blank=True, null=True)
    is_last = models.BooleanField(blank=True, null=True)
    is_repeated = models.BooleanField(blank=True, null=True)
    last_available_confirmed = models.BigIntegerField(blank=True, null=True)
    last_available_confirmed_per_100k_inhabitants = models.FloatField(blank=True, null=True)
    last_available_date = models.TextField(blank=True, null=True)
    last_available_death_rate = models.FloatField(blank=True, null=True)
    last_available_deaths = models.BigIntegerField(blank=True, null=True)
    order_for_place = models.BigIntegerField(blank=True, null=True)
    place_type = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    new_confirmed = models.BigIntegerField(blank=True, null=True)
    new_deaths = models.BigIntegerField(blank=True, null=True)
    insert_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Brasil_io_base_nacional'


class HdxBaseMundo(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    country_region = models.TextField(db_column='Country/Region', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    confirmed = models.TextField(db_column='Confirmed', blank=True, null=True)  # Field name made lowercase.
    deaths = models.TextField(db_column='Deaths', blank=True, null=True)  # Field name made lowercase.
    recovered = models.TextField(db_column='Recovered', blank=True, null=True)  # Field name made lowercase.
    insert_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HDX_base_mundo'


class SesaPdfCasossrag(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    srag = models.CharField(max_length=-1, blank=True, null=True)
    casos = models.IntegerField(blank=True, null=True)
    casos_porcentagem = models.FloatField(db_column='casos porcentagem', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    obitos = models.IntegerField(blank=True, null=True)
    obitos_porcentagem = models.FloatField(db_column='obitos porcentagem', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'SESA_PDF_casosSRAG'


class SesaPdfComorbidadesobitos(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    comorbidade_obitos = models.CharField(db_column='comorbidade obitos', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    numero = models.IntegerField(blank=True, null=True)
    porcentagem = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SESA_PDF_comorbidadesObitos'


class SesaPdfOcupacaoleitos(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    tipo_de_leito = models.TextField(db_column='tipo de leito', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    sus_susp = models.IntegerField(db_column='sus susp', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    sus_conf = models.IntegerField(db_column='sus conf', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    priv_susp = models.IntegerField(db_column='priv susp', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    priv_conf = models.IntegerField(db_column='priv conf', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'SESA_PDF_ocupacaoLeitos'


class SesaBasePr(models.Model):
    index = models.TextField(blank=True, null=True)
    regional = models.CharField(db_column='REGIONAL', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    municipio = models.CharField(db_column='MUNICIPIO', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    populacao = models.IntegerField(db_column='POPULACAO', blank=True, null=True)  # Field name made lowercase.
    confirmados = models.IntegerField(db_column='CONFIRMADOS', blank=True, null=True)  # Field name made lowercase.
    recuperados = models.IntegerField(db_column='RECUPERADOS', blank=True, null=True)  # Field name made lowercase.
    obitos = models.IntegerField(db_column='OBITOS', blank=True, null=True)  # Field name made lowercase.
    investigacao = models.IntegerField(db_column='INVESTIGACAO', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SESA_base_PR'


class SesaBaseCasossrag(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    srag = models.TextField(blank=True, null=True)
    casos_field = models.BigIntegerField(db_column='casos ', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    casos_porcentagem = models.TextField(db_column='casos porcentagem', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    obitos = models.BigIntegerField(blank=True, null=True)
    obitos_porcentagem = models.TextField(db_column='obitos porcentagem', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    insert_date = models.DateTimeField(blank=True, null=True)
    data_boletim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SESA_base_casosSRAG'


class SesaBaseComorbidadesobitos(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    comorbidades_obitos = models.TextField(db_column='comorbidades obitos', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    numero = models.BigIntegerField(blank=True, null=True)
    porcentagem = models.TextField(blank=True, null=True)
    insert_date = models.DateTimeField(blank=True, null=True)
    data_boletim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SESA_base_comorbidadesObitos'


class SesaBaseDadosgerais(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    total_de_confirmados = models.BigIntegerField(db_column='total de confirmados', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    total_de_obitos = models.BigIntegerField(db_column='total de obitos', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    confirmados_homens = models.BigIntegerField(blank=True, null=True)
    confirmados_mulheres = models.BigIntegerField(blank=True, null=True)
    obitos_homens = models.BigIntegerField(blank=True, null=True)
    obitos_mulheres = models.BigIntegerField(blank=True, null=True)
    media_de_idade_dos_confirmados = models.TextField(blank=True, null=True)
    media_de_idade_dos_obitos = models.TextField(blank=True, null=True)
    insert_date = models.DateTimeField(blank=True, null=True)
    data_boletim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SESA_base_dadosGerais'


class SesaBaseEvoluconfirmados(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    internados = models.BigIntegerField(blank=True, null=True)
    internados_enfermaria = models.BigIntegerField(db_column='internados enfermaria', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    internados_uti = models.BigIntegerField(db_column='internados uti', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    recuperados = models.BigIntegerField(blank=True, null=True)
    insert_date = models.DateTimeField(blank=True, null=True)
    data_boletim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SESA_base_evoluConfirmados'


class SesaBaseExamesrt(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    exames_rt_pcr_realizados = models.BigIntegerField(db_column='exames RT-PCR realizados', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exames_rt_pcr_negativos = models.BigIntegerField(db_column='exames RT-PCR negativos', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exames_rt_pcr_investigaþÒo = models.BigIntegerField(db_column='exames RT-PCR investigaþÒo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exames_rt_pcr_lacen_ibmp_dia = models.BigIntegerField(db_column='exames RT-PCR lacen ibmp dia', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    testes_rapidos = models.BigIntegerField(db_column='testes rapidos', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    insert_date = models.DateTimeField(blank=True, null=True)
    data_boletim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SESA_base_examesRT'


class SesaBaseFaixaetaria(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    idades = models.TextField(blank=True, null=True)
    confirmados = models.BigIntegerField(blank=True, null=True)
    obitos = models.BigIntegerField(blank=True, null=True)
    porcentagem_idade_confirmados = models.TextField(blank=True, null=True)
    porcentagem_idade_obitos = models.TextField(blank=True, null=True)
    confirmados_masculino = models.BigIntegerField(blank=True, null=True)
    obitos_masculino = models.BigIntegerField(blank=True, null=True)
    confirmados_feminino = models.BigIntegerField(blank=True, null=True)
    obitos_feminino = models.BigIntegerField(blank=True, null=True)
    insert_date = models.DateTimeField(blank=True, null=True)
    data_boletim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SESA_base_faixaEtaria'


class SesaBaseLeitosmacrorregiao(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    leitos = models.CharField(max_length=-1, blank=True, null=True)
    uti_adulto_exist = models.IntegerField(db_column='uti adulto exist', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    uti_adulto_ocup = models.IntegerField(db_column='uti adulto ocup', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    uti_adulto_tx_ocup = models.FloatField(db_column='uti adulto tx ocup', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    enf_adulto_exist = models.IntegerField(db_column='enf adulto exist', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    enf_adulto_ocup = models.IntegerField(db_column='enf adulto ocup', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    enf_adulto_tx_ocup = models.FloatField(db_column='enf adulto tx ocup', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    uti_infantil_exist = models.IntegerField(db_column='uti infantil exist', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    uti_infantil_ocup = models.IntegerField(db_column='uti infantil ocup', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    uti_infantil_tx_ocup = models.FloatField(db_column='uti infantil tx ocup', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    enf_infantil_exist = models.FloatField(db_column='enf infantil exist', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    enf_infantil_ocup = models.IntegerField(db_column='enf infantil ocup', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    enf_infantil_tx_ocup = models.FloatField(db_column='enf infantil tx ocup', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    data_boletim = models.DateField(blank=True, null=True)
    insert_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SESA_base_leitosMacrorregiao'


class SesaBaseObitoscor(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    obitos_por_raca = models.TextField(db_column='obitos por raca', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    obitos_por_raca_porcentagem = models.TextField(db_column='obitos por raca porcentagem', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    obitos_etinia = models.BigIntegerField(blank=True, null=True)
    insert_date = models.DateTimeField(blank=True, null=True)
    data_boletim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SESA_base_obitosCor'


class SesaBaseOcupacaoleitos(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    tipo_de_leito = models.CharField(max_length=-1, blank=True, null=True)
    sus_suspeitos = models.IntegerField(blank=True, null=True)
    sus_confirmados = models.IntegerField(blank=True, null=True)
    particular_suspeitos = models.IntegerField(blank=True, null=True)
    particular_confirmados = models.IntegerField(blank=True, null=True)
    data_boletim = models.DateField(blank=True, null=True)
    insert_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SESA_base_ocupacaoLeitos'


class SesaTimeBr(models.Model):
    cases = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SESA_time_Br'


class SesaTimePr(models.Model):
    cases = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SESA_time_PR'


class SesaTimeLeitosexclusivos(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    leitos = models.CharField(max_length=-1, blank=True, null=True)
    uti_adulto_exist = models.IntegerField(db_column='uti adulto exist', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    uti_adulto_ocup = models.IntegerField(db_column='uti adulto ocup', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    uti_adulto_tx_ocup = models.FloatField(db_column='uti adulto tx ocup', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    enf_adulto_exist = models.IntegerField(db_column='enf adulto exist', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    enf_adulto_ocup = models.IntegerField(db_column='enf adulto ocup', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    enf_adulto_tx_ocup = models.FloatField(db_column='enf adulto tx ocup', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    uti_infantil_exist = models.IntegerField(db_column='uti infantil exist', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    uti_infantil_ocup = models.IntegerField(db_column='uti infantil ocup', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    uti_infantil_tx_ocup = models.FloatField(db_column='uti infantil tx ocup', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    enf_infantil_exist = models.FloatField(db_column='enf infantil exist', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    enf_infantil_ocup = models.IntegerField(db_column='enf infantil ocup', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    enf_infantil_tx_ocup = models.FloatField(db_column='enf infantil tx ocup', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    data_boletim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SESA_time_leitosExclusivos'


class SesaTimeMundo(models.Model):
    cases = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SESA_time_mundo'


class SesaTimeOcupacaoleitos(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    tipo_de_leito = models.CharField(max_length=-1, blank=True, null=True)
    sus_suspeitos = models.IntegerField(blank=True, null=True)
    sus_confirmados = models.IntegerField(blank=True, null=True)
    particular_suspeitos = models.IntegerField(blank=True, null=True)
    particular_confirmados = models.IntegerField(blank=True, null=True)
    data_boletim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SESA_time_ocupacaoLeitos'


class ShBaseBairrocontagio(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    bairro = models.TextField(db_column='Bairro', blank=True, null=True)  # Field name made lowercase.
    latitude = models.TextField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    longitude = models.TextField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    n·mero = models.BigIntegerField(db_column='N·mero', blank=True, null=True)  # Field name made lowercase.
    insert_date = models.DateTimeField(blank=True, null=True)
    data_boletim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SH_base_bairroContagio'


class ShBaseBairromoradia(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    bairro = models.TextField(db_column='Bairro', blank=True, null=True)  # Field name made lowercase.
    n·mero = models.BigIntegerField(db_column='N·mero', blank=True, null=True)  # Field name made lowercase.
    insert_date = models.DateTimeField(blank=True, null=True)
    data_boletim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SH_base_bairroMoradia'


class ShBaseComorbidades(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    comorbidades_em_¾bitos = models.TextField(db_column='Comorbidades em ¾bitos', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    n·mero = models.BigIntegerField(db_column='N·mero', blank=True, null=True)  # Field name made lowercase.
    insert_date = models.DateTimeField(blank=True, null=True)
    data_boletim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SH_base_comorbidades'


class ShBaseDadosgerais(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    data_boletim = models.TextField(db_column='Data_boletim', blank=True, null=True)  # Field name made lowercase.
    confirmados = models.BigIntegerField(blank=True, null=True)
    ativos = models.BigIntegerField(blank=True, null=True)
    obitos = models.BigIntegerField(blank=True, null=True)
    investigacao = models.BigIntegerField(blank=True, null=True)
    recuperados = models.BigIntegerField(blank=True, null=True)
    descartados = models.TextField(blank=True, null=True)
    internados_enf = models.BigIntegerField(blank=True, null=True)
    internados_uti = models.BigIntegerField(blank=True, null=True)
    insert_date = models.DateTimeField(blank=True, null=True)
    data_boletim_0 = models.DateField(db_column='data_boletim', blank=True, null=True)  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'SH_base_dadosGerais'


class ShBaseDadosgeraisH(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    data_boletim = models.TextField(db_column='Data_boletim', blank=True, null=True)  # Field name made lowercase.
    confirmados = models.BigIntegerField(blank=True, null=True)
    ativos = models.BigIntegerField(blank=True, null=True)
    obitos = models.BigIntegerField(blank=True, null=True)
    investigacao = models.BigIntegerField(blank=True, null=True)
    recuperados = models.BigIntegerField(blank=True, null=True)
    descartados = models.TextField(blank=True, null=True)
    internados_enf = models.BigIntegerField(blank=True, null=True)
    internados_uti = models.BigIntegerField(blank=True, null=True)
    insert_date = models.DateTimeField(blank=True, null=True)
    data_boletim_0 = models.DateField(db_column='data_boletim', blank=True, null=True)  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'SH_base_dadosGerais_H'


class ShBaseEventos(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    data = models.TextField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    fechamento_comÚrcio = models.TextField(db_column='Fechamento ComÚrcio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechamento_praia = models.TextField(db_column='Fechamento Praia', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fechamento_eventos = models.TextField(db_column='Fechamento Eventos', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insert_date = models.DateTimeField(blank=True, null=True)
    data_boletim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SH_base_eventos'


class ShBaseExames(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    exames_rt_pcr_realizados = models.BigIntegerField(db_column='Exames RT-PCR realizados', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exames_rt_pcr_negativos = models.BigIntegerField(db_column='Exames RT-PCR negativos', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exames_rt_pcr_investigaþÒo = models.BigIntegerField(db_column='Exames RT-PCR investigaþÒo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exames_rt_pcr_lacen_ibmp_dia = models.BigIntegerField(db_column='Exames RT-PCR lacen ibmp dia', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    testes_rßpidos = models.BigIntegerField(db_column='Testes rßpidos', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insert_date = models.DateTimeField(blank=True, null=True)
    data_boletim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SH_base_exames'


class ShBaseFaixaetaria(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    idades = models.TextField(blank=True, null=True)
    confirmados_masculino = models.BigIntegerField(db_column='confirmados masculino', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    confirmados_feminino = models.BigIntegerField(db_column='confirmados feminino', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ¾bitos_masculino = models.BigIntegerField(db_column='¾bitos masculino', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ¾bitos_feminino = models.BigIntegerField(db_column='¾bitos feminino', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    confirmados = models.BigIntegerField(blank=True, null=True)
    obitos = models.BigIntegerField(blank=True, null=True)
    insert_date = models.DateTimeField(blank=True, null=True)
    data_boletim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SH_base_faixaEtaria'


class ShBaseHistoricoleitos(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    data_boletim = models.TextField(db_column='Data_boletim', blank=True, null=True)  # Field name made lowercase.
    sus_enfermaria = models.FloatField(db_column='SUS_enfermaria', blank=True, null=True)  # Field name made lowercase.
    sus_uti = models.BigIntegerField(db_column='SUS_UTI', blank=True, null=True)  # Field name made lowercase.
    particular_enfermaria = models.BigIntegerField(blank=True, null=True)
    particular_uti = models.BigIntegerField(db_column='particular_UTI', blank=True, null=True)  # Field name made lowercase.
    insert_date = models.DateTimeField(blank=True, null=True)
    data_boletim_0 = models.DateField(db_column='data_boletim', blank=True, null=True)  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'SH_base_historicoLeitos'


class ShBaseIncidencia100K(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    local = models.TextField(db_column='Local', blank=True, null=True)  # Field name made lowercase.
    situaþÒo = models.TextField(db_column='SituaþÒo', blank=True, null=True)  # Field name made lowercase.
    incidÛncia_por_100_mil_habitantes = models.BigIntegerField(db_column='IncidÛncia por 100 mil habitantes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insert_date = models.DateTimeField(blank=True, null=True)
    data_boletim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SH_base_incidencia100k'


class ShBaseInternamentos(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    localidade = models.TextField(db_column='Localidade', blank=True, null=True)  # Field name made lowercase.
    internados_enfermaria = models.BigIntegerField(db_column='Internados enfermaria', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    internados_uti = models.BigIntegerField(db_column='Internados UTI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    leitos_disponÝveis = models.FloatField(db_column='Leitos disponÝveis', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suspeitos_em_isolamento_domiciliar = models.FloatField(db_column='Suspeitos em Isolamento Domiciliar', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insert_date = models.DateTimeField(blank=True, null=True)
    data_boletim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SH_base_internamentos'


class ShBaseMobilidade(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    parks = models.FloatField(blank=True, null=True)
    loc_trabalho = models.FloatField(db_column='loc trabalho', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    residencial = models.FloatField(blank=True, null=True)
    insert_date = models.DateTimeField(blank=True, null=True)
    data_boletim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SH_base_mobilidade'


class ShBaseOcupleitos(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    tipo_de_leito = models.TextField(db_column='Tipo de Leito', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sus_suspeitos = models.BigIntegerField(db_column='SUS suspeitos', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sus_confirmados = models.BigIntegerField(db_column='SUS confirmados', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    particular_suspeitos = models.BigIntegerField(db_column='Particular suspeitos', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    particular_confirmados = models.BigIntegerField(db_column='Particular confirmados', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insert_date = models.DateTimeField(blank=True, null=True)
    data_boletim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SH_base_ocupLeitos'


class ShBaseSexofaixaetaria(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    idade = models.BigIntegerField(db_column='Idade', blank=True, null=True)  # Field name made lowercase.
    confirmados_masculino = models.FloatField(db_column='Confirmados masculino', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    confirmados_feminino = models.FloatField(db_column='Confirmados feminino', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ¾bitos_masculino = models.FloatField(db_column='Ëbitos masculino', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ¾bitos_feminino = models.FloatField(db_column='Ëbitos feminino', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mÚdia_idade_confirmados = models.TextField(db_column='MÚdia idade confirmados', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mÚdia_idade_¾bitos = models.TextField(db_column='MÚdia idade ¾bitos', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insert_date = models.DateTimeField(blank=True, null=True)
    data_boletim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SH_base_sexoFaixaEtaria'


class ShBaseTransmissao(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    tipo = models.TextField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    n·mero = models.BigIntegerField(db_column='N·mero', blank=True, null=True)  # Field name made lowercase.
    insert_date = models.DateTimeField(blank=True, null=True)
    data_boletim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SH_base_transmissao'


class ShHistoricoGeral(models.Model):
    id = models.IntegerField(primary_key=True)
    confirmados = models.IntegerField()
    ativos = models.IntegerField(blank=True, null=True)
    obitos = models.IntegerField(blank=True, null=True)
    investigacao = models.IntegerField(blank=True, null=True)
    descartados = models.IntegerField(blank=True, null=True)
    recuperados = models.IntegerField(blank=True, null=True)
    internados_enf = models.IntegerField(blank=True, null=True)
    internados_uti = models.IntegerField(blank=True, null=True)
    data_boletim = models.DateField()
    insert_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'SH_historico_geral'


class WcotaBaseLeitos(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    uf = models.TextField(db_column='UF', blank=True, null=True)  # Field name made lowercase.
    leitosocupados = models.IntegerField(db_column='leitosOcupados', blank=True, null=True)  # Field name made lowercase.
    quantidadeleitos = models.IntegerField(db_column='quantidadeLeitos', blank=True, null=True)  # Field name made lowercase.
    totalocupacao = models.FloatField(db_column='totalOcupacao', blank=True, null=True)  # Field name made lowercase.
    ultimaatualizacao = models.TextField(db_column='ultimaAtualizacao', blank=True, null=True)  # Field name made lowercase.
    insert_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WCota_base_leitos'


class WcotaBaseNacional(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    epi_week = models.BigIntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    ibgeid = models.BigIntegerField(db_column='ibgeID', blank=True, null=True)  # Field name made lowercase.
    cod_regiaodesaude = models.FloatField(db_column='cod_RegiaoDeSaude', blank=True, null=True)  # Field name made lowercase.
    name_regiaodesaude = models.TextField(db_column='name_RegiaoDeSaude', blank=True, null=True)  # Field name made lowercase.
    newdeaths = models.BigIntegerField(db_column='newDeaths', blank=True, null=True)  # Field name made lowercase.
    deaths = models.BigIntegerField(blank=True, null=True)
    newcases = models.BigIntegerField(db_column='newCases', blank=True, null=True)  # Field name made lowercase.
    totalcases = models.BigIntegerField(db_column='totalCases', blank=True, null=True)  # Field name made lowercase.
    deaths_per_100k_inhabitants = models.FloatField(blank=True, null=True)
    totalcases_per_100k_inhabitants = models.FloatField(db_column='totalCases_per_100k_inhabitants', blank=True, null=True)  # Field name made lowercase.
    deaths_by_totalcases = models.FloatField(db_column='deaths_by_totalCases', blank=True, null=True)  # Field name made lowercase.
    field_source = models.TextField(db_column='_source', blank=True, null=True)  # Field renamed because it started with '_'.
    last_info_date = models.TextField(blank=True, null=True)
    insert_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WCota_base_nacional'


class WcotaBaseSuspeitos(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    estado = models.TextField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    casos = models.IntegerField(db_column='Casos', blank=True, null=True)  # Field name made lowercase.
    suspeitos = models.IntegerField(db_column='Suspeitos', blank=True, null=True)  # Field name made lowercase.
    recuperados = models.IntegerField(db_column='Recuperados', blank=True, null=True)  # Field name made lowercase.
    obitos = models.IntegerField(db_column='Obitos', blank=True, null=True)  # Field name made lowercase.
    testes = models.IntegerField(db_column='Testes', blank=True, null=True)  # Field name made lowercase.
    novoscasos = models.IntegerField(db_column='novosCasos', blank=True, null=True)  # Field name made lowercase.
    novosobitos = models.IntegerField(db_column='novosObitos', blank=True, null=True)  # Field name made lowercase.
    insert_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WCota_base_suspeitos'


class WcotaNacionalTest(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    epi_week = models.BigIntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    ibgeid = models.BigIntegerField(db_column='ibgeID', blank=True, null=True)  # Field name made lowercase.
    cod_regiaodesaude = models.FloatField(db_column='cod_RegiaoDeSaude', blank=True, null=True)  # Field name made lowercase.
    name_regiaodesaude = models.TextField(db_column='name_RegiaoDeSaude', blank=True, null=True)  # Field name made lowercase.
    newdeaths = models.BigIntegerField(db_column='newDeaths', blank=True, null=True)  # Field name made lowercase.
    deaths = models.BigIntegerField(blank=True, null=True)
    newcases = models.BigIntegerField(db_column='newCases', blank=True, null=True)  # Field name made lowercase.
    totalcases = models.BigIntegerField(db_column='totalCases', blank=True, null=True)  # Field name made lowercase.
    deaths_per_100k_inhabitants = models.FloatField(blank=True, null=True)
    totalcases_per_100k_inhabitants = models.FloatField(db_column='totalCases_per_100k_inhabitants', blank=True, null=True)  # Field name made lowercase.
    deaths_by_totalcases = models.FloatField(db_column='deaths_by_totalCases', blank=True, null=True)  # Field name made lowercase.
    field_source = models.TextField(db_column='_source', blank=True, null=True)  # Field renamed because it started with '_'.
    insert_date = models.DateTimeField(blank=True, null=True)
    comercio_aberto = models.BooleanField(blank=True, null=True)
    nivel_comercio = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WCota_nacional_test'


class Estado(models.Model):
    codigouf = models.IntegerField()
    nome = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    regiao = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'estado'


class Municipio(models.Model):
    codigo = models.IntegerField()
    nome = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'municipio'


class Regiao(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'regiao'
