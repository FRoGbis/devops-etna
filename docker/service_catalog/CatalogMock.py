class CatalogMock:
    a = [
            {
                'roomId': 0,
                'address': '1 rue a',
                'category': 'Simple',
                'price': '5.50'
            },
            {
                'roomId': 1,
                'address': '2 rue b',
                'category': 'simple',
                'price': '780.21'
            }
        ]
    
    def catalog(self):
        return self.a
        
