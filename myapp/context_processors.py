from datetime import datetime


def add_year_to_context(request):
    return {
        'year': datetime.now().year
    }
