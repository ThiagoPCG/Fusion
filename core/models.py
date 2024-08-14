from django.db import models

from stdimage.models import StdImageField

class Base(models.Model):

    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('data de atualização:', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True
class Servico(Base):

    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráficos'),
        ('lni-users', 'Usúarios'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Servico', max_length=100)
    descricao = models.CharField('descrição', max_length=200)
    icone = models.CharField('Icone', max_length=15, choices=ICONE_CHOICES)


    class Meta:
        verbose_name = 'Servico'
        verbose_name_plural = 'Servicos'

    def __str__(self):
        return self.servico
class Cargo(Base):
    cargo = models.CharField('cargo', max_length=100)

    class Meta: 
        verbose_name = 'cargo'
        verbose_name_plural = 'cargos'

    def __str__(self):
        return self.cargo
class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)

    cargo = models.ForeignKey(Cargo, verbose_name='cargo', on_delete=models.CASCADE)
    bio = models.TextField('bio', max_length=200)

    imagem = StdImageField('imagem', upload_to='equipe', variations={'thumb':{'width':480, 'height':480, 'crop':True}})                        
    facebook = models.CharField('facebook', max_length=100, default='#')
    xtwitter = models.CharField('xtwitter', max_length=100, default='#')
    Instagram = models.CharField('Instagram', max_length=100, default='#')
    
    class Meta:
        verbose_name= 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self): 
        return self.nome
# Create your models here.
