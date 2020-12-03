# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Empresa(models.Model):
    codempresa = models.CharField(db_column='CODEMPRESA', primary_key=True, max_length=3)  # Field name made lowercase.
    id_bd = models.IntegerField(db_column='ID_BD', blank=True, null=True)  # Field name made lowercase.
    nit = models.CharField(db_column='NIT', max_length=13)  # Field name made lowercase.
    digverif = models.IntegerField(db_column='DIGVERIF')  # Field name made lowercase.
    codregimp = models.CharField(db_column='CODREGIMP', max_length=3)  # Field name made lowercase.
    cuadrado = models.CharField(db_column='CUADRADO', max_length=5, blank=True, null=True)  # Field name made lowercase.
    autoretenedor = models.CharField(db_column='AUTORETENEDOR', max_length=5, blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.CharField(db_column='RAZONSOCIAL', max_length=250, blank=True, null=True)  # Field name made lowercase.
    predeterminado = models.CharField(db_column='PREDETERMINADO', max_length=5, blank=True, null=True)  # Field name made lowercase.
    causacion = models.CharField(db_column='CAUSACION', max_length=5, blank=True, null=True)  # Field name made lowercase.
    agenteretenedor = models.CharField(db_column='AGENTERETENEDOR', max_length=5, blank=True, null=True)  # Field name made lowercase.
    representantelegal = models.CharField(db_column='REPRESENTANTELEGAL', max_length=80, blank=True, null=True)  # Field name made lowercase.
    cedulareplegal = models.CharField(db_column='CEDULAREPLEGAL', max_length=12, blank=True, null=True)  # Field name made lowercase.
    nomcargoreplegal = models.CharField(db_column='NOMCARGOREPLEGAL', max_length=80, blank=True, null=True)  # Field name made lowercase.
    contador = models.CharField(db_column='CONTADOR', max_length=80, blank=True, null=True)  # Field name made lowercase.
    tarjetap_contador = models.CharField(db_column='TARJETAP_CONTADOR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    nomcargocontador = models.CharField(db_column='NOMCARGOCONTADOR', max_length=80, blank=True, null=True)  # Field name made lowercase.
    revisorfiscal = models.CharField(db_column='REVISORFISCAL', max_length=80, blank=True, null=True)  # Field name made lowercase.
    tarjetap_revisor = models.CharField(db_column='TARJETAP_REVISOR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    nomcargorevfiscal = models.CharField(db_column='NOMCARGOREVFISCAL', max_length=80, blank=True, null=True)  # Field name made lowercase.
    jefeppto = models.CharField(db_column='JEFEPPTO', max_length=80, blank=True, null=True)  # Field name made lowercase.
    nomcargojefeppto = models.CharField(db_column='NOMCARGOJEFEPPTO', max_length=80, blank=True, null=True)  # Field name made lowercase.
    idjefeppto = models.CharField(db_column='IDJEFEPPTO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    conseccarne = models.IntegerField(db_column='CONSECCARNE', blank=True, null=True)  # Field name made lowercase.
    consecbeeper = models.CharField(db_column='CONSECBEEPER', max_length=16, blank=True, null=True)  # Field name made lowercase.
    es_oficial = models.CharField(db_column='ES_OFICIAL', max_length=5, blank=True, null=True)  # Field name made lowercase.
    pkeyreferencia = models.CharField(db_column='PKEYREFERENCIA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    calcostprolin = models.CharField(db_column='CALCOSTPROLIN', max_length=5, blank=True, null=True)  # Field name made lowercase.
    coddian = models.IntegerField(db_column='CODDIAN', blank=True, null=True)  # Field name made lowercase.
    autoretenedorica = models.CharField(db_column='AUTORETENEDORICA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    retenedorica = models.CharField(db_column='RETENEDORICA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    retenedorestampilla = models.CharField(db_column='RETENEDORESTAMPILLA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    retenedortimbre = models.CharField(db_column='RETENEDORTIMBRE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    baserta = models.CharField(db_column='BASERTA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    baseica = models.CharField(db_column='BASEICA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    baseestampilla = models.CharField(db_column='BASEESTAMPILLA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    basetimbre = models.CharField(db_column='BASETIMBRE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    grancontribuyente = models.CharField(db_column='GRANCONTRIBUYENTE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    basereteiva = models.CharField(db_column='BASERETEIVA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    doccontenppto = models.CharField(db_column='DOCCONTENPPTO', max_length=5, blank=True, null=True)  # Field name made lowercase.
    codelemento = models.CharField(db_column='CODELEMENTO', max_length=3, blank=True, null=True)  # Field name made lowercase.
    basereteivaesp = models.CharField(db_column='BASERETEIVAESP', max_length=8, blank=True, null=True)  # Field name made lowercase.
    contapptoauto = models.CharField(db_column='CONTAPPTOAUTO', max_length=5, blank=True, null=True)  # Field name made lowercase.
    hacecdpccr = models.CharField(db_column='HACECDPCCR', max_length=5, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='DIRECCION', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=80, blank=True, null=True)  # Field name made lowercase.
    codadmondian = models.CharField(db_column='CODADMONDIAN', max_length=6, blank=True, null=True)  # Field name made lowercase.
    codmunicipio = models.CharField(db_column='CODMUNICIPIO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    mod1 = models.CharField(db_column='MOD1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mod2 = models.CharField(db_column='MOD2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mod3 = models.CharField(db_column='MOD3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mod4 = models.CharField(db_column='MOD4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mod5 = models.CharField(db_column='MOD5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mod6 = models.CharField(db_column='MOD6', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mod7 = models.CharField(db_column='MOD7', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mod8 = models.CharField(db_column='MOD8', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mod9 = models.CharField(db_column='MOD9', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mod10 = models.CharField(db_column='MOD10', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mod11 = models.CharField(db_column='MOD11', max_length=20, blank=True, null=True)  # Field name made lowercase.
    codpais = models.CharField(db_column='CODPAIS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    codprovincia = models.CharField(db_column='CODPROVINCIA', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pptoafectaconta = models.CharField(db_column='PPTOAFECTACONTA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    rutalogo = models.CharField(db_column='RUTALOGO', max_length=120, blank=True, null=True)  # Field name made lowercase.
    usa_rubro_ppto = models.CharField(db_column='USA_RUBRO_PPTO', max_length=5, blank=True, null=True)  # Field name made lowercase.
    contabilizar_inv = models.CharField(db_column='CONTABILIZAR_INV', max_length=5, blank=True, null=True)  # Field name made lowercase.
    codactividaddian = models.CharField(db_column='CODACTIVIDADDIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.
    autoretenedorcree = models.CharField(db_column='AUTORETENEDORCREE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    retenedorcree = models.CharField(db_column='RETENEDORCREE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ley1429 = models.CharField(db_column='LEY1429', max_length=5, blank=True, null=True)  # Field name made lowercase.
    codtarifacree = models.CharField(db_column='CODTARIFACREE', max_length=8, blank=True, null=True)  # Field name made lowercase.
    contatradis = models.CharField(db_column='CONTATRADIS', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ajuprovnom = models.CharField(db_column='AJUPROVNOM', max_length=5, blank=True, null=True)  # Field name made lowercase.
    condessucdes = models.CharField(db_column='CONDESSUCDES', max_length=5)  # Field name made lowercase.
    manrcl = models.CharField(db_column='MANRCL', max_length=5)  # Field name made lowercase.
    manniif = models.CharField(db_column='MANNIIF', max_length=5)  # Field name made lowercase.
    nivel_costosabc = models.CharField(db_column='NIVEL_COSTOSABC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    diasmaxrecos = models.IntegerField(db_column='DIASMAXRECOS', blank=True, null=True)  # Field name made lowercase.
    condesproy = models.CharField(db_column='CONDESPROY', max_length=5)  # Field name made lowercase.
    condescencos = models.CharField(db_column='CONDESCENCOS', max_length=5)  # Field name made lowercase.
    cieaconproy = models.CharField(db_column='CIEACONPROY', max_length=5)  # Field name made lowercase.
    cieaconcc = models.CharField(db_column='CIEACONCC', max_length=5)  # Field name made lowercase.
    pptosalaprdef = models.CharField(db_column='PPTOSALAPRDEF', max_length=5)  # Field name made lowercase.
    pptosaldoccdp = models.CharField(db_column='PPTOSALDOCCDP', max_length=5)  # Field name made lowercase.
    mansia = models.CharField(db_column='MANSIA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cargabcmod = models.CharField(db_column='CARGABCMOD', max_length=5)  # Field name made lowercase.
    contabilizar_nom = models.CharField(db_column='CONTABILIZAR_NOM', max_length=5)  # Field name made lowercase.
    diasmaxliqsegsocpar = models.IntegerField(db_column='DIASMAXLIQSEGSOCPAR', blank=True, null=True)  # Field name made lowercase.
    diasmaxliqpro = models.IntegerField(db_column='DIASMAXLIQPRO', blank=True, null=True)  # Field name made lowercase.
    provisionar = models.CharField(db_column='PROVISIONAR', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa'
