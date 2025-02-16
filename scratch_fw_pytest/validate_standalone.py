def validate1():
    assert 2+3 ==5

def get_odds(test_list):
    odds = lambda x:x%2==1
    print(list(map(odds,test_list)))

get_odds([54,67,67,435,342,2])
validate1()