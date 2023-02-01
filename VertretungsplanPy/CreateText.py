import ast

def create_text(inputs):
    inputs = ast.literal_eval(inputs)

    if not inputs:
        return "Keine Änderung\n"
    hours = []
    teacher = []
    course = []
    room = []
    kind = []
    info = []

    for input in inputs:
        hour, teacher_, course_, room_, kind_, info_ = input
        hours.append(hour)
        teacher.append(teacher_)
        course.append(course_)
        room.append(room_)
        kind.append(kind_)
        info.append(info_)

    output = ""



    for i in range(len(hours)):
        output += f"Stunde: {hours[i]}, {course[i]}: "
        
        if "?" in teacher[i]:
            new_teacher = teacher[i].split("?")
            teacher[i] = new_teacher[1]+" statt "+new_teacher[0]
        output += f"bei {teacher[i]} folgende Änderung: {kind[i]}"
        if "?" in room[i] :
            new_room = room[i].split("?")
            room[i] = new_room[1]
            output += f" Raum: {room[i]}"
        if info[i]:
            output += f" Info: {info[i]}"
        output += "\n"

    return output
