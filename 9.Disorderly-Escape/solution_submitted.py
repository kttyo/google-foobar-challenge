def solution(w, h, s):
    import math

    all_transformations = math.factorial(w) * math.factorial(h)

    def get_cycle_pattern(cell_num):
        master_list = []
        limit = cell_num

        def cycle_generation(inherited_list, val):
            given_list = []
            if len(inherited_list) > 0:
                for i in inherited_list:
                    given_list.append(i)
            
            row_sum = 0
            if len(inherited_list) > 0:
                for i in given_list:
                    row_sum += i

            if row_sum == limit:
                master_list.append(given_list)
            elif row_sum < limit:
                for i in range(1,val + 1):
                    new_list = []
                    for j in given_list:
                        new_list.append(j)
                    new_list.append(i)

                    cycle_generation(new_list,i)
            
        cycle_generation([],cell_num)

        return master_list

    def get_merged_details(hori,vert):

        merged_details = {'cycle_num':0, 'distinct_cycles':0, 'position_pattern':0}

        def get_gcd(a,b):
                r = a % b
                while r != 0:
                    a, b = b, r
                    r = a % b
                return b

        def get_distinct_cycle_num(cycles):
            distinct_cycle_num = 1
            for i in cycles:
                if i != 1:
                    distinct_cycle_num *= math.factorial(i) / i

            return distinct_cycle_num
        
        def get_cycle_detail(pattern):
            cycle_detail = {}
            for i in pattern:
                if i not in cycle_detail:
                    cycle_detail[i] = 1
                else:
                    cycle_detail[i] += 1
            return cycle_detail

        def get_position_pattern_num(cycle_detail,cell_num):
            key_list = list(cycle_detail.keys())

            numerator = math.factorial(cell_num)
            denominator = 1
            for i in key_list:
                if i != 1:
                    denominator *= math.factorial(i) ** cycle_detail[i]
                    denominator *= math.factorial(cycle_detail[i])

            if 1 in key_list:
                denominator *= math.factorial(cycle_detail[1])

            position_pattern_num = numerator / denominator

            return position_pattern_num

        for i in hori:
            for j in vert:
                merged_details['cycle_num'] += get_gcd(i,j)

        distinct_cycle_num_hori = get_distinct_cycle_num(hori)
        distinct_cycle_num_vert = get_distinct_cycle_num(vert)

        cycle_detail_hori = get_cycle_detail(hori)
        cycle_detail_vert = get_cycle_detail(vert)

        merged_details['distinct_cycles'] = distinct_cycle_num_hori * distinct_cycle_num_vert
        
        position_pattern_num_hori = get_position_pattern_num(cycle_detail_hori,w)
        position_pattern_num_vert = get_position_pattern_num(cycle_detail_vert,h)

        merged_details['position_pattern'] = position_pattern_num_hori * position_pattern_num_vert

        return merged_details

    cycle_pattern_hori = get_cycle_pattern(w)
    cycle_pattern_vert = get_cycle_pattern(h)

    merged_cycle_details = []
    for hori_cycle in cycle_pattern_hori:
        for vert_cycle in cycle_pattern_vert:
            merged_cycle_details.append(get_merged_details(hori_cycle, vert_cycle))

    fixed_grids = 0
    for i in merged_cycle_details:
        fixed_grids += i['position_pattern'] * i['distinct_cycles'] * (s ** i['cycle_num'])

    print(fixed_grids/all_transformations)

solution(2, 2, 2)