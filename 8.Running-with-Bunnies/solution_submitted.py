def solution(times, times_limit):

    num_nodes = len(times)
    num_bunnies = num_nodes - 2
    time = times_limit
    bunnies_to_pick_up = []
    edges = []


    def get_possible_routes():
        arrays = []
        def search_order(array, nodes):
            for node in nodes:

                new_array = []
                new_nodes = []
                for i in array:
                    new_array.append(i)

                for i in nodes:
                    new_nodes.append(i)

                new_array.append(node)            
                new_nodes.pop(new_nodes.index(node))
                            
                if node == num_nodes - 1:
                    arrays.append(new_array)

                else:
                    search_order(new_array, new_nodes)
        
        search_order([0], range(1,num_nodes))
        return arrays

    def get_edges():
        for from_node in range(num_nodes):
            for to_node in range(num_nodes):
                if from_node != to_node:
                    edge = []
                    edge.append(from_node)
                    edge.append(to_node)
                    edge.append(times[from_node][to_node])
                    edges.append(edge)

    def bellman_ford(edges, num_v, start_point):
        dist = [float('inf') for i in range(num_v)]
        dist[start_point] = 0

        parent = [None for i in range(num_v)]
        parent[start_point] = -1

        loop_count = 0
        changed = True
        while changed:
            loop_count += 1
            if loop_count == num_v:
                return False
            changed = False
            for edge in edges:
                if dist[edge[1]] > dist[edge[0]] + edge[2]:
                    parent[edge[1]] = edge[0]
                    dist[edge[1]] = dist[edge[0]] + edge[2]
                    changed = True
        return [dist,parent]

    def get_from_to(dist_list, prnt_list, start_point):
        from_to = {}
        for i in range(len(prnt_list)):
            if prnt_list[i] != -1:
                via = [i]
                prnt = prnt_list[i]
                while prnt != -1:
                    via.append(prnt)
                    prnt = prnt_list[prnt]            
                from_to[i] = [via,dist_list[i]]
        return from_to 

    def route_calculation(route):
        bunnies = []
        total_cost = 0

        for i in range(len(route)-1):
            origin = route[i]
            destination = route[i + 1]
            step = from_to_list[origin][destination]
            via = step[0]
            cost = step[1]

            total_cost += cost

            for i in via:
                if i-1 not in bunnies and i != 0 and i != num_nodes - 1:
                    bunnies.append(i-1)

        if total_cost <= times_limit:
            valid_routes.append(bunnies)           

    get_edges()

    no_loop = True
    no_loop = bellman_ford(edges, num_nodes, 0)

    if not no_loop:
        bunnies_to_pick_up = range(num_bunnies)


    else:

        from_to_list = []

        for i in range(num_nodes):
            dist_prnt = bellman_ford(edges, num_nodes, i)        
            from_to = get_from_to(dist_prnt[0],dist_prnt[1],i)
            from_to_list.append(from_to)

        possible_routes = get_possible_routes()

        valid_routes = []
        for i in possible_routes:
            route_calculation(i)

        best_route = []
        for i in valid_routes:
            if len(i) > len(best_route):
                best_route = i
            elif len(i) == len(best_route) and sum(i) < sum(best_route):
                best_route = i
                
        bunnies_to_pick_up = best_route


    bunnies_to_pick_up.sort()
    return bunnies_to_pick_up