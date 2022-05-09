from django.shortcuts import render


def board(request):
    return render(request, 'free_talk/board.html')
