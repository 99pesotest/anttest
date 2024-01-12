
from PIL import Image, ImageDraw


def check_sum(num):
    if num < 10:
        return num
    return num % 10 + check_sum(num // 10)


def check_coord(coord):
    result = 0
    for i in coord:
        result += check_sum(i)
        if result > 25:
            return False
    return True


def find_100_points(coord, total, start):
    for x in range(10):
        for y in range(10):
            if x == 0 and y == 0 and coord[0] != start[0] and coord[1] != start[1] :
                left = (coord[0] - 1, coord[1])
                right = (coord[0], coord[1] - 1)

                if not check_coord(left) and not check_coord(right):
                    return False

            new = (coord[0] + x, coord[1] + y)

            if check_coord(new):
                total.add(new)
    return True


def get_all_points(start, max_dist):
    total = set()
    min_value = start[0]
    max_value = start[0] + max_dist

    for i in range(min_value, max_value, 10):
        for j in range(min_value, max_value, 10):

            if max_value - i < j - min_value:
                continue
            find_100_points((i, j), total, start)
    return total


def draw_points(points):
    new_img = Image.new('RGB', (2000, 2000), 'white')
    draw = ImageDraw.Draw(new_img)
    for coord in points:
        draw.point((coord[0], coord[1]), "green")
    new_img.show()


def get_max_coord_dist(start):

    for i in range(1000):
        if not check_coord((start[0], start[1] + i)):
            break
    return i


def main():

    start = (1000, 1000)
    max_coord_dist = get_max_coord_dist(start) + 1
    points = get_all_points(start, max_coord_dist)
    draw_points(points)
    print(len(points))


if __name__ == "__main__":
    main()
