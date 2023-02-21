DIRECTORY = '~/home/linekDocuments/'
def write_archive(archive_name, text='Creating archive'):
    archive = open(archive_name, 'w')
    archive.write(text)
    archive.close()


def update_archive(archive_name, text: str):
    archive = open(archive_name, 'a')
    archive.write(text)
    archive.close()


def read_archive(archive_name):
    archive = open(archive_name, 'r')
    text = archive.read()
    return text


def read_avg(archive):
    arch = open(archive, 'r')
    student_list = arch.read()
    student_list = student_list.split('\n')

    average_list = []

    for i in student_list:
        list_note = i.split(',')
        student_name = list_note[0]
        list_note.pop(0)
        average = lambda notes: sum([int(x) for x in notes]) / 4
        print(student_name)
        print(list_note)
        print(average(list_note))
        average_list.append({student_name: average(list_note)})
    return average_list


def copy_archive(archive_name, directory):
    import shutil
    shutil.copy(archive_name, directory)

def move_archive(archive_name, directory):
    import shutil
    shutil.move(archive_name, directory)


if __name__ == '__main__':
    copy_archive('notas.txt', DIRECTORY)
    lista_media = read_avg('notas.txt')
    print(lista_media)
    # avg = 'notas.txt'
    # student = '\nAmanda,9,6,6,8'
    # write_archive(avg, 'Linek,10,10,10,10')
    # update_archive(avg, student)
    # print(read_archive('test.txt'))
    # read_avg(avg)
