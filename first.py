from typing import TypedDict
from typing import Union
from typing import Optional

class Movie(TypedDict):
    name: str
    year: int

movie1 = Movie(name="vishwaroopam" , year = 2016)
movie2 = Movie(name = 90 , year = "")
print(movie1['name'])

def square(x : List[int]) -> int:
    def convert_to_int(num) -> int:
        return int(num)
    
    list = [convert_to_int(x)] * 5
    sum = 0
    for num in list:
        sum+=num

    return sum

print(square(5.909090))


#union , Optional , Any

def computeAns(x : Union[int, float] , y : Union[int, float]) -> float:
    return x*x + y*y
print(computeAns(10 , 0.88))

def computeAns1(x : Optional[int] , y : Optional[int]) -> int:
    return x*x + y*y

print(computeAns1(10.099 , 0.88))


cube = lambda x : x*x*x

print(cube(10))

square = [1,2,3,4]

list1 = list(map(lambda x : x * x, square))
print(list1)

list2 = [ x * x for x in square]

print(list2)


