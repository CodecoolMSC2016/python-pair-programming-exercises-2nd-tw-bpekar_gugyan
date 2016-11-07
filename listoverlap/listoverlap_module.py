def listoverlap(list1, list2):
    result = []
    for item in list1:
        if item in list2:
            if item not in result:
                result.append(item)
    return result




def main():
    return


if __name__ == '__main__':
    main()
