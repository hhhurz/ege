# Модули и библиотеки

# Импорт всей библиотеки
import math

# Импорт всей библиотеки через псевдоним
import math as m

# Имрпорт одной команды
from math import floor

# Имрпорт одной команды через псевдоним
from math import floor as f

# Импорт нескольких команд
from math import log2, log10

# Импорт нескольких команд через псевдоним
from math import log2 as l2, log10 as l10

# Импорт всех команд
from math import *

num = 10.5
print(math.ceil(num))  # округление в большую сторону
print(floor(num))  # округление в меньшую сторону
print(log2(16))
print(log10(100))
