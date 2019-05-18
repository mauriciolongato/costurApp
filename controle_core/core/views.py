from django.shortcuts import render
from django.http import HttpResponse
from core.models import objects
import datetime


# Create your views here.
def tracking(request):

	pistola = request.GET.get('pistola')
	cod_barras = request.GET.get('cod_barras')
	data_criacao = request.GET.get('data_criacao')
	# exemplo da data '2019/03/01 12:27:03.000'
	data_criacao_datetime = datetime.datetime.strptime(data_criacao, '%Y/%m/%d %H:%M:%S.%f')	

	objects.LogTrabalho.objects.create(
	  	pistola=pistola,
	  	cod_barras=cod_barras,
	  	data_criacao=data_criacao_datetime,
	  	)

	mensagem = "{} | {} | {}".format(pistola, cod_barras, data_criacao_datetime)
	
	return HttpResponse(mensagem)
