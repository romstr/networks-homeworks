station_a = "00011011"
station_b = "00101110"
station_c = "01011100"
station_d = "01000010"

signal = [-1, 3, -3, 1, -1, -1, -1, -1]


def number(i):
    return ord(i) - ord('0')


def zero_to_negative(i):
    if i == 0:
        return -1
    else:
        return i


def one(station):
    return list(map(lambda i: zero_to_negative(number(i)), station))


def zero(station):
    return list(map(lambda i: -zero_to_negative(number(i)), station))


def sum_stations(stations):
    result = [0] * 8
    for station in stations.keys():
        for i in range(0, 8):
            if (stations.get(station)) == 1:
                result[i] += one(station)[i]
            else:
                result[i] += zero(station)[i]
    return result


def find_bit(station, signal):
    result = 0
    for i in range(0, 8):
        result += one(station)[i] * signal[i]
    return result / 8


for station in [station_a, station_b, station_c, station_d]:
    print "Station: {0}".format(station)
    print "One: {0}".format(one(station))
    print "Zero: {0}".format(zero(station))
    print

print "Checking examples from the book:"
print sum_stations({station_c: 1})
print sum_stations({station_b: 1, station_c: 1})
print sum_stations({station_a: 1, station_b: 0})
print sum_stations({station_a: 1, station_b: 0, station_c: 1})
print sum_stations({station_a: 1, station_b: 1, station_c: 1, station_d: 1})
print sum_stations({station_a: 1, station_b: 1, station_c: 0, station_d: 1})

print
print "Solution:"
print "A -> {0}".format(find_bit(station_a, signal))
print "B -> {0}".format(find_bit(station_b, signal))
print "C -> {0}".format(find_bit(station_c, signal))
print "D -> {0}".format(find_bit(station_d, signal))

print
print "Check:"
print "Original signal:\n\t{0}".format(signal)
print "!B + C + D =\n\t{0}".format(sum_stations({station_b: 0, station_c: 1, station_d: 1}))






