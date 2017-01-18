from django.http import HttpResponse
from . import gamelogic


def home(request):
    board = request.GET.get('board', '')
    if (
            gamelogic.board_is_valid(board) and
            gamelogic.is_playable_by_o(board) and
            gamelogic.get_shallow_value(board) is None
    ):
        return HttpResponse(gamelogic.get_best_move(board),
                            content_type='text/plain')
    else:
        return HttpResponse('Board invalid', status=400)
