mylist = []
all_workers = []
this_year = 0

def input_values():
    inp_num = int(input())
    for i in range(inp_num):
        el = {}
        inp_string = input()
        lst1 = inp_string.split(" ")
        try:
            year = int(lst1[1])
        except ValueError:
            print("-1")
            exit("-1")
        el[lst1[0]] = year
        mylist.append(el)
    # print(mylist)



# mylist = [
#     {'Ivan': 1},
#     {'Anton': 1},
#     {'Victor': 2},
#     {'Anton': 3},
#     {'Ivan': 5},
#     {'Denis': 10},
#     {'Victor': 11},
#     {'Anton': 11},
#     {'Ivan': 12},
# ]


def if_worker_in_list(workers, name):
    for el in workers:
        if el.name == name:
            return el
    return False


def experience_update():
    # print('exper update')
    for wrkr in all_workers:
        # print(f'this_year : {this_year}')
        # print(f'wrkr.name {wrkr.name}  wrker_active {wrkr.is_active}  wrkr_start: {wrkr.year_start}')
        if wrkr.is_active:
            wrkr.experience = this_year - wrkr.year_start
            # print(f"{wrkr.name}   {wrkr.experience} updated")


def get_best_and_rest():
    best_name = ""
    best_exprer = 0
    for wrkr in all_workers:
        if wrkr.is_active and wrkr.experience >= best_exprer:
            best_exprer = wrkr.experience
            best_name = wrkr.name
    rest_summ_exper = 0
    for wrkr in all_workers:
        if wrkr.name != best_name and wrkr.is_active:
            rest_summ_exper += wrkr.experience
    return (best_name, rest_summ_exper)


class Worker:
    def __init__(self, name, year_start=this_year):
        self.name = name
        self.year_start = year_start
        self.experience = 0
        self.is_active = True


def main():
    global this_year

    input_values()
    # print(mylist)
    for el in mylist:
        # print('---------------')
        for name, v in el.items():
            this_year = v
            # print(f"this_year: {this_year}")
            the_worker = if_worker_in_list(all_workers, name)
            if the_worker:
                worker_status = the_worker.is_active
                if worker_status == True:
                    the_worker.is_active = False
                    the_worker.experience = this_year - the_worker.year_start
                    # print(f'worker_exist {name} status passive  exper {the_worker.experience}')
                if worker_status == False:
                    # print(f'worker_exist {name} status non_active')
                    the_worker.is_active = True
                    the_worker.year_start = this_year
                    # print(f'worker_exist {name} status active  exper {the_worker.experience}')

            else:
                worker = Worker(name, this_year)
                all_workers.append(worker)
                # print(f'worker_new {worker.name} status active  exper {worker.experience}')

            experience_update()

            best_name, rest_exper = get_best_and_rest()
            print(best_name, rest_exper)


if __name__ == "__main__":
    main()

