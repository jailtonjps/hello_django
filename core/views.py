from django.shortcuts import render, HttpResponse

# Create your views here.

#def calculo(request, num1,num2):

#def subtr(request, num1, num2):
    #return HttpResponse('divisão: {}'.format(num1/num2))
    #return HttpResponse('multiplição: {}\n'.format(num1*num2))
    #return HttpResponse('subtração: {}'.format(num1-num2))
    #return HttpResponse('soma: {}'.format(num1+num2))

def hello(request, nome,idade):
    return HttpResponse('<h1>Hello {} de {} anos<h1>'.format(nome, idade))

