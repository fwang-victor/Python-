import  re
import pickle

def sanitize(time_string):
    regexp = re.compile(r'[^\d]')
    mins, secs = regexp.split(time_string)
    return float(mins + '.' + secs)

class Athlete(object):
    def __init__(self,name,dob=None,times=[]):
        self.name = name
        self.dob = dob
        self.times = times

    def top3(self):
        return sorted(set([sanitize(t) for t in self.times]))[:3]

    def add_time(self,time_str: str):
        return self.times.append(time_str)

    def add_times(self,time_lst: list):
        return self.times.extend(time_lst)

class AthleteList(list):
    def __init__(self,name,dob=None,times=[]):
        super().__init__()
        self.name = name
        self.dob = dob
        self.extend(times)

    def top3(self):
        return sorted(set([sanitize(t) for t in self]))[:3]


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            temp = data.strip().split(',')
        return AthleteList(temp.pop(0),temp.pop(0),temp)
    except Exception as e:
        print(e)
        return None

def put_to_store(file_list):
    all_athletes = {}
    for each_file in file_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle','wb') as athf:
            pickle.dump(all_athletes,athf)
    except Exception as e:
        print(e)
    return all_athletes

def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle','rb') as athf:
            all_athletes = pickle.load(athf)
    except Exception as e:
        print(e)
    return all_athletes


if __name__ == '__main__':
    the_files = ['mikey.txt','sara.txt','james.txt','julia.txt']
    data = get_from_store()
    for each_ath in data:
        print(data[each_ath])

