from django.http import HttpResponse
from . import gamelogic

def home(request):
    board = request.GET.get('board', '')
    if (not gamelogic.is_playable_by_o(board) or
        not gamelogic.board_is_valid(board)
    ):
        return HttpResponse('Board invalid', status=400)
    return HttpResponse(gamelogic.get_best_move(board),
                        content_type='text/plain')

def selftest(request):
    return HttpResponse('200 YAY!')
