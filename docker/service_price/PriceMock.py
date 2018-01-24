class PriceMock:
    def price(self, request):
        if 'token' not in request or 'roomId' not in request or 'categoryId' not in request:
            return None
        else:
            return {'price': 789}
