# Cinema Room

You want to go to the cinema to see the next Marvel studio movie as soon as possible to avoid annoying spoilers. For this purpose, the movie theater page shows you the theater list with the availability of seats. The movie theater will always be represented by a list with `n` lists, each of them with `n` strings.

Each string can have the values `'O'` indicating that the seat is available or `'X'` indicating that it is occupied.

The following is an example for `n = 5`. Note: the value of `n` should not be important.

```
room = [
    ["X", "X", "X", "O", "O", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "O", "O", "O", "X", "O", "X"],
    ["X", "O", "X", "O", "X", "X", "O", "X", "O", "X"],
    ["X", "X", "X", "X", "O", "O", "O", "X", "X", "X"],
    ["O", "O", "X", "O", "O", "O", "X", "X", "X", "X"],
]
```

## Tasks

### Available seats

Write the function `available_seats(room)` that indicates if the theater room has available seats. The function should return `True` if the theater has available seats and `False` otherwise.

```
> available_seats(room)
True
```

### Available seat

Write the function `is_available_seat(row, column, room)` that receives a theater room. The function should return `True` if the seat of the entered row and column is available and `False` otherwise. If you enter a row or column that does not exist it should also return `False`.

```
> is_available_seat(2, 4, room)
False
> is_available_seat(10, 4, room)
False
> is_available_seat(0, 3, room)
True
```

### Available percentage

Write the function `available_percentage(room)` that indicates the percentage availability of a movie theater.

```
> available_percentage(room)
36.0
```

### Enough space

You want to go with your friends to see the movie and you all want to see the movie in the same theater. Due to the great success in the pre-sale it is possible that there are not many seats left.

Write the function `is_there_enough_space(m, room)` which receives an integer `m` with the number of friends (including you) who want to go to the movie theater. The function should return `True` if there is enough room for everyone to see the movie or `False` otherwise.

```
> is_there_enough_space(20, room)
False
> is_there_enough_space(5, room)
True
```
