def solution(dimensions, your_position, trainer_position, distance):
    import math

    vertical_flips = []

    all_flips = [[0, 0]]

    shooting_angle_me = {}
    shooting_angle_trainer = {}
    aim_me = []
    aim_trainer = []

    def get_straight_up(room_height):
        num_rooms_up = distance // room_height
        if distance % room_height != 0:
            num_rooms_up += 1
        for i in range(num_rooms_up):
            all_flips.append([0,i+1])
            vertical_flips.append([0,i+1])

    def get_straight_down(room_height):
        num_rooms_down = distance // room_height
        if distance % room_height != 0:
            num_rooms_down += 1
        for i in range(num_rooms_down):
            all_flips.append([0,-i-1])
            vertical_flips.append([0,-i-1])

    def get_straight_right(room_width):
        num_rooms_right = distance // room_width
        if distance % room_width != 0:
            num_rooms_right += 1
        for i in range(num_rooms_right):
            all_flips.append([i+1,0])

    def get_straight_left(room_width):
        num_rooms_left = distance // room_width
        if distance % room_width != 0:
            num_rooms_left += 1
        for i in range(num_rooms_left):
            all_flips.append([-i-1,0])

    def get_right(room_width, room_height):
        for vert_flip in vertical_flips:
            side_flip = 1
            current_distance = 0
            while current_distance < distance:
                if side_flip == 1:
                    current_distance = (abs(vert_flip[1])-1) * room_height
                else: 
                    a_square = ((side_flip - 1) * room_width)**2
                    b_square = ((abs(vert_flip[1])-1) * room_height)**2
                    c_square = a_square + b_square
                    current_distance = math.sqrt(c_square)

                if current_distance >= distance:
                    break

                all_flips.append([side_flip, vert_flip[1]])
                side_flip += 1

    
    def get_left(room_width, room_height):
        for vert_flip in vertical_flips:
            side_flip = -1
            current_distance = 0
            while current_distance < distance:
                if side_flip == -1:
                    current_distance = (abs(vert_flip[1])-1) * room_height
                else: 
                    a_square = ((side_flip + 1) * room_width)**2
                    b_square = ((abs(vert_flip[1])-1) * room_height)**2
                    c_square = a_square + b_square
                    current_distance = math.sqrt(c_square)

                if current_distance >= distance:
                    break

                all_flips.append([side_flip, vert_flip[1]])
                side_flip -= 1
    
    def get_virtual_pos(actual_position, virtual_map):
        flipped_pos = [0,0]
        virtual_pos = [0,0]

        if virtual_map[0] == 0:
            flipped_pos[0] = actual_position[0]
        elif virtual_map[0] % 2 == 0:
            flipped_pos[0] = actual_position[0] + virtual_map[0] * dimensions[0]
        else:
            flipped_pos[0] = actual_position[0] + virtual_map[0] * dimensions[0] + (dimensions[0] - actual_position[0] * 2)

        if virtual_map[1] == 0:
            flipped_pos[1] = actual_position[1]
        elif virtual_map[1] % 2 == 0:
            flipped_pos[1] = actual_position[1] + virtual_map[1] * dimensions[1]
        else:
            flipped_pos[1] = actual_position[1] + virtual_map[1] * dimensions[1] + (dimensions[1] - actual_position[1] * 2)    

        virtual_pos[0] = flipped_pos[0] - your_position[0]
        virtual_pos[1] = flipped_pos[1] - your_position[1]

        return virtual_pos


    def get_shooting_detail(virtual_pos):
        shooting_detail = {
            'aim': None,
            'distance': None,
            'angle': None
        }

        shooting_detail['aim'] = virtual_pos

        if virtual_pos[0] == 0:
            shooting_detail['distance'] = abs(virtual_pos[1])
        elif virtual_pos[1] == 0:
            shooting_detail['distance'] = abs(virtual_pos[0])
        else:
            shooting_detail['distance'] = math.sqrt(abs(virtual_pos[0])**2 + abs(virtual_pos[1])**2)

        if virtual_pos[0] != 0 and virtual_pos[1] != 0: #not vertical or horizontal
            if virtual_pos[0] >= 1 and virtual_pos[1] >= 1:
                shooting_detail['angle'] = 'tr'+str(float(virtual_pos[0]) / float(virtual_pos[1]))
            elif virtual_pos[0] >= 1 and virtual_pos[1] <= -1:
                shooting_detail['angle'] = 'br'+str(float(virtual_pos[0]) / float(virtual_pos[1]))
            elif virtual_pos[0] <= -1 and virtual_pos[1] <= -1:
                shooting_detail['angle'] = 'bl'+str(float(virtual_pos[0]) / float(virtual_pos[1]))
            elif virtual_pos[0] <= -1 and virtual_pos[1] >= 1:
                shooting_detail['angle'] = 'tl'+str(float(virtual_pos[0]) / float(virtual_pos[1]))

        elif virtual_pos[0] != 0: #horizonal
            if virtual_pos[0] >= 1:
                shooting_detail['angle'] = 'right'
            if virtual_pos[0] <= -1:
                shooting_detail['angle'] = 'left'

        elif virtual_pos[1] != 0: #vertical
            if virtual_pos[1] <= -1:
                shooting_detail['angle'] = 'bottom'
            if virtual_pos[1] >= 1:
                shooting_detail['angle'] = 'top'
        
        else:
            shooting_detail['angle'] = 'same'
        
        return shooting_detail

    #get all the flips 
    get_straight_up(dimensions[1])
    
    get_straight_down(dimensions[1])

    get_straight_right(dimensions[0])

    get_straight_left(dimensions[0])

    get_right(dimensions[0],dimensions[1])

    get_left(dimensions[0],dimensions[1])

    for map_flip in all_flips:

        my_virtual_pos = get_virtual_pos(your_position,map_flip)
        trainer_virtual_pos = get_virtual_pos(trainer_position,map_flip)

        shooting_detail_me = get_shooting_detail(my_virtual_pos)
        shooting_detail_trainer = get_shooting_detail(trainer_virtual_pos)

        if shooting_detail_me['distance'] <= distance:
            if shooting_detail_me['angle'] not in shooting_angle_me:
                shooting_angle_me[shooting_detail_me['angle']] = shooting_detail_me['distance']
                aim_me.append(shooting_detail_me['aim'])

        if shooting_detail_trainer['distance'] <= distance:
            if shooting_detail_trainer['angle'] not in shooting_angle_trainer:
                shooting_angle_trainer[shooting_detail_trainer['angle']] = shooting_detail_trainer['distance']         
                aim_trainer.append(shooting_detail_trainer['aim'])

    invalid_angle = 0
    
    for i in shooting_angle_trainer:
        if i in shooting_angle_me:
            if shooting_angle_me[i] < shooting_angle_trainer[i]:
                invalid_angle += 1

    return len(aim_trainer)-invalid_angle