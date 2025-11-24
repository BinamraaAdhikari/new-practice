class Player():
    def __init__(self):
        self._health=100
        
    @property
    def player_health(self):
        return self._health
    
    @player_health.setter
    def player_health(self,value):
        if value>100:
            value=100
        if value<0:
            value=0
        self._health=value
        
        
p=Player()
p.player_health=3000
print(p.player_health)
